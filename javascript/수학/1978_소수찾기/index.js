const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const numbers = input[1].split(" ").map((item) => parseInt(item));
  const isPrime = (num) => {
    if (num === 1) return false;
    for (let i = 2; i <= parseInt(Math.sqrt(num)); i++) {
      if (num % i === 0) return false;
    }
    return true;
  };
  let answer = 0;
  for (const num of numbers) {
    if (isPrime(num)) answer++;
  }
  return answer;
}

console.log(solution(input));
