const arr = [3, 2, 2, 4, 5, 2, 1, 0, 3];
answer = arr[0];
index = arr.length;
for(let i=0; i<arr.length; i++) {
    let curIndex = arr.indexOf(arr[i], i+1);
    console.log(answer, index, curIndex);
    if(curIndex != -1 && curIndex <= index) {
        index = curIndex;
        answer = arr[i]
    }
}
console.log(answer);