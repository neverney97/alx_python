def validate_password(password):
    if len(password) >= 8:
        return True
        if password.isupper() == True:
            return True
        if password.islower() == True:
            return True
        elif password.isdigit() == True:
            return True
    else:
        return False
    
