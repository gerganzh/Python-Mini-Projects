'''In this code I was tasked with creating a code that will multiply two polynomials in the form of a list.'''

import unittest

def main():
    def multiplication_poly(P1, P2):
        res = [] #set up an empty list
        dict = {} #going to use a dictionary for the multiplication, because it allows for more elegant code
        for i in range(len(P1)): #for each element in both polynomial lists
            for j in range(len(P2)):
                dict.setdefault(i + j, 0) #sets up 0 as the default value
                dict[i + j] += P1[i] * P2[j] #append the values with the new multiplied number
        for i in range(len(dict)): #append the values of the dictionary to the empty list
            res.append(dict[i])
        return res #and return it as a final result

    poly1 = []
    a = int(input("Enter the size of the first polynomial: "))
    for i in range(0, a):
        while True:
            try:
                x = int(input("Input the numbers for the polynomial: ")) #input validation
                poly1.append(x)
                print(poly1)

                break
            except:
                raise ValueError('You need to input numbers')

    poly2 = []
    b = int(input("Enter the size of the second polynomial: "))
    for i in range(0, b):
        while True:
            try:
                y = int(input("Input the numbers for the polynomial: ")) #input validation
                poly2.append(y)
                print(poly2)
                break
            except:
                raise ValueError('You need to input numbers')

    print("Multiplied polynomial is " + str(multiplication_poly(poly1, poly2)))

    restart = input("Would you like to restart the program? Y/N ")
    if restart == 'y' or restart == 'Y':
        main()

main()

