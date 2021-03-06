"""
CTEC 121
Robert Ballenger
Task: Programming Assignment
Module 2 Programming Assigment
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""

#Ignore this please#
#Ignore this please#




import time
from math import *
class color:
    PURPLE = '\033[95m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

#Ignore this please#
#Ignore this please#


def main():

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Section 1 Demonstrate assignment statements:")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(1)

    # create several variables and assign them values. At a minimum there should be an integer, a float, and a string
    # In creating your variable names, demonstrate self-documenting naming and the use of both upper and lower case.

    HF = "High Five!"
    hf = "high five!"
    half_of_five = 2.5
    NumberOfVariables = 2+2

    print("\n\n")

# print the values

    print(HF, hf, half_of_five, NumberOfVariables, sep=', ')

    print("\n\n")

# Demonstrate the intermixing of text and values in a print statement

    print("What do you get if you split 5 in half?", half_of_five)
    print("Good job!", hf)
    print("Oh wait, we were told to use profesionalism. Let me try this again...", HF)
    print("Take a guess how many variables were used in this. I can't help it, I gotta tell ya! It was", NumberOfVariables)

    print("\n\n")
    input("Press Enter to Continue...")

# Section 2

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Section 2 Demonstrate the use of the end and sep keywords in print statements.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(1)

    print("\n\n")

    # Here I use the end= keyword to make sure the next print statment stays on the same line.
    # I use a space between the two ' to make sure the next statment has a space between it and this one.
    print("Here I shall demonstrate", end=' ')

    # Here is another example, but this time I changed what the end statment used instead of the space.
    # in this case filling in the space with an underlined "I". However, due to how the I is getting underlined
    # I have to place the space between like this line and the next ON the next line or else the two spaces
    # between the I will be underlined as well.
    print("my awesome abilites in how one like ",
          end=color.UNDERLINE + "I" + color.END)
    print(" might use the", end=' ')

    # For this part, I wanted to show my understanding of the sep= keywords but also dip into the understanding
    # of using \ in a string. It's a little messier than it needs to be as the " around "end=" and "sep=" could
    # have just been put in a long string, but it's just a kinda unique way to demonstrate my understanding.
    print(" ", "end=", " ", sep='\"', end=' ')
    print("and", end=" ")
    print(" ", "sep=", " ", sep='\"')
    print("keywords. However I imagine there has to be an easier way to go about doing this.")

    print("\n\n")
    input("Press Enter to Continue...")

# Section 3

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Section 3 Demonstrate the use of the tab, quote and backslash escape characters.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(1)

    print("\n\n")

    # Here I make a fairly lazy demonstration of the use of the tab escape character.
    print("I can't think of any witty reasons why I would need to use the 'tab' escape character at the moment ")
    print(" \t \t \t \t \t So I'm just gonna do this.")

    # Here I demonstrate the use of the quote escape character to simplify my print statement from Section 3
    # but with a more 'clean' way.
    print("Now I can type \"end=\" and \"sep=\" in a more clean manor by fitting it all on one line.")

    # This line shows the se of the backslash escape character.
    print("Here is a stickman's arm. You should give it back to him. -> \\")
    print()

    print("\t         0    \"Can I get my arm back?\"")
    print("\t         |\/  ")
    print("\t         |    ")
    print("\t        /\\   ")
    print("\t   ____/___\\__")

    print("\n\n")
    input("Press Enter to Continue...")

# Section 4

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Section 4 Demonstrate getting input from the user (and printing the value obtained back out.)")
    print("            Print the type of each value in addition to its value.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(1)

    print("\n\n")

    # First part is to get a string
    StringGiven = input(
        "Alrigh, now to go any further I'm going to have to make you tell me your favorite color. \n")
    time.sleep(1)
    print()

    print("Really? Out of all the colors in the world",
          color.BOLD + StringGiven + color.END, "is yours? ")
    print(type(StringGiven))
    time.sleep(2)
    print()

    print("Well, okay I guess.")
    time.sleep(2)
    print()

    # Next I get an input with an int. It needs to be entered as numbers, no letters or it will crash!
    IntGiven = int(input(
        "How about you give me your age instead? Please make sure to use numbers, not letters! \n"))
    time.sleep(1)
    print()

    print("Oh! only", IntGiven, "really? Quite interesting")
    print(type(IntGiven))
    time.sleep(2)
    print()

    # Now getting the float input. Same idea as before, no letters only numbers.
    FloatGiven = float(input(
        "Here is an idea! Lets check your math skills, what would you say the answer to 3 + 2.5 is? Remember, use numbers! \n"))
    time.sleep(1)
    print()

    print("Well I can't really check your work so I just have to hope that 5.5 is the number right here -->", FloatGiven)
    print(type(FloatGiven))
    time.sleep(2)
    print()

    # Last a number using eval
    EvalGiven = eval(input(
        "Lets try some math for me, Go ahead and enter two big numbers for me to add. Go ahead with at least three digets each! \nIn xxx + xxx format please and thank you. \n"))
    time.sleep(1)
    print("Hmm.. that may actually be harder than I thought it would be. Let me really think on that one.")
    print()
    time.sleep(2)
    print("Alright, I think the answer is",
          EvalGiven, "but I'm not 100% sure.")
    print(type(EvalGiven))
    time.sleep(1)
    print("Well I'm glad we could chat like this.")

    print("\n\n")
    input("Press Enter to Continue...")

# Section 5

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Section 5 Demonstrate simultaneous assignment using an assignment statement and an input function")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(1)

    print("\n\n")

    # Using an assignment statement
    mybook_1, mybook_2, mybook_3 = " Enslaving the Human Race by Droidson Robots", " Coming to Grips with Moving on From HDDs", " Dune"

    print("Do you have a favorite book? I have three!", end=" ")
    print(mybook_1, mybook_2, " and", mybook_3, sep=",")

    print()

    # Using an input function

    word_1, word_2 = eval(input(
        "What's your two favorite numbers? Seperate them with a comma please!\n"))
    time.sleep(1)
    print()
    print("Oh, I wouldn't have expected you to like the number ",
          word_1, " that's quite the interesting thing to know.")
    print("Let's not forget what a great choice ",
          word_2, "was. I give you a round of applause!")
    time.sleep(1)

    print("\n\n")
    input("Press Enter to Continue...")

# Section 6

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Section 6 Demonstrate integer arithmetic, output the quotient of five divided by two and")
    print("\t\t the remainder of five divided by two.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(1)

    print("\n\n")

    # Integer arithmetic. Here I demonstrate how to do division of 5 by 2 in both ways for quotient and remainder.
    ans_1 = 5/2
    ans_2 = 5//2
    print("If you're just wanting to see the quotient, you could do 5//2=", ans_2)
    print("However if you'd like to see the remainder you'd need to do 5/2=", ans_1)

    print("\n\n")
    input("Press Enter to Continue...")

# Section 7

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Section 7 Demonstrate infinate loops using a list, using range, and output every third number")
    print("\t\t\t starting at 11 for 5 iterations")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(1)

    print("\n\n")

    # Here I shall show you a list of book titles.
    print("I really love The Lord of the Rings seires, the order they go in is:")
    for i in ["Fellowship of the Ring", "The Two Towers", "Return of the King"]:
        print(i)
    print()

    # Next up I show a look using range.
    print("Can you count to 5? I can, check it out!")
    for i in range(6):
        print(i)
    print("Can't forget that us computers start with 0!")
    print()

    # Last it's time to have a loop output every third number starting at 11 for 5 iterations.
    print("Nothing witty here, just 11-26, going up 3 numbers for 5 iterations")
    for i in range(11, 27, 3):
        print(i)
    time.sleep(1)

    print("\n\n")
    input("Press Enter to Continue...")

# Section 8

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Section 8 Demonstrate the use of: The value pi, the square root function, the ceil() function,")
    print("\t\t the floor() function, square a value, and cube a value.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(1)

    print("\n\n")

    # Demonstration of the use of Value pi.
    x = pi
    print("To start, were going to take a look at the value pi. Also known as")
    print(x)
    print()

    # Demonstrating the square root function.
    print("Now can we take and squre pi? What do you think would happen?")
    print(sqrt(x))
    print("Wow!")
    print()

    # Demonstration of ceil() and floor() function.
    print("What is the smallest whole number that is greater than pi?")
    print(ceil(x))
    print()

    print("What about the largest whole number that is less than pi?")
    print(floor(x))
    print()

    # Demonstration of squaring and cubing a value.
    print("What do you think the pi times pi would be? Well I'll tell you!")
    print(pow(x, 2))
    print()

    print("What about if we took and cubed pi?")
    print(pow(x, 3))
    print()
    time.sleep(1)

    print("\n\n")
    input("Press Enter to Continue...")

# Section 9

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Section 9 Demonstrate the accumulator pattern by getting five values from the user and")
    print("\t calculating the sum of the values and the sum of squares of the values.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(1)
    print("\n\n")

    # To start I know I'm going to have 2 sums I'm using. One for the normal added values and one for those values
    # squared. I then use the eval input from earlier to get five numbers and assign them to letters.
    sum_1 = 0
    sum_2 = 0
    a, b, c, d, e = eval(input(
        "Can you please pick five numbers for me? Seperate them with commas please!\n"))

    # Next I used the numbers give, and using the loop I have it add each together in order and assign that value to
    # the first variable, sum_1
    for i in [a, b, c, d, e]:
        sum_1 = sum_1 + i
        print(i)
    print("----")
    time.sleep(1)
    print(sum_1)
    print()

    # Next is to get the sqare of each number, then add them together.
    print("Look at that! I added them all together for you. Would you like to know what would happen if")
    print("we went and squared all those values and then added them together?")
    print()
    time.sleep(1)

    # Here I used the same method as earlier, but now I'm using the pow() function
    for i in [pow(a, 2), pow(b, 2), pow(c, 2), pow(d, 2), pow(e, 2)]:
        sum_2 = sum_2 + i
        print(i)
    print("----")
    time.sleep(1)
    print(sum_2)

    print("\n\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Thanks for coming to my Ted Talk")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\n\n")



main()
