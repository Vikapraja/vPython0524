#14. Write a Python program to count and display the vowels of a given text.  


def vowel(text):
    vowels = "aeiuoAEIOU"
    print(len([letter for letter in text if letter in vowels]))
    print([letter for letter in text if letter in vowels])

 
text=str(input('Enter a str=>'))
print(vowel(text))














