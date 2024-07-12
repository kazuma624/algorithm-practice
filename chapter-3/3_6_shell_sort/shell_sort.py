"""
挿入ソートを応用する
"""


def insertion_sort(A, n, g, cnt):
    """挿入ソート
    一定の間隔gだけ離れた要素のみを対象とする

    Args:
        A (list[int]): _description_
        n (int): _description_
        g (int): _description_
    """
    # 指定された n の数ぶんループ
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j + g] = A[j]
            j -= g
            cnt += 1

        A[j + g] = v
        print(A)

    return A, cnt


def shell_sort(A, n):
    """

    Args:
        A (_type_): _description_
        n (_type_): _description_
    """
    cnt = 0
    G = [4, 3, 1]
    m = len(G)
    for i in range(m):
        A, cnt = insertion_sort(A, n, G[i], cnt)
        print("-"*32)

    print(m)
    print(G)
    print("総入れ替え回数", cnt)
    print("\n".join(map(str, A)))


A = [5, 1, 4, 3, 2]
A = [4, 8, 9, 1, 10, 6, 2, 5, 3, 7]
n = len(A)

shell_sort(A, n)
