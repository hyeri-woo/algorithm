function reverseString(str) {
    if (str.length < 2 || typeof str !== 'string') {
        console.error("invalid input");
        return;
    }
    let returnVal = "";
    for(let i=str.length-1; i>=0; i--) {
        // console.log(str.charAt(i));
        returnVal += str[i];
    }
    return returnVal;
}

const str = "hello";
const answer = reverseString(str);