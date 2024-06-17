#!/usr/bin/node

const Arg1 = parseInt(process.argv[2]);
const Arg2 = parseInt(process.argv[3]);

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return NaN;
  }
  return a + b;
}
console.log(add(Arg1, Arg2));
