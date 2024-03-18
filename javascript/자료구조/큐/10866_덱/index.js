const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test2.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const deque = [];
  const answer = [];
  for (let i = 0; i <= input[0]; i++) {
    const [prompt, item] = input[i].split(" ");
    switch (prompt) {
      case "push_front":
        deque.unshift(parseInt(item));
        break;
      case "push_back":
        deque.push(parseInt(item));
        break;
      case "pop_front":
        deque.length === 0 ? answer.push(-1) : answer.push(deque.shift());
        break;
      case "pop_back":
        deque.length === 0 ? answer.push(-1) : answer.push(deque.pop());
        break;
      case "size":
        answer.push(deque.length);
        break;
      case "empty":
        deque.length === 0 ? answer.push(1) : answer.push(0);
        break;
      case "front":
        deque.length === 0 ? answer.push(-1) : answer.push(deque[0]);
        break;
      case "back":
        deque.length === 0
          ? answer.push(-1)
          : answer.push(deque[deque.length - 1]);
        break;
    }
  }
  return answer.join("\n");
}

console.log(solution(input));
