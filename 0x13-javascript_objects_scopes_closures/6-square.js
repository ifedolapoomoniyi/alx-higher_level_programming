#!/usr/bin/node

const parentSquare = require('./5-square');

class Square extends parentSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let horizontal = '';
      for (let j = 0; j < this.width; j++) {
        horizontal = horizontal + c;
      }
      console.log(horizontal);
    }
  }
}

module.exports = Square;
