list1 = []
for _ in range(10):
    number = int(input("Enter numbers: "))
    list1.append(number)
print("The entered numbers are: ",list1)
def even_num(list1):
    list2 = []
    for i in list1:
        if  i % 2 != 0:
            list2.append(i)
    print("Odd Numbers are : ",list2)
    return sum(list2)
a = even_num(list1)
print("Sum of odd numbers is :", a)