const fs = require("fs");

function getFirstAndLastNumbers(str) {
  let first;
  let current;
  for (let i = 0; i < str.length; i++) {
    if (+str[i] || +str[i] === 0) {
      if (!first && first !== 0) {
        first = str[i];
      } else {
        current = str[i];
      }
    }
  }
  if (!current && current !== 0) {
    return first + first;
  } else {
    return first + current;
  }
}
const file = fs.readFileSync("./day1.txt", { encoding: "utf-8" });
const strArr = file.split("\n");
const mapped = strArr.map((s) => getFirstAndLastNumbers(s));
const reduced = mapped.reduce((acc, curr) => acc + parseInt(curr), 0);
console.log(reduced);
