#!/usr/bin/node

const integer1 = parseInt(process.argv[2]);
const integer2 = parseInt(process.argv[3]);

function add(a, b) {
    console.log(a + b);
}

add(integer1, integer2);