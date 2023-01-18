#!/usr/bin/node

const request = require('request');
// const url = 'https://swapi-api.alx-tools.com/api/people/18';

// request(url, (error, response, body) => {
//   if (error) throw error;
//   console.log(JSON.parse(body).films.length);
// });
const url = process.argv[2];
const targ = 'https://swapi-api.alx-tools.com/api/people/18/';
let casts = 0;

request(url, (error, response, body) => {
  if (!error) {
    const result = JSON.parse(body);
    const count = result.count;
    const films = result.results;

    for (let i = 0; i < count; i++) {
      const buff = films[i].characters;
      const len = buff.length;
      for (let y = 0; y < len; y++) {
        if (buff[y] === targ) casts++;
      }
    }
    console.log(casts);
  }
});
