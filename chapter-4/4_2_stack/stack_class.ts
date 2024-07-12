export const MAX = 100;

class Stack {
  private top = 0;
  private max = MAX;
  private stack: (number | null)[] = [null].concat(Array(this.max - 1));

  isEmpty(): boolean {
    return this.top === 0;
  }

  isFull(): boolean {
    return this.top >= this.max - 1;
  }

  push(x: number) {
    if (this.isFull()) {
      throw new Error("オーバーフロー");
    }

    this.top += 1;
    this.stack[this.top] = x;
  }

  pop(): number | null {
    if (this.isEmpty()) {
      throw new Error("アンダーフロー");
    }

    this.top -= 1;
    return this.stack[this.top + 1];
  }
}

function main(A: string): number | null {
  let s = new Stack();
  let x: number | null;
  let y: number | null;
  for (const a of A.split(" ")) {
    switch (a) {
      case "+":
        y = s.pop();
        x = s.pop();
        if (typeof x === "number" && typeof y === "number") {
          s.push(x + y);
        }
        break;
      case "-":
        y = s.pop();
        x = s.pop();
        if (typeof x === "number" && typeof y === "number") {
          s.push(x - y);
        }
        break;
      case "*":
        y = s.pop();
        x = s.pop();
        if (typeof x === "number" && typeof y === "number") {
          s.push(x * y);
        }
        break;
      default:
        s.push(Number(a));
        break;
    }
  }
  return s.pop();
}

let A = "1 2 + 3 4 - *";
let result = main(A);
console.log(result);
