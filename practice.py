# A list is an ordered,mutable collection that allows duplicates
# we can access values by using indexing
info=[1,2,3,3,4,3,True,'avi']
print(info) # It takes heterogeneous data
print(type(info)) # <class list>
info[0]=99
print(info[0]) #99
print(f'The length of data is {len(info)}')