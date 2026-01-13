

#list=[]ordered and changeable. Duplicates okkk
#set={}unordered and immutable, but add/remove ok. no duplicable
#Tuple=()ordered and unchangable,  Duplicates ok.FASTER


fruits=["apple","banana","orange","strawberry"]
#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))
#print("apple" in fruits)
#print("pinaple"in fruits) #this all are  Tuple


fruits.append("pinaple")

#fruits.insert(1,"palm") #posi 1 add palm
#fruits.reverse() #z to a
#fruits.sort() #a to z
#print(fruits.index("apple")) # apple index
#print(fruits.count("apple")) # count apple

#fruits.add("apple")
fruits.pop()
fruits.append("palm")# add fruits
#fruits.remove("apple")
#fruits.clear() #clear all

print(fruits)

#print(fruits[::2])