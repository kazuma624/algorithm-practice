def bubble_sort(A, N):
    # 昇順にソート
    flag = 1 # 逆の隣接要素が存在する
    i = 0 # 未ソート部分裂の先頭インデックス
    cnt = 0 # 入れ替えた回数
    while flag:
        # for 文で何も起きなければ flag はゼロのままとなり while ループを抜ける
        # flag が 0 のままになるのは入れ替えが生じなかった時、つまりソートが完了したとき
        flag = 0
        # 配列を後ろから見ていく
        for j in range(N - 1, i, -1):
            # 一つ前の要素の方が大きい場合、交換する
            if A[j] < A[j - 1]:
                A[j - 1], A[j] = A[j], A[j - 1]
                flag = 1 # 入れ替えたのでフラグを1に
                cnt += 1 # 入れ替えたのでカウントアップ
        i += 1

    print(' '.join(map(str, A)))
    print(cnt)


N = 5
A = [5, 3, 2, 4, 1]
bubble_sort(A, N)
