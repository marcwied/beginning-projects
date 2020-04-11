"""
Takes in a whole number and returns its Prime Factors 
"""


def list_factors(n):                                    # function to create a list of factors for a given number(n)
    factors = []                                        # starts with empty list[factors]
    for x in range(1, n+1):                             # loops through range of 1 through (given number + 1)

        if n%x == 0:                                    # checks if number(n) has zero remainders (modulus) when divided by x
            factors.append(x)                           # if true, adds x to list of factors
        else:
            continue                                    # otherwise it moves onto next 'x' value in range
    return factors                                      # when done returns list of [factors]

#print(list_factors())                               # TEST FUNCTION

def is_prime(n):                                        # function to return T/F if a number is prime
    return len(list_factors(n)) == 2                    # if a number has > 2 factors, it is not a prime number

#print(is_prime(4))                                 # TEST FUNCTION

def list_prime_factors(n):                                      # function to return list of ONLY prime factors for a given number (n)
    prime_factors = list(filter(is_prime, list_factors(n)))     # variable = list filtered by if prime is True and in the [factors] list
    return prime_factors


#print(list_prime_factors(20))                       # TEST FUNCTION


def output(n):                                                  # function to return list of factors based on if number(n) is prime or not
    n = int(n)
    af = list_prime_factors(n)                                  # sets variable = to list of prime factors derived from number (n)
    if is_prime(n):                                             # checks if number(n) is prime
        return str(n)                                           # if true, returns number(n) as a string
    else:
        return str(af[0]) + ',' + output(n/af[0])               # otherwise, returns [prime_factor][index 0][string] + result of number(n)
                                                                # divided by [prime_factor][index 0][string
#print(output(9))                                    # TEST FUNCTION


print("Enter a number to see its factors, enter 'exit' to end the program")
num = 0


while True:                                                     # while loop to control game engine
    try:                                                        # try clause to handle exceptions

        if num:
            print(f"{output(num)} are the factors of {num}")    # if number is True, prints the prime factor list as factors of number(n)
        print(">>>", end='')                                    # formatting for input console
        num = input()                                           # user input
        if num == "exit":                                       # terminate program clause
            break                                               # if true, breaks out of game engine while loop
    except ValueError:                                          # if user enters invalid number, not an int or 'exit'
        print("Invalid Entry")                                  # returns error
        num = 0                                                 # sets num back to0
        continue                                                # restarts at beginning of while loop until valid entry
