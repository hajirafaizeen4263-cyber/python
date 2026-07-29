#regular expression
 
import re
# pattern=r"\D{4}\D{4}"
# pattern=r"[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}"
# data="my aadhar number is 2345-5678-3457-9876"
# #\d-decimal digit
# #\w-alpha numeric
# #\D- none decimal
# print(re.search(pattern,data))

# pattern=r"[a-z][a-zA-Z0-9!@#$%^&*()_]+@+[a-z]+.+[a-z]+.+[a-z]"
# data="my email is nDFTGHJ@#$%^&@yahoo.co.in"
# print(re.search(pattern,data))

# pattern=r"([a-z][a-zA-Z0-9!@#$%^&*()_]+)@([a-z]+).([a-z]+)"
# data="my email is nDFTGHJ@#$%^&@yahoo.co.in,nDFTGHJ@#$%^&@yahoo.co.in,nDFTGHJ@#$%^&@yahoo.co.in"
# k=re.findall(pattern,data)
# z=re.search(pattern,data)
# print(z.group(0))
# for i in k: 
    #  print(i)


pattern=r"[a-z]+:[a-zA-Z//]+[a-z]+.[a-z]+.[a-z]+/"
data="https://www.google.com/"
print(re.search(pattern,data))