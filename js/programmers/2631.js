let fs = require("fs");
let input = fs.readFileSync("case.txt").toString().split("\n");

let input_arr = input.map((x) => +x);
const n = input_arr[0];
const childOrder = input_arr.slice(1);

var board = Array.from(new Array(n + 1), () => Array(n + 1).fill(0));
// board[0][0].push(1);
for (let start = 0; start < n; start++) {
  for (let row = 0; row < n; row++) {
    if (row === 0) {
      board[row + 1][start + 1] = childOrder[start];
    } else {
      if (board[row][start] === 0) {
        continue;
      }
      if (childOrder[start] > board[row][start]) {
        board[row + 1][start + 1] = childOrder[start];
        if (board[row][start + 1] !== 0) {
          board[row][start + 1] = Math.min(
            childOrder[start],
            board[row][start],
            board[row][start + 1]
          );
        } else {
          board[row][start + 1] = Math.min(
            childOrder[start],
            board[row][start]
          );
        }
      } else {
        if (board[row][start] === 0) {
          continue;
        }
        if (board[row][start + 1] == 0) {
          board[row][start + 1] = board[row][start];
        } else {
          board[row][start + 1] = Math.min(
            board[row][start + 1],
            childOrder[start]
          );
        }
      }
      // board[row][start + 1] ;
      //   } else {
      //     board[row][start + 1] = board[row][start];
      //   }
    }
  }
  //   if (start == 4) {
  //     break;
  //   }
}

const find = (board) => {
  for (let row = n; row >= 0; row--) {
    for (let col = 0; col < n + 1; col++) {
      if (board[row][col] !== 0) {
        return row;
      }
    }
  }
};
// console.log(board);
console.log(n - find(board));
// find(board);
// console.log(board);
// console.log(n);
// console.log(childOrder);
// console.log(num);
