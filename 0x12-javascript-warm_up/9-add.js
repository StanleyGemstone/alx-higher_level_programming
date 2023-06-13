#!/usr/bin/node
function add(a, b) {
  return a + b;
}

const firstInteger = parseInt(process.argv[2]);
const secondInteger = parseInt(process.argv[3]);

if (!isNaN(firstInteger) && !isNaN(secondInteger)) {
  const result = add(firstInteger, secondInteger);
  console.log(result);
} else {
  console.log('NaN');
}
