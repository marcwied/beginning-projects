# Takes user int input, limited to 10, and prints corresponding decimal places of e

import math

print(math.e)
print("{:.10f}".format(math.e))

# Engine

selection = int(input("Enter the number of decimal places to round 'e' to, limited to 10: "))

if selection == 1:
    print("{:.1f}".format(math.e))
elif selection == 2:
    print("{:.2f}".format(math.e))
elif selection == 3:
    print("{:.3f}".format(math.e))
elif selection == 4:
    print("{:.4f}".format(math.e))
elif selection == 5:
    print("{:.5f}".format(math.e))
elif selection == 6:
    print("{:.6f}".format(math.e))
elif selection == 7:
    print("{:.7f}".format(math.e))
elif selection == 8:
    print("{:.8f}".format(math.e))
elif selection == 9:
    print("{:.9f}".format(math.e))
elif selection == 10:
    print("{:.10f}".format(math.e))



