#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/people/18'

request(url, (error, response, body) => {
  if (error) throw error;
  console.log(JSON.parse(body).films.length);
});
