let fs = require("fs");
let input = fs.readFileSync("case.txt").toString().split("\n");
const n = parseInt(input[0]);
const m = parseInt(input[1]);
const parents = Array.from({ length: n + 1 }, (_, i) => i);
const path = [];
for (let i = 2; i < input.length; i++) {
  const [a, b, c] = input[i].split(" ").map((x) => +x);
  path.push([c, a, b]);
}

path.sort((a, b) => a[0] - b[0]);
let answer = 0;

const selected = [];

const findParent = (s, parents) => {
  if (s === parents[s]) {
    return s;
  }
  parents[s] = findParent(parents[s], parents);
  return parents[s];
};

const paintParent = (s, parents) => {
  const arr = [];
  return arr;
};

for (let i = 0; i < path.length; i++) {
  const [c, a, b] = path[i];
  //   if (a === b) {
  //     continue;
  //   }
  const parentA = findParent(a, parents);
  const parentB = findParent(b, parents);

  // const parentA = findParent(a, parents);

  // console.log(a, parentA);
  // console.log(b, parentB);
  if (parentA === parentB) {
    continue;
  } else {
    answer += c;
    if (parentA < parentB) {
      parents[parentB] = parentA;
    } else {
      parents[parentA] = parentB;
    }
    //   parent = Math.min(a, b);
    //   parents[a] = parent;
    //   parents[b] = parent;
  }

  selected.push(path[i]);
  //   console.log(parents);
}
// console.log(selected);
// console.log(counts);
// console.log(n);
// console.log(parents);
console.log(answer);
