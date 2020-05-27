import math
import random
rand = random.randint(1, 3)

play_str=input("Would you like to play the Game of Nim? (0=no, 1=yes) ")

human = int(0)     # Initialize the number of times humans win the game
computer = int(0)  # Initialize the number of times computer win the game

def minimax(curDepth, nodeIndex,
            maxTurn, scores,
            targetDepth):

    if (curDepth == targetDepth):
        return scores[nodeIndex]

    if (maxTurn):
        return max(minimax(curDepth + 1, nodeIndex * 2,
                           False, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1,
                           False, scores, targetDepth))

    else:
        return min(minimax(curDepth + 1, nodeIndex * 2,
                           True, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1,
                           True, scores, targetDepth))


scores = [1,2,3]

treeDepth = math.log(len(scores), 2)
while int(play_str) != 0:

    pile1 = int(12)
    pile2 = int(12)
    print("Start --> Pile 1:",pile1,"   Pile 2:",pile2)

    while (pile1 > 0) or (pile2 > 0):
        pile = int(input("Choose a pile (1 or 2): "))

        while ((pile == 1)and(pile1 == 0))or((pile == 2)and(pile2 == 0)):
            # If one of the piles is empty. No more stones can be removed from this pile.

            print("Pile must be 1 or 2 and non-empty. Please try again.")
            pile = int(input("Choose a pile (1 or 2): "))

        else:

            while (pile != 1) and (pile != 2): # If the number of the pile is not legal. Can't continue.


                print("Pile must be 1 or 2 and non-empty. Please try again.")
                pile = int(input("Choose a pile (1 or 2): "))

            else:
                stones = int(input("Choose stones to remove from pile: "))

                while (stones > 3) or (stones < 1):


                    print("Invalid number of stones. Please try again.")
                    stones = int(input("Choose stones to remove from pile: "))

                else:
                    print("Player -> ",end='')
                    print("Remove",stones,"stones from pile",pile)

                    if (pile == 1) and (pile1 >= stones):
                        #If it is pile1 and there are enough stones in the pile1.

                        pile1 = pile1 - stones
                        print("Pile 1:",pile1,"   Pile 2:",pile2)

                        if (pile1 <= 0) and (pile2 <= 0):
                            # If the piles are taken empty.

                            human = human + 1  # Humans win the game plus one.
                            print("\nPlayer wins!")
                            print("Score -> human:",human,"; computer:",computer)

                        else:


                            if (pile2 > 0):


                                pile2 = pile2 - rand
                                print("Computer -> ",end='')
                                print("Removed stones from pile 2")
                                print("Pile 1:",pile1,"   Pile 2:",pile2)

                            else:


                                pile1 = pile1 - rand
                                print("Computer -> ",end='')
                                print("Removed stones from pile 1")
                                print("Pile 1:",pile1,"   Pile 2:",pile2)

                            if (pile1 <= 0) and (pile2 <= 0):
                                # The stones was taken empty by computer.

                                computer = computer + 1  # Computer win the game plus one.
                                print("\nComputer wins!")
                                print("Score -> human:",human,"; computer:",computer)

                    if (pile == 2) and (pile2 >= stones):
                        # If it is pile2 and there are enough stones in the pile2.

                        pile2 = pile2 - stones
                        print("Pile 1:",pile1,"   Pile 2:",pile2)

                        if (pile1 <= 0) and (pile2 <= 0):
                            # If the piles are taken empty.

                            human = human + 1  # Humans win the game plus one.
                            print("\nPlayer wins!")
                            print("Score -> human:",human,"; computer:",computer)

                        else:
                            # The stones was not taken by humans.

                            if (pile1 > 0):
                                # If the pile1 is not taken empty.

                                pile1 = pile1 - rand
                                print("Computer -> ",end='')
                                print("Removed stones from pile 1")
                                print("Pile 1:",pile1,"   Pile 2:",pile2)

                            else:
                                # If the pile1 is taken empty.

                                pile2 = pile2 - rand
                                print("Computer -> ",end='')
                                print("Removed stones from pile 2")
                                print("Pile 1:",pile1,"   Pile 2:",pile2)

                            if (pile1 <= 0) and (pile2 <= 0):
                                # The stones was taken empty by computer.

                                computer = computer + 1
                                print("\nComputer wins!")
                                print("Score -> human:",human,"; computer:",computer)

    else:
        play_str = input("\nWould you like to play again? (0=no, 1=yes) ")


else:
   print("\nThanks for playing! See you again soon!")