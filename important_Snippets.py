'Snippets of useful code that I wrote and constantly reuse. \n As of June 2024: \n 1. Test Case Verification \n 2. Open Window using TKinter \n 3. Print contents of file to a list. \n 4. Count lines in file. \n 5. Turn a word into a List of letters.\n 6. Turn list to string.\n 7. Random Code Generator.\n 8. A Base Converter up to Base 36.\n 9. Show time and date.\n 10. Show time only. 11. Countdown.'

import random, sys, string, time

def main():
    print("ALL MODULES WORKING.")

# MANUAL UNIT TEST FOR BASIC FUNCTION
def test_cases_verified(test_cases = list(), test_answers = list()):

    'Gets a list of elements and performs an operation via a function on them. It then compares the results to a list of answers entered by user.'
    
    # MANUAL UNIT TEST FUNCTION
    # TAKING TWO LISTS(QUESTIONS AND ANSWERS) AND SEEING IF
    # ANSWERS MATCH ONCE A FUNCTION IS PERFORMED UPON THEM.

    from calculator import squared

    x = 0
        
    if len(test_cases) == len(test_answers):

        for i in test_cases:
            try:
                assert squared(i) == test_answers[x]
            except AssertionError:
                print(f"{i} FAILED")
            else:
                print(f"{i} PASSED.")

            x += 1

    else:
        print(f"{len(test_cases)} != {len(test_answers)}.\n Lists must be of same length.")

# OPENING BASIC WINDOW USING TKINTER
def window(x = 100,y = 100,title = str(),text = str()):
    import tkinter as tk

    root = tk.Tk()
    root.geometry(f"{x}x{y}")
    root.title(title)

    label = tk.Label(root, text=f"{text}")
    label.pack(padx=20, pady=20)

    root.mainloop()

# PRINTING CONTENTS OF FILE TO LIST
def saveToList(filename = str(),listname = list()):
    
    with open(f"{filename}","r") as file:
        for lines in file:
            listname.append(lines.strip())
    
    return listname

# HOW MANY LINES OF CONTENT IN FILE
def linesOfContent(filename = str()):
    x = 0
    with open(f"{filename}","r") as file:
        for line in file:
            x += 1

    return x

# TAKES A WORD AND TURNS IT INTO LIST BY LETTERS:
def makeList(word = str()):

    'Recieves a single word as input and returns a list with each letter in word as individual element.'

    madeList = []

    for i in word:
        madeList.append(i)

    return madeList

# TURNS LIST INTO STRING WITH NO WHITESPACE
def makeString(list = list()):

    'Takes a list ["a","b","c"] and returns it as string abc'

    word = ""

    for i in list:
        word = word + i

    return word

# GENERATES RANDOM CODE
def genCode(length = int(), prefix = ""):

    'Generate a random code with prefix and random letters and numbers of length.'

    letters = makeList(string.ascii_uppercase)
    numbers = makeList("1234567890")
    code = ""

    for i in range(0, length):
        code = code + random.choice(letters) + random.choice(numbers)

    return str(prefix) + "-" + code

# CONVERTS INT TO BINARY OR OTHER BASE
def integerToBase(integer, base):

    'Takes Integer and converts it to Base 2(binary) up to Base 36. I HAVE LITTLE TO NO IDEA HOW THIS WORKS.'

    digs = string.digits + string.ascii_uppercase

    if integer < 0:
        sign = -1
    elif integer == 0:
        return digs[0] # RETURNS THE NUMBER 0 IF INTEGER ENTERED IS 0
    else:
        sign = 1

    integer *= sign

    digits = []

    while integer:
        digits.append(digs[int(integer % base)])

        integer = int(integer / base)

    if sign < 0:

        digits.append('-') 

    digits.reverse()

    return ''.join(digits)

# FULL TIME AND DATE
def showTimeDate():
    'Returns full time and date in the form:\n11:21:20 PM on Monday, June 24, 2024'

    return time.strftime("%I:%M:%S %p on %A, %B %e, %Y")

# FULL TIME ONLY
def showTime():
    return time.strftime("%I:%M:%S %p",time.localtime(time.time()))

# COUNTDOWN CLOCK
def counter(seconds):
    startTime = time.time()
    while time.time() < startTime + seconds:
        counter = time.strftime("%I:%M:%S",time.localtime(time.time()))
        time.sleep(1)
        print(counter)

if __name__ ==  "__name__":
    main()