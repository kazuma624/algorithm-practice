"""
- 先頭の要素をソート済みとする
- 未ソートの部分がなくなるまで、以下の処理を繰り返す
    - 未ソート部分の先頭から要素を一つ取り出し v に記録する
    - ソート済みの部分において、 v より大きい要素を後方へ一つずつ移動する
    - 最後に開いた位置に、「取り出した要素 v」を挿入する
"""
N = 6
A = [5, 2, 4, 6, 1, 3]

print(A)
for i in range(1, N):
    v = A[i]
    j = i - 1
    while j >= 0 and A[j] > v:
        # A[j] は先頭から v = A[i] の一つ前まで
        A[j + 1] = A[j]
        j -= 1

    A[j + 1] = v
    print(' '.join(map(str, A)))

