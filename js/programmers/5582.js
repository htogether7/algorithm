let fs = require("fs");
let input = fs.readFileSync("case.txt").toString().split("\n");
const str1 = input[0];
const str2 = input[1];

const board = Array.from(new Array(str1.length + 1), () =>
  new Array(str2.length + 1).fill(0)
);
// board[0][0][0] = 1;
// console.log(board);
let answer = 0;
for (let i = 1; i < str1.length + 1; i++) {
  for (let j = 1; j < str2.length + 1; j++) {
    if (str1[i - 1] === str2[j - 1]) {
      board[i][j] = board[i - 1][j - 1] + 1;
      //       board[i][j][1] = 1;
      //       answer = Math.max(answer, 1);
    }
    //     if (i === str1.length - 1) {
    //       continue;
    //     }
    //     if (j === 0) {
    //       continue;
    //     }
    //     if (board[i][j - 1][0] !== 0 && str1[i + board[i][j - 1][0]] === str2[j]) {
    //       board[i][j][0] = board[i][j - 1][0] + 1;
    //       answer = Math.max(board[i][j][0], answer);
    //     }
    //     if (board[i][j - 1][1] !== 0 && str1[i + board[i][j - 1][1]] === str2[j]) {
    //       board[i][j][0] = board[i][j - 1][1] + 1;
    //       answer = Math.max(board[i][j][0], answer);
    //     }
  }
}
for (let i = 1; i < str1.length + 1; i++) {
  answer = Math.max(answer, Math.max(...board[i]));
}
// console.log(board);
console.log(answer);

// console.log(str1);
// console.log(str2);
// let result = 0;
// let i1 = 0;
// let i2 = 0;

// while (i1 < str1.length) {
//   let moveCount = 0;
//   while (i2 < str2.length) {
//     if (str1[i1] === str2[i2]) {
//       let tmp_result = 0;
//       let tmpI1 = i1;
//       while (str1[tmpI1] === str2[i2]) {
//         tmpI1++;
//         i2++;
//         tmp_result++;
//       }
//       moveCount = Math.max(moveCount, tmp_result);
//       console.log(i1, i2, tmp_result);
//       result = Math.max(result, tmp_result);
//     } else {
//       i2++;
//       console.log(i1, i2);
//     }
//     // break;
//     // i2++;
//   }
//   if (moveCount === 0) {
//     i1++;
//   } else {
//     i1 += moveCount;
//   }
//   i2 = 0;
//   //   break;
// }
// for (let i1 = 0; i1 < str1.length; i1++) {
//   for (let i2 = 0; i2 < str2.length; i2++) {
//     // console.log(i1, i2);
//     if (str1[i1] === str2[i2]) {
//       //   if (i1 < str1.length - 1 && i2 < str2.length - 1) {
//       // if (str1[i1+1] === str2[i2+1]) {
//       //     while (str1[])
//       // }
//       let tmpI1 = i1;
//       let tmpI2 = i2;
//       let tmp_result = 0;
//       while (str1[tmpI1] === str2[tmpI2]) {
//         tmp_result++;
//         tmpI1++;
//         tmpI2++;
//         if (tmpI1 === str1.length || tmpI2 === str2.length) {
//           break;
//         }
//       }
//       //   i2 = tmpI2 - 1;
//       //   console.log(tmp_result, i1, i2);
//       result = Math.max(result, tmp_result);
//     }
//     // }
//   }
// }
// console.log(result);
