"""
R_j - R_i (j < i) の最大値を求める

最初の行に整数 n が与えられる。
続く n 行に整数 R_t (t = 0,1,...,n-1) が順番に与えられる

2 <= n <= 200,000
1 <= R_t <= 10^9
"""

args = list(map(int, iter(input, '')))
n = args[0]
R = args[1:]

# O(n^2) の計算量バージョン
maxv = R[1] - R[0]
for j in range(1, n):
    for i in range(j):
        maxv = max(maxv, R[j] - R[i])

print(maxv)
