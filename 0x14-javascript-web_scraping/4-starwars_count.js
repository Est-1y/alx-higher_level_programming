#!/usr/bin/node

const request = require('request');

const api_Url = process.argv[2];

request(api_Url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const filmIndex in films) {
      const filmChars = films[filmIndex].characters;
      for (const charIndex in filmChars) {
        if (filmChars[charIndex].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
