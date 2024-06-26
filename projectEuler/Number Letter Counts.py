units = ["", "one", "two", "three", "four", "five",
             "six", "seven", "eight", "nine"]
specialTens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
               "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "ten", "twenty", "thirty", "forty", "fifty",
            "sixty", "seventy", "eighty", "ninety"]

def getWrittenNumber(number):
    """returns a string with the wirtten number.
    Max number == 999"""

    numberStr = str(number)
    digits = len(numberStr)

    unit = units[int(numberStr[-1])]

    if digits >= 2:
        # Si la decena empieza en 1
        if(numberStr[-2] == "1"):
            unit = units[0]
            # The value of the ten name changes depending the 'one' digit
            ten = specialTens[int(numberStr[-1])]
        else:
            ten = tens[int(numberStr[-2])]

    if digits >= 3:
        # name of hundreds is the name of the unit with a 'hundred' at the end
        hundred = units[int(numberStr[-3])] + " hundred"

    # Everything returns spaces so it can be more readable for debugging

    if digits == 1:
        return unit + " "

    if digits == 2:
        return ten + " " + unit + " "

    if digits == 3:
        if ten == "" and unit == "":
            return hundred + " "
        else:
            return hundred + " and " + ten + " " + unit + " "


def main():
    allNumbers = ""
    charCount = 0

    for n in range(1, 1000):
        allNumbers += getWrittenNumber(n)
    # 1000 is not included
    allNumbers += "one thousand"

    for c in allNumbers:
        if c != " ":
            charCount += 1

    # The answer is the sum of all chars in the written numbers
    print(charCount)

if __name__ == "__main__":
    main()