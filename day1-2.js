const fs = require("fs");

const numberStrings = {
  one: 1,
  two: 2,
  three: 3,
  four: 4,
  five: 5,
  six: 6,
  seven: 7,
  eight: 8,
  nine: 9,
};

function getFirstAndLastNumbers(str) {
  let first;
  let last;
  let firstWordList = [];
  let lastWordList = [];

  for (let i = 0; i < str.length; i++) {
    if (+str[i]) {
      first = { value: str[i], idx: i };
      break;
    }
  }

  for (let i = str.length - 1; i >= 0; i--) {
    if (+str[i]) {
      last = { value: str[i], idx: i };
      break;
    }
  }

  for (const number in numberStrings) {
    firstWordIdx = str.indexOf(number);
    lastWordIdx = str.lastIndexOf(number);
    if (firstWordIdx >= 0) {
      firstWordList.push({ value: numberStrings[number], idx: firstWordIdx });
    }
    if (lastWordIdx >= 0) {
      lastWordList.push({ value: numberStrings[number], idx: lastWordIdx });
    }
  }

  if (firstWordList.length === 0) {
    return `${first.value}${last.value}`;
  }

  if (!first) {
    return `${
      firstWordList.toSorted((a, b) => {
        if (a.idx > b.idx) return -1;
        if (a.idx < b.idx) return 1;
      })[0].value
    }
    ${
      lastWordList.toSorted((a, b) => {
        if (a.idx > b.idx) return -1;
        if (a.idx < b.idx) return 1;
      })[0].value
    }`;
  }

  let firstValue = [
    first,
    firstWordList.toSorted((a, b) => {
      if (a.idx < b.idx) return -1;
      if (a.idx > b.idx) return 1;
    })[0],
  ].sort((a, b) => {
    if (a.idx < b.idx) return -1;
    if (a.idx > b.idx) return 1;
  })[0].value;

  let lastValue = [
    last,
    lastWordList.toSorted((a, b) => {
      if (a.idx > b.idx) return -1;
      if (a.idx < b.idx) return 1;
    })[0],
  ].sort((a, b) => {
    if (a.idx > b.idx) return -1;
    if (a.idx < b.idx) return 1;
  })[0].value;

  return `${firstValue}${lastValue}`;
}

const file = fs.readFileSync("./elf-calibration.txt", { encoding: "utf-8" });
const strArr = file.split("\n");
const mapped = strArr.map((s) => getFirstAndLastNumbers(s));
const reduced = mapped.reduce((acc, curr) => acc + parseInt(curr), 0);
console.log(reduced);
