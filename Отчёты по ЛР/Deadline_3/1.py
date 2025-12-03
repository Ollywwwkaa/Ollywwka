def create():
    count=0
    def create1():
        nonlocal count 
        count += 1
        return count
    return create1
create1 = create()
print (create1())
print (create1())
print(create1())
print(create1())