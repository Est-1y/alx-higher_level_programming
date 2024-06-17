#!/usr/bin/node
const n = parseInt(process.argv[2]);
function factorial(n) {
  if (isNaN(n)) {
    return 1;
  }

  if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
console.log(factorial(n));
