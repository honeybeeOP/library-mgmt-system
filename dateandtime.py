def Date():
    #retriving current date
    import datetime
    now=datetime.datetime.now
    return str(now().date())

def Time():
    #retriving current Time
    import datetime
    now=datetime.datetime.now
    return str(now().time())
