import string

def woertle_uebung(dateiname, ausgabedatei):
    # Leere Menge zur Speicherung der einzigartigen Wörter
    unique_words = set()

    # Satzzeichen und unerwünschte Sonderzeichen definieren
    unerwuenschte_zeichen = string.punctuation + "„“"

    try:
        # Datei öffnen und Zeilen lesen
        with open(dateiname, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Die Datei {dateiname} wurde nicht gefunden.")
        return

    # Zeilen verarbeiten
    for line in lines:
        # Entfernen von führenden und nachfolgenden Leerzeichen
        line = line.strip()

        # Leerzeilen überspringen
        if not line:
            continue

        # Entfernen von Satzzeichen und unerwünschten Sonderzeichen
        line = line.translate(str.maketrans('', '', unerwuenschte_zeichen))

        # Aufteilen der Zeile in durch Leerzeichen getrennte Teile
        parts = line.split()

        # Wörter mit genau fünf Zeichen zur Menge hinzufügen
        for word in parts:
            if len(word) == 5:
                unique_words.add(word.lower())

    # Wörter in eine neue Datei schreiben
    with open(ausgabedatei, 'w') as file:
        for word in sorted(unique_words):
            file.write(word + '\n')

    # Statistische Daten ausgeben
    print(f"Anzahl der Wörter: {len(unique_words)}")
    print(f"Anzahl der einzigartigen Wörter: {len(unique_words)}")

# Aufruf der Funktion, wenn das Skript ausgeführt wird
if __name__ == "__main__":
    dateiname = "/Users/metehandurdu/Desktop/FOM/3.Semester/Skriptsprachenorientiertes Programmieren (Python)/Klausur/Woertle_Uebung/eingabedatei.txt"
    ausgabedatei = "/Users/metehandurdu/Desktop/FOM/3.Semester/Skriptsprachenorientiertes Programmieren (Python)/Klausur/Woertle_Uebung/ausgabedatei.txt"
    woertle_uebung(dateiname, ausgabedatei)