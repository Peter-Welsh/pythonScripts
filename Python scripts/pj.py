#pxw120530
#December 1, 2014
#Programming Assignment #3
#Note: This was written in Python 3, meaning print() has parentheses

def compound_interest(principle, rate, years):
	if years == 0:
		return principle #base case
	else:
		principle *= (1 + rate)
		years -= 1
		return compound_interest(principle, rate, years) #recursive call


def list_same(list1, list2):
	if not list1: #if list1 is empty
		return 1
	elif not list2: #if list2 is empty
		return 1
	elif list1[0] == list2[0]:
		return list_same(list1[1:],list2[1:]) #recursive call with the rest of the lists
	else:
		return 0

def compare(string1, string2):
	if string1[0] < string2[0]: #if the 1st character of string1 is less than the 1st character of string2
		return -1
	elif string1[0] > string2[0]: #if the 1st character of string1 is greater than the 1st char of string2
		return 1
	else:
		if string1[1:] and string2[1:]: #if both strings have characters left
			return compare(string1[1:], string2[1:]) #recursive call
		elif string1[1:] or string2[1:]: #if either string has characters left
			if string1[1:]: #if string1 is longer than string2
				return 1
			elif string2[1:]: #if string2 is longer than string1
				return -1
		return 0

def mult(int1, int2):
	if int2 == 1:
		return int1 #base case: anything times 1 = itself
	elif int1 == 0 or int2 == 0:
		return 0 #anything times 0 = 0
	else:
		return int1 + mult(int1, int2-1) #recursive call