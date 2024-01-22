const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const [n, m] = input[0].split(" ").map((item) => parseInt(item));
  const getCount = (number, n) => {
    let result = 0;
    while (number > 0) {
      result += parseInt(number / n);
      number = parseInt(number / n);
    }
    return result;
  };
  const count2 = getCount(n, 2) - getCount(m, 2) - getCount(n - m, 2);
  const count5 = getCount(n, 5) - getCount(m, 5) - getCount(n - m, 5);
  return Math.min(count2, count5);
}

console.log(solution(input));
