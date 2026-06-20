#Reverse words in a given String in Python

def reverse_words(sentence):
    words = sentence.split()           # Split the sentence into a list of words
    reversed_list = words[::-1]        # Reverse the list of words
    reversed_sentence = ' '.join(reversed_list)  # Join them back into a string
    print("🔁 Reversed sentence:", reversed_sentence)
# Example usage
user_input = input("Enter a sentence: ")
reverse_words(user_input)