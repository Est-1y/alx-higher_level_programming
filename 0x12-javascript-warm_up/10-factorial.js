#!/usr/bin/node
function factorial(n) {
  if (isNaN(n)) {
    console.log(1);
    return;
  }
  
  if (n === 0) {
    console.log(1);
    return 1;
  } else {
    let result = n * factorial(n - 1);
    console.log(result);
    return result;
  }
}

const n = parseInt(process.argv[2]);
factorial(n);
