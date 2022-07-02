
def main():
    g = Game()
    
    while g.answer != "q":
        print()
        g.makeItRandom()
        answer1 = input("Pick one: rock, paper, scissors, lizard, spock:  ")
        print()
        g.answer = answer1
        print()
        print("You Choose ({})".format(g.answer))
        print()
        g.print()
        print()
        g.letsCheck()

if __name__ == "__main__":
    main()
