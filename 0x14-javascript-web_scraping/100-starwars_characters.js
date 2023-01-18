#!/usr/bin/node
// Prints all characters of a Star Wars movie which id is given as parameter 

const request = require('request');
const mvId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url, (error, response, body) => {
  if (!error) {
    const result = JSON.parse(body).results;

    result.forEach(element => {
      if (element.episode_id.toString() === mvId) {
        element.characters.forEach(char => {
          request(char, (err, resp, bdy) => {
            if (!err) {
              console.log(JSON.parse(bdy).name);
            }
          });
        });
      }
    });
  }
});
