def int32_to_ip(int32):
    # your code here
    
    first = (int32 & 4278190080)>>24
    second = (int32 & 16711680)>>16
    third =  (int32 & 65280)>>8
    fourth = (int32 & 255)
    
    return f'{str(first)}.{str(second)}.{str(third)}.{str(fourth)}'