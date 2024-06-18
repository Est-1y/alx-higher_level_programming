#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (dimension) {
    super(dimension, dimension);
  }
};
