from tkinter import messagebox, filedialog
from datetime import datetime
from src.Decompression.TextDecompression import TextDecompression


class FileSaver:
    """
    Třída FileSaver poskytuje funkcionality pro ukládání a správu komprimovaných a dekomprimovaných souborů.
    :Metody:
    - save_file(content): Metoda pro uložení komprimovaného textového souboru.
    """
    @staticmethod
    def save_file(content):
        """
        Uloží obsah do textového souboru na základě vstupního obsahu.
        Po uložení komprimovaného souboru se zobrazí dialogové okno pro případnou dekompresi.
        :param content: Obsah, který se má uložit do souboru.
        """
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])

        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(content)

                compressed_file_path = "Data/Compressed.txt"
                compressed_file_log_path = "Log/CompressedFileLog.txt"

                with open(compressed_file_path, 'w') as compressed_copy:
                    compressed_copy.write(content)

                with open(compressed_file_log_path, 'w') as compressed_file_log:
                    now = datetime.now()
                    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
                    compressed_file_log.write(f"Success! Compressed file: " + file_path + f", creation time: {current_time}\n")

                # Zobrazit okno se zprávou při úspěšném uložení
                messagebox.showinfo("Saved", f"File was successfully compressed and saved here: {file_path}")

                # Dotaz na dekompresi
                should_decompress = messagebox.askyesno("Saved", f"Do you want to decode the file back?")

                if should_decompress:
                    messagebox.showinfo("Decompressing", f"Choose a location to save the decompressed file")
                    decompressed_file_path_text = "Data/Decompressed.txt"
                    decompressed_file_path_text_log = "Log/DecompressedFileLog.txt"
                    decompressed_content = TextDecompression.decompress(content, "Data/Dictionary.txt")
                    if not isinstance(decompressed_content, str):
                        messagebox.showerror("Error", decompressed_content)
                    else:
                        decompressed_file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                                              filetypes=[("Text Files", "*.txt")])
                        messagebox.showinfo("Saved", f"The file was successfully decoded and saved here: {decompressed_file_path}")
                        if decompressed_file_path:
                            with open(decompressed_file_path, 'w') as decompressed_copy:
                                decompressed_copy.write(decompressed_content)
                        with open(decompressed_file_path_text_log, 'w') as decompressed_file_log:
                            now = datetime.now()
                            current_time = now.strftime("%Y-%m-%d %H:%M:%S")
                            decompressed_file_log.write(f"Success! Decompressed file: {decompressed_file_path}, creation time: {current_time}\n")
                    with open(decompressed_file_path_text, 'w') as decompressed_copy:
                        decompressed_copy.write(decompressed_content)
            except Exception as e:
                error_message = f"An error occurred: {e}"
                messagebox.showerror("Error", f"Unable to save the file: {str(e)}")
                with open("Log/ErrorFileLog.txt", 'a') as error_file:
                    now = datetime.now()
                    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
                    error_file.write(f"{current_time}: {error_message}\n\n")
