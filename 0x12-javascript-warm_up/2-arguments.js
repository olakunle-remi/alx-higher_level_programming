#!/usr/bin/node
const argulength = process.argv.length;
if (argulength === 2) {
  console.log('No argument');
} else if (argulength === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
