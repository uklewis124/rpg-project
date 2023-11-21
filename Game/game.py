def wrong_file():
    print("Unfortunately, you've ran the wrong file.")

def load():
    import os
    print("Game Loaded")
    os.system("cls" if os.name == "nt" else "clear")

def mainloop():
    print("Test")

if __name__ == '__main__':
    wrong_file()