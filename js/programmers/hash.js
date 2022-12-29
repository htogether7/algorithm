function solution(data, col, row_begin, row_end) {
  var answer = 0;
  data.sort((a, b) => {
    if (a[col - 1] - b[col - 1] < 0) {
      return -1;
    } else if (a[col - 1] - b[col - 1] > 0) {
      return 1;
    } else {
      if (a[0] - b[0] < 0) {
        return 1;
      } else if (a[0] - b[0] > 0) {
        return -1;
      } else {
        return 0;
      }
    }
  });

  const newArr = data.map((arr, i) => {
    return arr.map((x) => x % (i + 1)).reduce((a, b) => a + b);
  });

  for (let i = row_begin - 1; i <= row_end - 1; i++) {
    if (i == row_begin - 1) answer = newArr[i];
    else {
      answer = answer ^ newArr[i];
    }
  }
  return answer;
}
