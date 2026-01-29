from importlib.metadata import files
with open('notes.txt','w') as f:
    print(f.write('This is line 1\n'))
    print(f.write('This is line 2\n'))
    print(f.write('This is line 3\n'))
    print(f.write('This is line 4\n'))
    print(f.write('This is line 5\n'))

with open('notes.txt','r') as f:
    
    data=f.read()
    print(data)

with open('notes.txt','r') as f :
    data =f.readline()
    print(data)

with open('notes.txt','w') as f :
    data=f.write('my name is avinash\n')
    data=f.write('I am 21 years old\n')

with open('notes.txt','a')as f:
    data=f.write('Today date is 29-jan-2026')

with open('notes.txt','r') as f :
    data=f.read()
    print('Number of characters :',len(data))

with open('notes.txt','r') as f :
    lines=f.readlines()  
    print('Number of lines : ',len(lines))

count=0
with open('notes.txt','r') as f :
    for line in f :
        count+=1
print("Number of lines :",count)


# Task
# Invoke restapis(request)
# read json file(products.json)
# write into new pdf files

# task1
# products.json
# readwrite.py
# prod.pdf




