#Stephen Cornelius
#Dr. Dutter
#MSCS 271-001
#Due: 2/20/2023

#This program will take in a string and determine if it is accepted by the NFA

def recursiveBacktrackNFA(delta, string, acceptingStates = [1, 2, 3], current_state = 0):
    #This function will take in a string and determine if it is accepted by the NFA
    #delta is the transition function
    #string is the string to be checked
    #return True if the string is accepted, False otherwise

    #if the string is empty, check if the current state is in the accepting states
    if len(string) == 0:
        if current_state in acceptingStates:
            return True
        else:
            return False

    #if the current state is not in the transition function, return False
    if current_state not in delta:
        return False

    #if the current state is in the transition function, but the current character is not in the transition function, return False
    if string[0] not in delta[current_state]:
        return False

    #if the current state and character are in the transition function, set the current state to the next state
    for next_state in delta[current_state][string[0]]:
        #if the recursive call returns True, return True
        if recursiveBacktrackNFA(delta, string[1:], acceptingStates, next_state):
            return True

    #if the recursive call returns False, return False
    return False
    #A delta that would work for this NFA is as follows:
    #delta = {0: {'a': 1, 'b': 0}, 1: {'a': 2, 'b': 0}, 2: {'a': 3, 'b': 0}, 3: {'a': 3, 'b': 3}}

    #An appropriate string to test is 'abba'

def parallelBitmapSearchNFA(delta, string, acceptingStates = [1, 2, 3], current_state = 0):
    #This function will take in a string and determine if it is accepted by the NFA
    #delta is the transition function represented as an array of bitmaps
    #string is the string to be checked
    #return True if the string is accepted, False otherwise
    pass



#Declare the transition function
delta = {   #This is the delta for the NFA in the book for Chapter 6 Question 7
    0: {'a': [0, 1], 'b': [0]},
    1: {'a': [2], 'b': []},
    2: {'a': [2], 'b': [2]}
}


#Declare the accepting states
acceptingStates = [2]

#Make a list of strings to test
strings = [
    'a', 'b', 'aa', 'ab', 'ba', 
    'bb', 'aaa', 'aab', 'aba', 
    'abb', 'baa', 'bab', 'bba', 
    'bbb', 'aaaa', 'aaab', 'aaba', 
    'aabb', 'abaa', 'abab', 
    'abba', 'abbb', 'baaa', 
    'baab', 'baba', 'babb', 
    'bbaa', 'bbab', 'bbba', 'bbbb'
    ]



#Loop through the list of strings and print the results
print(len(strings))
i = 0
for string in strings:
    if recursiveBacktrackNFA(delta, string, acceptingStates):
        print(i, string, 'is accepted')
    else:
        print(i, string, 'is not accepted')
    i += 1
        

#------------------------------------------------------------------
#The following code is for the parallelBitmapSearchNFA function

#Declare the transition function
delta2 = [  #This is the delta for the NFA in the book for Chapter 6 Question 7
    #q_n,: [1<<0, 1<<2|1<<1, 1<<2] as an example
    [1<<0|1<<1, 1<<0],
    [1<<2, 0],
    [1<<2, 1<<2]
]

deltaHw3 = [
    [1<<1|1<<4,     1<<2|1<<5],         #0
    [1<<1,      1<<0|1<<1|1<<2|1<<4],   #1
    [1<<3|1<<4,     1<<1|1<<2|1<<5],    #2
    [1<<0|1<<1|1<<2|1<<4,       1<<3],  #3
    [1<<4,      1<<5],                  #4
    [1<<0|1<<1|1<<4|1<<6,       1<<7],  #5
    [1<<8|1<<4|1<<1, 1<<2|1<<4|1<<5],   #6
    [1<<5,      1<<0|1<<1|1<<3|1<<6],   #7
    [1<<7, 1<<8]                        #8
]

#NOTE: Test delta2 first because I know what the results should be

#Define the function
