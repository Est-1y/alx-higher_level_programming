#!/usr/bin/node
function executeXTimes(x, theFunction) {
  if (x <= 0) {
    return;
  }
  
  theFunction();
  
  executeXTimes(x - 1, theFunction);
}
