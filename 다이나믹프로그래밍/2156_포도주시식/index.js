const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const nums = input.slice(1).map((n) => parseInt(n));
  if (nums.length === 1) return nums[0];
  if (nums.length === 2) return nums[0] + nums[1];
  const dp = Array(nums.length).fill(0);
  dp[0] = nums[0];
  dp[1] = nums[0] + nums[1];
  dp[2] = Math.max(dp[1], dp[0] + nums[2], nums[2] + nums[1]);
  for (let i = 3; i < dp.length; i++) {
    dp[i] = Math.max(
      dp[i - 3] + nums[i] + nums[i - 1],
      dp[i - 2] + nums[i],
      dp[i - 1]
    );
  }
  return dp[dp.length - 1];
}

console.log(solution(input));
