const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const answer = [];
  const regExps = [/[a-z]/g, /[A-Z]/g, /[0-9]/g, /[ ]/g];
  for (let i = 0; i < input.length; i++) {
    const single = [];
    regExps.forEach((exp) => {
      single.push(input[i].match(exp)?.length || 0);
    });
    answer.push(single.join(" "));
  }
  return answer.join("\n");
}

console.log(solution(input));
