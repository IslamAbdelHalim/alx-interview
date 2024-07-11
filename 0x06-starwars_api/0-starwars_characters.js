#!/usr/bin/node
const request = require('request');
const args = process.argv;
const film = args[2];

const url = 'https://swapi-api.alx-tools.com/api/films/' + film;

request(url, function(err, res, body) {
    if(err)
        throw err
    characters = JSON.parse(body).characters;
    for (const character of characters) {
        request(character, function(err, res, body){
            console.log(JSON.parse(body).name)
        })
    }
})