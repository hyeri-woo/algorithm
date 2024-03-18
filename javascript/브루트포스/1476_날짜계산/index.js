const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test4.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const [E, S, M] = input[0].split(" ").map(Number);

  let count = 1;
  while (true) {
    if (
      (count - E) % 15 === 0 &&
      (count - S) % 28 === 0 &&
      (count - M) % 19 === 0
    ) {
      break;
    }
    count++;
  }
  return count;
}

console.log(solution(input));
