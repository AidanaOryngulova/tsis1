def isPalindrome(s):
    s=s.lower()
    return s==s[::-1]

s=input()
if isPalindrome(s):
    print(" it is Palindrome")
else:
    print("it is not a Palindrome")