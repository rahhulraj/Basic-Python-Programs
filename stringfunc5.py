"""
text="python,java,python,c++,java"
cnt=text.count("python")
print(cnt)
replacing=text.replace("java","django")
result=replacing.split(",")
print(result)

"""

text=str(input("ENTER THE SENTENCE :"))
cnt=text.count(input("ENTER THE WORD TO BE COUNT :"))
print(cnt)
replacing=text.replace(input("ENTER THE WORD TO BE REPLACE :"),input("ENTER THE NEW WORD :"))
result=replacing.split(",")
print(result)


