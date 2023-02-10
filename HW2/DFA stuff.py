#Stephen Cornelius
#Dr. Dutter
#MSCS271-001
#11 Febuary 2023

#Below is my code for the Man, Wolf, Goat, Cabbage problem as described in Ch.4 Q:3



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