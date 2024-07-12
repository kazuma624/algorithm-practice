"""
1 2 + 3 4 - *
"""

_max = 100

class stack:
    def __init__(self) -> None:
        self.top = 0
        self.max = _max
        self.stack = [None] * self.max

    def is_empty(self) -> bool:
        return self.top == 0

    def is_full(self) -> bool:
        return self.top >= self.max - 1

    def push(self, x: str):
        if self.is_full():
            raise OverflowError("オーバーフロー")

        self.top += 1
        self.stack[self.top] = x

    def pop(self) -> str:
        if self.is_empty():
            raise UnderFlowException("アンダーフロー")

        self.top -= 1
        return self.stack[self.top + 1]


class OverFlowException(IndexError):
    pass


class UnderFlowException(IndexError):
    pass


def main(A: str) -> str:
    s = stack()
    for a in A.split(" "):
        if a == "+":
            y, x = s.pop(), s.pop()
            s.push(x + y)
        elif a == "-":
            y, x = s.pop(), s.pop()
            s.push(x - y)
        elif a == "*":
            y, x = s.pop(), s.pop()
            s.push(x * y)
        else:
            s.push(int(a))

    print(s.stack)
    return s.pop()


A = "1 2 + 3 4 - *"
# A = "1 2 - 3 4 * +"
# A = "10 2 - 3 4 * +"
result = main(A)
print(result)
