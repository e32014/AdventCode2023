file = open("input.txt")
wordRep = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
matchOn = [str(i) for i in range(10)] + ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

total = 0
for line in file:
    dig1 = -1
    dig2 = -1
    build = ""
    for chr in line:
        build += chr
        for check in matchOn:
            if check in build:
                if check in wordRep:
                    dig1 = wordRep[check]
                else:
                    dig1 = int(check)
                break
        if dig1 != -1:
            break
    build = ""
    for chr in reversed(line.strip()):
        build = chr + build
        for check in matchOn:
            if check in build:
                if check in wordRep:
                    dig2 = wordRep[check]
                else:
                    dig2 = int(check)
                break
        if dig2 != -1:
            break
    total += dig1 * 10 + dig2
print(total)