# A module to parse python tracebacks

## This module needs to be made more defensive

#strip bad characters
def strip_bad(string):
    bad = ['(', ')', '&', '*', '^', '$', '<', '>', '\\', '/']
    return ''.join([ch for ch in string if ch not in bad]).strip()


def format_error(err):
    
    split_err = err.split('\n')

    if split_err[-2].find('SyntaxError') != -1:

        error_type = strip_bad(split_err[-2])
        error_info = strip_bad(split_err[-5])
        
    else:
        
        error_type = strip_bad(split_err[-2])
        error_info = strip_bad(split_err[-4])

    return error_info + '--' + error_type


