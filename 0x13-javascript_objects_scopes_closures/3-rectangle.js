#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let k = 0; k < this.height; k++) {
      let stri = '';
      for (let j = 0; j < this.width; j++) {
        stri += 'X';
      }
      console.log(stri);
    }
  }
};
