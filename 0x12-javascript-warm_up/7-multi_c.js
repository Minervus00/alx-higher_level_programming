#!/usr/bin/node

let vari = process.argv[2];

if (!vari) {
  console.log('Missing number of occurrences');
} else {
  vari = parseInt(vari);
  if (vari > 0) {
    for (let k = 0; k < vari; k++) {
      console.log('C is fun');
    }
  }
}
