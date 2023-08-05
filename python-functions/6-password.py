def validate_password(password):
    if password.len(8):
        return True
    if password.isupper() == True:
        return True
    if password.islower() == True:
        return True
    elif password.isdigit() == True:
        return True
    else:
        return False
    
