def main(A: str) -> str:
    """最初からスタックに入れる想定で作ってしまった"""
    stack = A.split(" ")
    operands, operators = read(stack)
    while True:
        operands, operators = calc(operands, operators)
        if len(operands) == 1:
            break

    return operands[0]


def read(stack: list[str]):
    """スタックから取り出して数値と演算子を別々のスタックに格納する。"""
    operands = []
    operators = []
    while True:
        try:
            a = stack.pop()
            if a.isdigit():
                operands.append(a)
            else:
                operators.append(a)

        except IndexError:
            break

    return operands, operators


def calc(operands: list[str], operators: list[str]):
    """
    数値のスタックから2つ要素を取り出す。
    対応する演算子のスタックから取り出した演算を行う。
    計算結果を新しい数値のスタックに格納する。
    数値のスタックを全て取り出したら、新しい数値のスタックと残った演算子のスタックを返却する。
    """
    result = []
    while True:
        try:
            x, y = operands.pop(), operands.pop()
            op = operators.pop()
            result.append(eval(f"{x} {op} {y}"))
        except IndexError:
            break

    return result, operators


A = "1 2 + 3 4 - *"
# A = "1 2 - 3 4 * +"
# A = "10 2 - 3 4 * +"
result = main(A)
print(result)
