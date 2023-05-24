const arr = [1, 2, 3, 4];
arr.push(5);            // O(1)
arr.pop();              // O(1)
arr.unshift(0);         // O(n)
arr.splice(2, 1, 6);    // O(1) ~ O(n)

class MyArray {
    constructor() {
        this.data = {}
        this.length = 0;
    }
    get() {
        return this.data;
    }

    push(item) {
        this.data[this.length] = item;
        this.length++;
        return this.length;
    }

    pop() {
        if(this.length == 0) {
            console.error("Nothing to delete");
            return;
        }
        const returnItem = this.data[this.length-1];
        delete this.data[this.length-1];
        this.length--;
        return returnItem;
    }

    changeOrderOfItems(index) {
        for(let i = index; i<this.length-1; i++) {
            this.data[i] = this.data[i+1]
        }
        delete this.data[this.length-1];
        this.length--;
    }

    deleteWithIndex(index) {
        if(index > this.length || index < 0) {
            console.error("invalid index");
            return;
        }
        const removedItem = this.data[index];
        this.changeOrderOfItems(index);
        return removedItem;
    }
}

const myArr = new MyArray();
myArr.push(10);
myArr.pop();