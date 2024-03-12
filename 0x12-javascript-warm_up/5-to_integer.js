#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  const x = parseInt(process.argv[2]);
  console.log('My number: ' + x);
}
