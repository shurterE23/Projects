#define play again
def play_again():
    print('Would you like to play again? (y or n)')

    choice = input('>').lower()

    if 'y' in choice:
        start()
    else:
        exit()

#game over
def game_over(reason):
    print('\n' + reason)
    print('Game Over!')
    play_again()

#treasure room
def treasure_room():
    print('You are greeted by a room filled with treasure chests all of which are opened exposing the gold coins inside')
    print("you've never seen so much wealth in one place!")
    input()
    print('Do you make a break for the exit leaving the gold behind?  Or do you load your pockets with as much as you can before leaving?')
    print('1) GRAB THE LOOT AND RUN!')
    print("2) Leave the gold behind there's no telling what curses come along with it.")

    choice = input('>')

    if choice =='1':
        print('You grab as much gold as you can and open the door to the exit')
        print('You are greeted by a man asking you for the toll to leave.  You toss the man a gold coin and you head on your way.')
        print("Good job you've won the game!")
        play_again()

    elif choice == '2':
        print('You honest person, you.  You leave the gold and whatever curses come with it and leave the room')
        input()
        print("Upon opening the door you're greeted by a man asking you for the toll to pass through the door.")
        input()
        print('You reach into your pockets realizing you have nothing to offer.')
        input
        print('The man puts a curse on you and you immediately burst into a cloud of dust.')
        game_over("Next time I'm sure you'll pay yourself first.")

    else:
        game_over('You had one job.  To just pick one of the two numbers.')



#snakepitroom
def snake_pit():
    print('You open the door and immediately hear hissing')
    input()
    print("You take a look around and there's a snakepit at your feet with a rope bridge going across it.")
    input()
    print("You also notice there is a very tiny ledge across one of the walls, it looks like it's barely small enough to inch across the snakepit")
    input()
    print('Which would you like to do?')
    input()
    print(' 1) Take the rope bridge')
    print(' 2) Walk along the edge.')

    choice = input('>')

    if choice == '1':
        #game over
        game_over('The rope bridge immediately snaps and you fall to the snakepit never to be seen again!')
    elif choice == '2':
        #continue to treasure room
        print('\nYou successfully climb across the small ledge and make it to the door on the other side')
        treasure_room()
    else:
        game_over("I didn't think the game would end because you didn't pick one of two numbers..")

def dragon_room():
    #some dialogue and storytelling
    print('You open the door and hear thunderous snoring.  Slowly the snoring comes to a stop and you see yellow eyes light up')
    input()
    print("You suddenly realized you're locked in a room with a fire-breathing dragon!")
    input()
    print('Your eyes scan to room to plot your next move.  You notice a long sword halfway between you and the dragon.')
    input()
    print('You also notice a hole to the right of you.  Not knowing how deep or where it leads to, but may be a viable option.')
    input()
    print('Which will you choose?')
    print('1) To dive into the hole and pray for the best.')
    print('2) To lunge for the sword and fight the dragon')
        
    choice = input()

    if choice=='1':
        #continue to treasure room
        print("You dive into the hole hoping not knowing what's in the abyss.")
        input()
        print("You begin to feel around and realize you're in a tunnel")
        input()
        print('Slowly, you crawl through the dark until you see a light.  Following the light you pop up in a room filled with treasure all around you')
        treasure_room()

    elif choice=='2':
        print('You make a run for the sword and grab it and lock eyes with the dragon.')
        input()
        print("With no time to think twice about your next move, you vault off of the wall and lunge for the dragon's next making contact")
        input()
        print("The dragon's head comes clean off and you land on your feet victorious! Well done!")
        input()
        print("As you walk towards your exit the dragon's head lands on you.  Crushing you instantly.  Unlucky.")    
        game_over('Better luck next time')

    else:
        game_over("Imagine making it this far and losing because you misclicked")  

#place at end
def start():
    print('You wake up in a dark room.  Your eyes adjust to the low light and you notice there are 2 doors to choose from.')
    print('With no other options available you choose a door to open.  Which one do you open?  Type Left or Right.')

    choice = input('>').lower()

    if 'l' in choice:
    #if the reply was 'left' or 'l' the player ends up in the snakepit
        snake_pit()
    
    elif 'r' in choice:
    #if the reply is 'right' or 'r' the player ends up in the dragon room
        dragon_room()
    
    else:
        game_over('All you had to do was pick one of the two options!')
   
start()