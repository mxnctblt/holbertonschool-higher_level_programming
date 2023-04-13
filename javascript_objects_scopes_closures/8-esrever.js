#!/usr/bin/node
exports.esrever = function (list) {
let rev = [];
  while (list.length) {
    rev.push(list.pop());
  }
  return rev;
}
