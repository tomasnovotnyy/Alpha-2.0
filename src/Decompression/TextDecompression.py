from datetime import datetime


class TextDecompression:
    """
    Tato třída poskytuje metodu pro dekompresi textu pomocí slovníku.
    :Metody:
    - decompress(compressed_text, dictionary_file_path): Metoda pro dekompresi textu pomocí poskytnutého slovníku.
    """
    @staticmethod
    def decompress(compressed_text, dictionary_file_path):
        """
        Metoda pro dekompresi textu pomocí poskytnutého slovníku.
        :param compressed_text: Kompresovaný text, který má být dekomprimován.
        :param dictionary_file_path: Cesta k souboru se slovníkem pro dekompresi.
        :return: Dekomprimovaný text nebo chybová zpráva v případě neúspěchu.
        """
        try:
            # Načtení slovníku
            word_dict = {}
            with open(dictionary_file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    word, abbreviation = line.strip().split('=')
                    word_dict[abbreviation.strip()] = word.strip()

            # Dekomprese textu
            words = compressed_text.split()
            decompressed_words = []
            for word in words:
                if word.startswith('(') and word.endswith(')'):
                    decompressed_words.append(word_dict.get(word, word))
                else:
                    decompressed_words.append(word)

            return ' '.join(decompressed_words)

        except Exception as e:
            error_message = f"Cannot decompress the file: {str(e)}"
            with open("Log/ErrorFileLog.txt", 'a') as error_file:
                now = datetime.now()
                current_time = now.strftime("%Y-%m-%d %H:%M:%S")
                error_file.write(f"{current_time}: {error_message}\n\n")
            return error_message
