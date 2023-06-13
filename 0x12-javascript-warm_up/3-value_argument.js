#!/usr/bin/node
if (process.argv.length > 2) {
	const firstArgv = process.argv[2];
	console.log(firstArgv);
} else {
	console.log("No argument");
}
