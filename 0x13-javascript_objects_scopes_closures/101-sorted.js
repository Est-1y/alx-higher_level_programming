#!/usr/bin/node
// Importing statement
const { dict } = require('./101-data.js');

// New dictionary
const usersByOccurrence = {};

// Loop over
for (const userId in dict) {
  const occurrence = dict[userId];
  
  if (!usersByOccurrence[occurrence]) {
    usersByOccurrence[occurrence] = [];
  }
  
  usersByOccurrence[occurrence].push(userId);
}

console.log(usersByOccurrence);
