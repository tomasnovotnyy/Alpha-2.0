# Alpha-2.0 (Ztrátová komprese textového souboru)

# *Popis programu*
- Alpha-2.0 je aplikace, která je určena pro práci s textovými soubory, umožňuje uživateli provádět kompresi a dekompresi textu.
- Program je rozdělen do několika tříd, které zastávají různé úkoly, včetně uživatelského rozhraní, správy souborů a manipulace s textem.
- Tento program je napsán v jazyce Python s využitím knihoven Tkinter pro uživatelské rozhraní.
- Program je primárně navržen pro anglický jazyk. Může být použit i pro jiné jazyky, ale je nutné, aby se jednalo o jazyk bez háčků a čárek. -> To je také důvod, proč je UI a celkově celé rozhraní aplikace v angličtině.
</br></br>

# *Spuštění programu*
Pro správné spuštění aplikace je třeba mít nainstalovaný Python a je zapotřebí spustit skript Main.py z terminálu.</br>
## *Spuštění skriptu Main.py:*
1. Stáhněte si .zip soubor programu do svého PC.
2. Soubor extrahujte. Extrahovaný soubor bude obsahovat 3 následující soubory:
   - Složka Alpha2.0, kde je uložený celý projekt.
   - Textový soubor s odkazem na tuto GitHub stránku a s kontaktem na mě.
   - README.md soubor v Markdown formátu.
4. Spusťte si příkazový řádek.
5. Pomocí příkazu `cd` se dostaňte do složky, kde máte uložený projekt.
6. Pokud jste již uvnitř složky, kde máte uložený projekt, tak program spustíte následujícím příkazem: `python Main.py`

Po úspěšném spuštění skriptu se program inicializuje a zobrazí uživatelské rozhraní, které umožní interakci a využití všech funkcí aplikace.
</br></br>

# *Struktura projektu*
- `/Data`: Adresář pro uložení dat aplikace.
  - slovník zkratek
  - komprimovaný soubor
  - dekomprimovaný soubor
  - kopie originálního souboru pro kompresi
- `/Log`: Adresář pro logování chyb a událostí.
  - ChosenFileLog
  - DictionaryFileLog
  - CompressedFileLog
  - AbbreviationsFileLog
  - DecompressedFileLog
- `/src`: Adresář obsahující třídy pro funkcionalitu aplikace.
  - `/Compression`
    - TextCompression.py
  - `/Decompression`
    - TextDecompression.py
  - `/Saver`
    - FileSaver.py
  - `/Test`
    - TestTextCompression.py
  - `/UI`
    - HelpWindow.py
    - UI.py
- Main.py
</br></br>

# *Třída UI.py*

Třída `UI` obsahuje funkce pro interakci uživatele s aplikací. Proces komprese textového souboru je spuštěn voláním metody `start_action`. Uživatel má možnost vybrat textový soubor pro kompresi a zobrazit nápovědu, stejně jako ukončit aplikaci pomocí tlačítka "Exit".

## *Metody*
`__init__(self, root)`: Inicializuje objekt rozhraní, nastavuje základní vzhled a prvky okna.

`start_action(self)`: Spouští akci komprese textového souboru.

`save_file(self, content)`: Ukládá komprimovaný textový soubor.

`log_error(self, error_message)`: Zaznamenává chyby do logu.

`show_file_dialog(self)`: Zobrazuje dialogové okno pro výběr souboru.

`choose_file_for_compression(self, file_dialog)`: Vybere textový soubor pro kompresi.

`show_save_dialog(self, content)`: Zobrazuje dialogové okno pro výběr umístění uložení souboru.

`help_action(self)`: Zobrazuje okno nápovědy.

`quit_action(self)`: Ukončuje program.

## *Implementované funkce*

- **Komprese textu**: Uživatel vybírá textový soubor, který má být komprimován. Program komprimuje obsah souboru a umožňuje uživateli uložit komprimovaný soubor na vybraném umístění.
- **Nápověda**: Aplikace nabízí možnost zobrazit uživateli nápovědu, která obsahuje užitečné informace k použití programu.
- **Ukončení programu**: Pro ukončení aplikace slouží tlačítko "Exit".
</br></br>

# *Třída FileSaver.py*
Třída `FileSaver` poskytuje funkce pro ukládání a správu komprimovaných a dekomprimovaných souborů.

## *Metody*
`save_file(content)`: Ukládá obsah do textového souboru na základě poskytnutého vstupu. Po uložení komprimovaného souboru se zobrazí dialogové okno pro případnou dekompresi.</br>

## *Parametry*:
  - `content`
    - Obsah, který se má uložit do souboru.

## *Popis chyb*
Při chybě při ukládání souboru se zobrazí chybové hlášení a chyba se zaznamená do logu.
</br></br>

# *Třída TextCompression.py*
Třída `TextCompression` poskytuje metody pro kompresi textových dat pomocí vlastního kompresního algoritmu.

## *Metody*
`compress(text)`: Komprimuje vstupní text pomocí kompresního algoritmu.

Metoda `compress(text)` generuje soubor se slovníkem obsahujícím zkratky pro slova použitá při kompresi. Zároveň zaznamenává proces v logovacím souboru a jakékoliv chyby během komprese do chybového logovacího souboru.

## *Parametry*:
  - `text`
    - Vstupní text pro kompresi.
  
## *Návratová hodnota*:
  - `str`
     - Kompresovaný text.

Tato metoda používá mou vlastní kompresní techniku -> odstraňuje interpunkci, identifikuje často se vyskytující se slova, přiřazuje zkratky a vytváří slovník pro budoucí dekompresi. V případě jakýchkoli chyb během komprese zaznamenává podrobnosti o chybách.

## *Vygenerované soubory*
- Soubor se slovníkem: ../Data/Dictionary.txt
- Logovací soubor: ../Log/DictionaryFileLog.txt
- Chybový logovací soubor: ../Log/ErrorFileLog.txt
</br></br>

# *Třída TextDecompression.py*
Třída `TextDecompression` poskytuje metodu pro dekompresi textu pomocí poskytnutého slovníku.

## *Metody*
`decompress(compressed_text, dictionary_file_path)`: Dekomprimuje poskytnutý text pomocí poskytnutého slovníku.

## *Parametry*:

- `compressed_text`
  - Kompresovaný text, který má být dekomprimován.
- `dictionary_file_path`
  - Cesta k souboru se slovníkem pro dekompresi.

## *Návratová hodnota*:
- `str`
  - Dekomprimovaný text nebo chybová zpráva v případě neúspěchu.

Tato metoda poskytuje funkci pro dekomprimaci textu na základě poskytnutého slovníku. V případě chyby zaznamenává událost do chybového logu.
</br></br>

# *Třída HelpWindow.py*
Třída `HelpWindow` představuje okno nápovědy v aplikaci. Tato třída vám umožňuje získat nápovědu pro použití aplikace a vrátit se zpět na hlavní obrazovku aplikace.

## *Metody*
`__init__(self, root, main_window)`: Inicializuje novou instanci okna nápovědy.
   - `root`: Hlavní okno aplikace.
   - `main_window`: Reference na hlavní okno pro návrat zpět.

`return_home(self)`: Metoda pro návrat na úvodní obrazovku hlavního okna.

`on_close(self)`: Metoda pro zavření okna nápovědy a zachycení zavíracího signálu.
   - V případě zavření okna nápovědy vypíše chybovou hlášku.
</br></br>

# *Třída TestTextCompression.py*
Třída `TestTextCompression` je určena pro testování funkcionality třídy `TextCompression`.

## *Metody*
`test_file_compression(self)`: Metoda pro testování komprese textového souboru.
## *Návratová hodnota*: 
- Testuje, zda byl obsah souboru komprimován.

Tato třída pomáhá ověřit správnou funkčnost třídy `TextCompression` testováním její schopnosti komprimovat textové soubory.
</br></br>

# *Třída Main.py*
Třída `Main` obsahuje logiku pro spuštění hlavní části aplikace.

## *Ukázka třídy*
Soubor Main.py obsahuje vstupní bod aplikace. Spuštěním tohoto souboru je inicializováno hlavní okno a celý aplikační proces. Struktura třídy vypadá takto:
``` python
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

```

## *Popis*
`log_error(error_message)`: Funkce pro zaznamenávání chyb do logu. Chybové zprávy jsou zapisovány do souboru ErrorFileLog.txt v adresáři Log s časovým razítkem.

`__main__`: Hlavní běh programu. Inicializuje hlavní okno Tkinter a spouští hlavní uživatelské rozhraní aplikace UI.

## *Použití*
1. Po spuštění programu klikněte na tlačítko 'Start'.
2. Vyberte textový soubor pro kompresi přes dialogové okno. Podporované jsou soubory s příponou `.txt`.
3. Po úspěšném výběru souboru bude spuštěna komprese.
4. Klikněte na tlačítko 'Select Location' pro uložení souboru. Kompresovaný soubor se uloží na vybrané místo.
5. Pro dekompresi zvolte možnost 'Yes' v okně, které se Vás zeptá zda si přejete soubor dekódovat zpět.
6. Vyberte umístění pro uložení dekomprimovaného souboru.
7. Uloží se původní obsah souboru.
8. Ukončete program kliknutím na tlačítko 'Exit'.
</br></br>

# *Testování programu*
## *Unit Testy*
- Program byl podroben důkladnému testování pomocí unit testů využívajících třídu `TestTextCompression` pro ověření správnosti chování funkce pro kompresi textu.
## *Zpětná vazba uživatelů*
- Program byl také podroben testování a zkoušení ze strany přátel.
- Kamarádi, kteří program otestovali, poskytli pozitivní zpětnou vazbu. Zde jsou některé z jejich komentářů:
</br></br>
![Test (1)](https://github.com/tomasnovotnyy/Alpha-2.0/assets/84340580/5b9d0f96-2029-4549-a2cd-125d0fe12487)
</br>
