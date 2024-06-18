#!/usr/bin/node
module.exports = class Rectangle {
  constructor (m, n) {
    if (m > 0 && n > 0) {
      this.width = m;
      this.height = n;
    }
  }

  print () {
    let rectChar;
    for (let index = 0; index < this.height; index++) {
      rectChar = '';
      for (let j = 0; j < this.width; j++) {
        rectChar += 'X';
      }
      console.log(rectChar);
    }
  }
};
