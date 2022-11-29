#!/usr/bin/node
const Square1 = require('./5-square');

module.exports = class Square extends Square1 {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let k = 0; k < this.height; k++) {
      let stri = '';
      for (let j = 0; j < this.width; j++) {
        stri += c;
      }
      console.log(stri);
    }
  }
};
