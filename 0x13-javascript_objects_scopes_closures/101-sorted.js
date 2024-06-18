#!/usr/bin/node
//Import statement
const {dict} = require('./101-data');

// Initializing a new object.
let sortedDict = {};
//Iteration
for (const userId in dict) {
  const occurrences = dict[userId];

  if (!sortedDict[occurrences]) {
    sortedDict[occurrences] = [];
  }

  sortedDict[occurrences].push(userId);
}

console.log(sortedDict);
