# # A list is an ordered,mutable collection that allows duplicates
# # we can access values by using indexing
# info=[1,2,3,3,4,3,True,'avi']
# print(info) # It takes heterogeneous data
# print(type(info)) # <class list>
# info[0]=99
# print(info[0]) #99
# print(f'The length of data is {len(info)}')

# # Tuple : A tuple is an ordered, immutable collection that allows duplicates
# # Faster than list

# data=(1,2,3,'akash','siri','alexa',False,5.7)
# print(data)
# print(type(data))
# print(f'length of data is {len(data)}')
# # data[0]=656 # Tuple object does not support item assignment
# # print(data[0])


# # Set : A set is an unordered mutable collection that does not allow duplicates.
# # set object doesn't support item assignment
# ids={1,2,3,3,3,2,4,6}
# print(ids)
# print(f'The length of ids is {len(ids)}')


# # ids[2]=99
# # print(ids)
# # print(f'The length of ids is {len(ids)}')


# Dictionary : A dictionary stores data in key : value pairs, it is ordered, mutable and 
# keys must be unique, can be accessed via keys

student={
    'name':'Avinash',
    'course':'BCA'
}

print(student)
print(type(student))
print(len(student))
print(student['course']) # can be accessed via keys

