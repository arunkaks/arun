#what is list?
#A list in pyhton is need to store the sequence of various types of data.
#python lists are mutable type its mean we can modigy its element after ot created.
#A list can be defined as a collection of value or items of different types.

#list is mutable in nature
#list is enclosed with square brackets[].
#list will allow duplicate values.
#list will support indexing.



#How many types we can define list?

# arun=[]
# print(arun)

# arun=list()
# print(type(arun))



 #list methods
 #append(),copy(),clear(),count(),extend(),index(),insert(),pop(),remove(),reverse(),sort()
#syntax=variable_name.method()

#Append

#
# arun=[1,2,3,4,5,777,888,999]
# arun.append('arjun')
# print(arun)
#
# arun=[1,2,5,6,7,9]
# arun.append([1,2,3,4,5,5,7,8,8,9945,3,45,345])
# print(arun)


#Extend
# data=[1,2,4,5,6,7,8,9,2]
# data.extend([10,11,13,1,4,1,13,13,24,253,657,342])
# print(data)


# user=[2,3,4,5,6,87,4,3,2,34,43242]
# user.extend([89])
# print(user)

# #Index
# abhi=[1,2,3,4,52,1,13,32,432,32]
# print(abhi.index(52))

# count

# harsha=[3,6,2,5,3,44,5,5,6,7,8,9]
# print(harsha.count(5))

#
# # clear
# harsha=[3,6,2,5,3,44,5,5,6,7,8,9]
# harsha.clear()
# print(harsha)
#
# #insert
# harsha=[3,6,2,5,3,44,5,5,6,7,8,9]
# harsha.insert(3,4564333)
# print(harsha)
#
# #pop by using index it will remove the elements
# sai=[3,4,5,6,7,8,4,2,5]
# sai.pop(6)
# print(sai)
#
# #Remove by using elements it will remove
# jagu=[3,4,5,6,7,8,4,2,5]
# jagu.remove(6)
# print(jagu)

#
# #reverse
# li=[1,2,3,4,5,6,7,8,9]
# print(li[::-1])
#
# li=[1,2,3,4,5,6,7,8,9]
# li.reverse()
# print(li)


# a=15
#
# if (a<5):
#     print("A is less than five")
# if(a<10):
#     print("A is less than ten")
# if (a<15):
#     print("A is less than fifteen")
# if(a<20):
#     print("A is less than twenty")
# if(a<25):
#     print("A is less than twentyfive")

#
# li=[1,2,3,456,56,456,5,6,7]
# for i in range(len(li)):
#     if li[i]==456:
#         li[i]=2
# print(li)


# l=[1,2,3,456,32,456]
# for i in range(len(l)):
#     if l[i]==456:
#         print(i)
#
#
#
# l=[1,2,3,456,32,456]
# for i in range(len(l)):
#     if l[i]==456:
#         l[i]=5
# print(l)
#
#


#list compresion

# print([i**2 for i in [1,2,3,4,5,6]])





#Membership operator
#
# a=[1,-2,3,4,5,56]
# print(-2 not in a)
#
#
#
# aa=[1,-2,3,4,5,56]
# print(-2 in aa)


#identity Operator
# a=[1,2,3,4,5,6,7,8]
# aa=[1,2,3,4,5,6,7,8]    [here values are same but id will come different because it is list]
# print(id(a)==id(aa))


# a=1
# aa=1                  [here valuse are als same and id also same beacause its not in list]
# print(id(a)==id(aa))



