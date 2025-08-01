import json
from pathlib import Path
from loguru import logger
from datetime import datetime

def extract_latest_failures(tracking_dir: str = "data/tracking/failures", 
                          all_emissions_path: str = "emisiones_pendientes.json",
                          output_path: str = "emisiones_pendientes_v2.json"):
    """
    Extract complete information of failed emissions from the latest tracking file.
    
    Args:
        tracking_dir (str): Directory containing failure tracking files
        all_emissions_path (str): Path to the complete emissions JSON file
        output_path (str): Where to save the extracted emissions
    """
    try:
        # Find the latest failures file
        tracking_path = Path(tracking_dir)
        failure_files = list(tracking_path.glob("failures_*.json"))
        if not failure_files:
            logger.error("❌ No failure tracking files found")
            return
            
        latest_file = max(failure_files, key=lambda x: x.stat().st_mtime)
        logger.info(f"📖 Reading failures from latest file: {latest_file}")
        
        # Read failures file
        with open(latest_file, 'r', encoding='utf-8') as f:
            failures_data = json.load(f)
            failures = failures_data.get('emisiones_fallidas', [])
        
        # Extract factura numbers from failures
        failed_facturas = set()
        for failure in failures:
            factura = failure.get('factura')
            if factura:
                failed_facturas.add(str(factura))
                logger.info(f"📝 Found failed factura: {factura}")
        
        logger.info(f"Found {len(failed_facturas)} failed facturas")
        
        # Read complete emissions file
        with open(all_emissions_path, 'r', encoding='utf-8') as f:
            all_emissions = json.load(f)
            
        # Extract only failed emissions
        failed_emissions = {}
        for factura, data in all_emissions.items():
            if factura in failed_facturas:
                failed_emissions[factura] = data
                logger.info(f"✅ Found complete data for factura {factura}")
                
        # Save to new file
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(failed_emissions, f, indent=2, ensure_ascii=False)
            
        logger.success(f"✨ Successfully saved {len(failed_emissions)} failed emissions to {output_path}")
        
    except Exception as e:
        logger.error(f"❌ Error processing failures: {str(e)}")
        
if __name__ == "__main__":
    extract_latest_failures() 