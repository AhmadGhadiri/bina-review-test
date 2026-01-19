# Category: style (Rule: N001) - SHOULD BE REPORTED
def get_status():
    pass

# Category: maintainability (Rule: B001) - SHOULD BE REPORTED
def process_items(items=[]):
    items.append(1)
    return items

# Category: correctness (Rule: L001) - SHOULD NOT BE REPORTED (not in custom-demo profile)
def forever():
    while True:
        pass
