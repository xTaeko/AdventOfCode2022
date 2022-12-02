import Commons
from itertools import cycle
# https://adventofcode.com/2022/day/2

# Rock      = A    X
# Paper     = B    Y
# Scissors  = C    Z

# What would your total score be if everything goes exactly according to your strategy guide?
def part_one():
    testinput = Commons.readInputAsStringList()
    testinput = [line.split(" ") for line in testinput]

    win = [['A', 'Y'], ['B', 'Z'], ['C', 'X']]
    draw = [['A', 'X'], ['B', 'Y'], ['C', 'Z']]
    lose = [['A', 'Z'], ['B', 'X'], ['C', 'Y']]

    points_for_winning = 0

    for game in testinput:
        if game in win:
            points_for_winning = points_for_winning + 6
        elif game in draw:
            points_for_winning = points_for_winning + 3
        elif game in lose:
            points_for_winning = points_for_winning
        else:
            print("We fucked up the winning")


    points_for_shape = 0

    for game in testinput:
        if game[1] == 'X': # Rock
            points_for_shape = points_for_shape + 1
        elif game[1] == 'Y': # Paper
            points_for_shape = points_for_shape + 2
        elif game[1] == 'Z': # Scissors
            points_for_shape = points_for_shape + 3
        else:
            print("We fucked up the shape thing")


    result = points_for_winning + points_for_shape
    print(result)

    return result



# Rock      = A
# Paper     = B
# Scissors  = C

# Lose = X
# Draw = Y
# Win = Z
#Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?

def part_two():
    testinput = Commons.readInputAsStringList()
    testinput = [line.split(" ") for line in testinput]


    ## The point for the shapes are the index + 1
    shapes = ['A', 'B', 'C']
    # index    0    1    2
    # points   1    2    3

    points = 0
    for game in testinput:
        if game[1] == 'X': # lose
            points = points + 0
            points = points + ((shapes.index(game[0]) - 1) % 3) + 1
        elif game[1] == 'Y': # draw
            points = points + 3
            points = points + ((shapes.index(game[0])) % 3)     + 1
        elif game[1] == 'Z': # win
            points = points + 6
            points = points + ((shapes.index(game[0]) + 1) % 3) + 1

    ## Explaination
    # To win you need the shape one index further of the shape of your opponent (index + 1): If they have A, you need B. If they have C, you need A -- Cycle through the list
    # To lose you need the shape one index before the shape of your opponent (index - 1): If they have A, you need C. If they have C, you need B -- Cycle through the list
    # In case of draw, you just need the same shape so the index stays the same  (index)
    # Since you cycle through the list the index you need may be higher then your list is. So you need to calculate modolo len(list) in our case 3
    # For the points just add one. Since points for shapes are the index of your shape +1

    print(points)
    return points

print("Part 1 result is: ")
part_one()
print("Part 2 result is: ")
part_two()