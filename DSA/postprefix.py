# Function to check precedence
def precedence(op):
    if op in ['+', '-']:
        return 1
    elif op in ['*', '/']:
        return 2
    elif op == '^':
        return 3
    return 0


# Infix to Postfix
def infix_to_postfix(exp):
    stack = []
    result = ""

    for ch in exp:
        if ch.isalnum():  # Operand
            result += ch
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
        else:  # Operator
            while stack and precedence(ch) <= precedence(stack[-1]):
                result += stack.pop()
            stack.append(ch)

    while stack:
        result += stack.pop()

    return result


# Infix to Prefix
def infix_to_prefix(exp):
    exp = exp[::-1]   # Reverse
    new_exp = ""

    # Change brackets
    for ch in exp:
        if ch == '(':
            new_exp += ')'
        elif ch == ')':
            new_exp += '('
        else:
            new_exp += ch

    postfix = infix_to_postfix(new_exp)
    return postfix[::-1]   # Reverse again


# -------- Main Program --------

exp = input("Enter Infix Expression: ")

postfix = infix_to_postfix(exp)
prefix = infix_to_prefix(exp)

print("Postfix Expression:", postfix)
print("Prefix Expression :", prefix)

