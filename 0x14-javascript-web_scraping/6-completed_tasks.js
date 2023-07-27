#!/usr/bin/node
const request = require('request');

const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

request(apiUrl, { json: true }, (error, response, body) => {
  if (error) {
    console.error('Error:', error.message);
  } else if (response.statusCode !== 200) {
    console.error('Status:', response.statusCode);
  } else {
    const completedTasks = {};
    body.forEach(task => {
      if (task.completed) {
        if (!completedTasks[task.userId]) {
          completedTasks[task.userId] = [];
        }
        completedTasks[task.userId].push({
          task: task.title,
          completed: task.completed,
          username: ''
        });
      }
    });
    request('https://jsonplaceholder.typicode.com/users', { json: true }, (error, response, body) => {
      if (error) {
        console.error('Error:', error.message);
      } else {
        body.forEach(user => {
          const userId = user.id;
          if (completedTasks[userId]) {
            completedTasks[userId].forEach(task => {
              task.username = user.username;
            });
          }
        });
        console.log(JSON.stringify(completedTasks, null, 2));
      }
    });
  }
});

