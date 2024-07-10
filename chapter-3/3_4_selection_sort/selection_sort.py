def selection_sort(A, N):
    cnt = 0
    for i in range(N): # i = 0, 1, ..., N - 1
        minj = i # 未ソートの部分列の先頭インデックス
        for j in range(i, N): # i より後ろ全て
            # 未ソートの部分列の先頭より小さい要素がある場合
            if A[j] < A[minj]:
                # 未ソートの部分列の先頭インデックスを、その小さい要素のインデックスに差し替える
                minj = j

        # 特定の i に対する minj の値が確定してから入れ替え
        A[i], A[minj] = A[minj], A[i]
        cnt += 1

    print(' '.join(map(str, A)))
    print(cnt)


N = 6
A = [5, 6, 4, 2, 1, 3]
selection_sort(A, N)
