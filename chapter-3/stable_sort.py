"""
5
H4 C9 S4 D2 C3
"""

"""
D2 C3 H4 S4 C9
Sable
D2 C3 S4 H4 C9
Not stable
"""

class Card:
    def __init__(self, name: str):
        self.suit = name[0]
        self.number = int(name[1])

    def __repr__(self) -> str:
        return f"{self.suit}{self.number}"


def bubble_sort(A: list[Card], N: int):
    for i in range(N):
        for j in range(N - 1, i + 1):
            if A[j].number < A[j - 1].number:
                A[j], A[j - 1] = A[j], A[j - 1]

    return A


def selection_sort(A: list[Card], N: int):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if A[j].number < A[minj].number:
                minj = j

        A[i], A[minj] = A[minj], A[i]

    return A


def is_stable(A: list[Card], B: list[Card], N: int) -> bool:
    for i in range(N):
        if A[i].suit != B[i].suit:
            return False

    return True


def _print(A: list[Card]) -> str:
    print(" ".join(map(str, A)))


def main(A: list[Card], N: int):
    bubble = bubble_sort(A, N)
    _print(bubble)
    selection = selection_sort(A, N)
    _print(selection)

    if is_stable(bubble, selection, N):
        print("Stable")
    else:
        print("Not stable")


if __name__ == '__main__':
    # N = input('要素数: ')
    # A = input('スペース区切りの配列: ')

    N = 5
    cards = ["H4", "C9", "S4", "D2", "C3"]

    A = [Card(i) for i in cards]
    main(A, N)
