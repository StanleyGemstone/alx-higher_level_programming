#!/usr/bin/node
const { dict } = require('./101-data.js');

function computeUserIdsByOccurrence(occurrences) {
  const userIdsByOccurrence = {};

  for (const userId in occurrences) {
    const occurrenceCount = occurrences[userId];
    if (!userIdsByOccurrence[occurrenceCount]) {
      userIdsByOccurrence[occurrenceCount] = [];
    }
    userIdsByOccurrence[occurrenceCount].push(userId);
  }

  return userIdsByOccurrence;
}

const userIdsByOccurrence = computeUserIdsByOccurrence(dict);
console.log(userIdsByOccurrence);

