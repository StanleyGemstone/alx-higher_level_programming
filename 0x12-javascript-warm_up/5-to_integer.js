#!/usr/bin/node
const fArgv = process.argv[2];
const conArgv = parseInt(fArgv);

if (!isNaN(conArgv)) {
	console.log("My number: "+conArgv);
} else {
	console.log("Not a number");
}
