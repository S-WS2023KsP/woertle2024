def woertle_uebung():
    words_list=[]
    print("Geben Sie einen Text ein (Enter = beenden)") 

    while True: 

        line = input()

        if line == "":
            break

        parts = line.split()
        words_list.extend(parts)

    words_list.sort()

    print("Sortierte Liste der Teile: ", words_list)

if __name__ == "__main__":
    woertle_uebung()