#!/usr/bin/node
//iterate throug the occurences
const { dict } = require('./101-data');

const occurrencesDict = {};
for (const userId in dict) {
  const occurrences = dict[userId];

  if (occurrencesDict.hasOwnProperty(occurrences)) {
    occurrencesDict[occurrences].push(userId);
  } else {
    occurrencesDict[occurrences] = [userId];
  }
}

console.log(occurrencesDict);
