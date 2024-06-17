#!/usr/bin/node

const numsList = process.argv.slice(2);
function secondMax (list) {
  if (list.length < 2) {
    return 0;
  } else {
    list.sort((x, y) => x - y);
    list.pop();
    return list.pop();
  }
}
console.log(secondMax(numsList));
