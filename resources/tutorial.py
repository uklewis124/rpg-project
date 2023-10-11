# Tutorial Resource
def from_file():
    print("You opened a resource file. Try running the main game file instead!")

def run_tutorial(player):
    import os, time
    class Game:
        def console_clear():
            os.system('cls' if os.name == 'nt' else 'clear')
        def __init__(self):
            print("Welcome to the game!")
        def next():
            time.sleep(0.5)
        def wait_prompt():
            input("Press enter to continue... ")
    
    Game.console_clear()
    print("Welcome to the tutorial!")
    Game.next()
    print("This tutorial will teach you the basics of the game.")
    Game.next()
    print("Let's get started!")
    Game.wait_prompt()
    
    #Tutorial begins here
    Game.console_clear()
    name = player.name
    print("Okay. First let's go over movement.")
    Game.next()
    print("You currently have access to the following areas:")
    Game.next()
    print("The Tavern")
    print("The Market")
    print("The Town Square")
    print("The Forest")
    print("Home")
    Game.wait_prompt()
    Game.console_clear()
    
    print("When prompted to move, You can type the name of the area you want to go to.")
    Game.next()
    print("For example, if you want to go to the tavern, type 'tavern'.")
    print("However, if you forget where you want to go, you can type 'help'.")
    Game.wait_prompt()
    Game.console_clear()
    print("Okay. I'm going to test you on moving now...")
    Game.wait_prompt()
    
    def movement_test():
        questions = [
            ["When can you move?","A) When prompted", "B) By typing the name of the place"],
            ["How do you move?","A) By typing the name of the place", "B) By typing 'move'"],
            ]
        randomized_answers = []
        for i in questions:
            randomized_answers.append(random.sample(i[1:], len(i[1:])))
        for i in range(len(questions)):
            print(questions[i][0])
            for j in randomized_answers[i]:
                print(j)
            answer = input("Answer: ")
            if answer == "A":
                print("Correct!")
                score += 1
            else:
                print("Incorrect!")
        Game.wait_prompt()
        Game.console_clear()
        print("Let's see how you did...")
        Game.next()
        Game.console_clear()
        print("You got {} out of {} correct!".format(score, len(questions)))
        Game.next()
        Game.console_clear()
        

if __name__ == "__main__":
    from_file()