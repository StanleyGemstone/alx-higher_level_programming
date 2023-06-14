#!/usr/bin/node
const { list } = require('./100-data.js');

function computeNewArray(inputArray) {
  return inputArray.map((value, index) => value * index);
}

console.log("Initial list:", list);
console.log("New list:", computeNewArray(list));

