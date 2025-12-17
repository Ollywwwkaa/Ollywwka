class SmartList(list):
    def __getitem__(self, index):
        if isinstance(index, slice):
            return super().__getitem__(index)
        if index < 0:
            index = abs(index) - 1
        return super().__getitem__(index)
sl = SmartList([10, 20, 30])
print(sl[0]) 
print(sl[-1]) 
print(sl[-2])   
print(sl[-3]) 
print(sl[1])   
print(sl[2]) 
sl2 = SmartList([1, 2, 3, 4, 5])
print(sl2[1:4])    
print(sl2[-3:]) 
print(sl2[:-2])      