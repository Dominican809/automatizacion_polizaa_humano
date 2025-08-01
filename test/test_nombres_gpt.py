from emisor_goval.utils.nombres_gpt import extract_name_components_and_gender

def print_test_result(name):
    result = extract_name_components_and_gender(name)
    print(f"\nInput: '{name}'")
    print(f"Output: {result}")
    print(f"Length of components:")
    print(f"  First name: {len(result[0])} chars - '{result[0]}'")
    print(f"  Paternal: {len(result[1])} chars - '{result[1]}'")
    print(f"  Maternal: {len(result[2])} chars - '{result[2]}'")
    print(f"  Middle: {len(result[3])} chars - '{result[3]}'")
    print(f"  Gender: {result[4]}")
    print("-" * 80)

def run_tests():
    # Test Case 1: Normal name
    print_test_result("Juan Carlos Pérez González")
    
    # Test Case 2: Very long name (>60 chars)
    print_test_result("Maria Fernanda de los Santos Rodriguez Gutierrez del Valle")
    
    # Test Case 3: Compound surname with particles
    print_test_result("Ana María de la Rosa Martínez")
    
    # Test Case 4: Single word name
    print_test_result("Pedro")
    
    # Test Case 5: Name with exactly 30 chars in first part
    print_test_result("Juan Carlos Fernando Martínez de la Rosa González")
    
    # Test Case 6: Name with special characters and accents
    print_test_result("José Ángel Martínez-Góngora del Río")
    
    # Test Case 7: Very short name
    print_test_result("Li Wu")
    
    # Test Case 8: Name with multiple spaces
    print_test_result("Maria  de   los    Angeles     Pérez")
    
    # Test Case 9: Name with initials
    print_test_result("J. R. Martinez de la Torre")
    
    # Test Case 10: Extremely long name components
    print_test_result("Maria Fernanda Alejandra Carolina de los Angeles Rodriguez Montenegro de la Torre del Castillo")

if __name__ == "__main__":
    run_tests() 