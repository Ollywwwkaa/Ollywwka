def deep_flatten(lst):
    result = []
    for element in lst:
        if isinstance(element, list):
            result.extend(deep_flatten(element))
        else:
            result.append(element)
    return result
complex_lst = [1, [2, [3, 4], 5], 6, [[7], 8]]
print(deep_flatten(complex_lst))
print(deep_flatten([]))          
print(deep_flatten([1, 2, 3])) 
print(deep_flatten([[[1]]]))
print(deep_flatten([1, [2], [3, [4, [5]]]]))