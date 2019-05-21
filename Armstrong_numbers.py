""" This code check if a number is an Armstrong number. An Armstrong number is a number in which
the sum of the cubes of each digits is equal to the number itself."""

import unittest

def check_Armstrong(number):
    temp = number  # we need to assign number to a variable
    sum = 0  # establish sum as zero

    while temp != 0:  # As long it is not a zero
        rem = temp % 10  # get the remainder
        sum = sum + rem ** 3  # and then add it to power of three  in sum
        temp = temp // 10  # floor division and loop again until it reaches 0

    if sum == number:
        print('The number ' + str(number) + ' is an Armstrong number')
    else:
        print('The number ' + str(number) + ' is not an Armstrong number')


# examples of working code
example1 = 153
check_Armstrong(153)
example2 = 124
check_Armstrong(124)

a = input('Would you like to try a number of your own? Please use y or Y :) ')
if a == 'y' or a == 'Y':
    while True:
        try:
            user_input = int(input('Please input a number: '))
            check_Armstrong(user_input)
            break
        except:
            raise ValueError('You need to input an integer!')

class tes1(unittest.TestCase):
    def armstrong(self):
        self.assertEqual(check_Armstrong(121),'The number 121 is an Armstrong number')

if __name__ == '__main__':
    unittest.main()
    
'''Pseudocode to design an algorithm for Armstrong numbers
Availability at: http://www.geekinterview.com/question_details/27053'''
