def collatz_conjecture(x):
    # Initialize the sequence list
    seq = [x]

    #Base Case: If x is 1 then return
    if x is 1:
        return []

    #Start the infinite loop, loop will break when x is 1
    while x > 1:
        #If x is even, divide by 2
        #If x is odd, multiply by 3 and add 1
        if x % 2 == 0:
            x = x / 2
        else:
            x = (x*3)+1
        #Add x to the sequence
        seq.append(x)

    #return the sequence when 1 is reached
    return seq


print collatz_conjecture(11)
