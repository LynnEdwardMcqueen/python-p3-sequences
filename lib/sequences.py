#!/usr/bin/env python3

def print_fibonacci(length):
    fib_vals = []

    if length == 0:
        print ('[]' )
        return
    
    if length == 1:
        print( '[0]')
        return

    if length == 2:
        print("[0, 1]")
        return
    
    if length > 0 :
        for i in range(length) :
    
            if (i == 0):
                fib_vals.append(0)
            elif (i == 1):
                fib_vals.append(1)
            else:
                fib_vals.append(fib_vals[-1] + fib_vals[-2])
    
    ret_val = "["
    for i in range(length):
        ret_val += str(fib_vals[i])
        if (i < length - 1):
            ret_val += ", "
    
    ret_val += "]"
    print(ret_val)

for i in range(9):
    print_fibonacci(i)

