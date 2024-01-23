#Program 2 – Weekly Loan Calculator
#Develop a short term loan calculator program as a console application 

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    # Start of program
    # Context message: print()
    print("Weekly Loan Calculator")

    # Declare variables: float(input()) and do the math(correctly use the formula):
    amountOfLoan = float(input("\nEnter the amount of loan: "))
    interestRate = float(input("Enter the interest rate (%): ")) 
    numberOfYears = float(input("Enter the number of years: "))

    # Do the math
    i = interestRate / 5200
    weeklyPayment = ( i / (1 - (1 + i) ** ( -52 * numberOfYears ) )) * amountOfLoan

    # Give the outcome: print()
    print("\nYour weekly payment will be: ${0:.2f}".format(weeklyPayment) )

    # End of program
    
    # Ready for Marking


    # YOUR CODE ENDS HERE

main()