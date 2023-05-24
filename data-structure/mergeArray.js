function mergeArray(arr1, arr2) {
    let mergedArr = [];
    let [i1, i2] = [0, 0];
    while (mergedArr.length < arr1.length + arr2.length) {
        if(arr1[i1] < arr2[i2]) {
            mergedArr.push(arr1[i1]);
            i1++;
        } else {
            mergedArr.push(arr2[i2]);
            i2++;
        }
    }
    return mergedArr;
}

const arr1 = [1, 3, 4, 6];
const arr2 = [2, 3, 5, 7];
const merged = mergeArray(arr1, arr2);