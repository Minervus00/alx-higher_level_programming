#!/usr/bin/node
// ./6-* https://jsonplaceholder.typicode.com/todos

const request = require('request');
const url = process.argv[2];
var data = {};

for (let i = 1; i <= 10; i++) {
  const key = i.toString();
  request(url + '?userId=' + key + '&completed=true', (err, resp, body) => {
    body = JSON.parse(body);
    const len = body.length;
    if (len !== 0) {
      data[key] = len;
      console.log(data);
    }
  });
}
