
def bad_mutable(a=[]): # B001
    return a

def bad_infinite(): # L001
    while True:
        pass

def bad_none(): # L003
    x = None
    print(x.foo)

def safe_none(x=None): # Should be safe in V2 if guarded
    if x is None:
        return
    print(x.foo)

def new_silent_exception():
    try:
        1/0
    except:
        pass
