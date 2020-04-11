"""
Flooring Cost Calculator.  Takes in dimensions of floor, cost of material and returns cost of materials for floor dimensions
"""


def floorcost(length, width, tilecost):
    sqft = length * width
    totalcost = sqft * tilecost
    return '$' + str(totalcost)

#print(floorcost(10,10,15))                         # TEST FUNCTION


# ENGINE


print("Flooring Cost Calculator\n")

while True:
    length = int(input("Length of the Room = "))
    width = int(input("Width the the Room  = "))
    tilecost = int(input("Cost of tile     = "))

    print(floorcost(length,width,tilecost))
    break

