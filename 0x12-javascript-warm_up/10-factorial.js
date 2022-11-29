#!/usr/bin/node

function factorial (a) {
  if (a <= 1 || Object.is(a, NaN)) {
    return (1);
  }
  return (a * factorial(a - 1));
}

console.log(factorial(parseInt(process.argv[2])));
