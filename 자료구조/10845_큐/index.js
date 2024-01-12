const fs = require("fs");

const input = fs.readFileSync("test.txt").toString().trim().split("\n");

function solution(input) {
  const queue = [];
  const answer = [];
  for (let i = 1; i <= input[0]; i++) {
    const [prompt, item] = input[i].split(" ");
    switch (prompt) {
      case "push":
        queue.push(item);
        break;
      case "pop":
        queue.length === 0 ? answer.push(-1) : answer.push(queue.shift());
        break;
      case "size":
        answer.push(queue.length);
        break;
      case "empty":
        queue.length === 0 ? answer.push(1) : answer.push(0);
        break;
      case "front":
        queue.length === 0 ? answer.push(-1) : answer.push(queue[0]);
        break;
      case "back":
        queue.length === 0
          ? answer.push(-1)
          : answer.push(queue[queue.length - 1]);
        break;
    }
  }
  return answer.join("\n");
}

console.log(solution(input));
