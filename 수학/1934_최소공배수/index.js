const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const answer = [];
  const gcd = (a, b) => (a % b === 0 ? b : gcd(b, a % b));
  const lcd = (a, b) => (a * b) / gcd(a, b);
  for (let i = 1; i < input.length; i++) {
    const [a, b] = input[i].split(" ").map((item) => parseInt(item));
    answer.push(lcd(a, b));
  }
  return answer.join("\n");
}

console.log(solution(input));
