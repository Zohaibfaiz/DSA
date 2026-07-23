# count=1
# while count<=5:
#     print("true")
#     count+=1

# print(count)

# i=2
# while i>1:
#     print("hello")
    
    
#1-100
# i=1
# while i<=100:
#     print(i)
#     i+=1
# print("loop end")

#100-1
# i=100
# while i>=1:
#     print(i)
#     i-=1
# print("loop end")

# #table n
# i=19
# while i<=190:
#     print(i)
#     i+=19
# print("table end")

# i=1
# while i<=10:
#     print(19*i)
#     i+=1

#list
#nums=(1,4,9,16,25,36,49,64,81,100)
# x=int(input("enter a no:"))
# i=0
# while i<len(nums):
#     if(nums[i]==x):
#         print("found at index:",i)
#         break
#     else:
#         print("finding")
#     i+=1
    


# print(nums[0])
# print(nums[1])
    
#continue
# i=0
# while i<=5:
#     if(i==3):
#         i+=2
#         continue
#     print(i)
    
#     student = {
#     "name": "Zohaib",
#     "marks": [80, 90, 70, 85]
# }
# total=0
# for i in student.values():
#   total+=student[i]
# print("total marks is:",total)
n=5
def fac(i):
    if i==0:
      return 1
    fac*=i
    return fac+fac(i-1)
  
print(fac(n))
