def valid_parentheses(string):
    if not string:
        return True
    
    stack = []
    for i in string:
        if i == '(':
            stack.append(i)
            
        elif i == ')':
            if not stack:
                stack.append(i)
            elif stack[-1] == '(':
                stack.pop()
            
    return not stack