let fs = require("fs");
let input = fs.readFileSync("case.txt").toString().split("\n");
const n = parseInt(input[0]);
const m = parseInt(input[1]);
const parents = new Array(n + 1).fill(0);
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
  return findParent(parents[s], parents);
};

for (let i = 0; i < path.length; i++) {
  const [c, a, b] = path[i];
  if (a === b) {
    continue;
  }
  const parentA = findParent(a, parents);
  const parentB = findParent(b, parents);
  if (parents[a] === 0 && parents[b] === 0) {
    answer += c;
    parents[a] = Math.min(a, b);
    parents[b] = Math.min(a, b);
  } else if (parents[a] === 0) {
    answer += c;
    // const parentB = findParent(b);
    if (a < parentB) {
      parents[a] = a;
      parents[parentB] = a;
    } else {
      parents[a] = parentB;
    }
    // parents[a] = b;
  } else if (parents[b] === 0) {
    answer += c;

    if (b < parentA) {
      parents[parentA] = b;
      parents[b] = b;
    } else {
      parents[b] = parentA;
    }
  } else {
    // const parentA = findParent(a, parents);

    // console.log(a, parentA);
    // console.log(b, parentB);
    if (parentA === parentB) {
      continue;
    } else {
      answer += c;
      if (parentA < parentB) {
        parents[b] = parentA;
      } else {
        parents[a] = parentB;
      }
      //   parent = Math.min(a, b);
      //   parents[a] = parent;
      //   parents[b] = parent;
    }
  }
  selected.push(path[i]);
}
// console.log(selected);
// console.log(counts);
// console.log(n);
// console.log(parents);
console.log(answer);
