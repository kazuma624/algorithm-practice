from dataclasses import dataclass


MAX = 100
MAX = 10

@dataclass
class P:
    name: str = ""
    t: int = 0


class Queue:
    def __init__(self) -> None:
        """初期化処理"""
        self.head = 1
        self.tail = 1
        self.Q = [None] * MAX

    def is_empty(self) -> bool:
        """head と tail のポインタが一致しているとき、キューは空"""
        return self.head == self.tail

    def is_full(self) -> bool:
        """
        head と tail の次のポインタと重なるとき、キューは満杯
        リングバッファを想定
        """
        return self.head == (self.tail + 1) % MAX

    def enqueue(self, x: P) -> None:
        """キューの末尾に要素を一つ追加する

        Args:
            x (P): _description_

        Raises:
            OverFlowException: キューがすでに満杯であるとき
        """
        if self.is_full():
            raise OverFlowException("オーバーフロー")

        # 末尾に要素を追加
        self.Q[self.tail] = x
        # tail のポインタが上限（一周の長さ）を超えたら 0 に戻す
        if self.tail + 1 == MAX:
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self) -> P:
        """キューの先頭から要素を一つ取り出す

        Raises:
            UnderFlowException: キューがすでに空であるとき

        Returns:
            int: _description_
        """
        if self.is_empty():
            raise UnderFlowException("アンダーフロー")

        # 先頭の要素を取り出す
        x = self.Q[self.head]
        # tail のポインタが上限（一周の長さ）を超えたら 0 に戻す
        if self.head + 1 == MAX:
            self.head = 0
        else:
            self.head += 1

        return x


class OverFlowException(IndexError):
    """キューがいっぱいのため、アイテムを追加できない時"""
    pass


class UnderFlowException(IndexError):
    """キューが空のため、アイテムが取り出せない時"""
    pass


if __name__ == "__main__":
    elaps = 0
    args = input("キューの個数 最大プロセス時間")
    arg_list = args.split(" ")
    queue_count = int(arg_list[0])
    max_process_time = int(arg_list[1])
    q = Queue()
    # 全てのプロセスをキューに順番に追加する
    for i in range(queue_count):
        args = input("キューの名前 処理時間\n")
        arg_list = args.split(" ")
        q.enqueue(P(name=arg_list[0], t=int(arg_list[1])))

    # シミュレーション
    while q.head != q.tail:
        # check(Q)
        u = q.dequeue()
        # q または u.t の時間だけ処理を行う（短い方）
        c = min(max_process_time, u.t)
        # 残りの必要時間を計算
        u.t -= c
        # 処理が完了していなければキューに追加
        elaps += c
        if u.t > 0:
            q.enqueue(u)
        else:
            print(f"{u.name} {elaps}")
