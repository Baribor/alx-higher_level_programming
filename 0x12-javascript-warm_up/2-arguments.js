#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length > 0) {
	console.log(`Argument${args.length === 1 ? '' : 's'} found`);
} else {
	console.log('No argument');
}
