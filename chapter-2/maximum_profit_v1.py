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

minv = R[0]
maxv = -200_000_000
for i in range(1, n):
    maxv = max(maxv, R[i] - minv)
    minv = min(minv, R[i])

print(maxv)
