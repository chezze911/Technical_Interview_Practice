'''
Question 2
Given a string a, find the longest palindromic substring contained in a. Your function
definition should look like question2(a), and return a string.
'''

def question2(a):

	longest_palindrome = ""

	# Initial string is a palindrome
	if is_palindrome(a):
	    return a

	start = 0
	end = len(a)


	# Get all the substrings and check if is_palindrome
	# if is_palindrome, and longer than longest_palindrome, make longest_palindrome = current_substring
	while start != end:
	   
	   while end != start:
	       
	       if is_palindrome(a[start:end]) and len(a[start:end]) >= len(longest_palindrome):
	           longest_palindrome = a[start:end]
	       end -= 1
	       
	   start += 1
	   end = len(a)
	   
	return longest_palindrome


#helper function to determine if string s is_palindrome
def is_palindrome(s):
    # if s is empty
    if not s:
        return True
    # is s a single char?
    # print(len(s) == 1)
    if len(s) == 1:
        return True
    
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    return False

def test1():

	# Empty string
	a = ""
	print question2(a)

	# Single char
	a = "s"
	print question2(a)

	# palindrome 
	a = "kayak"
	print question2(a)

    # non-palindrome
	a = "cannon"
	print question2(a)

if __name__ == '__main__':
    test1()
    
#output 
# ""  (empty string)
# s
# kayak
# non
# [Finished in 0.2s]

