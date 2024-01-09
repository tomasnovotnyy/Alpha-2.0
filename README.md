# Alpha-2.0 (Ztrátová komprese textového souboru)

# *Popis programu*
Alpha-2.0 je aplikace, která je určena pro práci s textovými soubory, umožňuje uživateli provádět kompresi a dekompresi textu. Program je rozdělen do několika tříd, které zastávají různé úkoly, včetně uživatelského rozhraní, správy souborů a manipulace s textem. Tento program je napsán v jazyce Python s využitím knihoven Tkinter pro uživatelské rozhraní.
</br></br>

# *Spuštění programu*
Pro správné spuštění aplikace je třeba mít nainstalovaný Python a je zapotřebí spustit skript Main.py z terminálu.</br>
## *Spuštění skriptu Main.py:*
1. Stáhněte si .zip soubor programu do svého PC.
2. Soubor extrahujte. Extrahovaný soubor bude obsahovat 3 následující soubory:
   - Složka Alpha, kde je uložený celý projekt.
   - Textový soubor s odkazem na tuto GitHub stránku a s kontaktem na mě.
   - README.md soubor v Markdown formátu.
4. Spusťte si příkazový řádek.
5. Pomocí příkazu `cd` se dostaňte ke složce, kde máte uložený projekt.
6. Následně se ve složce programu přesuňte do složky `Classes`.
7. Pokud jste již ve složce `Classes`, tak program spustíte následujícím příkazem: `python Main.py`

Po úspěšném spuštění skriptu se program inicializuje a zobrazí uživatelské rozhraní, které umožní interakci a využití všech funkcí aplikace.
</br></br>

# *Struktura projektu*

- `/Classes`: Adresář obsahující třídy pro funkcionalitu aplikace.
- `/Data`: Adresář pro uložení dat aplikace ->
  - kopie originálního souboru pro kompresi
  - komprimovaný soubor
  - dekomprimovaný soubor
  - slovník zkratek
- `/Log`: Adresář pro logování chyb a událostí.
</br></br>

# *Třída UI.py*

Třída `UI` obsahuje funkce pro interakci uživatele s aplikací. Proces komprese textového souboru je spuštěn voláním metody `start_action`. Uživatel má možnost vybrat textový soubor pro kompresi a zobrazit nápovědu, stejně jako ukončit aplikaci pomocí tlačítka "Konec".

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
- **Ukončení programu**: Pro ukončení aplikace slouží tlačítko "Konec".
</br></br>

# *Třída FileSaver.py*
Třída `FileSaver` poskytuje funkce pro ukládání a správu komprimovaných a dekomprimovaných souborů.

## *Metody*
`save_file(content)`: Ukládá obsah do textového souboru na základě poskytnutého vstupu. Po uložení komprimovaného souboru se zobrazí dialogové okno pro případnou dekompresi.</br>

### Parametry:
  - `content`
    - Obsah, který se má uložit do souboru.

## *Použití*
1. Uživatel je vyzván k výběru umístění pro uložení souboru.
2. Soubor je uložen a zkomprimován.
3. Zobrazí se informační okno o úspěšném uložení.
4. Uživatel je dotázán, zda chce soubor dekódovat zpět.
5. Pokud uživatel souhlasí s dekompresí, zobrazí se dialog pro výběr umístění pro dekomprimovaný soubor.

## *Popis chyb*
Při chybě při ukládání souboru se zobrazí chybové hlášení a chyba se zaznamená do logu.</br></br>

# *Třída TextCompression.py*
Třída `TextCompression` poskytuje metody pro kompresi textových dat pomocí vlastního kompresního algoritmu.

## *Metody*
`compress(text)`: Komprimuje vstupní text pomocí kompresního algoritmu.

### Parametry:
  - `text`
    - Vstupní text pro kompresi.
  
### Návratová hodnota:
  - `str`
     - Kompresovaný text.

Tato metoda používá mou vlastní kompresní techniku -> odstraňuje interpunkci, identifikuje často se vyskytující se slova, přiřazuje zkratky a vytváří slovník pro budoucí dekompresi. V případě jakýchkoli chyb během komprese zaznamenává podrobnosti o chybách.

## *Vygenerované soubory*
- Soubor se slovníkem: ../Data/Dictionary.txt
- Logovací soubor: ../Log/DictionaryFileLog.txt
- Chybový logovací soubor: ../Log/ErrorFileLog.txt

Metoda `compress(text)` generuje soubor se slovníkem obsahujícím zkratky pro slova použitá při kompresi. Zároveň zaznamenává proces v logovacím souboru a jakékoliv chyby během komprese do chybového logovacího souboru.</br></br>

# *Třída TextDecompression.py*
Třída `TextDecompression` poskytuje metodu pro dekompresi textu pomocí poskytnutého slovníku.

## *Metody*
`decompress(compressed_text, dictionary_file_path)`: Dekomprimuje poskytnutý text pomocí poskytnutého slovníku.

### Parametry:

- `compressed_text`
  - Kompresovaný text, který má být dekomprimován.
- `dictionary_file_path`
  - Cesta k souboru se slovníkem pro dekompresi.

### Návratová hodnota:
- `str`
  - Dekomprimovaný text nebo chybová zpráva v případě neúspěchu.

Tato metoda poskytuje funkci pro dekomprimaci textu na základě poskytnutého slovníku. V případě chyby zaznamenává událost do chybového logu.
</br></br>

# *Třída HelpWindow.py*
