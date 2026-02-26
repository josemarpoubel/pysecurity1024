# test_security.py

import unittest
from pysecurity1024 import SecurityEngine, ALFABETO, DIGITOS

class TestSecurityEngine(unittest.TestCase):
    
    def setUp(self):
        """Inicializa o motor antes de cada teste."""
        self.engine = SecurityEngine()

    def test_gerar_letras(self):
        resultado = self.engine.gerar_letras(15)
        self.assertEqual(len(resultado), 15)
        self.assertTrue(all(c in ALFABETO for c in resultado))

    def test_gerar_palavra_estrutura(self):
        palavra, bits = self.engine.gerar_palavra()
        self.assertIn(len(palavra), [7, 8])
        self.assertTrue(palavra[-1] in DIGITOS)

    def test_entropia_suprema(self):
        resultado = self.engine.gerar_frase_mestra()
        self.assertGreater(resultado['entropia_bits'], 1024)
        print(f"\n[TEST] Entropia validada: {resultado['entropia_bits']} bits")

    def test_id_aleatorio(self):
        id_gerado = self.engine.gerar_id_aleatorio(5, 10)
        self.assertTrue(5 <= len(id_gerado) <= 10)

if __name__ == "__main__":
    unittest.main()
