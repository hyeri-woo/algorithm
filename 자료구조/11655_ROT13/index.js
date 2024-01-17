const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test2.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const sentence = input[0];
  let answer = "";
  for (const s of sentence) {
    if (!/[a-zA-z]/g.test(s)) {
      answer += s;
      continue;
    }
    let index = s.charCodeAt() + 13;
    if (s === s.toLowerCase() && index > 122) index -= 26;
    else if (s === s.toUpperCase() && index > 90) index -= 26;
    answer += String.fromCharCode(index);
  }
  return answer;
}

console.log(solution(input));
