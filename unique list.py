def unique_elements(list):
    unique_list = []
    for i in list:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

original_list = []
for nbr in range(9):
    a = int(input("enter the list: "))
    original_list.append(a)
print(unique_elements(original_list))
# original_list = [1,2,2,3,4,4,4,5,5,5,6,7,8,9,1]