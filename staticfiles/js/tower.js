"use strict";

// remove first removing layer div from tower-container
function removeFirstLayer() {
  let towerContainer = document.getElementsByClassName("tower-container")[0];
  towerContainer.removeChild(towerContainer.getElementsByClassName("layer")[0]);
  countOfLayers = document.getElementsByClassName("layer").length;
}

function animateLayer(layer) {
  let layerKeyFrames = [{ top: "-20%" }, { top: "120%" }];
  let layerAnimationOptions = {
    duration: 6000,
  };

  layer.animate(layerKeyFrames, layerAnimationOptions);
}

// function that animates bricks
function animateBrick(brick) {
  //random number between 0 and 100
  let random = Math.floor(Math.random() * 400 - 200);

  let flyingBrickKeyFrames = [
    { left: `${random}%`, bottom: "1000%" },
    { left: "0%", bottom: "0%" },
    { left: "0%", bottom: "0%" },
  ];
  let flyingBrickAnimationOptions = {
    duration: 8000,
  };
  brick.animate(flyingBrickKeyFrames, flyingBrickAnimationOptions);
}

// named function that creates a new layer element that has five bricks inside
function createLayer() {
  let newLayer = document.createElement("div");
  newLayer.classList.add("layer");
  document.getElementsByClassName("tower-container")[0].appendChild(newLayer);
  animateLayer(newLayer);
  if (oddLayer === true) {
    // create five bricks inside the new layer
    for (let i = 0; i < 5; i++) {
      let newBrick = document.createElement("div");
      newBrick.classList.add("brick");

      newLayer.appendChild(newBrick);
      animateBrick(newBrick);
    }
    oddLayer = false;
  } else {
    // create 2 short bricks and 4 long bricks
    for (let i = 0; i < 6; i++) {
      let newBrick = document.createElement("div");
      if (i === 0 || i === 5) {
        newBrick.classList.add("brick");
        newBrick.classList.add("shortbrick");
      } else {
        newBrick.classList.add("brick");
      }
      newLayer.appendChild(newBrick);
      animateBrick(newBrick);
    }

    oddLayer = true;
  }
  countOfLayers = document.getElementsByClassName("layer").length;
}

let delay = 300;
let oddLayer = true;
let countOfLayers = 0;

setInterval(createLayer, delay);
setTimeout(() => {
  setInterval(removeFirstLayer, delay);
}, 6000);
