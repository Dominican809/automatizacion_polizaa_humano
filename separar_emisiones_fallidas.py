import json
from pathlib import Path
from loguru import logger

def extract_failed_emissions(failures_path, all_emissions_path, output_path):
    """
    Extract complete information of failed emissions and save to a new file.
    
    Args:
        failures_path (str): Path to the failures JSON file
        all_emissions_path (str): Path to the complete emissions JSON file
        output_path (str): Where to save the extracted emissions
    """
    try:
        # Read failures file
        logger.info(f"📖 Reading failures from: {failures_path}")
        with open(failures_path, 'r', encoding='utf-8') as f:
            failures_data = json.load(f)
            failures = failures_data.get('emisiones_fallidas', [])
        
        # Extract factura numbers from failures
        failed_facturas = set()
        for failure in failures:
            factura = failure.get('factura')
            if factura:
                failed_facturas.add(str(factura))
                logger.info(f"Found failed factura: {factura} - Error: {failure.get('error')} - Step: {failure.get('step')}")
        
        logger.info(f"🔍 Found {len(failed_facturas)} failed facturas")
        
        # Read complete emissions
        logger.info(f"📖 Reading all emissions from: {all_emissions_path}")
        with open(all_emissions_path, 'r', encoding='utf-8') as f:
            all_emissions = json.load(f)
            
        # Extract failed emissions with complete information
        pending_emissions = {}
        for factura in failed_facturas:
            if factura in all_emissions:
                pending_emissions[factura] = all_emissions[factura]
                logger.info(f"✓ Found complete information for factura: {factura}")
            else:
                logger.warning(f"⚠️ Could not find information for factura: {factura}")
        
        # Save to new file
        logger.info(f"💾 Saving {len(pending_emissions)} pending emissions to: {output_path}")
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(pending_emissions, f, ensure_ascii=False, indent=2)
            
        logger.success(f"✅ Successfully extracted {len(pending_emissions)} pending emissions")
        
    except Exception as e:
        logger.error(f"❌ Error processing emissions: {str(e)}")
        raise

if __name__ == "__main__":
    # Configure logging
    logger.remove()
    logger.add(lambda msg: print(msg), level="INFO")
    
    # Paths
    failures_path = "data/tracking/failures/failures_20250618_21_54_33.json"
    all_emissions_path = "emisiones_generadas.json"
    output_path = "emisiones_pendientes.json"
    
    # Process emissions
    extract_failed_emissions(failures_path, all_emissions_path, output_path) 