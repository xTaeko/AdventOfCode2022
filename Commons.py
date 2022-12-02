from typing import List


def readTestInputAsStringList():
    with open("TestInput.txt") as file:
        content = [line for line in file.read().splitlines()]
        return content

def readInputAsStringList():
    with open("Input.txt") as file:
        content = [line for line in file.read().splitlines()]
        return content
