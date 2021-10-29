def chessboard(n=8):
    aux_1 = '# # # # \n'
    aux_2 = '# # # # \n # # # #\n'
    result_thing = ''
    
    while n > 0:
        if n == 1:
            result_thing += aux_1
            n -= 1
        else:
            result_thing += aux_2
            n -= 2
    return result_thing

check = chessboard(10)
print(check)
            
	
