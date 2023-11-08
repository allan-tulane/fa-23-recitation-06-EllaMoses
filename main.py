def fib_recursive(n, counts):
    """
    Return the nth Fibonacci number. 
    counts is a list of n+1 elements, where counts[i] is incremented
    each time fib_recursive(i, counts) is called.
    """    
    counts[n] += 1 #keeps track of how many times fib_recursive(n, counts) is called for each n
    if n == 0: #base case, if n is 0, fib value is 0
        return 0
    elif n== 1: #base case, if n is 1, fib value is 1
        return 1
    else: #recursive case, if n >= 2, the fib value is the sum of the previous 2 elements
        return fib_recursive(n-1, counts) + fib_recursive(n-2, counts)
    
 
def fib_top_down(n, fibs):
    if fibs[n] != -1: #fibs is initialized with all -1s so if the nth term of fibs is not -1 it has already been found
        return fibs[n] 
    elif n == 0: #base case, if n is 0, fib value is 0
        fibs[n] = 0
    elif n == 1: #base case, if n is 1, fib value is 1
        fibs[n] = 1
    else: #recursive case: the nth term of the fibonacci sequence is equal to the sum of the previous two terms
        fibs[n] = fib_top_down(n-1,fibs) + fib_top_down(n-2,fibs)
    return fibs[n]



def fib_bottom_up(n):
    list = [0] * (n+1) #create a list with n+1 0's
    if n >= 1: # if n is greater than 1, set the second term in the list to 1
        list[1] = 1
    for i in range(2, n+1): #for every value after the first 2 values, the fibonacci sequence is equal to the sum of the previous two terms
        list[i] = list[i - 1] + list [i-2]
    return list[-1] #return the final value in the list, the nth fibonacci number

 
