# Program 3 – Imperial to Metric Conversion
# Write a console program that converts a weight given in tons (imperial), stones, pounds, and ounces 
# to the metric equivalent in metric tons, kilograms, and grams.

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    # Start of Program
    # Context Message : print()
    print("Imperrial To Metric Conversion")

    # Declare the variables and do the math
    # Ask the user to enter the number of tons: int(input())
    numOfTons = int(input("\nEnter the number of tons: "))

    # Ask the user to enter the number of stones: int(input())
    numOfStone = int(input("Enter the number of stone: "))

    # Ask the user to enter the number of pounds: int(input())
    numOfPounds = int(input("Enter the number of pounds: "))

    # Ask the user to enter the number of ounces: int(input())
    numOfOunces = int(input("Enter the number of ounces: "))

    # Do the math
    # Convert user's entered data to total ounces
    totalOunces = 35840 * numOfTons + 224 * numOfStone + 16 * numOfPounds + numOfOunces

    # Convert total ounces to total kilos
    totalKilos = totalOunces / 35.274

    # Convert kilos to metric tons
    metricTons = int(totalKilos / 1000)

    # Calculate the remaining kilos
    remainingKilos = int(totalKilos % 1000)

    # Calculate the remaining grams
    remainingGrams = (totalKilos - metricTons * 1000 - remainingKilos) * 1000

    # Give the final converted values:print()
    print("\nThe metric weight is {0} mertric tons, {1} kilos, and {2:.1f} grams. ".format(metricTons,remainingKilos,remainingGrams))


    # End of program



    # Ready for Marking




    # YOUR CODE ENDS HERE

main()