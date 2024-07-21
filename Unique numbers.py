list1 = []
for nbr in range(9):
    a = int(input("Enter the numbers: "))
    list1.append(a)
print(f"Entered list: {list1}")
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print(f"unique numbers are: {list2}")