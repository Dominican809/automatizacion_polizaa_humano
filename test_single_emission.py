"""
Test script for processing a single emission with detailed logging.
"""

import json
from loguru import logger
import sys
from emisor_goval.api.auth import TokenManager
from emisor_goval.api.consultas import consultar_linea_credito, consultar_producto_detalle
from emisor_goval.api.cotizacion import cotizar_emision, process_manager_validation
from emisor_goval.api.pago import apply_payment
from datetime import datetime, timedelta
from emisor_goval.config import API_BASE
import requests

# Configure logging
logger.remove()  # Remove default handler
logger.add(sys.stderr, level="DEBUG")  # Add stderr handler with DEBUG level
logger.add("logs/test_single.log", level="DEBUG", rotation="500 MB")  # Add file handler

def get_test_emission():
    """Create a test emission with real data"""
    return {
        "agency_id": 1,
        "discount": 0.0,
        "salesman_id": 10,
        "products": [
            {
                "id": 1
            }
        ],
        "destiny_id": 840,
        "destination_id": 840,
        "from": "2026-06-24",
        "to": "2026-07-05",
        "terms": "",
        "insured": [
            {
                "identity": "",
                "passport": "6682595-0",
                "firstname": "GISNELLY DE LOURDES LUCIANO",
                "lastname": "LASSIS",
                "birthdate": "1977-10-03",
                "gender": "M"  # Changed from sex to gender
            },
            {
                "identity": "",
                "passport": "6682595-3",
                "firstname": "CANDELA MARÍA PONCE",
                "lastname": "LUCIANO",
                "birthdate": "2014-01-03",
                "gender": "M"  # Changed from sex to gender
            }
        ],
        "addresses": [
            {
                "line1": ".",
                "line2": "",
                "city": ".",
                "state": ".",
                "country_id": 214,
                "zip": "00000",
                "phone": [
                    "."
                ],
                "email": [
                    "."
                ],
                "kind": "Por defecto"
            }
        ]
    }

def test_single_emission():
    try:
        logger.info("🚀 Starting single emission test")
        
        # Step 1: Get authentication token
        logger.info("Step 1: Getting authentication token")
        token = TokenManager.get_token()
        logger.success("✅ Authentication successful")
        
        # Step 2: Check credit line
        logger.info("Step 2: Checking credit line for agency")
        credit_info = consultar_linea_credito(1)
        logger.info("Credit line information:")
        logger.info(json.dumps(credit_info, indent=2))
        
        # Step 3: Check product details
        logger.info("Step 3: Checking product details")
        product_info = consultar_producto_detalle(1)
        logger.info("Product configuration:")
        logger.info(json.dumps(product_info, indent=2))
        
        # Step 4: Create test emission
        logger.info("Step 4: Creating test emission")
        emission_data = get_test_emission()
        logger.info("Emission payload:")
        logger.info(json.dumps(emission_data, indent=2))
        
        # Step 5: Create quotation
        logger.info("Step 5: Creating quotation")
        quotation_id, manager_uri, quotation_response = cotizar_emision(emission_data)
        
        if not quotation_id:
            logger.error("❌ Failed to create quotation")
            logger.error(f"Response status: {quotation_response.status_code}")
            logger.error(f"Response body: {quotation_response.text}")
            return False
            
        logger.success(f"✅ Quotation created successfully (ID: {quotation_id})")
        logger.debug(f"Manager URI: {manager_uri}")
        
        # Step 6: Process manager validation
        logger.info("Step 6: Processing manager validation")
        manager_success, manager_error, final_uri, manager_response = process_manager_validation(quotation_id, token)
        
        if not manager_success:
            logger.error("❌ Manager validation failed")
            logger.error(f"Error: {manager_error}")
            if manager_response:
                logger.error(f"Response status: {manager_response.status_code}")
                logger.error(f"Response body: {manager_response.text}")
            return False
            
        logger.success("✅ Manager validation successful")
        
        # Step 7: Apply payment
        logger.info("Step 7: Applying payment")
        
        # Log payment request details
        payment_url = f"{API_BASE}/issue/retail/apply/{quotation_id}/credit"
        payment_headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            **TokenManager.get_auth_header()
        }
        
        logger.info("Payment Request Details:")
        logger.info(f"URL: {payment_url}")
        logger.info("Headers:")
        logger.info(json.dumps(payment_headers, indent=2))
        
        # Make the payment request
        payment_response = requests.post(payment_url, headers=payment_headers)
        
        logger.info("Payment Response:")
        logger.info(f"Status Code: {payment_response.status_code}")
        logger.info(f"Response Headers: {dict(payment_response.headers)}")
        logger.info(f"Response Body: {payment_response.text}")
        
        if payment_response.status_code not in [200, 201]:
            logger.error("❌ Payment failed")
            logger.error(f"Response status: {payment_response.status_code}")
            logger.error(f"Response body: {payment_response.text}")
            return False
            
        payment_data = payment_response.json()
        logger.success("✅ Payment successful")
        logger.info("Payment result:")
        logger.info(json.dumps(payment_data, indent=2))
        
        return True
        
    except Exception as e:
        logger.exception(f"❌ Unexpected error: {str(e)}")
        return False

if __name__ == "__main__":
    logger.info("=== Starting Single Emission Test ===")
    success = test_single_emission()
    
    if success:
        logger.success("\n✨ Test completed successfully!")
        sys.exit(0)
    else:
        logger.error("\n❌ Test failed!")
        sys.exit(1) 