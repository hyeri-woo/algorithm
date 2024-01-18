const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const word = input[0];
  const answer = [];
  for (let i = 0; i < word.length; i++) {
    answer.push(word.slice(i));
  }
  return answer.sort().join("\n");
}

console.log(solution(input));
