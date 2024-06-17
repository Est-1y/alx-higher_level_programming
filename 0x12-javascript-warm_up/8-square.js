#!/usr/bin/node
const argSquare = process.argv;
const size = parseInt(argSquare[2], 10);

if (argSquare[2]) {
  if (size) {
    for (let i = 0; i < size; i++) {
      let square = '';
      for (let j = 0; j < size; j++) {
        square += 'X';
      }
      console.log(square);
    }
  } else {
    console.log('Missing size');
  }
} else {
  console.log('Missing size');
}
