#!/usr/bin/node

const x = process.argv[2];
if (isNaN(x)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < parseInt(x); i++) {
    console.log('C is fun');
  }
}
