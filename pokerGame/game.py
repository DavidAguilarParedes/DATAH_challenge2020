from poker import PokerHand


if __name__ == "__main__":    

    while(1):

        #We ask for the cards
        print("\n POKER GAME by David Aguilar\n")

        string1 = input("Insert the first hand :") # "AH KH QH JH 9H"
        string2 = input("Insert the second hand :") #"5S 6S 7S 8S AH9S"
        
        #If everthing is ok ,we analize the hands and determine which
        #one is the stronger hand
        try:
            ans = PokerHand(string1).compare_with(PokerHand(string2))
        except Exception as e:
            ans = "error"


        # show the answer
        if ans == "WIN":
            message = "\n The first hand is the winner\n"
        elif ans == "LOSS":
            message = "\n The second hand is the winner\n"
        else:
            message = "error"

        print("*******  {}  *********".format(message))

       