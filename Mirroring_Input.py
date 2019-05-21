#Week3, Task 1

''' I created a program that will take words as an input and will mirror them'''

import unittest

def main():
    def mirror(string): #using the same function as Week 2 for Palindromes
        if len(string) <= 1:
            return string
        return mirror(string[1:]) + string[0]

    array = []
    user_input = int(input("How many words would you like to reverse? "))

    for i in range(0, user_input): #append a list with word/s
        x = input("Enter the word:")
        array.append(x)

    for i in array: #for every element in the array, mirror and print
        print(mirror(i), end = " ")

    class mirror(unittest.TestCase):
        def mirrortest(self):
            self.assertTrue(mirror('hey'),'yeh')

    if __name__ == '__main__':
        unittest.main()
main()
