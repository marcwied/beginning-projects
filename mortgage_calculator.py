'''

M = P[r(1+r)^n/((1+r)^n)-1)] M = the total monthly mortgage payment. P = the principal loan amount. r = your monthly interest rate.
Lenders provide you an annual rate so you'll need to divide that figure by 12 (the number of months in a year) to get the monthly rate.
N = term of loan


Mortgage Calculator - Returns monthly payment amount based on given principle, rate and term of loan

'''

def monthly_payment(principle, rate, n):
    numerator = (rate)*(1+rate)**n
    denom = ((1+rate)**n)-1

    pmt = principle * (numerator/denom)
    return "Monthly Payment: " + '${:.2f}'.format(pmt)


# ENGINE


print("Mortage Calculator\n")

while True:

    try:
        p = float(input("Principle Amount of the loan: "))
    except ValueError:
        print("Invalid Entry")
        continue

    try:
        r = float(input("Annual Interest Rate: "))
    except ValueError:
        print("Invalid Entry")
        continue
    try:
        n = int(input("Term of the loan: "))
    except ValueError:
        print("Invalid Entry")
        continue

    print(monthly_payment(p, ((r/100)/12), (n*12)))

    cont = str(input("Calculate another? Y/N ").lower())
    if cont == 'y':
        continue
    else:
        break