#Rewrite the program that prompts the user for a list of
#numbers and prints out the maximum and minimum of the numbers at
#the end when the user enters “done”. Write the program to store the
#numbers the user enters in a list and use the max() and min() functions to
#compute the maximum and minimum numbers after the loop completes.

#Creating a list to store numbers
numberList = list()

#loop run until user enter done
while True:

    #prompt user and read the number
    inp = input("\nEnter the number: ")

    try:
        #convert type from string to int
        numbers = float(inp)

        #if user enter the negative number, the below message will be display.
        if numbers < 0:

            print("Kindly, enter positive integer")

        else:
            #if number is positive, add it to the numberList
            numberList.append(numbers)

        #prompt user if he/she wants to continue the program or done.
        ask = input("\nenter 'done' to compute the result OR Press any key to continue\n")

        #if user enter the done, the loop will end and compute the result
        if (ask.upper() == 'DONE'):
            break

        else:
            continue

    except:
        print("Wrong input!! Please enter interger or float value")

print("Maximum number in the list is ", max(numberList), " & minimum number in the list is ", min(numberList))
