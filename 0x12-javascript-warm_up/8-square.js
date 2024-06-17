#!/usr/bin/node

const size = process.argv[2];

if (isNaN(parseInt(squareSize))) {
  console.log('Missing size');
} else {

  for (let i = 0; i < squareSize; i++) {
    let line = '';
    for (let j = 0; j < squareSize; j++) {
      line += 'X';
    }
    console.log(line);
  }
}
