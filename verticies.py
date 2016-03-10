#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      KatieHarte
#
# Created:     14/11/2015
# Copyright:   (c) KatieHarte 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

"""This can be used to calculate how many possible lines you can draw between
verticies inside a shape. Why would you need to do that? I'm honestly not sure"""

verticies = input("How many verticies does your shape have?")

print("Verticies: " + str(verticies))

allines = 0

if verticies <= 2 or type(verticies) != int:
    print("This is not a shape you dummy!")
else:
    for x in range (3, verticies):
        totallines = verticies - x
        x += 1
        #print(totallines)
        allines = allines + totallines

    allines = allines + (verticies-3)

    print("Total lines: " + str(allines))

if verticies == 3:
    print("Your shape is a triangle")
elif verticies == 4:
    print("Your shape is a square")
elif verticies == 5:
    print("Your shape is a pentagon")
elif verticies == 6:
    print("Your shape is a hexagon")
elif verticies == 8:
    print("Your shape is an octagon")
elif verticies <= 2:
    print()
else:
    print("Your shape is a " + str(verticies) + "-gon")





