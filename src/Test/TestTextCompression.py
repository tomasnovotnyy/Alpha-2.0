import unittest
from src.Compression.TextCompression import TextCompression


class TestTextCompression(unittest.TestCase):
    """
    Třída TestTextCompression slouží k testování třídy TextCompression.
    :Metody:
    - test_file_compression(self): Metoda pro testování komprese textového souboru.
    """

    def test_file_compression(self):
        """
        Metoda pro testování komprese textového souboru.
        :return: Test, zda se obsah souboru komprimoval.
        """
        try:
            file_path = "Data/Original.txt"
            with open(file_path, "r") as file:
                original_content = file.read()

            compressed_content = TextCompression.compress(original_content)

            # Test, zda se obsah souboru komprimoval
            self.assertNotEqual(original_content, compressed_content)

        except Exception as e:
            error_message = f"Error during file compression test: {str(e)}"
            print(error_message)
            with open("Log/ErrorFileLog.txt", 'a') as error_file:
                error_file.write(f"{error_message}\n")
