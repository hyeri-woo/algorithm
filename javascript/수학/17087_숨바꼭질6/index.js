const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test2.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const myPos = parseInt(input[0].split(" ")[1]);
  const otherPos = input[1].split(" ").map((n) => parseInt(n));
  const gcd = (a, b) => (a % b === 0 ? b : gcd(b, a % b));
  let answer = Math.abs(otherPos[0] - myPos);
  for (let i = 1; i < otherPos.length; i++) {
    answer = gcd(answer, Math.abs(otherPos[i] - myPos));
  }
  return answer;
}

console.log(solution(input));
