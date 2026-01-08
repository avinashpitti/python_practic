# Decorator is a function,it takes one function as an argument,
# and modify the functionality and returns a modified function as a value.

# without decorators : not validating login status
def home_page(name,login_status):
    return 'home page'


def product_page(name,login_status):
    return 'product page'

def order_page(name,login_status):
    return 'order page'

def profile_page(name,login_status):
    return 'profile page'


print(home_page('RG',False))
print(product_page('RG',False))
print(order_page('RG',False))
print(profile_page('RG',False))


# with decorators






