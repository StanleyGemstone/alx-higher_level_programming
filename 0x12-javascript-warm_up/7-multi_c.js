#!/usr/bin/node
const multiPrint = process.argv[2];
const conMultiPrint = parseInt(multiPrint);

if (!isNaN(conMultiPrint)) {
  for (let i = 0; i < conMultiPrint; i++) {
    console.log ('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
