let fs = require("fs");
let input = fs
  .readFileSync("case.txt")
  .toString()
  .split("\n")
  .map((x) => +x);

const n = input[0];

const nums = input.slice(1);
const originalMap = new Set();
const copyMap = new Set();
const compareMap = new Map();

for (let num of nums) {
  originalMap.add(num);
}
const m = Math.max(...originalMap);
const stack = [];
const dfs = (l) => {
  if (l == 2) {
    const [a, b] = stack;
    if (!compareMap.has(Math.abs(a - b))) {
      compareMap.set(Math.abs(a - b), Math.max(a, b));
    } else {
      compareMap.set(
        Math.abs(a - b),
        Math.max(compareMap.get(Math.abs(a - b)), Math.max(a, b))
      );
    }
    if (stack.reduce((a, b) => a + b) < m) {
      copyMap.add(stack.reduce((a, b) => a + b));
    }
    // console.log(stack);
    return;
  }
  for (let i = 0; i < n; i++) {
    stack.push(nums[i]);
    dfs(l + 1);
    stack.pop();
  }
};
// for (let i = 0; i < n; i++) {
//   dfs(l);
// }
dfs(0);
// console.log(m);
let result = 0;
for (let num of copyMap) {
  if (compareMap.has(num)) {
    result = Math.max(result, compareMap.get(num));
  }
}
// console.log(copyMap);
// console.log(compareMap);
// console.log(originalMap);
console.log(result);
