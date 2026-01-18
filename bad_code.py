
def mutable_default(l=None):
    if l is None:
        l = []
    l.append(1)
    return l

def silent_exception():
    try:
        x = 1 / 0
    except:
        pass

def infinite_loop():
    count = 0
    while True:
        print("forever")
        count += 1
        if count > 5:
            break

def none_deref():
    x = None
    print(x.attribute)
