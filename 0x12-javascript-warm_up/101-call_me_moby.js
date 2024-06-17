#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let m = 0; m < x; m++) {
    theFunction();
  }
};
