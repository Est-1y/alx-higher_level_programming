#!/usr/bin/node
const { dict } = require('./101-data');
//iterate throug the occurences
const occurrencesDict = {};
for (const userId in dict) {
  const occurrences = dict[userId];

  if (occurrences in occurrencesDict) {
    occurrencesDict[occurrences].push(userId);
  } else {
    occurrencesDict[occurrences] = [userId];
  }
}

console.log(occurrencesDict);
