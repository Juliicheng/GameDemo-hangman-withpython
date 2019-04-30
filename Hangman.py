import random
import sys


def initial():  # initial function to set the game ready for play
    food = ['apple', 'orange', 'grape', 'melon', 'pomelo', 'banana', 'lemon', 'onion', 'berry',
             'butter', 'steak', 'cream', 'pizza', 'noodle', 'potato', 'tomato', 'mango', 'almond']
    animal = ['monkey', 'elephant', 'horse', 'lizard', 'frog', 'rabbit', 'chicken', 'sheep', 'lion',
               'donkey', 'kangaroo', 'jellyfish', 'tiger', 'penguin', 'koala', 'giraffe', 'zebra']
    global rantag   # I'm not using any database here, bcz this is just a demo.
    rantag = random.randint(0, 1)
    x = random.randint(0, 17)
    if rantag == 0:
        answer = food[x]
        rantag = 'food'
    else:
        answer = animal[x]
        rantag = 'animal'
    global lanswer      # use global variables to record the answer
    global shader       # ready a shader to enhance UI
    lanswer = list(answer)      # break the word into a list
    shader = ['_']
    for i in range(1, lanswer.__len__()):
        shader.append('_')              # finish the shader


def compare():      # compare function
    for i in range(0, lanswer.__len__()):       # compare from first char to last
        if lanswer[i] == guess:
            shader[i] = guess              # if the answer is right, remove the shaders


def main():         # main function for game
    initial()       # call the initial function to setup the game
    global guess
    print('The answer is ' + str(rantag) + ' and is ' + str(lanswer.__len__()) + ' characters long.')
    print(' '.join(shader))
    for i in range(0, 8):       # for loop to record the trying times
        print('You have ' + str(8-i) + ' chances to go')
        guess = input("Guess a letter!")
        if guess.isalpha() and len(guess) == 1:     # valid the input to be one letter
            compare()              # if the input is valid, call compare func
            print(' '.join(shader))         # the shader has been changed by compare func, print that again
            if '_' not in shader:       # if statement to check if the user already win
                print("You Win!")
                sys.exit()              # if there is no '_' in shader, which means user win, end program
        else:
            print('Invalid input, you wasted one chance')       # if the input is invalid
            print(' '.join(shader))
    print("You lose, the right answer is \n" + ''.join(lanswer))        # end of for loop, means user failed


if __name__ == "__main__":
    main()



