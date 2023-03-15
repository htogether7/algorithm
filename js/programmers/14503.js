const input = require("fs")
  .readFileSync("case.txt")
  .toString()
  .trim()
  .split("\n");
// console.log(input);
const [n, m] = input[0].split(" ").map((x) => +x);
let [r, c, d] = input[1].split(" ").map((x) => +x);

const board = input.slice(2).map((str) => str.split(" ").map((x) => +x));
const ds = {
  0: [-1, 0],
  1: [0, 1],
  2: [1, 0],
  3: [0, -1],
};
let answer = 0;

const find_unclean = (y, x) => {
  const pos = [];
  for (let i = 0; i < 4; i++) {
    const [dy, dx] = ds[i];
    const next_y = y + dy;
    const next_x = x + dx;
    if (next_y < 0 || next_y >= n || next_x < 0 || next_x >= m) {
      continue;
    }
    if (board[next_y][next_x] === 0) {
      pos.push((next_y, next_x));
    }
  }
  return pos;
};

while (true) {
  if (board[r][c] === 0) {
    answer += 1;
    board[r][c] = 2;
  } else {
    const unclean_pos = find_unclean(r, c);
    if (unclean_pos.length !== 0) {
      d = d === 0 ? 3 : (d - 1) % 4;
      const [next_r, next_c] = [r + ds[d][0], c + ds[d][1]];

      if (board[next_r][next_c] === 0) {
        r = next_r;
        c = next_c;
      }
    } else {
      const [back_r, back_c] = [r + ds[d][0] * -1, c + ds[d][1] * -1];
      if (back_r < 0 || back_r >= n || back_c < 0 || back_c >= m) {
        break;
      }
      if (board[back_r][back_c] === 1) {
        break;
      }
      r = back_r;
      c = back_c;
    }
  }
}
console.log(answer);
