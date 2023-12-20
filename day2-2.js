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
  const minColorsForGame = [];
  gameList.forEach((currGame, gameIdx) => {
    const minColors = {};
    currGame.forEach((currentTurn) => {
      currentTurn.forEach((color) => {
        if (!minColors[color[1]]) {
          minColors[color[1]] = +color[0];
        } else {
          minColors[color[1]] = Math.max(+color[0], minColors[color[1]]);
        }
      });
    });
    minColorsForGame.push(minColors);
  });

  return minColorsForGame
    .map((color) => Object.values(color).reduce((acc, curr) => acc * curr))
    .reduce((acc, curr) => acc + curr, 0);
}

console.log(sumLegalGames(games));
