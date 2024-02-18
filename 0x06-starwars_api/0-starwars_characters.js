#!/usr/bin/node
const util = require('util');
const request = util.promisify(require('request'));

const movieId = process.argv[2];
if (movieId === undefined || isNaN(movieId)) {
    console.log('Movie ID not provided or invalid.');
    return;
}

async function getMovieData (movieId) {
  const apiUrl = 'https://swapi-api.hbtn.io/api/films/' + movieId;
  

  const response = await request(apiUrl);
  const movieData = JSON.parse(response.body);
  const charactersUrls = movieData.characters;

  for (const characterUrl of (charactersUrls)) {
    let character = await (await request(characterUrl)).body;
    character = JSON.parse(character);
    console.log(character.name);
  }
}

getMovieData(movieId);
