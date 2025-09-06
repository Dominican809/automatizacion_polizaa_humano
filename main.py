"""
Script principal para la emisión automatizada de pólizas usando los módulos refactorizados.
"""

import sys
import json
from pathlib import Path
from loguru import logger
from emisor_goval.utils.procesar_validacion import procesar_validacion
from emisor_goval.utils.excel_to_emision_v2 import cargar_emisiones_desde_excel

input("Presiona Enter para empezar a cargar las emisiones desde excel:")

cargar_emisiones_desde_excel("Exceles/Asegurados_Viajeros.xlsx", "emisiones_generadas.json")

input("Presiona Enter para continuar con la carga de emisiones a Goval:")

def test_multiple_emissions(json_path: str = "emisiones_generadas.json", num_emissions: int = 1) -> bool:
    """
    Prueba el procesamiento de emisiones (puede ser una sola o múltiples).
    
    Args:
        json_path (str): Ruta al archivo de emisiones
        num_emissions (int): Número de emisiones a procesar (default: 1)
        
    Returns:
        bool: True si la prueba fue exitosa, False en caso contrario
    """
    try:
        # Crear directorio data si no existe
        data_dir = Path("data")
        data_dir.mkdir(exist_ok=True)
        
        # Crear archivo temporal con las primeras N emisiones
        with open(json_path, 'r') as f:
            emisiones = json.load(f)
            
        if not emisiones:
            logger.error("❌ No hay emisiones en el archivo")
            return False
            
        # Tomar las primeras N emisiones
        primeras_emisiones = dict(list(emisiones.items())[:num_emissions])
        logger.info(f"🔍 Procesando las primeras {len(primeras_emisiones)} emisiones")
        
        # Guardar en archivo temporal
        test_file = data_dir / "test_emissions.json"
        with open(test_file, 'w') as f:
            json.dump(primeras_emisiones, f, indent=2)
            
        # Procesar las emisiones
        emisiones_exitosas, emisiones_fallidas = procesar_validacion(
            emisiones_path=str(test_file),
            output_success_path=str(data_dir / "test_success.json"),
            output_errors_path=str(data_dir / "test_errors.json")
        )
        
        # Calcular tasa de éxito
        total = len(emisiones_exitosas) + len(emisiones_fallidas)
        tasa_exito = (len(emisiones_exitosas) / total) * 100 if total > 0 else 0
        
        logger.info("\n📊 Resumen de la prueba:")
        logger.info(f"Total procesadas: {total}")
        logger.info(f"Exitosas: {len(emisiones_exitosas)}")
        logger.info(f"Fallidas: {len(emisiones_fallidas)}")
        logger.info(f"Tasa de éxito: {tasa_exito:.2f}%")
        
        success = len(emisiones_exitosas) > 0
        if success:
            logger.success("✅ Prueba completada!")
        else:
            logger.error("❌ La prueba falló - No hubo emisiones exitosas")
            
        return success
        
    except Exception as e:
        logger.error(f"❌ Error durante la prueba: {str(e)}")
        return False

def main():
    """
    Función principal que procesa el archivo de emisiones.
    """
    # Configurar logging
    logger.remove()
    logger.add("logs/emisor.log", rotation="500 MB", level="DEBUG")
    logger.add(lambda msg: print(msg), level="INFO")
    
    # Verificar argumentos
    if len(sys.argv) > 1:
        if sys.argv[1] == "--test":
            # Modo prueba con emisiones (default: 1 emisión)
            json_path = sys.argv[2] if len(sys.argv) > 2 else "emisiones_generadas.json"
            num_emissions = int(sys.argv[3]) if len(sys.argv) > 3 else 1
            return 0 if test_multiple_emissions(json_path, num_emissions) else 1
        else:
            json_path = sys.argv[1]
    else:
        json_path = "emisiones_generadas.json"
        
    logger.info(f"🚀 Iniciando procesamiento de emisiones desde {json_path}")
    
    try:
        # Procesar emisiones
        emisiones_exitosas, emisiones_fallidas = procesar_validacion(emisiones_path=json_path)
        
        # El resumen ya se muestra en la función procesar_validacion
        return 0 if not emisiones_fallidas else 1
        
    except Exception as e:
        logger.error(f"❌ Error durante el procesamiento: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 