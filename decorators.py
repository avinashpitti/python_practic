def login_req(func):
    def inner(name, login_status):
        if not login_status:
            print("Login Required")
        else:
            return func(name, login_status)
    return inner
