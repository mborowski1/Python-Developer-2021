import random

size = random.randint(3, 9)
print(size)

table_of_stars = []

while size > 0:
    table_of_stars.append('*')
    size -= 1

final_table = []

for i in table_of_stars:    
        final_table.append('*')
        joined_table = ''.join(final_table)
        print(joined_table)
    

        

