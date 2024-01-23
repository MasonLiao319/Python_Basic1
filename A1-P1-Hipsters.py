#Program 1 – Hipster's Local Vinyl Records
#Hipster’s Local Vinyl Records sell and hand-deliver vinyl records to their customers.

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    #Start of program 
    #Context message: print()
    print("Hipster's Local Vinyl Records - Customer Order Details")

    #Declare variables & do the math
    #Ask user to enter the customer's name: input()
    userName = input("\nEnter the customer's name: ")

    #Ask user to enter the distance: input()
    distanceOfDelivery = float(input("Enter the distance in kilometers for delivery: "))

    #ask user to the cost of records purchased: input()
    recordsOfPurchase = float(input("Enter the cost of records purchased: "))
    
    #Do the math
    tax = 0.14
    deliveryCost = distanceOfDelivery * 15
    purchaseCost = recordsOfPurchase + recordsOfPurchase * tax
    totalCost = deliveryCost + purchaseCost

    #Give the outcome: Print()
    #Summary for (userName)
    print("\nPurchase summary for {0}".format(userName))

    #A: Delivery Cost:(deliveryCost)
    print("Delivery Cost: ${0:.2f}".format(deliveryCost))

    #B: Purchase Cost:(purchaseCost)
    print("Purchase Cost: ${0:.2f}".format(purchaseCost))

    #C: Total Cost:(totalCost)
    print("Total Cost   : ${0:.2f}".format(totalCost))

    #End of program

    #Ready for Marking




    # YOUR CODE ENDS HERE

main()