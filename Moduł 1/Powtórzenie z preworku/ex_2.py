import random

rows = random.randint(5, 15)
columns = random.randint(5, 15)
a = ''

print('Wartość zmiennej rows:', rows)
print('Wartość zmiennej columns:', columns)

table_of_stars = []

while columns > 0:
   table_of_stars.append('*')
   columns -= 1

joined_table = ''.join(table_of_stars)

while rows > 0:
    print(joined_table)
    rows -= 1


        

