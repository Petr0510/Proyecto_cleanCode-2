from io import StringIO
import unittest

"""Para hacer que las pruebas corra importamos sys"""
import sys
from unittest.mock import patch
sys.path.append("src")


from console.huffman_menu import HuffmanMenu
from logica.huffman_cleanCode import HuffmanCoding


class TestHuffmanCoding(unittest.TestCase):
    
    SPECIAL_CHARACTER_TEST = "!@#$%^&*()"
    WORD_TEST = "abracadabra"
    REPEATED_CHARACTERS_TEST = "aaaaabbbbccccc"
    
    def test_encode_normal_text(self):
        """Prueba normal: Comprime un texto normal y verifica el resultado"""
        coding = HuffmanCoding(self.WORD_TEST)
        encoded = coding.encode()
        expected_result = "01111100101010001111100"
        self.assertEqual(encoded, expected_result)

    def test_decode_normal_text(self):
        """Prueba normal: Descomprime un texto normal y verifica el resultado"""
        coding = HuffmanCoding(self.WORD_TEST)
        encoded = coding.encode()
        decoded = coding.decode(encoded)
        self.assertEqual(decoded, self.WORD_TEST)

    def test_encode_special_characters(self):
        """Prueba normal: Comprime un texto con caracteres especiales y verifica el resultado"""
        coding = HuffmanCoding(self.SPECIAL_CHARACTER_TEST)
        encoded = coding.encode()
        expected_result = "1100110101110000010101011100011111"
        self.assertEqual(encoded, expected_result)

    def test_decode_special_characters(self):
        """Prueba normal: Descomprime un texto con caracteres especiales y verifica el resultado"""
        coding = HuffmanCoding(self.SPECIAL_CHARACTER_TEST)
        encoded = coding.encode()
        decoded = coding.decode(encoded)
        self.assertEqual(decoded, self.SPECIAL_CHARACTER_TEST)

    def test_encode_repeated_characters(self):
        """Prueba normal: Comprime un texto con caracteres repetidos y verifica el resultado"""
        coding = HuffmanCoding(self.REPEATED_CHARACTERS_TEST)
        encoded = coding.encode()
        expected_result = "11111111111010101000000"
        self.assertEqual(encoded, expected_result)

    def test_decode_repeated_characters(self):
        """Prueba normal: Descomprime un texto con caracteres repetidos y verifica el resultado"""
        coding = HuffmanCoding(self.REPEATED_CHARACTERS_TEST)
        encoded = coding.encode()
        decoded = coding.decode(encoded)
        self.assertEqual(decoded, self.REPEATED_CHARACTERS_TEST)

    def test_none_text(self):
        """Prueba excepcional: Intenta comprimir un texto que es None y verifica la excepción"""
        with self.assertRaises(ValueError):
            HuffmanCoding(None)

    def test_empty_text(self):
        """Prueba excepcional: Descomprime un texto con texto vacío y verifica la excepción"""
        with self.assertRaises(ValueError):
            HuffmanCoding("")

    def test_encode_invalid_text_type(self):
        """Prueba excepcional: Intenta comprimir un texto que no es de tipo string y verifica la excepción"""
        coding = HuffmanCoding('123')
        with self.assertRaises(TypeError):
            coding.encode("")

    def test_decode_invalid_encoded_text(self):
        """Prueba excepcional: Intenta descomprimir un texto codificado inválido y verifica la excepción"""
        coding = HuffmanCoding(self.WORD_TEST)
        with self.assertRaises(ValueError):
            coding.decode("101010101")

    def test_encode_invalid_tree_structure(self):
        """Prueba excepcional: Intenta comprimir un texto con una estructura de árbol inválida y verifica la excepción"""
        coding = HuffmanCoding(self.WORD_TEST)
        coding.heap = None  # Simula una estructura de árbol inválida
        with self.assertRaises(ValueError):
            coding.encode()

    def test_decode_long_text(self):
        """Prueba de error: Descomprime un texto largo y verifica que el resultado sea igual al texto original"""
        text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        coding = HuffmanCoding(text)
        encoded = coding.encode()
        decoded = coding.decode(encoded)
        self.assertEqual(decoded, text)
            
    def test_decode_invalid_tree_structure(self):
        """Prueba excepcional: Intenta descomprimir un texto con una estructura de árbol inválida y verifica la excepción"""
        coding = HuffmanCoding(self.WORD_TEST)
        coding.tree = None  # Simula una estructura de árbol inválida
        with self.assertRaises(ValueError):
            coding.decode("")

    def test_decode_invalid_character_in_encoded_text(self):
        """Prueba de error: Intenta descomprimir un texto codificado con caracteres inválidos y verifica la excepción"""
        coding = HuffmanCoding(self.WORD_TEST)
        with self.assertRaises(ValueError):
            coding.decode("1010abc10101")
    
    def test_encode_invalid_text_length(self):
        """Prueba de error: Intenta comprimir un texto muy corto y verifica la excepción"""
        coding = HuffmanCoding("a")
        with self.assertRaises(ValueError):
            coding.encode()

    def test_decode_invalid_encoded_data(self):
        """Prueba de error: Intenta descomprimir datos codificados inválidos y verifica la excepción"""
        coding = HuffmanCoding(self.WORD_TEST)
        with self.assertRaises(ValueError):
            coding.decode("01010101")

    def test_decode_missing_encoded_data(self):
        """Prueba de error: Intenta descomprimir datos codificados faltantes y verifica la excepción"""
        coding = HuffmanCoding(self.WORD_TEST)
        with self.assertRaises(ValueError):
            coding.decode("")

    def test_decode_invalid_encoded_data_length(self):
        """Prueba de error: Intenta descomprimir datos codificados de longitud incorrecta y verifica la excepción"""
        coding = HuffmanCoding(self.WORD_TEST)
        with self.assertRaises(ValueError):
            coding.decode("101010111")

    def test_decode_invalid_encoded_data_format(self):
        """Prueba de error: Intenta descomprimir datos codificados con formato incorrecto y verifica la excepción"""
        coding = HuffmanCoding(self.WORD_TEST)
        with self.assertRaises(ValueError):
            coding.decode("1a0b1c0d1a0b1c0d")
    
    def test_bad_bit_sequence(self):
        """Prueba de error: Intenta descomprimir una secuencia de bits erronea"""
        coding = HuffmanCoding(self.WORD_TEST)
        with self.assertRaises(ValueError):
            coding.decode("000000")
    
    def test_encode_text(self):
        with patch('sys.stdout', new=StringIO()) as fake_out, patch('builtins.input', side_effect=['1', 'hello', '3']):  # Opción de codificación, texto a codificar y luego salir
            menu = HuffmanMenu()
            menu.display_menu()
            output = fake_out.getvalue().strip()
            self.assertIn("Texto codificado:", output)
    
    def test_decode_without_encode_text(self):
        with patch('sys.stdout', new=StringIO()) as fake_out, patch('builtins.input', side_effect=['2', 'hello', '3']):  # Opción de decodificacion y luego salir
            menu = HuffmanMenu()
            menu.display_menu()
            output = fake_out.getvalue().strip()
            self.assertIn("Debe realizar una ejecución de codificación antes de usar esta opción", output)

if __name__ == "__main__":
    unittest.main()
