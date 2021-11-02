#Create a list of unique words, which will contain the final result. Write
#a program to open the file romeo.txt and read it line by line. For each
#line, split the line into a list of words using the split function. For
#each word, check to see if the word is already in the list of unique
#words. If the word is not in the list of unique words, add it to the list.
#When the program completes, sort and print the list of unique words
#in alphabetical order.


#prompt user and read file name
fname = input("Enter File name: ")

try:
    #open the file
    fhand = open(fname)

    #create a list
    lstUniqueWords = list()


    for line in fhand:

        #split the file into list
        words = line.split()

        for element in words:

            #if element is not included in the list of unique words, append it.
            if not element in lstUniqueWords:

                lstUniqueWords.append(element)

    lstUniqueWords.sort()

    print(lstUniqueWords)

except:
    print("file name incorrect, please enter again")
