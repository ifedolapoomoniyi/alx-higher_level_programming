#!/usr/bin/node

const integer = parseInt(process.argv[2]);

if (!integer) {
    console.log('Missing size');
} else {
    for (let i = 0; i < integer; i++) {
        let row = 'x';
        while(row.length < integer) {
            row = row + 'x'
        }
        console.log(row)
    }
}