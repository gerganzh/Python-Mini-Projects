''' I created a function, which will check if a list is a palindrome. There is a pythonic way to do this
task very easily, but using built-in methods ([::1]) is not allowed. '''

def reverse_list(lst): #using recursion to reverse the list
    str1 = ''.join(str(e) for e in lst) #first make a string and add the list values
    if len(str1) <=1: #when the length of the string smaller or equals 1
        return str1 #return the reversed string

    return reverse_list(str1[1:]) + str1[0] #call the function - start the list from index 1 and add index 0 at the end
                                            #repeat this until the word is fully reversed

def pali_check(num): #another funtion to actually check if a list is a palindrome
    num = ''.join(str(e) for e in num) #make a string from the list
    if num == reverse_list(num): #make a comparison with the reversed string, while calling the other function
        return ('This number is a palindrome')
    else:
        return ('This number is not a palindrome')

while True: #input validation 
    try:
        print('Please input the numbers in the array, seperated by spaces. ')
        input_str = [int(x) for x in input().split()] #to display the list
        print('Your list : ' + str(input_str))
        print(pali_check(input_str)) #check if the number is a palindrome
        break
    except:
        raise ValueError('Only numbers allowed for this task!')

#Notation is O(2N)
