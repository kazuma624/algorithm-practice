"""
1 2 + 3 4 - *
"""

_max = 100


class stack:
    def __init__(self) -> None:
        """スタックの枠を作る
        """
        self.top = 0
        self.max = _max
        self.stack = [None] * self.max

    def is_empty(self) -> bool:
        """スタックが空か否かを返す

        Returns:
            bool: スタックが空の場合 True
        """
        return self.top == 0

    def is_full(self) -> bool:
        """スタックがいっぱいか否かを返す

        Returns:
            bool: スタックがいっぱいの場合 True
        """
        return self.top >= self.max - 1

    def push(self, x: str):
        """スタックがいっぱいでない時、スタックにアイテムを一つ追加する

        Args:
            x (str): スタックに追加したいアイテム

        Raises:
            OverflowError: スタックがすでにいっぱいの場合
        """
        if self.is_full():
            raise OverflowError("オーバーフロー")

        self.top += 1
        self.stack[self.top] = x

    def pop(self) -> str:
        """スタックが空でないとき、スタックからアイテムを一つ取り出す

        Raises:
            UnderFlowException: スタックが空の場合

        Returns:
            str: スタックから取り出されたアイテム
        """
        if self.is_empty():
            raise UnderFlowException("アンダーフロー")

        self.top -= 1
        return self.stack[self.top + 1]


class OverFlowException(IndexError):
    """スタックがいっぱいのため、アイテムを追加できない時"""
    pass


class UnderFlowException(IndexError):
    """スタックが空のため、アイテムが取り出せない時"""
    pass


def main(A: str) -> str:
    """逆ポーランド記法で指定された文字列の計算結果を、スタックを用いて算出する"""
    s = stack()
    for a in A.split(" "):
        match a:
            case "+":
                y, x = s.pop(), s.pop()
                s.push(x + y)
            case  "-":
                y, x = s.pop(), s.pop()
                s.push(x - y)
            case "*":
                y, x = s.pop(), s.pop()
                s.push(x * y)
            case _:
                s.push(int(a))

    print(s.stack)
    return s.pop()


A = "1 2 + 3 4 - *"
# A = "1 2 - 3 4 * +"
# A = "10 2 - 3 4 * +"
result = main(A)
print(result)
