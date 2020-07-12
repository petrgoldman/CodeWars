def move_zeros(array):
    
    l = len(array)
    
    new_array = [x for x in array if x!= 0 or str(x) == 'False']
    
    return new_array + [0]*(l-len(new_array))