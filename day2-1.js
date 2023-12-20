// day 2 part 1
const fs = require("fs");
const file = fs.readFileSync("./day2.txt", { encoding: "utf-8" });
const splitGames = file.split("\n");
const games = splitGames
  .map((game) => {
    const gameNumber = game.indexOf(":");
    const turns = game.substring(gameNumber + 2);
    return turns.split(";");
  })
  .map((g) => {
    return g.map((t) =>
      t
        .split(",")
        .map((c) => c.trim())
        .map((c) => c.split(" "))
    );
  });

function sumLegalGames(gameList) {
  const illegalGames = [];
  gameList.forEach((currGame, gameIdx) => {
    const allColors = {
      red: 12,
      green: 13,
      blue: 14,
    };
    currGame.forEach((currentTurn) => {
      currentTurn.forEach((color) => {
        if (+color[0] > allColors[color[1]]) {
          illegalGames.push(gameIdx + 1);
        }
      });
    });
  });
  const legalGames = new Array(gameList.length)
    .fill(0)
    .map((g, idx) => idx + 1)
    .map((currGame, idx) =>
      illegalGames.find((ill) => ill == idx + 1) ? null : currGame
    );
  return legalGames.filter((g) => !!g).reduce((acc, curr) => acc + curr, 0);
}

console.log(sumLegalGames(games));
