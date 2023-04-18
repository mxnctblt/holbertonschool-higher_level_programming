#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const fs = require('fs');
    fs.writeFile(process.argv[3], body, 'utf8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
