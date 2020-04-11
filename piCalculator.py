"""
Returns specified number of deimal places for pi
"""


import math

pi = math.pi

print("{:.17f}".format(pi))
print(pi)



# Engine

decimal = int(input("Enter the number of decimal places you'd like to show for pi, limited up to 16 "))

if decimal == 2:
    print("{:.2f}".format(pi))
elif decimal == 3:
    print("{:.3f}".format(pi))
elif decimal == 4:
    print("{:.5f}".format(pi))
elif decimal == 5:
    print("{:.5f}".format(pi))
elif decimal == 6:
    print("{:.6f}".format(pi))
elif decimal == 7:
    print("{:.7f}".format(pi))
elif decimal == 8:
    print("{:.8f}".format(pi))
elif decimal == 9:
    print("{:.9f}".format(pi))
elif decimal == 10:
    print("{:.10f}".format(pi))
elif decimal == 11:
    print("{:.11f}".format(pi))
elif decimal == 12:
    print("{:.12f}".format(pi))
elif decimal == 13:
    print("{:.13f}".format(pi))
elif decimal == 14:
    print("{:.14f}".format(pi))
elif decimal == 15:
    print("{:.15f}".format(pi))
elif decimal == 16:
    print("{:.16f}".format(pi))
