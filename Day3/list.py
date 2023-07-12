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


#reverse
li=[1,2,3,4,5,6,7,8,9]
print(li[::-1])

li=[1,2,3,4,5,6,7,8,9]
li.reverse()
print(li)

