"use strict"

// var Xslider = document.getElementById("Xslider");
// var Xoutput = document.getElementById("XDisplay");

// var Yslider = document.getElementById("Yslider");
// var Youtput = document.getElementById("YDisplay");

// var Zslider = document.getElementById("Zslider");
// var Zoutput = document.getElementById("ZDisplay");

// output.innerHTML = slider.value; // Display the default slider value

// // Update the current slider value (each time you drag the slider handle)
// slider.oninput = function () {
//     output.innerHTML = this.value;
// }

class Slider {
    constructor(input, output) {
        this.input = input;
        this.output = output;

        // Add event listener to input element to update output element
        this.input.addEventListener('input', () => {
            this.output.textContent = this.input.value;
        });
    }
}

const Xslider = new Slider(document.querySelector('#Xslider'), document.querySelector('#XDisplay'));
const Yslider = new Slider(document.querySelector('#Yslider'), document.querySelector('#YDisplay'));
const Zslider = new Slider(document.querySelector('#Zslider'), document.querySelector('#ZDisplay'));

class Cube {
    constructor(cubeDiv, inputX, inputY, inputZ) {
        this.cubeDiv = cubeDiv;
        this.inputX = inputX
        this.inputY = inputY
        this.inputZ = inputZ

        console.log(`${this.cubeDiv.style}`)

        this.cubeDiv.style.transform = "rotateZ(45deg) rotateX(45deg) rotateY(90deg)";
        // Add event listener to input element to update output element
        this.inputY.addEventListener('input', () => {
            console.log(`${this.inputY.value}`)
            this.cubeDiv.style.transform = `rotateZ(${this.inputZ.value}deg) rotateX(${this.inputX.value}deg) rotateY(${this.inputY.value}deg)`;
        });
        this.inputX.addEventListener('input', () => {
            console.log(`${this.inputX.value}`)
            this.cubeDiv.style.transform = `rotateZ(${this.inputZ.value}deg) rotateX(${this.inputX.value}deg) rotateY(${this.inputY.value}deg)`;
        });
        this.inputZ.addEventListener('input', () => {
            console.log(`${this.inputZ.value}`)
            this.cubeDiv.style.transform = `rotateZ(${this.inputZ.value}deg) rotateX(${this.inputX.value}deg) rotateY(${this.inputY.value}deg)`;
        });
    }
}

const cube = new Cube(document.getElementsByClassName('cube')[0], document.querySelector('#Xslider'), document.querySelector('#Yslider'), document.querySelector('#Zslider'))