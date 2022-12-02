import Commons
# https://adventofcode.com/2022/day/1

# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
def part_one():
    testinput = Commons.readInputAsStringList()
    divided_by_elves = [[0]]
    elve_index = 0

    for food in testinput:
        if food == '':
            elve_index = elve_index + 1
            divided_by_elves.append([0])
        else:
            divided_by_elves[elve_index].append(int(food))

    divided_by_elves = list(map(sum, divided_by_elves))

    result = max(divided_by_elves)
    print(result)
    return result

# Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
def part_two():
    testinput = Commons.readInputAsStringList()
    divided_by_elves = [[0]]
    elve_index = 0

    for food in testinput:
        if food == '':
            elve_index = elve_index + 1
            divided_by_elves.append([0])
        else:
            divided_by_elves[elve_index].append(int(food))

    divided_by_elves = list(map(sum, divided_by_elves))

    divided_by_elves.sort(reverse=True)
    result = divided_by_elves[0] + divided_by_elves[1] + divided_by_elves[2]

    print(result)
    return result

print("Part 1 result is: ")
part_one()
print("Part 2 result is: ")
part_two()