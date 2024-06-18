#!/usr/bin/node
const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js fileA fileB fileC');
  process.exit(1);
}

const [, , file1, file2, file3] = process.argv;

try {
  const data1 = fs.readFileSync(file1, 'utf8');
  const data2 = fs.readFileSync(file2, 'utf8');
  const concatenatedData = `${data1}${data2}`;
  fs.writeFileSync(file3, concatenatedData);
} catch (error) {
  console.error(`Error: ${error.message}`);
  process.exit(1);
}
