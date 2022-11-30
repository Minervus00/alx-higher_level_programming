#!/usr/bin/node

let list = require('./100-data.js').list;
console.log(list);
list = list.map((elem, index) => elem * index);
console.log(list);
