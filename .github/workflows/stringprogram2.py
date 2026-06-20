#Python program to check whether the string is Symmetrical or Palindrome
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    if s == s[::-1]:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

def is_symmetrical(s):
    s = s.replace(" ", "").lower()
    mid = len(s) // 2
    if len(s) % 2 == 0:
        if s[:mid] == s[mid:]:
            print("The string is symmetrical.")
        else:
            print("The string is not symmetrical.")
    else:
        if s[:mid] == s[mid+1:]:
            print("The string is symmetrical.")
        else:
            print("The string is not symmetrical.")

# Example usage
user_input = input("Enter a string: ")
is_palindrome(user_input)
is_symmetrical(user_input)