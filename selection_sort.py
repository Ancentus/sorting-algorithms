def selection_sort(a_list):
    for fill_spot in range(len(a_list)-1, 0, -1):
        pos_of_max = 0
        for location in range(1, fill_spot+1):
            if a_list[location] > a_list[pos_of_max]:
                pos_of_max = location
        a_list[pos_of_max], a_list[fill_spot] = a_list[fill_spot], a_list[pos_of_max]

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort(a_list)
print(a_list)