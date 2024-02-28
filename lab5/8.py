#Write a Python program to split a string at uppercase letters.
import re

text = "SdnidawpwsmoGsamdasS"

x = re.split('[A-Z]', text)
print(x)