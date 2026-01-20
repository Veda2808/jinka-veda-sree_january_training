# Q3.py
# Fixed version to avoid default mutable argument pitfall

def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items


# Calling multiple times to prove correctness
print(add_item("apple"))
print(add_item("banana"))
print(add_item("orange"))
