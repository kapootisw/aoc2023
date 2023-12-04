def replaceSpelledOutWithDigits(word):
    if len(word) == 0:
        return ""
    
    match word:
        case "one":
            return "1"
        case "two":
            return "2"
        case "three":
            return "3"
        case "four":
            return "4"
        case "five":
            return "5"
        case "six":
            return "6"
        case "seven":
            return "7"
        case "eight":
            return "8"
        case "nine":
            return "9"

    return word if "one".startswith(word) or "two".startswith(word) or "three".startswith(word) or "four".startswith(word) or "five".startswith(word) or "six".startswith(word) or "seven".startswith(word) or "eight".startswith(word) or "nine".startswith(word) else replaceSpelledOutWithDigits(word[1:])

calibrationFile = open("Day01Input.txt", "r")
calibrationLines = calibrationFile.readlines()
calibrations = []

for cal in calibrationLines:
    firstDigit = ""
    lastDigit = ""
    word = ""
    for letter in cal:
        print(letter)
        if letter.isdigit():
            firstDigit = letter if firstDigit == "" else firstDigit
            lastDigit = letter
            word = ""
        else:
            word += letter
            wordDigit = replaceSpelledOutWithDigits(word)
            print(word, wordDigit)
            if wordDigit.isdigit():
                firstDigit = wordDigit if firstDigit == "" else firstDigit
                lastDigit = wordDigit
                word = letter
            elif wordDigit == "":
                word = replaceSpelledOutWithDigits(letter)
                print(word)
            else:
                word = wordDigit
    
    calibrations.append(int(firstDigit + lastDigit))

print(calibrations)
print(sum(calibrations))