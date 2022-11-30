#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let cnt = 0;
  list.forEach(element => {
    if (element === searchElement) {
      cnt++;
    }
  });
  return (cnt);
};
