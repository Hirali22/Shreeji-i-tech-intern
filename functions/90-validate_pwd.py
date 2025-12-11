# validate password
def validate_pwd(pwd):
    if len(pwd) < 8:
        return False
    else:
        return True
print(validate_pwd("12345678"))