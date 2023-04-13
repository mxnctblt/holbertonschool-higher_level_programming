#!/usr/bin/node
exports.esrever = function (list) {
var rev = [];
  while (list.length) {
    rev.push(list.pop());
  }
  return rev;
}
