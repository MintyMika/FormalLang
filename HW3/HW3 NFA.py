#Stephen Cornelius
#Dr. Dutter
#MSCS 271-001
#Due: 2/20/2023

#This program will take in a string and determine if it is accepted by the NFA


#------------------------------------------------------------------
#The following code is for the parallelBitmapSearchNFA function

#Declare the transition function
delta2 = [  #This is the delta for the NFA in the book for Chapter 6 Question 7
    [1<<0|1<<1, 1<<0],
    [1<<2, 0],
    [1<<2, 1<<2]
]


#NOTE: Test delta2 first because I know what the results should be

#Define the function
def parallelBitmapSearchNFA(delta, string, acceptingStates = [1, 2, 3], current_state = 0):
    #This function will take in a string and determine if it is accepted by the NFA
    #delta is the transition function represented as an array of bitmaps
    #string is the string to be checked
    #return True if the string is accepted, False otherwise

    #Declare the current state
    current_state = 0

    #Declare the current bitmap
    current_bitmap = 1<<current_state

    #Loop through the string
    for char in range(string):
        #Declare the next bitmap
        next_bitmap = 0

        #Loop through the current bitmap
        for i in range(0, len(delta)):
            #If the current state is in the current bitmap
            if current_bitmap & 1<<i:
                #Add the next state to the next bitmap
                try:
                    next_bitmap |= delta[i][char]
                except:
                    #In effect next_bitmap |= 0
                    pass

        #If the next bitmap is 0, return False
        if next_bitmap == 0:
            return False

        #Set the current bitmap to the next bitmap
        current_bitmap = next_bitmap

    #Loop through the accepting states
    for state in acceptingStates:
        #If the state is in the current bitmap, return True
        if current_bitmap & 1<<state:
            return True

    #If the state is not in the current bitmap, return False
    return False

#---------------------------------------------------------------
#Test the parallelBitmapSearchNFA function
#Declare the accepting states
acceptingStates = [2]

#rewrite the strings to test where a is 1 and b is 0 to test the parallelBitmapSearchNFA function
strings0 = [
    0b1, 0b0, 0b11, 0b10, 0b01,
    0b00, 0b111, 0b110, 0b101,
    0b100, 0b011, 0b010, 0b001,
    0b000, 0b1111, 0b1110, 0b1101,
    0b1100, 0b1011, 0b1010,
    0b1001, 0b1000, 0b0111,
    0b0110, 0b0101, 0b0100,
    0b0011, 0b0010, 0b0001, 0b0000
]

#Uncomment the following code to test the parallelBitmapSearchNFA function
# i = 1
# for x in strings0:
#     print(i, parallelBitmapSearchNFA(delta2, x, acceptingStates))
#     i += 1


#---------------------------------------------------------------
#below is a test of the assigned homework problem

#Declare the transition function
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

#Declare the accepting states
acceptingStates = [2, 6]


#Declare some binary numbers to test
myNums = [
    0b100000000, 0b100000001, 0b100000010, 0b100000011, 0b100000100, 0b100000101, 0b100000110, 0b100000111,
    0b100001000, 0b100001001, 0b100001010, 0b100001011, 0b100001100, 0b100001101, 0b100001110, 0b100001111,
    0b100010000, 0b100010001, 0b100010010, 0b100010011, 0b100010100, 0b100010101, 0b100010110, 0b100010111,
    0b100011000, 0b100011001, 0b100011010, 0b100011011, 0b100011100, 0b100011101, 0b100011110, 0b100011111,
    0b100100000, 0b100100001, 0b100100010, 0b100100011, 0b100100100, 0b100100101, 0b100100110, 0b100100111,
    0b100101000, 0b100101001, 0b100101010, 0b100101011, 0b100101100, 0b100101101, 0b100101110, 0b100101111
]

#Loop through the numbers and test them

i = 1
for x in myNums:
    print(i, parallelBitmapSearchNFA(deltaHw3, x, acceptingStates))
    i += 1