const fs = require("fs");

// const input = fs.readFileSync("test1.txt").toString().trim().split("\n");
// const input = fs.readFileSync("test2.txt").toString().trim().split("\n");
const input = fs.readFileSync("test3.txt").toString().trim().split("\n");

function solution(input) {
  const word = input[0].split("");
  const temp = [];
  for (let i = 2; i < input.length; i++) {
    const [prompt, char] = input[i].split(" ");
    if (prompt === "L" && word.length) temp.push(word.pop());
    else if (prompt === "D" && temp.length) word.push(temp.pop());
    else if (prompt === "B" && word.length) word.pop();
    else if (prompt === "P") word.push(char);
  }
  return word.join("") + temp.reverse().join("");
}

console.log(solution(input));
