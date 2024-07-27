export const MAX = 100;

class P {
  pname: string = "";
  t: number = 0;
}

class Queue {
  head = 1;
  tail = 1;
  Q: (P | null)[] = [null].concat(Array(MAX));

  isEmpty(): boolean {
    return this.head === this.tail;
  }

  isFull(): boolean {
    return this.head === (this.tail + 1) % MAX;
  }

  enqueue(x: P) {
    if (this.isFull()) {
      throw new Error("オーバーフロー");
    }

    this.Q[this.tail] = x;
    if (this.tail + 1 === MAX) {
      this.tail = 0;
    } else {
      this.tail += 1;
    }
  }

  dequeue(): P | null {
    if (this.isEmpty()) {
      throw new Error("アンダーフロー");
    }

    const x = this.Q[this.head];
    if (this.head + 1 === MAX) {
      this.head = 0;
    } else {
      this.head += 1;
    }

    return x;
  }
}


(() => {
  let elaps = 0;
  const queueCount = 5;
  const maxProcessTime = 100;
  const q = new Queue();
  // コマンドラインからの入力がわからないので一旦ベタ書き
  const qs = [
    { name: "q1", t: 150 },
    { name: "q2", t: 80 },
    { name: "q3", t: 200 },
    { name: "q4", t: 350 },
    { name: "q5", t: 20 },
  ];
  // 全てのプロセスをキューに追加する
  for (let i = 0; i < queueCount; i++) {
    const p = new P();
    p.pname = qs[i].name;
    p.t = qs[i].t;
    q.enqueue(p);
  }

  // シミュレーション
  while (q.head !== q.tail) {
    const u = q.dequeue();
    if (u !== null) {
      // q または u.t の時間だけ処理を行う
      const c = Math.min(maxProcessTime, u.t);
      // 残りの必要時間を計算
      u.t -= c
      // 処理が完了していなければキューに追加
      elaps += c;
      if (u.t > 0) {
        q.enqueue(u);
      } else {
        console.log(`${u.pname} ${elaps}`);
      }
    } else {
      console.log("キューの要素がnullです")
    }
  }
})();
