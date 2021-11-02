#Rewrite the guardian code in the above example without
#two if statements. Instead, use a compound logical expression using
#the or logical operator with a single if statement.

#Prompt user and read file name
fname = input("Enter the file name: ")

try:
    fhand = open(fname)

    for line in fhand:

    words = line.split()

    if len(words) == 0 or words[0] != 'From':
        continue

    print(words[2])

except:
    print("File not found, kindly check your file name & try again!")
