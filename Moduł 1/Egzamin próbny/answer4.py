def div(argument_1, argument_2):

    aux_list_1 = [x for x in range(argument_1)]
    aux_list_2 = [x for x in range(argument_2 + 1)]

    for i in aux_list_1:

        if i in aux_list_2:

            aux_list_2.remove(i)

    for i in aux_list_2:    

        if i % 2 != 0:

            aux_list_2.remove(i)

    for i in aux_list_2:

        if i % 3 == 0:

            aux_list_2.remove(i)


    return aux_list_2

test_1 = 20
test_2 = 30

print(div(test_1, test_2))
