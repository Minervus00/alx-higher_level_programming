#!/usr/bin/node
// Prints all characters in the right order of a movie which id is given

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (error, response, body) => {
  if (!error) {
    let result = JSON.parse(body).characters;

    for (let idx = 0; idx < result.length; idx++) {
      request(result[idx], (err, resp, bdy) => {
        console.log(JSON.parse(bdy).name);
      });
    }
  }
});
