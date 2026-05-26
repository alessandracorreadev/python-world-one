def file_validator(file_name):
    try:
        f = open(file_name, 'r')
        f.close()
    except:
        return False
    else:
        return True
