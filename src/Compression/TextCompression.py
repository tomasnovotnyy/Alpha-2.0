from collections import Counter
from datetime import datetime
import string


class TextCompression:
    """
    Tato třída poskytuje metodu pro kompresi textových dat.
    :Metody:
    - compress(text): Metoda pro kompresi textu.
    """

    @staticmethod
    def compress(text):
        """
        Metoda pro kompresi textu.
        :param text: Vstupní text, který má být komprimován.
        :return: Kompresovaný text.
        """
        try:
            # Odstranění čárek a teček ze vstupního textu
            text = text.replace(',', '').replace('.', '').replace('?', '').replace('!', '')

            words = text.split()
            word_counts = Counter(words)
            top_words = [word for word, count in word_counts.items() if len(word) >= 5]

            # Přidání slov se 4 písmeny, která se vyskytují alespoň 3krát
            four_letter_words = [word for word, count in word_counts.items() if count > 2 and len(word) == 4]
            top_words.extend(four_letter_words)

            compressed_words = []
            word_dict = {}
            word_abbreviations = {}

            alphabet = list(string.ascii_lowercase)
            abbreviation_counter = 0

            for word in words:
                if word in top_words:
                    try:
                        if word not in word_dict:
                            if abbreviation_counter < 26:
                                abbreviation = f"({alphabet[abbreviation_counter]})"
                                abbreviation_counter += 1
                            else:
                                abbreviation = f"({string.ascii_lowercase[abbreviation_counter // 26 - 1]}{string.ascii_lowercase[abbreviation_counter % 26]})"
                                abbreviation_counter += 1

                            word_dict[word] = abbreviation
                            compressed_words.append(abbreviation)
                            word_abbreviations[word] = abbreviation
                        else:
                            compressed_words.append(word_dict[word])
                    except Exception as e:
                        print(f"Error processing word '{word}': {e}")
                        compressed_words.append(word)
                else:
                    compressed_words.append(word)

            dictionary_text = "\n".join([f"{word}={abbreviation}" for word, abbreviation in word_dict.items()])
            stored_dictionary_path = "Data/Dictionary.txt"
            with open(stored_dictionary_path, "w") as file:
                file.write(dictionary_text)

            dictionary_file_log_path = "Log/DictionaryFileLog.txt"
            with open(dictionary_file_log_path, 'w') as dictionary_file_log:
                now = datetime.now()
                current_time = now.strftime("%Y-%m-%d %H:%M:%S")
                dictionary_file_log.write(f"Success! Dictionary file created at: {current_time}\n")

            # Log zkrácených slov a jejich zkratky
            abbreviations_log_path = "Log/AbbreviationsFileLog.txt"
            with open(abbreviations_log_path, 'w') as abbreviations_log:
                now = datetime.now()
                current_time = now.strftime("%Y-%m-%d %H:%M:%S")
                for word, abbreviation in word_abbreviations.items():
                    abbreviations_log.write(f"Word: {word}, Abbreviation: {abbreviation}, time: {current_time}\n")

            return ' '.join(compressed_words)
        except Exception as ex:
            error_message = f"An error occurred: {ex}"
            print(error_message)
            with open("Log/ErrorFileLog.txt", 'a') as error_file:
                now = datetime.now()
                current_time = now.strftime("%Y-%m-%d %H:%M:%S")
                error_file.write(f"{current_time}: {error_message}\n\n")
            return text
