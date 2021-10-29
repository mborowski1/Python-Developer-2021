import re

def check_dice(the_code):
    
    result = re.search(r'[0-9]*[Dd][0-9]+[+-]?[0-9]*', the_code)
    
    try:
        testing = result.group()

    except Exception:
        return False

    if result.group() in the_code:
        return True
   
    
    

test = '8d-h'
print(check_dice(test))

