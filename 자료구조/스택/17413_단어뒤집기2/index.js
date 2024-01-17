const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test2.txt").toString().split("\n");

// 풀이
function solution(input) {
  // const sentence = input[0];
  // const answer = [];
  // const word = [];
  // for (let i = 0; i < sentence.length; i++) {
  //   if (sentence[i] === "<") {
  //     if (word.length > 0) {
  //       answer.push(word.reverse().join(""));
  //       word.splice(0, word.length);
  //     }
  //     word.push("<");
  //   } else if (sentence[i] === ">") {
  //     word.push(">");
  //     answer.push(word.join(""));
  //     word.splice(0, word.length);
  //   } else if (sentence[i] === " ") {
  //     if (word.length > 0 && !word.includes("<")) {
  //       answer.push(word.reverse().join("") + " ");
  //       word.splice(0, word.length);
  //     }
  //   } else {
  //     word.push(sentence[i]);
  //   }
  // }
  // if (word.length > 0) {
  //   answer.push(word.reverse().join(""));
  // }
  // return answer.join("");
  let answer = input[0];
  const regExp = /<[a-z\s]+>|[a-z0-9]+/g;

  answer = answer.replace(regExp, (word) => {
    return word.startsWith("<") ? word : word.split("").reverse().join("");
  });

  return answer;
}

console.log(solution(input));
