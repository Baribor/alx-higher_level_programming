#!/usr/bin/node
function add (a, b) {
  return a + b;
}

const [first, second] = process.argv.slice(2);
console.log(add(parseInt(first), parseInt(second)));
