
def mutable_default(l=[]):
    l.append(1)
    return l

def silent_exception():
    try:
        x = 1 / 0
    except:
        pass

def infinite_loop():
    while True:
        print("forever")

def none_deref():
    x = None
    print(x.attribute)
