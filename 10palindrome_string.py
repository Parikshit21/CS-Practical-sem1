#Q10 WAF that takes a string as an input from the user 
# and determine whether it is palindrome or not.

def palindrome():
    s=str(input('Enter string: '))
    if s==s[::-1]:
        return True
    else:
        return False

print(palindrome())