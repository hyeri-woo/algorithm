const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test4.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const dp = input.slice(1).map((item) => {
    const [R, G, B] = item.split(" ").map((n) => parseInt(n));
    return { R, G, B };
  });
  for (let i = 1; i < dp.length; i++) {
    dp[i].R += Math.min(dp[i - 1].G, dp[i - 1].B);
    dp[i].G += Math.min(dp[i - 1].R, dp[i - 1].B);
    dp[i].B += Math.min(dp[i - 1].R, dp[i - 1].G);
  }
  const { R, G, B } = dp[dp.length - 1];
  return Math.min(R, G, B);
}

console.log(solution(input));
