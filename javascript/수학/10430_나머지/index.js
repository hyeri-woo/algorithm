const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const numbers = input[0].split(" ").map((item) => parseInt(item));
  const [a, b, c] = numbers;
  const answer = [];
  answer.push((a + b) % c);
  answer.push(((a % c) + (b % c)) % c);
  answer.push((a * b) % c);
  answer.push(((a % c) * (b % c)) % c);
  return answer.join("\n");
}

console.log(solution(input));
