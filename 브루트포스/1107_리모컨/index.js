const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test7.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const channel = parseInt(input[0]);
  if (channel === 100) return 0;
  const brokenButtons = input?.[2]?.split(" ");
  let answer = Math.abs(100 - channel);
  for (let i = 0; i < 1000000; i++) {
    const str = i.toString();
    let isValid = true;
    for (let j = 0; j < str.length; j++) {
      if (brokenButtons?.includes(str[j])) {
        isValid = false;
        break;
      }
    }
    if (isValid) {
      answer = Math.min(answer, Math.abs(i - channel) + str.length);
    }
  }
  return answer;
}

console.log(solution(input));
