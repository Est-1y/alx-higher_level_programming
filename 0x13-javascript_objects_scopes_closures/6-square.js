#!/usr/bin/node
const SquareOne = require('./5-square');

module.exports = class Square extends SquareOne {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let index = 0; index < this.height; index++) {
      console.log(c.repeat(this.width));
    }
  }
};
