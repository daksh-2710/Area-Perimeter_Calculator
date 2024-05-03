import time 
import sys 
import math

#Functions
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
        elif response == "parallelogram":
            return "parallelogram"
        elif response == "rectangle":
            return "rectangle"
        else:
            print("Please enter a shape from the list above")
#shapes area and perimeter formulas
def rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter
def square(sides):
    area = sides * sides
    perimeter = 4 * (sides)
    return area, perimeter
def circle(radius):
    area = math.pi * radius ** 2
    perimeter = 2 * math.pi * radius
    return area, perimeter
def parallelogram(base, height, side):
    area = base * height
    perimeter = 2 * (base + side)
    return area, perimeter
def triangle_area(base, height):
    area = 1/2 * base * height
    return area
def triangle_perimeter(side1, side2, side3):
    perimeter = side1 + side2 + side3
    return perimeter

#Main Routine 
#list of shapes that are able to be calculated
list = [ "- Circle\n","- Square\n","- Rectangle\n","- Triangle\n","- Parallelogram\n" ]

#instrutions will be printed here
instructions()
#list of shapes will be printed here
print("These are the shapes that can be calculated:")
time.sleep(2)
character_timer("".join(list))
print()

#asks the user what shape they want

request_shape = ask_shape("What shape do you want to calculate?: ")


if request_shape == "square":
    side = float(input("Enter side: "))
    area, perimeter = square(side)
    print()
elif request_shape == "triangle":
    print("--For Area--")
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    print("--For Perimeter--")
    side1 = float(input("Enter side 1: "))
    side2 = float(input("Enter side 2: "))
    side3 = float(input("Enter side 3: "))
    area = triangle_area(base, height)
    perimeter = triangle_perimeter(side1, side2, side3)
    print()
elif request_shape == "circle":
    radius = float(input("Enter radius: "))
    area, perimeter = circle(radius)
    print()
elif request_shape == "rectangle":
    lenght = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area, perimeter = rectangle(lenght, width)
    print()
elif request_shape =="parallelogram":
    bas = float(input("Enter base: "))
    heigh = float(input("Enter height: "))
    sidep = float(input("Enter side: "))
    area, perimeter = parallelogram(bas, heigh, sidep)
    print()


#outputs the answers for area and perimeter
character_timer(f"Your {request_shape}'s area is {area} and its perimeter is {perimeter}")
print()
print()
print("---Answers---")
print("Area: ", area)
print("Perimeter: ", perimeter)

   
