const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const len = parseInt(input[0]);
  const lis = Array(len).fill(1);
  const lds = Array(len).fill(1);
  const numbers = input[1].split(" ").map((n) => parseInt(n));
  const reverse = [...numbers].reverse();
  for (let i = 1; i < numbers.length; i++) {
    for (let j = 0; j < i; j++) {
      if (numbers[i] > numbers[j]) {
        lis[i] = Math.max(lis[i], lis[j] + 1);
      }
      if (reverse[i] > reverse[j]) {
        lds[i] = Math.max(lds[i], lds[j] + 1);
      }
    }
  }

  const answers = Array(len).fill(1);
  lds.reverse();
  for (let i = 0; i < answers.length; i++) {
    answers[i] = lis[i] + lds[i] - 1;
  }
  return Math.max(...answers);
}

console.log(solution(input));
