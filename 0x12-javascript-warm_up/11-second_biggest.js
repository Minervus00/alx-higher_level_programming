#!/usr/bin/node

const argtab = process.argv;
let maxi = 0;
let maxi2 = 0;
let tmp = 0;
let k = 2;

for (; argtab[k]; k++) {
  tmp = parseInt(argtab[k]);
  if (tmp > maxi) {
    maxi2 = maxi;
    maxi = tmp;
  } else if (tmp > maxi2 && tmp !== maxi) {
    maxi2 = tmp;
  }
}

if (k === 3) {
  console.log(0);
} else {
  console.log(maxi2);
}
