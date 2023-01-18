#!/usr/bin/node
// ./6-* https://jsonplaceholder.typicode.com/todos

const request = require('request');
const url = process.argv[2];
const data = {}

for (let i = 0; i < 10; i++) {
  const key = i.toString();
  request(url + '?userId=' + key + '&completed=true', (err, resp, body) => {
    body = JSON.parse(body);
    console.log(body);
    const len = body.length;
    if (!err && len) data[key] = len;
  });
}
console.log(data);
