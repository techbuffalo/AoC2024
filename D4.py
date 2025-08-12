from itertools import count


def findXMAS(wordSearchTxt):
    lines = wordSearchTxt.strip().split("\n")
    grid = [list(line) for line in lines]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    targetWord = "XMAS"
    wordLength = len(targetWord)
    count = 0
    found_positions = []

    directions = [
        (0, 1),  # right
        (0, -1),  # left
        (1, 0),  # down
        (-1, 0),  # up
        (1, 1),  # diagonal down-right
        (1, -1),  # diagonal down-left
        (-1, 1),  # diagonal up-right
        (-1, -1)  # diagonal up-left
    ]

    #Checking the position to make sure the directions don't move outside the wordsearch boundary
    def validPositionCheck(row, col):
        return 0 <= row < rows and 0 <= col < cols

    #Making the movement aspect of the search based on the directions list
    def wordPositionCheck(startRow, startCol, directionalIndex):
        dirRow, dirCol = directions[directionalIndex]

        endRow = startRow + dirRow * (wordLength - 1)
        endCol = startCol + dirCol * (wordLength - 1)

        #Checking that our new end row and collumn are valid positions
        if not validPositionCheck(endRow, endCol):
            return False

        #Check each letter of our valid starting position
        for i in range(wordLength):
            row = startRow + dirRow * i
            col = startCol + dirCol * i
            if grid[row][col] != targetWord[i]:
                return False

        return True

    for row in range(rows):
        for col in range(cols):
            for directionalIndex in range(8):
                if wordPositionCheck(row, col, directionalIndex):
                    count += 1

    print(count)

def main():
    with open("input.txt") as inputFile:
        wordSearchTxt = inputFile.read()
    result = findXMAS(wordSearchTxt)  # Call the function!


if __name__ == "__main__":
    main()