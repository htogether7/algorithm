let fs = require("fs");
let input = fs.readFileSync("case.txt").toString().split("\n");
const [n, m] = input[0].split(" ").map((x) => +x);
const map = Array.from(new Array(n + 1), () => new Array());
const check = new Array(n + 1).fill(0);
for (let i = 1; i < m + 1; i++) {
  const [a, b] = input[i].split(" ").map((x) => +x);
  //   console.log(a, b);
  check[a] = 1;
  map[b].push(a);
}
// const compareOrder = input.slice(1).map((x) => x.split(" ").map((i) => +i));
const visited = new Array(n + 1).fill(0);
// for (let [a, b] of compareOrder) {
//   check[a] = 1;
//   map[b].push(a);
// }
// console.log(map);
// console.log(check);
const result = [];
let stack = [];
const dfs = (s) => {
  stack = [s];
  const tmp_result = [];
  while (stack.length !== 0) {
    next = stack.pop();
    tmp_result.push(next);

    for (let num of map[next]) {
      if (visited[num] === 1) {
        continue;
      }
      stack.push(num);
      visited[num] = 1;
    }
  }
  //   console.log(tmp_result);
  while (tmp_result.length !== 0) {
    result.push(tmp_result.pop());
  }
};

// dfs(3);
// const dfs = (l) => {
//   if (map[l].length === 0) {
//     // console.log(stack);
//     return;
//   }
//   for (let x of map[l]) {
//     if (visited[x] === 1) {
//       continue;
//     }
//     stack.push(x);
//     visited[x] = 1;
//     dfs(x);
//     result.push(stack.pop());
//     // console.log(stack.pop());
//     // console.log(stack.pop());
//   }
// };

// console.log(result);
for (let i = 1; i < n + 1; i++) {
  if (check[i] === 0) {
    visited[i] = 1;
    dfs(i);
  }
  stack = [];
}
// console.log(check);
// console.log(map);
// console.log(visited);
console.log(result.join(" "));
// console.log(compareOrder);
// console.log(n, m);
// console.log(input);
