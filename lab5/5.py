#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'
import re

text = "hdsbbadhbd_dyg3vxcbgjhn44rtdfshab"
x = re.findall('^.*a.*b$', text)   #. -- Any character (except newline character)
print(x)