import tkinter as tk
import unittest
from datetime import datetime
from src.UI.UI import UI
from src.Test.TestTextCompression import TestTextCompression


# Funkce pro zaznamenávání chyb do logu
def log_error(error_message):
    """
    Zapisuje chybové hlášky do souboru ErrorFileLog.txt.
    :param error_message: Chybová hláška.
    """
    error_log_path = "Log/ErrorFileLog.txt"
    with open(error_log_path, 'a') as error_file:
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        error_file.write(f"{current_time}: {error_message}\n\n")


# Hlavní část programu
if __name__ == "__main__":
    try:
        root = tk.Tk()  # Inicializace hlavního okna Tkinter
        app = UI(root)  # Vytvoření instance uživatelského rozhraní
        root.mainloop()  # Spuštění hlavní smyčky pro zobrazení GUI
        unittest.main(exit=False)  # Spuštění testů
    except Exception as e:
        log_error(f"Main Error: {str(e)}")  # Zaznamenání hlavní chyby do logu
