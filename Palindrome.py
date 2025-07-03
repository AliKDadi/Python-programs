#BSCIT-05-0836/2022
#Palindrome function
def palindrome():
    original_string=input("Enter a string: ")
    
#remove no-alphanumeric characters and convert to lowercase
    cleaned_string=''.join(char.lower() for char in original_string if char.isalnum())

#check if the cleaned string is equal to it's reverse
    if cleaned_string==cleaned_string[::-1]:
        return f'"{original_string}" is a palindrome.'
    else:
        return f'"{original_string}" is not a palindrome.'

print(palindrome())
