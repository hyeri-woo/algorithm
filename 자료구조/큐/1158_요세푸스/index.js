const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const [N, K] = input[0].split(" ");
  const people = Array(parseInt(N))
    .fill()
    .map((_, index) => index + 1);
  const answer = [];
  while (people.length > 0) {
    for (let i = 1; i < K; i++) {
      people.push(people.shift());
    }
    answer.push(people.shift());
  }
  return "<" + answer.join(", ") + ">";
}

console.log(solution(input));
