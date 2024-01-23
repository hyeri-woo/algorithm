const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const number = input[0].split("");
  const answer = [];
  while (number.length) {
    let temp = 0;
    for (let i = 0; i < 3; i++) {
      let eachChar = parseInt(number.pop());
      if (!eachChar) continue;
      temp += 1 << i;
    }
    answer.push(temp);
  }
  return answer.reverse().join("");
}

console.log(solution(input));
