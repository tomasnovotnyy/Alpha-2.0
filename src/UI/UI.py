import tkinter as tk
from datetime import datetime
from tkinter import filedialog, messagebox
from src.Saver.FileSaver import FileSaver
from src.Compression.TextCompression import TextCompression
from src.UI.HelpWindow import HelpWindow


class UI:
    """
    Třída UI reprezentuje uživatelské rozhraní aplikace Alpha 2.0.
    :Metody:
    - __init__(self, root): Konstruktor třídy UI.
    - start_action(self): Metoda pro spuštění komprese textového souboru.
    - save_file(self, content): Metoda pro uložení komprimovaného textového souboru.
    - log_error(self, error_message): Metoda pro zapsání chyby do logu.
    - show_file_dialog(self): Metoda pro zobrazení dialogového okna pro výběr souboru.
    - choose_file_for_compression(self, file_dialog): Metoda pro výběr souboru pro kompresi.
    - show_save_dialog(self, content): Metoda pro zobrazení dialogového okna pro výběr umístění uložení souboru.
    - help_action(self): Metoda pro zobrazení nápovědy.
    - quit_action(self): Metoda pro ukončení programu.
    """

    def __init__(self, root):
        """
        Inicializace objektu UI.
        :param root: Hlavní okno aplikace.
        """

        # Nastavení hlavního okna
        self.root = root
        self.root.title("Alpha 2.0")

        # Nastavení titulku
        self.title_label = tk.Label(self.root, text="Alpha 2.0")
        self.title_label.config(font=("Arial", 20))
        self.title_label.pack(pady=30)

        # Nastavení tlačítek pro kompresi
        self.start_button = tk.Button(self.root, text="Start", command=self.start_action, width=15)
        self.start_button.pack(pady=30)

        # Nastavení tlačítek pro nápovědu
        self.help_button = tk.Button(self.root, text="Help", command=self.help_action, width=15)
        self.help_button.pack(pady=30)

        # Nastavení tlačítek pro ukončení programu
        self.quit_button = tk.Button(self.root, text="Exit", command=self.quit_action, width=15)
        self.quit_button.pack(pady=30)

        # Nastavení šířky a výšky okna
        self.root.geometry("500x400")
        # Nastavení nezměnitelnosti velikosti okna
        self.root.resizable(False, False)

    def start_action(self):
        """
        Metoda pro spuštění komprese textového souboru.
        Zahájení akce -> zobrazení dialogu pro výběr souboru.
        """
        self.show_file_dialog()

    def save_file(self, content):
        """
        Metoda pro uložení komprimovaného textového souboru.
        :param content: Obsah, který se má uložit do souboru.
        """
        try:
            FileSaver.save_file(content)
        except Exception as e:
            self.log_error(f"Unable to save the file: {str(e)}")

    def log_error(self, error_message):
        """
        Metoda pro zapsání chyby do logu.
        :param error_message: Chybová hláška.
        """
        error_log_path = "Log/ErrorFileLog.txt"
        with open(error_log_path, 'a') as error_file:
            now = datetime.now()
            current_time = now.strftime("%Y-%m-%d %H:%M:%S")
            error_file.write(f"{current_time}: {error_message}\n\n")

    def show_file_dialog(self):
        """
        Metoda pro zobrazení dialogového okna pro výběr souboru.
        """
        file_dialog = tk.Toplevel(self.root)
        file_dialog.title("File Selection")

        label = tk.Label(file_dialog, text="Select a text file for compression")
        label.pack(padx=20, pady=20)

        button = tk.Button(file_dialog, text="Select File",
                           command=lambda: self.choose_file_for_compression(file_dialog))
        button.pack(pady=10)

    def choose_file_for_compression(self, file_dialog):
        """
        Metoda pro výběr souboru pro kompresi.
        :param file_dialog: Dialogové okno pro výběr souboru.
        """
        file_dialog.destroy()  # Zavřít dialogové okno po výběru souboru
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

        if file_path:
            try:
                with open(file_path, 'r') as file:
                    original_content = file.read()
                    content = TextCompression.compress(original_content)
                    self.show_save_dialog(content)  # Zobrazit dialog pro výběr místa uložení souboru
                chosen_file_log_path = "Log/ChosenFileLog.txt"
                with open(chosen_file_log_path, 'w') as chosen_file_log:
                    now = datetime.now()
                    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
                    chosen_file_log.write(f"Success! Selected file: " + file_path + f", creation time: {current_time}\n")
                original_file_path = "Data/Original.txt"
                with open(original_file_path, 'w') as original_file:
                    original_file.write(original_content)
            except Exception as e:
                messagebox.showerror("Error", f"Unable to open file: {str(e)}")

    def show_save_dialog(self, content):
        """
        Metoda pro zobrazení dialogového okna pro výběr umístění uložení souboru.
        :param content: Obsah, který se má uložit do souboru.
        """
        try:
            def save_and_close():
                """
                Metoda pro zavření dialogového okna.
                """
                save_dialog.destroy()

            save_dialog = tk.Toplevel(self.root)
            save_dialog.title("Save Location")

            label = tk.Label(save_dialog, text="Choose a location to save the compressed file")
            label.pack(padx=20, pady=20)

            button = tk.Button(save_dialog, text="Select Location",
                               command=lambda: [self.save_file(content), save_and_close()])
            button.pack(pady=10)
        except Exception as e:
            self.log_error(f"Unable to display save dialog: {str(e)}")

    def help_action(self):
        """
        Metoda pro zobrazení nápovědy.
        """
        try:
            self.root.withdraw()
            help_window = HelpWindow(self.root, self.root)
            self.root.wait_window(help_window.help_window)
        except Exception as e:
            self.log_error(f"Error starting 'Help': {str(e)}")

    def quit_action(self):
        """
        Metoda pro ukončení programu.
        """
        try:
            self.root.destroy()
        except Exception as e:
            self.log_error(f"Error quitting the program: {str(e)}")
