const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const primeNums = [];
  const nums = Array(1_000_000 + 1).fill(true);
  nums[0] = false;
  nums[1] = false;

  for (let i = 2; i <= Math.sqrt(1_000_000); i++) {
    if (!nums[i]) {
      continue;
    }
    primeNums.push(i);
    for (let j = i * 2; j <= 1_000_000; j += i) {
      nums[j] = false;
    }
  }
  return input
    .slice(0, -1)
    .map((num) => {
      const low = primeNums.find((primeNum) => nums[num - primeNum]);
      if (low) {
        const high = num - low;
        return `${num} = ${low} + ${high}`;
      }
      return "Goldbach's conjecture is wrong.";
    })
    .join("\n");
}

console.log(solution(input));
