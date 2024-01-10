import tkinter as tk
from tkinter import scrolledtext, messagebox


class HelpWindow:
    """
    Třída HelpWindow reprezentuje okno nápovědy.
    :Metody:
    - __init__(self, root, main_window): Inicializace instance okna nápovědy.
    - return_home(self): Metoda pro návrat na úvodní obrazovku.
    - on_close(self): Metoda pro zavření okna nápovědy a zachycení zavíracího signálu.
    """
    def __init__(self, root, main_window):
        """
        Inicializace instance okna nápovědy.
        :param root: Hlavní okno aplikace.
        :param main_window: Reference na hlavní okno pro návrat zpět.
        """
        self.root = root
        self.main_window = main_window
        self.help_window = tk.Toplevel(self.root)
        self.help_window.title("Help")
        self.help_window.geometry("500x400")  # Nastavení velikosti okna
        self.help_window.resizable(False, False)  # Nastavení nezměnitelnosti velikosti okna

        self.scroll_text = scrolledtext.ScrolledText(self.help_window, wrap=tk.WORD, width=60, height=20)
        self.scroll_text.pack(expand=True, fill='both')

        self.scroll_text.insert(tk.END, "Application usage:\n\n"
                                        "1. Start by clicking on the 'Start' button.\n\n"
                                        "2. Choose a text file for compression via the dialog window.\n"
                                        "(Note: Only files with the .txt extension are supported)\n\n"
                                        "3. After successfully selecting the file, compression will be initiated.\n\n"
                                        "4. Click on the 'Select Location' button in the new window to save the file.\n"
                                        "The compressed file will be automatically saved to the location you choose.\n\n"
                                        "5. For decompression of the compressed file, select 'Yes' when prompted whether you want to decode the file back.\n\n"
                                        "6. In the new window, select where you want to save the decompressed file.\n"
                                        "(Decompression allows you to save the original content.)\n\n"
                                        "7. To exit the program, click on the 'Exit' button.")

        self.scroll_text.configure(state='disabled')  # Nastavení ScrolledText jako jen pro čtení

        self.return_button = tk.Button(self.help_window, text="Back to Home Screen", command=self.return_home)
        self.return_button.pack(side=tk.BOTTOM, pady=10)

        # Zachycení zavíracího signálu
        self.help_window.protocol("WM_DELETE_WINDOW", self.on_close)

    def return_home(self):
        """
        Metoda pro návrat na úvodní obrazovku hlavního okna.
        """
        self.help_window.destroy()  # Zavření okna nápovědy
        self.main_window.deiconify()  # Odkrytí původního okna

    def on_close(self):
        """
        Metoda pro zavření okna nápovědy a zachycení zavíracího signálu.
        :return: Zastavení běhu programu a vypsání chybové hlášky.
        """
        self.root.withdraw()  # Skrytí hlavního okna
        messagebox.showerror("Error", "Cannot close the help window!\nReturn to the home screen.")
