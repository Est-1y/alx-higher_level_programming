#!/usr/bin/node

const req = require('request');
const episodeID = process.argv[2];
const apiUrl = 'https://swapi-api.hbtn.io/api/films/';
req.get(apiUrl + episodeID, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const episodeData = JSON.parse(body);
  const dd = episodeData.characters;
  for (const index of dd) {
    req.get(index, function (err, response, body1) {
      if (err) {
        console.log(err);
      }
      const episodeData1 = JSON.parse(body1);
      console.log(episodeData1.name);
    });
  }
});
