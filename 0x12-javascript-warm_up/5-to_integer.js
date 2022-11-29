#!/usr/bin/node

let vari = process.argv[2];
if (vari === undefined) {
  console.log('Not a number');
} else {
  vari = parseInt(vari);
  if (Object.is(vari, NaN)) {
    console.log('Not a number');
  } else {
    console.log(`My first number: ${vari}`);
  }
}
