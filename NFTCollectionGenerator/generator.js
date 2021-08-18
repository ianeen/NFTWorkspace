const { createCanvas } = require("canvas");
const fs = require("fs");

const width = 1400;
const height = 400;
const images = 1;
const lineWidthBounds = [1, 3];
const lineBounds = [5, 10];
const pointBounds = [10, 69];

for (var image = 1; image <= images; image++) {
    const canvas = createCanvas(width, height);

    const context = canvas.getContext("2d");

    context.fillStyle = genRandomHex();
    context.fillRect(0, 0, width, height);
    for (var i = 0; i < genRandomNum(lineBounds[0], lineBounds[1]); i++) {
        context.strokeStyle = genRandomHex();
        context.lineWidth = genRandomNum(lineWidthBounds[0], lineWidthBounds[1]);
        context.beginPath();
        for (var j = 0; j < genRandomNum(pointBounds[0], pointBounds[1]); j++) {
            context.lineTo(genRandomNum(0, width), genRandomNum(0, height));
        }
        context.stroke();
    }

    const buffer = canvas.toBuffer("image/png");

    console.log(`Generating ${image}`)
    fs.writeFileSync(`./collection/banner${image}.png`, buffer);
}

/* ---------------------------- Helper Functions ---------------------------- */

function genRandomNum(start, end) {
    return Math.floor((Math.random() * end) + start);
}

function genRandomHex() {
    return '#'+(Math.random() * 0xFFFFFF << 0).toString(16).padStart(6, '0');
}