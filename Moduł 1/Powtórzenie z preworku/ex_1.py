import random

no_of_stars = random.randint(1, 20)
backup_no_of_stars = no_of_stars
table_of_stars = []

while no_of_stars > 0:
    table_of_stars.append('*')
    no_of_stars -=1

joined_table = ''.join(table_of_stars)


print("Liczba gwiazdek:", backup_no_of_stars)
print(joined_table)
