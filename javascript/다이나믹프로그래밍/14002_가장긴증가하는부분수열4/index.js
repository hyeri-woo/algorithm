const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const numbers = input[1].split(" ").map((n) => parseInt(n));
  const dp = Array(numbers.length).fill(1);
  const seq = [];
  for (let i = 0; i < numbers.length; i++) {
    let max = 0;
    let maxIndex = -1;
    for (let j = 0; j < i; j++) {
      if (numbers[j] < numbers[i] && dp[j] > max) {
        max = dp[j];
        maxIndex = j;
      }
    }
    dp[i] = max + 1;
    seq[i] = maxIndex !== -1 ? seq[maxIndex].concat(numbers[i]) : [numbers[i]];
  }
  const maxLen = Math.max(...dp);
  const answer = [
    maxLen,
    seq.filter((item) => item.length === maxLen)[0].join(" "),
  ];
  return answer.join("\n");
}

console.log(solution(input));
