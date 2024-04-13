import sys
sys.path.append("src")
from logica.huffman_cleanCode import HuffmanCoding


class HuffmanMenu:
    def __init__(self):
        self.huffman_coding = None

    def print_menu_options(self):
        print("\n--- Menú de Huffman Coding ---")
        print("1. Codificar texto")
        print("2. Decodificar texto")
        print("3. Salir")

    def execute_option(self, option):
        try:
            if option == "1":
                text = input("Ingresa el texto a codificar: ")
                self.huffman_coding = HuffmanCoding(text)
                encoded = self.huffman_coding.encode()
                print(f"Texto original: {text}")
                print(f"Texto codificado: {encoded}")
            elif option == "2":
                if self.huffman_coding:
                    text_to_decode = input("Ingresa el texto a decodificar: ")
                    decoded_text = self.huffman_coding.decode(text_to_decode)
                    print(f"Texto decodificado: {decoded_text}")
                else:
                    text_to_decode = input("Ingresa el texto a decodificar: ")
                    self.huffman_coding = HuffmanCoding(text_to_decode)
                    decoded_text = self.huffman_coding.decode(text_to_decode)
                    print(f"Texto decodificado: {decoded_text}")
            elif option == "3":
                print("Saliendo del programa...")
            else:
                print("Opción no válida. Por favor, selecciona una opción válida.")
        except Exception as e:
            print(f"Error: {e}")

    def display_menu(self):
        while True:
            self.print_menu_options()
            choice = input("Selecciona una opción: ")
            self.execute_option(choice)
            if choice == "3":
                break

            input("Presiona Enter para continuar...")

if __name__ == "__main__":
    menu = HuffmanMenu()
    menu.display_menu()
