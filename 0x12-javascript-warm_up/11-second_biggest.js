#!/usr/bin/node

const args = process.argv.slice(2);
function secondLargest (args) {
  if (args.length < 2) {
    return 0;
  } else {
    args.sort((x, y) => x - y);
    args.pop();
    return args.pop();
  }
}
console.log(secondLargest(numsArgs));
