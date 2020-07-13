def removNb(n):
    input_list = list(range(1,n+1))
    total = sum(input_list)
    out = []
    for a in input_list:
        b = (total - a)/(a+1)
        if b//1==b and b > 0 and b < n+1:
            out.append((a,int(b)))
    return(sorted(out))