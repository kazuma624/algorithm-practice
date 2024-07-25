"""
名前 name_i, 処理時間 time_i を持つn個のプロセスが直列に並んでいる
書くプロセスは最大 q [ms]だけ処理が実行される。
q [ms] で処理が終わらなかった場合、そのプロセスは列の最後尾に移動する
"""

"""
入力
n q
name_1 time_1
name_2 time_2
...
name_n time_n

"""

"""
出力
各プロセスの名前と終了時刻をスペース区切り
"""

"""
入力例
5 100
p1 150
p2 80
p3 200
p4 350
p5 20
"""

"""
出力例
p2 180
p5 400
p1 450
p3 550
p4 800
"""

from dataclasses import dataclass


LEN = 1_000_005


@dataclass
class P:
    name: str = ""
    t: int = 0

    def __repr__(self) -> str:
        return f"name: {self.name}, t: {self.t}"


Q: list[P] = [P for _ in range(LEN)]


def enqueue(x: P):
    """キューに1件追加する

    Args:
        x (P): キューに追加する要素
    """
    global tail
    Q[tail] = x
    tail = (tail + 1) % LEN


def dequeue() -> P:
    """キューから1件取り出す(FIFO)

    Returns:
        P: キューの要素
    """
    global head
    x = Q[head]
    head = (head + 1) % LEN
    return x


def check(Q: list[P]):
    """キューの中身を出力する

    Args:
        Q (list[P]): キュー
    """
    global head, tail
    indices = []
    ts = []
    names = []
    for i, q in enumerate(Q):
        if i > tail:
            break

        indices.append(f"{i:^5}")
        ts.append(f"{q.t:^5}")
        names.append(f"{q.name:^5}")

    print("|".join(indices))
    print("|".join(names))
    print("|".join(ts))
    print(f"head: {head}")
    print(f"tail: {tail}")


if __name__ == "__main__":
    elaps = 0
    args = input("キューの個数 最大プロセス時間")
    arg_list = args.split(" ")
    n = int(arg_list[0])
    q = int(arg_list[1])
    # 全てのプロセスをキューに順番に追加する
    for i in range(int(n)):
        args = input("キューの名前 処理時間\n")
        arg_list = args.split(" ")
        Q[i+1] = P(name=arg_list[0], t=int(arg_list[1]))

    global head
    head = 1
    global tail
    tail = n + 1

    # シミュレーション
    while head != tail:
        # check(Q)
        u = dequeue()
        # q または u.t の時間だけ処理を行う（短い方）
        c = min(q, u.t)
        # 残りの必要時間を計算
        u.t -= c
        # 処理が完了していなければキューに追加
        elaps += c
        if u.t > 0:
            enqueue(u)
        else:
            print(f"{u.name} {elaps}")
