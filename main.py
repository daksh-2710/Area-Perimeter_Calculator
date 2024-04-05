import time
import sys

#function used to print out words letter by letter
def character_timer(string):  
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.06)
#function used to print out the instructions
def instructions():
    print("Welcome to the Area/Perimeter Calculator")
    print()
    print("This program's intended purpose is to calculate a shape's area and perimeter.")
    print("Enter the shapes dimensions (measurements) and the program will output the answers for your shape's area and perimeter.")
    print()
#asks the user for a shape
def ask_shape(question): 
    while True:
        response = input(question).lower()

        if response == "square":
            return "square"
        elif response == "triangle":
            return "triangle"
        elif response == "circle":
            return "circle"
        elif response == "parralellogram":
            return "parralellogram"
        elif response == "rectangle":
            return "rectangle"
        else:
            print("Please enter a shape from the list above")

#used to print out the shapes that can be calculated
list = [ "- Circle\n","- Square\n","- Rectangle\n","- Triangle\n","- Parrallelogram\n" ]

#instrutions will be printed here
instructions()
#list of shapes will be printed here
print("These are the shapes that can be calculated:")
time.sleep(2)
character_timer("".join(list))

#asks the user what shape they want
request_shape = ask_shape("What shape do you want to calculate?: ")

if request_shape == "square":
    print("square")
elif request_shape == "triangle":
    print("triangle")
elif request_shape == "circle":
    print("circle")
elif request_shape == "rectangle":
    print("rectangle")
elif request_shape =="parralellogram":
    print("parralellogram")









