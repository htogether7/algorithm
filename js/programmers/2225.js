let fs = require("fs");
let input = fs
  .readFileSync("case.txt")
  .toString()
  .split(" ")
  .map((x) => +x);
const n = input[0];
const k = input[1];

const board = Array.from(new Array(k), () => Array(n + 1).fill(0));
for (let i = 0; i < k; i++) {
  for (let j = 0; j < n + 1; j++) {
    if (i === 0) {
      board[i][j] = 1;
    } else {
      board[i][j] =
        board[i - 1].slice(0, j + 1).reduce((a, b) => a + b) % 1000000000;
    }
  }
}
console.log(board[k - 1][n]);
// console.log(board);
// console.log(n);
// console.log(k);
