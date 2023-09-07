def is_balanced(expression):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if not stack or stack.pop() != brackets[char]:
                return False

    return not stack

# Test 
expression1 = "([])"
expression2 = "([{)}]"
expression3= "([]{})"
print(is_balanced(expression1))  
print(is_balanced(expression2))  
print(is_balanced(expression3))
