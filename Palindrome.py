def is_palindrome(string):
    string = ''.join(
        char.lower()
                for char in string
                if char.isalnum()
    )
    return string == string[::-1]

user_input = input("Enter a string: ")

print(is_palindrome(user_input))