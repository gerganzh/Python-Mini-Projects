#Week3, Task 2

""" This code does linear search on an array of integers. It uses
recursion in order to accomplish it."""

import unittest

def linear_search(lst, target, i = 0, count = 0): #i for comparing integers, count for number of recursions
    if lst[i] == target:
        return ('Target was found!')
    elif len(lst) == count+1: #if the size of the list equals the number of recursions
        return ('Target was not found!')
    else:
        return linear_search(lst,target, i+1, count+1) #recursion

def main(): #main function to run the program
    print('Please input the array (separated by spaces)')
    user_list = [int(x) for x in input().split()] #splitting the integers into a newly created list
    print('List :' + str(user_list))
    target_user = int(input('Enter a target: '))
    print(linear_search(user_list,target_user))

    class find_target(unittest.TestCase):
        def linearsrch_test(self):
            self.assertTrue(linear_search([1,2,3],3), 'Target was found')

    if __name__ == '__main__':
        unittest.main()
main()
 

