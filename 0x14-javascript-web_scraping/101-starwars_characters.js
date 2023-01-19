#!/usr/bin/node
// Prints all characters in the right order of a movie which id is given

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (error, response, body) => {
  if (!error) {
    const result = JSON.parse(body).characters;

    let txt = '';
    result.forEach(char => {
      request(char, (err, resp, bdy) => {
        if (!err) {
          txt += JSON.parse(bdy).name;
          if (char !== result[result.length - 1]) txt += '\n';
        }
      });
    });
  }
});
