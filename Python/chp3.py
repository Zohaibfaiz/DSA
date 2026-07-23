# marks=[12,23,34,45,56,67,78,89,90]
# print(marks)
# print(marks[4])
# print(len(marks))
# marks[5]=00
# print(marks)
# print(type(marks))
# print(marks[1:4])
# print(marks[:4])
# print(marks[1:])
# print(marks[-4:-1])


#methods
#list=[5,6,7,3,2,4,1,8]
#list.append(9)
# print(list)
# list.sort()
# print(list)
# list.sort(reverse=True)
# print(list)

# list1=["banana","apple","litchi"]
# list1.reverse()
# print(list1)

# list.insert(5,9)
# print(list)

# list.remove(3)
# list.pop(7)
# print(list)


#tuple
# tuple=(23,43,65,67,89,67,67)
# # print(tuple)
# # print(tuple[4])
# # print(type(tuple))
# tup=tuple.index(65)
# print(tup)


# print(tuple.count(67))


#movie
# movie1=input("enter  movie1:")
# movie2=input("enter  movie2:")
# movie3=input("enter  movie3:")
# list=[movie1,movie2,movie3]
# print(list)


#palindrome
# list1=[1,2,3,2,1]
# list2=[1,"abc","abc",6,6,1]

# copy_list1=list1.copy()
# copy_list1.reverse()

# copy_list2=list2.copy()
# copy_list2.reverse()

# if(copy_list1==list1):
#     print("list contain a palindrome element")
# else:
#     print("list  not contain a palindrome element")
    
    
    
# if(copy_list2==list2):
#     print("list contain a palindrome element")
# else:
#     print("list not contain a palindrome element")



# count/store
# list=["C","D","A","A","B","B","A"]
# print(list.count("A"))
# list.sort()
# print(list)

#search in list
# list=["ali","ahmad","usman","zohiab","hamza"]
# name=input("Enter your name:")
# if(name in list):
#     print("found")
# else:
#     print("not found")


# password
# password=input("enter a strong password:")
# if(len(password)>8):
#     print("strong password")
# else:
#     print("weak password")
    
# bill calculate/disscount
list=[100,250,300,150]
bill=sum(list)
print("total bill is:",bill)
if(bill >700):
    print("discount available")
else:
    print("no disscount")
