"""
text="python, python, java, django, python"
text=text.replace(" ","")
print("AFTER REMOVING SPACES :",text)
count=text.count("python")
print(count)
text=text.replace("python", "Python")
result=text.split(",")
print(result)

"""
text=str(input("ENTER THE SENTENCE :"))
text=text.replace(" ","")
print("AFTER REMOVING SPACES :",text)
cnt=text.count(str(input("ENTER THE WORD TO BE COUNT :")))
print("THE COUNT IS :",cnt)
text=text.replace(input("ENTER THE WORD TO BE REPLACE :"),input("ENTER THE NEW WORD :"))
result=text.split(",")
print(result)