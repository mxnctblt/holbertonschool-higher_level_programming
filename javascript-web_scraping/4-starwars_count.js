#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    results = JSON.parse(body).results;
    let count = 0;
    for (let i = 0; i < results.length; ++i) {
      const characters = results[i].characters;
      for (let j = 0; j < characters.length; ++j) {
	if (characters[j].endsWith('/18/') === true) {
	count += 1;
	}
      }
    }
    console.log(count);
  }
});
