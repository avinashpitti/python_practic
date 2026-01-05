def user_details(**info):
    for key,value in info.items():
        print(key,':',value)
user_details(name='avinash',age=22,city='bengaluru')        
    