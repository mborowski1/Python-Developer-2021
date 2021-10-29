import random

def dice(the_thing):

    the_thing_list = list(the_thing)
    minus_one = the_thing_list[-1]
    available_dice = ['D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100']

    if "+" in the_thing_list and "-" in the_thing_list:

        return 'Niewłaściwy format - Wprowadzono zarówno "+", jak i "-".'

    if the_thing_list[-1] == 'D':

        return 'Niewłaściwy format - nie podałeś typu kostki.'
    
    if "D" not in the_thing_list:
        return 'Niewłaściwy format - brak litery D.'

    if "+" not in the_thing_list and "-" not in the_thing_list:

       the_thing_list.remove("D")

       try:

            the_thing_list_joined = ''.join(the_thing_list)
            int_the_thing_list_joined = int(the_thing_list_joined)

       except Exception:

            return 'Niewłaściwy format - użyłeś niedozwolonych znaków.'
    
    if '+' in the_thing_list:

        the_thing_list.remove('+')
        
        if '+' in the_thing_list:
            return 'Niewłaściwy format - zbyt dużo znaków "+".'

        the_thing_list.remove('D')
    
    
        try:

            the_thing_list_joined = ''.join(the_thing_list)
            int_the_thing_list_joined = int(the_thing_list_joined)

        except Exception:

            return 'Niewłaściwy format - użyłeś niedozwolonych znaków.'

    if '-' in the_thing_list:

        the_thing_list.remove('-')
        
        if '-' in the_thing_list:
            return 'Niewłaściwy format - zbyt dużo znaków "-".'

        the_thing_list.remove('D')
    
    
        try:

            the_thing_list_joined = ''.join(the_thing_list)
            int_the_thing_list_joined = int(the_thing_list_joined)

        except Exception:

            return 'Niewłaściwy format - użyłeś niedozwolonych znaków.'

    the_thing_list = list(the_thing)
    
    if '-' in the_thing_list:
        
        

        d_index = the_thing_list.index('D')

        the_thing_list.reverse()

        while d_index > 0:
            the_thing_list.pop()
            d_index -= 1

        
        minus_index = the_thing_list.index('-')

        the_thing_list.reverse()
        

        while minus_index > 0:
            the_thing_list.pop()
            minus_index -= 1

        

        the_thing_list.remove('-')

        this_list_thing_joined = ''.join(the_thing_list)

        

        if this_list_thing_joined not in available_dice:

            return 'Nie ma takiej kostki.'

        the_thing_list = list(the_thing)

    the_thing_list = list(the_thing)

    if '+' in the_thing_list:
        
        

        d_index = the_thing_list.index('D')

        the_thing_list.reverse()

        while d_index > 0:
            the_thing_list.pop()
            d_index -= 1

        
        plus_index = the_thing_list.index('+')

        the_thing_list.reverse()
        

        while plus_index > 0:
            the_thing_list.pop()
            plus_index -= 1

        

        the_thing_list.remove('+')

        this_list_thing_joined = ''.join(the_thing_list)

        

        if this_list_thing_joined not in available_dice:

            return 'Nie ma takiej kostki.'

        the_thing_list = list(the_thing)

    the_thing_list = list(the_thing)

    if '+' not in the_thing_list and '-' not in the_thing_list:

        d_index = the_thing_list.index('D')
        the_thing_list.reverse()

        while d_index > 0:
            the_thing_list.pop() 
            d_index -= 1

        the_thing_list.reverse()   

        this_thing_list_joined = ''.join(the_thing_list)
        
        

        if this_thing_list_joined not in available_dice:

            return 'Nie ma takiej kostki.'

    the_thing_list = list(the_thing)

    if the_thing_list[0] == 'D' and '+' not in the_thing_list and '-' not in the_thing_list:

        the_thing_list.remove('D')
        the_thing_list_joined = ''.join(the_thing_list)
        the_thing_list_joined_int = int(the_thing_list_joined)

        the_result = random.randint(1, the_thing_list_joined_int)

        return the_result

    if the_thing_list[0] != 'D' and '+' not in the_thing_list and '-' not in the_thing_list:
        
        how_many_rolls = []
        the_result = 0
        
        for i in the_thing_list:
            if i != 'D':
                how_many_rolls.append(i)
            if i == 'D':
                break

        

        joined = ''.join(how_many_rolls)
        how_many_rolls_int = int(joined)
        
        

        
                 
        d_index = the_thing_list.index('D')
        the_thing_list.reverse()

        while d_index > 0:
            the_thing_list.pop() 
            d_index -= 1

        the_thing_list.reverse()   

        

        the_thing_list.remove('D')
        the_type_of_die = ''.join(the_thing_list)
        the_type_of_die_int = int(the_type_of_die)
        
        

        while how_many_rolls_int > 0:
            the_result += random.randint(1, the_type_of_die_int)
            how_many_rolls_int -= 1

        return the_result 

    if the_thing_list[0] == 'D' and '+' in the_thing_list:

        the_thing_list.remove('D')

        type_of_die = []
        modifier = []
        the_result = 0
        
        plus_index = the_thing_list.index('+')
        
        while plus_index >= 0:
            type_of_die.append(the_thing_list[plus_index])
            plus_index -= 1

        type_of_die.remove('+')
        type_of_die.reverse()
        type_of_die_joined = ''.join(type_of_die)
        type_of_die_joined_int = int(type_of_die_joined)
        
        the_thing_list.reverse()
        plus_index = the_thing_list.index('+')
            
        while plus_index >= 0:
            modifier.append(the_thing_list[plus_index])
            plus_index -= 1

        modifier.remove('+')

        modifier_joined = ''.join(modifier)
        modifier_joined_int = int(modifier_joined)

        the_result += random.randint(1, type_of_die_joined_int)
        the_result += modifier_joined_int

        return the_result

    if the_thing_list[0] == 'D' and '-' in the_thing_list:

        the_thing_list.remove('D')

        type_of_die = []
        modifier = []
        the_result = 0
        
        minus_index = the_thing_list.index('-')
        
        while minus_index >= 0:
            type_of_die.append(the_thing_list[minus_index])
            minus_index -= 1

        type_of_die.remove('-')
        type_of_die.reverse()
        type_of_die_joined = ''.join(type_of_die)
        type_of_die_joined_int = int(type_of_die_joined)
        
        the_thing_list.reverse()
        minus_index = the_thing_list.index('-')
            
        while minus_index >= 0:
            modifier.append(the_thing_list[minus_index])
            minus_index -= 1

        modifier.remove('-')

        modifier_joined = ''.join(modifier)
        modifier_joined_int = int(modifier_joined)

        the_result += random.randint(1, type_of_die_joined_int)
        the_result -= modifier_joined_int

        return the_result

    if the_thing_list[0] != 'D' and '+' in the_thing_list:

        modifier = []
        how_many_rolls = []
        the_result = 0
        
        

        for i in the_thing_list:
            if i != 'D':
                how_many_rolls.append(i)
            if i == 'D':
                break

        

        joined = ''.join(how_many_rolls)
        how_many_rolls_int = int(joined)
        
        

        
                 
        d_index = the_thing_list.index('D')
        the_thing_list.reverse()

        while d_index > 0:
            the_thing_list.pop() 
            d_index -= 1

          

        

        the_thing_list.remove('D')
        the_thing_list.reverse()

        plus_index = the_thing_list.index('+')

        
        while plus_index > 0:
            the_thing_list.pop()
            plus_index -= 1

        

        the_type_of_die = ''.join(the_thing_list)
        the_type_of_die_int = int(the_type_of_die)
        
        

        while how_many_rolls_int > 0:
            the_result += random.randint(1, the_type_of_die_int)
            how_many_rolls_int -= 1

        the_thing_list = list(the_thing)
        the_thing_list.reverse()
        plus_index = the_thing_list.index('+')
        
        while plus_index >= 0:
            modifier.append(the_thing_list[plus_index])
            plus_index -= 1

        modifier.remove('+')
        modifier_joined = ''.join(modifier)
        modifier_int = int(modifier_joined)
        the_result += modifier_int
        
        return the_result
    
    if the_thing_list[0] != 'D' and '-' in the_thing_list:

        modifier = []
        how_many_rolls = []
        the_result = 0
        
        

        for i in the_thing_list:
            if i != 'D':
                how_many_rolls.append(i)
            if i == 'D':
                break

        

        joined = ''.join(how_many_rolls)
        how_many_rolls_int = int(joined)
        
        

        
                 
        d_index = the_thing_list.index('D')
        the_thing_list.reverse()

        while d_index > 0:
            the_thing_list.pop() 
            d_index -= 1

          

        

        the_thing_list.remove('D')
        the_thing_list.reverse()

        minus_index = the_thing_list.index('-')

        
        while minus_index > 0:
            the_thing_list.pop()
            minus_index -= 1

        

        the_type_of_die = ''.join(the_thing_list)
        the_type_of_die_int = int(the_type_of_die)
        
        

        while how_many_rolls_int > 0:
            the_result += random.randint(1, the_type_of_die_int)
            how_many_rolls_int -= 1

        the_thing_list = list(the_thing)
        the_thing_list.reverse()
        minus_index = the_thing_list.index('-')
        
        while minus_index >= 0:
            modifier.append(the_thing_list[minus_index])
            minus_index -= 1

        modifier.remove('-')
        modifier_joined = ''.join(modifier)
        modifier_int = int(modifier_joined)
        the_result -= modifier_int
        
        return the_result
        
test = dice('2D10-5')
print(test)








































    
