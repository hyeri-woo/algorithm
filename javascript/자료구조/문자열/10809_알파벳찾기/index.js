const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const word = input[0];
  const answer = Array(26).fill(-1);
  for (let i = 0; i < answer.length; i++) {
    answer[i] = word.indexOf(String.fromCharCode(97 + i));
  }
  return answer.join(" ");
}

console.log(solution(input));
