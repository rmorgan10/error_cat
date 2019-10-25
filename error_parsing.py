# A module to parse python tracebacks

#strip bad characters
def strip_bad(string):
    bad = ['(', ')', '&', '*', '^', '$', '<', '>', '\\', '/']
    return ''.join([ch for ch in string if ch not in bad])




def format_error(err):
    
    split_err = err.split('\n')

    if split_err[-2].find('SyntaxError') != -1:

        error_type = strip_bad(split_err[-2])
        error_info = strip_bad(split_err[-5])
        
    else:
        
        error_type = strip_bad(split_err[-2])
        error_info = strip_bad(split_err[-4])

    #return error_info, error_type
    return error_info + '--' + error_type

"""
Traceback (most recent call last):
  File "fake_error.py", line 14, in <module>
    func()
  File "fake_error.py", line 7, in func
    func2()
  File "fake_error.py", line 11, in func2
    print(5.0 / 0)
ZeroDivisionError: float division by zero

"""
