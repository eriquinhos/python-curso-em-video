# This directory is going to be used to put some useful functions through the development of the exercises

def isnumber(string):
    '''
    This function should be used instead of isnumeric() one, because this standard function does not consider '.' as
    numeric. That is why isnumber() is useful when you need to analyse float numbers.

    :param string: The user should put a string type variable or value here to be analysed
    :return: Return True if it is a int/float type number, False if it is not
    '''
    try:
        float(string)
        return True
    except ValueError:
        return False
