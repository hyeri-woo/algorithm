const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const [baseA, baseB] = input[0].split(" ").map((n) => parseInt(n));
  const nums = input[2]
    .split(" ")
    .map((n) => parseInt(n))
    .reverse();
  const answer = [];
  let decimal = 0;
  for (let i = 0; i < nums.length; i++) {
    decimal += nums[i] * Math.pow(baseA, i);
  }
  if (decimal === 0) return 0;
  while (decimal > 0) {
    answer.unshift(decimal % baseB);
    decimal = Math.floor(decimal / baseB);
  }
  return answer.join(" ");
}

console.log(solution(input));
