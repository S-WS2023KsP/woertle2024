def woertle_uebung(dateiname):
    # Leere Liste zur Speicherung der Teile
    words_list = []

    
    # Datei öffnen und Zeilen lesen
    with open(dateiname, 'r') as file:
        lines = file.readlines()
    

    # Zeilen verarbeiten
    for line in lines:
        # Entfernen von führenden und nachfolgenden Leerzeichen
        line = line.strip()

        # Leerzeilen überspringen
        if not line:
            continue

        # Aufteilen der Zeile in durch Leerzeichen getrennte Teile
        parts = line.split()

        # Teile der Liste hinzufügen
        words_list.extend(parts)

    # Liste sortieren und ausgeben
    words_list.sort()
    print("Sortierte Liste:", words_list)

# Aufruf der Funktion, wenn das Skript ausgeführt wird
if __name__ == "__main__":
    dateiname = "/Users/metehandurdu/Desktop/FOM/3.Semester/Skriptsprachenorientiertes Programmieren (Python)/Klausur/Woertle_Uebung/eingabedatei.txt"
    woertle_uebung(dateiname)