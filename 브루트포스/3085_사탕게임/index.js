const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test3.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const candy = input.slice(1).map((n) => n.split(""));
  const checkMaxCandies = (candy) => {
    let max = Number.NEGATIVE_INFINITY;
    for (let i = 0; i < candy.length; i++) {
      const dpRow = Array(candy.length).fill(1);
      const dpCol = Array(candy.length).fill(1);
      for (let j = 1; j < candy.length; j++) {
        if (candy[i][j] === candy[i][j - 1]) {
          dpRow[j] = dpRow[j - 1] + 1;
        }
        if (candy[j][i] === candy[j - 1][i]) {
          dpCol[j] = dpCol[j - 1] + 1;
        }
      }
      const partialMax = Math.max(...dpRow, ...dpCol);
      if (max < partialMax) {
        max = partialMax;
      }
    }
    return max;
  };

  const swap = (candy, i1, j1, i2, j2) => {
    const temp = candy[i1][j1];
    candy[i1][j1] = candy[i2][j2];
    candy[i2][j2] = temp;
  };

  let max = Number.NEGATIVE_INFINITY;
  let partialMax = Number.NEGATIVE_INFINITY;
  for (let i = 0; i < candy.length; i++) {
    for (let j = 0; j < candy.length; j++) {
      // row
      if (j < candy.length - 1) {
        swap(candy, i, j, i, j + 1);
        partialMax = checkMaxCandies(candy);
        swap(candy, i, j + 1, i, j);
        if (partialMax > max) {
          max = partialMax;
        }
      }

      // column
      if (i < candy.length - 1) {
        swap(candy, i, j, i + 1, j);
        partialMax = checkMaxCandies(candy);
        swap(candy, i + 1, j, i, j);
        if (partialMax > max) {
          max = partialMax;
        }
      }
    }
  }

  return max;
}

console.log(solution(input));
