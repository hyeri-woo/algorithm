const hash = {};
hash.one = 1;
hash.one = 2;
hash.two = 10;
hash.three;
delete hash.three;

class HashTable {
    constructor(size) {
        this.data = new Array(size);
    }

    generateRandomHash(key) {
        let hash = 0;
        for(let i=0; i<key.length; i++) {
            hash = (hash + key.charCodeAt(i) * i) % this.data.length;
        }

        return hash;
    }

    getData() {
        return this.data;
    }

    set(key, value) {
        const address = this.generateRandomHash(key);
        if(!this.data[address]) {
            this.data[address] = [];
            this.data[address].push([key, value]);
            return value;
        } else {
            for(let i=0; i<this.data[address].length; i++) {
                if(this.data[address][i][0] === key) {
                    this.data[address][i][0] = value;
                    return value;
                }
            }
        }
        this.data[address].push([key, value]);
        return value
    }

    get(key) {
        const address = this.generateRandomHash(key);
        const returnVal = this.data[address].find(e => e[0] === key);
        if(returnVal === undefined) {
            console.error("cannot find value");
            return undefined;
        }
        return returnVal[1];
    }

    keys() {
        const keyArr = [];
        for(let i=0; i<this.data.length; i++) {
            if(this.data[i]) {
                if(this.data[i].length > 1) {
                    for (let j=0; j<this.data[i].length; i++) {
                        keyArr.push(this.data[i][j][0])
                    }
                } else {
                    keyArr.push(this.data[i][0][0])
                }
            }
        }
        return keyArr;
    }
}

const hashTable = new HashTable(10);
hashTable.set('key1', "h");
hashTable.set('key2', "e");
hashTable.set('key3', "l");
hashTable.set('key4', "l");
hashTable.set('key5', "o");

hashTable.get(1);