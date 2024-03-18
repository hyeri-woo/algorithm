const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const numbers = input[0].split(" ").map((item) => parseInt(item));
  const [a, b] = numbers;
  const gcd = (a, b) => (a % b === 0 ? b : gcd(b, a % b));
  const lcm = (a, b) => (a * b) / gcd(a, b);
  return gcd(a, b) + "\n" + lcm(a, b);
}

console.log(solution(input));
