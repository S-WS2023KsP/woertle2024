def woertle_uebung():
    # Leere Liste zur Speicherung der Teile
    words_list = []

    print("Geben Sie Textzeilen ein (leere Zeile zum Beenden):")

    # Endlosschleife zum Einlesen der Zeilen
    while True:
        # Einlesen der Zeile
        line = input()

        # Beenden, wenn die Eingabezeile leer ist
        if line == "":
            break

        # Aufteilen der Zeile in durch Leerzeichen getrennte Teile
        parts = line.split()

        # Teile der Liste hinzufügen
        words_list.extend(parts)

    # Liste sortieren und ausgeben
    words_list.sort()
    print("Sortierte Liste:", words_list)

# Aufruf der Funktion, wenn das Skript ausgeführt wird
if __name__ == "__main__":
    woertle_uebung()
