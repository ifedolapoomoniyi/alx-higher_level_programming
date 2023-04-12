#!/usr/bin/node

const args = process.argv;
let highest = args[2];

if (args.length < 3) {
    console.log(0)
} else if (args.length < 4) {
    console.log(0)
} else {
    for (let i = 2; i < args.length; i++) {
        if (args[i] > highest ) {
          highest = args[i];
        }
      }
      console.log(highest)
}