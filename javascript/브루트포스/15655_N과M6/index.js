const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test1.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const [n, m] = input[0].split(" ").map(Number);
  const arr = input[1].split(" ").map(Number).sort();
  const combination = (arr, selectNum) => {
    const result = [];
    if (selectNum === 1) return arr.map((v) => [v]);
    arr.forEach((v, idx, arr) => {
      const fixed = v;
      const restArr = arr.slice(idx + 1);
      const combinationArr = combination(restArr, selectNum - 1);
      const combineFix = combinationArr.map((v) => [fixed, ...v]);
      result.push(...combineFix);
    });
    return result;
  };
  const answer = combination(arr, m).map((n) => n.join(" "));
  return answer.join("\n");
}


let re = function(cnt,n,m,k){
    if(cnt==m){
      result.push(list.join(' '))
      return 1;
    }
    for(let i=1;i<=n;i++){    
      list[cnt] = i;
      k = i;
      re(cnt+1,n,m);      
    }
    return 1;
  }
  
console.log(solution(input));
