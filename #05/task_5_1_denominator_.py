'''
    Write  the function divide(numerator, denominator) the two
    input parameters of which are numbers.
    The function returns the result of dividing two numbers.
    
    GOOD INPUT:
    1)  in case of correct data the function should be displayed the
        corresponding message – "Result is  numerator / denominator" 

    BAD INPUT:
    2) in the case of division by zero the function should be displayed
       the corresponding message – "Oops, numerator / denominator, division by zero is error!!!" 

    3) in the case of incorrect data the function should be displayed the message – "Value Error! You did not enter a number!"
    Note: in the function you must use the "try except" construct. 

    Function example:
    divide(8, 16)        #output:   "Result is 0.5" 

    divide (5, 0)        #output:   "Oops, 5 / 0 denominator, division by zero is error!!!" 
    !!! NOTE denominator - should be not placed in formatted str

    divide_number("25", 5)    #output:   "Value Error! You did not enter a number!"
    !!! NOTE: should define divide() function instead of divide_number()

    divide_number("abc", 9)  #output:    "Value Error! You did not enter a number!"
    
'''


def divide(numerator, denominator):
    try:
        return f'Result is {numerator / denominator}'
    except ZeroDivisionError as error:
        return f'Oops, {numerator}/{denominator}, division by zero is error!!!'
    except (ValueError, TypeError) as error:
        return f'Value Error! You did not enter a number!'


# tests Soft serve:

# 1 divide(8, 16)            #output: "Result is 0.5"
#print(divide(8, 16))        # ok +

# 2 divide (5, 0)            #output: "Oops, 5 / 0 denominator, division by zero is error!!!"
#print(divide(5, 0))         # ok +

# 3 divide_number("25", 5)   #output:   "Value Error! You did not enter a number!" ### shuold be divide() instead of divide_number()
#print(divide("25", 5))      # ok +

# 4 divide_number("abc", 9)  #output:    "Value Error! You did not enter a number!"
#print(divide("abc", 9))
