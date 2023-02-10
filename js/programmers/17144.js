const { lookupService } = require("dns");
let fs = require("fs");
let input = fs.readFileSync("case.txt").toString().split("\n");
const [r, c, t] = input[0].split(" ").map((x) => +x);
const board = Array.from(new Array(r), (_, i) =>
  input[i + 1]
    .slice()
    .split(" ")
    .map((x) => +x)
);

let upperClean = 0;
let lowerClean = 0;
for (let row = 0; row < r; row++) {
  if (board[row][0] === -1) {
    upperClean = row;
    lowerClean = row + 1;
    break;
  }
}

const dy = [1, -1, 0, 0];
const dx = [0, 0, 1, -1];

const move = (board) => {
  const check = Array.from(new Array(r), () => new Array(c).fill(0));
  for (let row = 0; row < r; row++) {
    for (let col = 0; col < c; col++) {
      const moveAmount = Math.floor(board[row][col] / 5);
      if (moveAmount >= 1) {
        let moveCount = 0;
        for (let i = 0; i < 4; i++) {
          const next_y = row + dy[i];
          const next_x = col + dx[i];
          if (next_y < 0 || next_y >= r || next_x < 0 || next_x >= c) {
            continue;
          }
          if (board[next_y][next_x] === -1) {
            continue;
          }
          check[next_y][next_x] += moveAmount;
          moveCount++;
        }
        check[row][col] -= moveAmount * moveCount;
        // console.log(board[row][col]);
      }
    }
  }
  //   console.log("check");
  //   console.log(check);
  let checkSum = 0;
  for (let row = 0; row < r; row++) {
    for (let col = 0; col < c; col++) {
      checkSum += check[row][col];
    }
  }
  //   console.log(checkSum);
  for (let row = 0; row < r; row++) {
    for (let col = 0; col < c; col++) {
      board[row][col] += check[row][col];
    }
  }
  //   console.log("board");
  //   console.log(board);
  //   console.log(check);
  //   console.log(check);
};

const upRotate = (board, upperClean) => {
  const list = [0];
  for (let col = 1; col < c; col++) {
    list.push(board[upperClean][col]);
  }
  for (let row = upperClean - 1; row > 0; row--) {
    list.push(board[row][c - 1]);
  }

  for (let col = c - 1; col >= 0; col--) {
    list.push(board[0][col]);
  }
  for (let row = 1; row < upperClean; row++) {
    list.push(board[row][0]);
  }
  let index = 0;
  for (let col = 1; col < c; col++) {
    board[upperClean][col] = list[index];
    index++;
  }
  for (let row = upperClean - 1; row > 0; row--) {
    board[row][c - 1] = list[index];
    index++;
  }

  for (let col = c - 1; col >= 0; col--) {
    board[0][col] = list[index];
    index++;
  }
  for (let row = 1; row < upperClean; row++) {
    board[row][0] = list[index];
    index++;
  }
};

const downRotate = (board, lowerClean) => {
  const list = [0];
  for (let col = 1; col < c; col++) {
    list.push(board[lowerClean][col]);
  }
  for (let row = lowerClean + 1; row < r - 1; row++) {
    list.push(board[row][c - 1]);
  }

  for (let col = c - 1; col > 0; col--) {
    list.push(board[r - 1][col]);
  }
  for (let row = r - 1; row > lowerClean; row--) {
    list.push(board[row][0]);
  }
  //   console.log(list);
  let index = 0;
  for (let col = 1; col < c; col++) {
    board[lowerClean][col] = list[index];
    index++;
  }
  for (let row = lowerClean + 1; row < r - 1; row++) {
    board[row][c - 1] = list[index];
    index++;
  }

  for (let col = c - 1; col > 0; col--) {
    board[r - 1][col] = list[index];
    index++;
  }
  for (let row = r - 1; row > lowerClean; row--) {
    board[row][0] = list[index];
    index++;
  }
};

const rotate = (board, upperClean, lowerClean) => {
  upRotate(board, upperClean);
  downRotate(board, lowerClean);
};

for (let time = 0; time < t; time++) {
  move(board);
  //   console.log(board);
  rotate(board, upperClean, lowerClean);
  //   console.log(board);
}

let answer = 0;
for (let row = 0; row < r; row++) {
  for (let col = 0; col < c; col++) {
    if (board[row][col] === -1) {
      continue;
    }
    answer += board[row][col];
  }
  //   answer += board[row].reduce((a, b) => a + b);
}
console.log(answer);
// console.log(board);
