"""
1 2 + 3 4 - *
"""
def main(A: str) -> str:
    stack = []
    for a in A.split(" "):
        if a.isdigit():
            stack.append(a)
        else:
            y, x = stack.pop(), stack.pop()
            # ずるいかも
            stack.append(eval(f"{x} {a} {y}"))

    return stack[0]


A = "1 2 + 3 4 - *"
# A = "1 2 - 3 4 * +"
# A = "10 2 - 3 4 * +"
result = main(A)
print(result)
