#!/usr/bin/node
exports.esrever = function (list) {
  const reversedList = [];
  for (let index = list.length - 1; index >= 0; index--) {
    reversedList.push(list[index]);
  }
  return reversedList;
};
