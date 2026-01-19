# This file will generate findings to be exported in SARIF format

def unsafe_mutable_default(items=[]): # Rule B001 (Maintainability)
    items.append("finding")
    return items

def unchecked_none(x): # Rule L003 (Correctness)
    val = None
    if x > 10:
        val = {"key": "value"}
    
    # Potential None dereference if x <= 10
    print(val["key"])

def infinite_loop(): # Rule L001 (Correctness)
    while True:
        pass
