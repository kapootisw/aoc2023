def isRevealValid(reveal):
    colorSets = reveal.split(", ")
    valid = 1
    for colorSet in colorSets:
        set = colorSet.split(" ")
        count = int(set[0])
        color = set[1]
        if color == "red":
            valid = valid and count <= 12
        elif "green" == color:
            valid = valid and count <= 13
        elif "blue" == color:
            valid = valid and count <= 14
        
        if not valid:
            break
    return valid

def part1(gameLines):
    validSum = 0
    for idx, game in enumerate(gameLines):
        reveals = game.strip().split(": ")[1].split("; ")
        gameIsValid = 1
        for reveal in reveals:
            gameIsValid = gameIsValid and isRevealValid(reveal)
            
            if not gameIsValid:
                break
        
        if gameIsValid:
            validSum += idx + 1

    print(validSum)


gameFile = open("Day02Input.txt", "r")
gameLines = gameFile.readlines()

powerSum = 0
for game in gameLines:
    reveals = game.strip().split(": ")[1].split("; ")
    redMin = -1
    greenMin = -1
    blueMin = -1
    for reveal in reveals:
        colorSets = reveal.split(", ")
        for colorSet in colorSets:
            set = colorSet.split(" ")
            count = int(set[0])
            color = set[1]
            if color == "red":
                redMin = count if redMin == -1 or redMin < count else redMin
            elif color == "green":
                greenMin = count if greenMin < count or greenMin == -1 else greenMin
            elif color == "blue":
                blueMin = count if blueMin < count or blueMin == -1 else blueMin

    power = redMin * greenMin * blueMin
    powerSum += power
    print(redMin, greenMin, blueMin, power, powerSum)
