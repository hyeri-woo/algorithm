const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const answer = [];
  const gcd = (a, b) => (a % b === 0 ? b : gcd(b, a % b));
  for (let index = 1; index < input.length; index++) {
    const numbers = input[index].split(" ").map((n) => parseInt(n));
    let sum = 0;
    for (let i = 0; i < numbers.length - 1; i++) {
      for (let j = i + 1; j < numbers.length; j++) {
        sum += gcd(numbers[i], numbers[j]);
      }
    }
    answer.push(sum);
  }

  return answer.join("\n");
}

console.log(solution(input));
