#!/usr/bin/node
const nums = process.argv.slice(2).map(n => parseInt(n)).sort();
if (nums.length in [0, 1]) {
  console.log(0);
} else {
  let found = false;
  const max = nums[nums.length - 1];
  for (let i = nums.length - 2; i >= 0; --i) {
    if (nums[i] !== max) {
      console.log(nums[i]);
      found = true;
      break;
    }
  }
  if (!found) {
    console.log(0);
  }
}
