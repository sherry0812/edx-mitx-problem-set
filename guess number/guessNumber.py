
h = 100
l = 0
g = (h+l)//2
  
print('Please think of a number between 0 and 100')
print('Is your secret number ' + str(g) + '?')
x = input('Enter h to indicate the guess is too high. Enter l to indicate the guess is too low. Enter c to indicate I guessed correctly.')

while not x == 'c':
    if x != 'h' and x!= 'l':
        print('Sorry, I did not understand your input. Please try again.')
        x = input('h, l, or c?')
    elif x == 'h':
        h = g
        g = (h+l)//2
        print('Is yor secret number ' + str(g))
        x = input('Enter h to indicate the guess is too high. Enter l to indicate the guess is too low. Enter c to indicate I guessed correctly.')
    elif x == 'l':
        l = g
        g = (h+l)//2
        print('Is yor secret number ' + str(g))
        x = input('Enter h to indicate the guess is too high. Enter l to indicate the guess is too low. Enter c to indicate I guessed correctly.')
if x == 'c':
    print('Game over. Your secret number is ' + str(g))



    