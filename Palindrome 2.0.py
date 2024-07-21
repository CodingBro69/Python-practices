user_input = input("Enter name: ").lower()

new_list = ""
for i in range(len(user_input) - 1, -1, -1):
    a = user_input[i]
    new_list = new_list + a

print(f"New Revesed Name: {new_list}")

if user_input == new_list:
    print("Palindrome")
else:
    print("Not a Palindrome")