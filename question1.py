'''Question 1
Given two strings s and t, determine whether some anagram of t is a substring of s. 
For example: if s = "udacity" and t = "ad", then the function returns True. 
Your function definition should look like: question1(s, t) and return a boolean True or False.'''

def question1(s,t):

	for character in t:
        	if character in s:
            		s = s.replace(character, "", 1)
            		t = t.replace(character, "", 1)
	if not t:
    		return True
	return False


def test1():
	print question1("udacity", "ad")
	# True 

	print question1("u d", " ")
	# True

	print question1("udacity", "udacious")
	# False 

	print question1("racecar", "car")
	# True 

	print question1("12345567890", "0")
	# True

	print question1("!@#$%^&*", "$#")
	# True

	print question1("nanodegree", "")
	# True

	#[Finished in 0.1s]

if __name__ == '__main__':
    test1()