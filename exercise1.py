#Write a function called chop that takes a list and modifies
#it, removing the first and last elements, and returns None. Then write
#a function called middle that takes a list and returns a new list that
#contains all but the first and last elements.


#This function removes the first and last elements & returns none
def chop(l1):

    l1.remove('a')
    l1.remove('b')

#This function retuns a new list that contains all but the first and last elements
def middle(l2):

    del l2[0]
    del l2[-1]

    return l2

set1 = ['a', 'b', 'c', 'd']
set2 = [1, 2, 3, 4]

#invoking chop function
chop_function = chop(set1)

print(chop_function)

#invoking middle function
middle_function = middle(set2)

print(middle_function)
