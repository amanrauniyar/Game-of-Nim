play_str=input("Would you like to play? (0=no, 1=yes) ")

human = int(0)     # Initialize the number of times humans win the game
computer = int(0)  # Initialize the number of times computer win the game

while int(play_str) != 0:  # use while to determine if the game starts

    pile1 = int(12)
    pile2 = int(12)
    print("Start --> Pile 1:",pile1,"   Pile 2:",pile2)

    while (pile1 > 0) or (pile2 > 0):  # use while to determine if the pile is empty.
        pile = int(input("Choose a pile (1 or 2): "))

        while ((pile == 1)and(pile1 == 0))or((pile == 2)and(pile2 == 0)):
            # If one of the piles is empty. No more stones can be removed from this pile.

            print("Pile must be 1 or 2 and non-empty. Please try again.")
            pile = int(input("Choose a pile (1 or 2): "))

        else:

            while (pile != 1) and (pile != 2):
                # If the number of the pile is not legal. Can't continue.

                print("Pile must be 1 or 2 and non-empty. Please try again.")
                pile = int(input("Choose a pile (1 or 2): "))

            else:
                stones = int(input("Choose stones to remove from pile: "))

                while (stones > 3) or (stones < 1):
                    # If the number of the stones is not beween 1 and 3. Can't continue.

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
                            # The stones was not taken by humans.

                            if (pile2 > 0):
                                # If the pile2 is not taken empty.

                                pile2 = pile2 - 1
                                print("Computer -> ",end='')
                                print("Remove 1 stones from pile 2")
                                print("Pile 1:",pile1,"   Pile 2:",pile2)

                            else:
                                # If the pile2 is taken empty.

                                pile1 = pile1 - 1
                                print("Computer -> ",end='')
                                print("Remove 1 stones from pile 1")
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

                                pile1 = pile1 - 1
                                print("Computer -> ",end='')
                                print("Remove 1 stones from pile 1")
                                print("Pile 1:",pile1,"   Pile 2:",pile2)

                            else:
                                # If the pile1 is taken empty.

                                pile2 = pile2 - 1
                                print("Computer -> ",end='')
                                print("Remove 1 stones from pile 2")
                                print("Pile 1:",pile1,"   Pile 2:",pile2)

                            if (pile1 <= 0) and (pile2 <= 0):
                                # The stones was taken empty by computer.

                                computer = computer + 1  # Computer win the game plus one.
                                print("\nComputer wins!")
                                print("Score -> human:",human,"; computer:",computer)

    else:
        play_str = input("\nWould you like to play again? (0=no, 1=yes) ")
        # Judge whether to come again

else:
   print("\nThanks for playing! See you again soon!")