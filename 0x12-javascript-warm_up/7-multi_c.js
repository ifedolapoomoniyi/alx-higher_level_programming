#!/usr/bin/node

const integer = parseInt(process.argv[2]);

if (!integer) {
    console.log('Missing number of occurrences');
} else {
    for (let i = 0; i < integer; i++) {
        console.log('C is fun');
    }
}