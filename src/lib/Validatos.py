

def validateString(field ,value):
    if type(value) != str :
        raise TypeError("The value "+ field + " should be a String")

def validateNumber(field,value):
    if type(value) != int and type(value) != float:
        raise TypeError("The value "+ field + " should be a number" )

def validatePositive(field, value):
    if value <=0 :
        raise ValueError("The value "+ field + " should be greater than cero")