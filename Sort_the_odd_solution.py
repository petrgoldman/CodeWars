def sort_array(source_array):
    if not source_array:
        return []
    
    helper = [True if i % 2 != 0 and i != 0 else False for i in source_array]
    
    odd_list = []
    new_list = []
    for i in source_array:
        if i % 2 != 0 and i != 0:
            odd_list.append(i)
            
    sorted_odd = sorted(odd_list)
            
    x = 0    
    for i in range(len(source_array)):
        if helper[i]:
            new_list.append(sorted_odd[x])
            x += 1
        else:
            new_list.append(source_array[i])
    return new_list