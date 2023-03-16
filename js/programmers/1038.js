const n = parseInt(require("fs").readFileSync("case.txt").toString());

const nums = [];
const result = [];
const dfs = (l, s, target) => {
  if (l === target) {
    result.push(nums.reduce((a, b) => a + b));
    return;
  }
  for (let n = s; n >= 0; n--) {
    nums.push(n * 10 ** (target - l - 1));
    dfs(l + 1, n - 1, target);
    nums.pop();
  }
};

for (let l = 1; l <= 10; l++) {
  dfs(0, 9, l);
}
result.sort((a, b) => a - b);
if (n >= result.length) {
  console.log(-1);
} else {
  console.log(result[n]);
}
