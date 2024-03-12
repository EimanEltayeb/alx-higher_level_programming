#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  const x = parseInt(process.argv[2]);
  let st = '';
  for (let i = 0; i < x; i++) {
    st += 'X';
  }
  for (let i = 0; i < x; i++) {
    console.log(st);
  }
}
