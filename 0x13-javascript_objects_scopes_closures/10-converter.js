#!/usr/bin/node
exports.converter = function (base) {
  if (base < 2 || isNaN(base)) {
    return;
  }
  return function (num) {
    return num.toString(base);
  };
};
