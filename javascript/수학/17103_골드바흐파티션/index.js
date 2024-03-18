const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const max = Math.max(...input);
  const nums = Array(max + 1).fill(true);
  nums[0] = false;
  nums[1] = false;

  for (let i = 2; i <= max; i++) {
    if (!nums[i]) continue;
    for (let j = i * 2; j <= max; j += i) {
      nums[j] = false;
    }
  }
  const answer = [];
  for (let i = 1; i < input.length; i++) {
    const number = parseInt(input[i]);
    let sum = 0;
    for (let j = 2; j <= number / 2; j++) {
      if (nums[j] && nums[number - j]) sum++;
    }
    answer.push(sum);
  }
  return answer.join("\n");
}

console.log(solution(input));
