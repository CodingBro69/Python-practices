def unique_elements(list):
    unique_list = []
    for i in list:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list


original_list = []
no_of_elements = int(input("how many elemnets u want in list: "))  # 5
while no_of_elements > 0:
    no_of_elements -= 1
    numbers = int(input("enter numbers: "))
    original_list.append(numbers)

print(unique_elements(original_list))