#Stephen Cornelius
#Dr. Dutter
#MSCS271-001
#11 Febuary 2023

#Below is my code for the Man, Wolf, Goat, Cabbage problem as described in Ch.4 Q:3

# char m  w  g  c
delta = [
    [10, 10, 1, 10],    # State 0 Start
    [2, 10, 0, 10],     # State 1
    [1, 5, 10, 3],      # State 2
    [10, 10, 4, 2],     # State 3
    [10, 7, 3, 10],     # State 4
    [10, 2, 6, 10],     # State 5
    [10, 10, 5, 7],     # State 6
    [8, 4, 10, 6],      # State 7
    [7, 10, 9, 10],     # State 8
    [10, 10, 8, 10],    # State 9 ACCEPTING
    [10, 10, 10, 10]    # State 10 TRAP
]

asdf = {
    'm': 0,
    'w': 1,
    'g': 2,
    'c': 3
}

start_state = 0
input_string = input("Enter an Appropriate String: ")
final = [9]

while len(input_string) > 0:
    current_state = start_state
    for character in input_string:
        placeholder = asdf[character]
        current_state = delta[current_state][placeholder]

    if current_state in final:
        print("String Accepted.")
        pass
    else:
        print("String Denied.")
        pass


#Below is my code for "Write a program that 
# takes as input a string x and accepts it if 
# and only if x is a binary string whose 
# remainder is 2 when divided by 7."

#0 1
delta = [
    [0, 1],     #0
    [2, 3],     #1
    [4, 5],     #2
    [6, 0],     #3
    [1, 2],     #4
    [3, 4],     #5
    [5, 6],     #6
]

startState = 0
F = [2]
inputString = input("Enter a binary number: ")

while len(inputString) > 0:
    currentState = startState
    for x in inputString:
        currentState = delta[currentState][int(x)]
    
    if currentState in F:
        print("String Accepted!")
        quit()
    else:
        print("String Denied")
        quit()
