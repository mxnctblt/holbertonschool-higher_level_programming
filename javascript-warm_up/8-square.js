#!/usr/bin/node
let i;
let j;

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (i = 0; i < process.argv[2]; i++) {
    let x = '';
    const y = 'X';
    for (j = 0; j < process.argv[2]; j++) {
      x += y;
    }
    console.log(x);
  }
}
