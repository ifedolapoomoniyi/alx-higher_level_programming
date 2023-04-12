#!/usr/bin/node

exports.callMeMoby = function (x, arg) {
  for (let i = 0; i < x; i++) {
    arg();
  }
};
