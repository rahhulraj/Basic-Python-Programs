"""
text=" Hello Python Programming "
striping=text.strip()
print(striping)
print("start with Hello ?",striping.startswith("Hello"))
print("ends with Programming ?",striping.endswith("Programming"))

"""

text=str(input("ENTER THE STRING TO CHECK :"))
striping=text.strip()
print(striping)
print("start with ?",striping.startswith(input("string start :")))
print("ends with ?",striping.endswith(input("string end :"))) 