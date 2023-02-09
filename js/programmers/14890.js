let fs = require("fs");
let input = fs.readFileSync("case.txt").toString().split("\n");
const [n, l] = input[0].split(" ").map((x) => +x);
const board = Array.from(new Array(n), (_, i) =>
  input[i + 1].split(" ").map((x) => +x)
);
let answer = 0;

const moveAndCheck = (path) => {
  let height = path[0];
  let index = 1;
  const check = new Array(path.length).fill(0);
  while (index < path.length) {
    if (Math.abs(height - path[index]) > 1) {
      return false;
    } else if (height - path[index] === 1) {
      for (let i = 0; i < l; i++) {
        check[index + i] = 1;
        if (path[index] !== path[index + i]) {
          return false;
        }
      }
      height = path[index + l - 1];
      index += l;
    } else if (height - path[index] === -1) {
      for (let i = 1; i < l + 1; i++) {
        if (check[index - i] === 1) {
          return false;
        }
        if (height !== path[index - i]) {
          return false;
        }
      }
      height = path[index];
      index++;
    } else {
      index++;
    }
  }
  return true;
};

for (let row = 0; row < n; row++) {
  const now_path = board[row];
  const now_path_2 = [];
  for (let col = 0; col < n; col++) {
    now_path_2.push(board[col][row]);
  }
  //   const reverse_path = now_path.slice().reverse();
  //   console.log(row, moveAndCheck(now_path));
  if (moveAndCheck(now_path)) {
    answer++;
  }
  //   console.log(now_path_2);
  if (moveAndCheck(now_path_2)) {
    answer++;
  }
  //   console.log(row, "reverse", moveAndCheck(reverse_path));
}
console.log(answer);
// console.log(board);
