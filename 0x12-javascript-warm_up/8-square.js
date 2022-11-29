#!/usr/bin/node

let vari = process.argv[2];

if (vari === undefined) {
  console.log('Missing size');
} else {
  vari = parseInt(vari);
  if (Object.is(vari, NaN)) {
    console.log('Missing size');
  } else {
    for (let k = 0; k < vari; k++) {
      let stri = '';
      for (let j = 0; j < vari; j++) {
        stri += 'X';
      }
      console.log(stri);
    }
  }
}
