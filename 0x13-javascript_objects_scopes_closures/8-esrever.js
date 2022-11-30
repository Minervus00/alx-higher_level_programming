#!/usr/bin/node
exports.esrever = function (list) {
  const len = list.length;
  const vari = Math.floor(len / 2);
  let buff;
  for (let k = 0; k < vari; k++) {
    buff = list[k];
    list[k] = list[len - 1 - k];
    list[len - 1 - k] = buff;
  }
  return (list);
};
