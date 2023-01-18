#!/usr/bin/node
// ./6-* https://jsonplaceholder.typicode.com/todos

const request = require('request');
const url = process.argv[2];

request(url, (err, resp, body) => {
  if (!err) {
    let data = {};
    resp = JSON.parse(body);
    resp.forEach(todo => {
      if (todo.completed && data[todo.userId] === undefined) {
        data[todo.userId] = 1;
      } else if (todo.completed) data[todo.userId] += 1;
    });
    console.log(data);
  }
});
