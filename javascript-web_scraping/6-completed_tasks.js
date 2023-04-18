#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const task = {};
    body = JSON.parse(body);
    for (let i = 0; i < body.length; ++i) {
      const userId = body[i].userId;
      const completed = body[i].completed;
      if (completed && task[userId] === undefined) {
	task[userId] = 1;
      } else if (completed) {
        task[userId] += 1;
      }
    }
    console.log(task);
  }
});
