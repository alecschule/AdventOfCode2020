with open('input.txt') as f:
    availableSeats = [[ True for i in range(8) ] for j in range(128)]
    for line in f.readlines():
        row = int(line[:7].replace('F', '0').replace('B', '1'), 2)
        column = int(line[7:].replace('L', '0').replace('R', '1'), 2)
        availableSeats[row][column] = False
    # given an array of available seats, pick the one most in the middle
    bestChoice = (None, None)
    for i in range(64):
        for j in range(8):
            if availableSeats[i][j]:
                bestChoice = (i, j)
            if availableSeats[127-i][j]:
                bestChoice = (127-i, j)
    print(bestChoice[0]*8 + bestChoice[1])
