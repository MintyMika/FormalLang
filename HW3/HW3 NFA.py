#Stephen Cornelius
#Dr. Dutter
#MSCS 271-001
#Due: 2/20/2023

#This program will take in a string and determine if it is accepted by the NFA

def backtrackNFA(delta, string, acceptingStates = [1, 2, 3], current_state = 0):
    #This function will take in a string and determine if it is accepted by the NFA
    #delta is the transition function
    #string is the string to be checked
    #return True if the string is accepted, False otherwise

    #initialize the current state to 0
    current_state = 0

    #loop through the string
    for i in range(len(string)):
        #if the current state is not in the transition function, return False
        if current_state not in delta:
            return False
        #if the current state is in the transition function, but the current character is not in the transition function, return False
        if string[i] not in delta[current_state]:
            return False
        #if the current state and character are in the transition function, set the current state to the next state
        current_state = delta[current_state][string[i]]

    #if the current state is in the final state, return True
    if current_state in acceptingStates:
        return True
    #otherwise, return False
    else:
        return False
    
    #A delta that would work for this NFA is as follows:
    #delta = {0: {'a': 1, 'b': 0}, 1: {'a': 2, 'b': 0}, 2: {'a': 3, 'b': 0}, 3: {'a': 3, 'b': 3}}

#Declare the transition function
delta = {
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
for string in strings:
    if backtrackNFA(delta, string):
        print(string, 'is accepted')
    else:
        print(string, 'is not accepted')
