""" This program combines two strings, by taking one character from the first one, then it takes one from the second string. This
goes on until one string has no characters left. Then it just finishes the combined string by using the remaining characters
from the longer string. """

import unittest

def Combine_Strings(String1, String2, i = 0):
    Result = ' '
    while i<len(String1) or i<len(String2): #while the length of either list is bigger than zero
        if i<len(String1) and i<len(String2): #combines the characters one by one until one list runs out of characters
            Result = Result + String1[i] + String2[i]
        elif i>=len(String1): #if the first string has less characters, get the all the remaining characters from the second
            Result = Result + String2[i]
        else:   #if the second string has less characters, use all the the remaining characters from the first string
            Result = Result + String1[i]
        i = i + 1 #for the loop
    return Result

String_1 = str(input("Please input the first string: "))
String_2 = str(input("Please input the second string: "))

print('The combined string is: ' + Combine_Strings(String_1,String_2))

class Test1(unittest.TestCase):
    def testing(self):
        self.assertTrue(Combine_Strings('haha','hehe'),'hhaehhae')
        self.assertTrue(Combine_Strings('longer','word'),'lwoonrgder')

if __name__ == '__main__':
    unittest.main()

