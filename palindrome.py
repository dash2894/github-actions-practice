def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniformity
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# Example usage
user_input = input("Enter a string: ")
if is_palindrome(user_input):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")