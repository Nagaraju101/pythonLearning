def addTwoNumbers(a,b):
    try:
        return (a + b)
    # except TypeError:
    #     return ('Invalid number')
    # except NameError:
    #     return ('Invalid parametername')
    except Exception as e:
        return(e)
    else:
        print("Execution successful")
    finally:
        print('THE END')



print(addTwoNumbers(1,5))
print(addTwoNumbers(7, 7))
print(addTwoNumbers(7,'a'))
print(addTwoNumbers(10, 15))
print('Execution completed')


# User defined Exception
def add2Numbers(a, b):
    try:
        if (isinstance(a,int) or isinstance(a, float)) and isinstance(b,int) or isinstance(b,float):
            return (a + b)
        else:
            raise Exception('Only INT or FLOAT values are accepted!!')
    except Exception as ex:
        return ex
    
    

    
