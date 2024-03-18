const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test2.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const [n, m] = input[0].split(" ").map(Number);
  const arr = input[1].split(" ").map(Number).sort();
  const permutation = (arr, selectNum) => {
    const result = [];
    if (selectNum === 1) return arr.map((v) => [v]);
    arr.forEach((v, idx, arr) => {
      const fixer = v;
      const restArr = arr.filter((_, index) => index !== idx);
      const permutationArr = permutation(restArr, selectNum - 1);
      const combineFixer = permutationArr.map((v) => [fixer, ...v]);
      result.push(...combineFixer);
    });
    return result;
  };
  const answer = Array.from(
    new Set(permutation(arr, m).map((n) => n.join(" ")))
  );
  return answer.join("\n");
}

console.log(solution(input));
