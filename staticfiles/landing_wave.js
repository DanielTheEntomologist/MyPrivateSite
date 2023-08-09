"use strict"

console.log("Script loaded")

// function that updates part of path d attribute to have new x value
function change_paths(x, y) {

    let wave_path_upper = document.getElementById("animated-path-upper")
    // let wave_path_upper_d = wave_path.getAttribute("d")

    let wave_path_lower = document.getElementById("animated-path-lower")
    // let wave_path_lower_d = wave_path.getAttribute("d")

    // let wave_path_d_array = wave_path_d.split(" ")
    let domrect = document.getElementById("wave-container").getBoundingClientRect()

    // console.log(domrect.width)
    // console.log(domrect.y)

    // const new_wave_path_d = wave_path_d_array[0] + " " + wave_path_d_array[1] + " " + wave_path_d_array[2] + " " + wave_path_d_array[3] + " " + x + " " + wave_path_d_array[5] + " " + wave_path_d_array[6] + " " + wave_path_d_array[7] + " " + wave_path_d_array[8]

    // console.log(`x,y:`, x, y, `width,height:`, domrect.width, domrect.height)

    // let new_wave_path_d = `M00,1000 C${x - 100},100 ${x},100 1000,1000`
    // let new_wave_path_d = `M00,1000 C100,100 ${x / domrect.width * 1000},${y / domrect.height * 1000}, 750,800 S800,800 1000,1000`

    // let new_wave_path_d = `M00,1000 ${x / domrect.width * 1000},${y / domrect.height * 1000}, 1000,1000`


    let new_wave_path_lower_d = `M00,1000 C${x / domrect.width * 1000},${y / domrect.height * 1000} ${x / domrect.width * 1000},${y / domrect.height * 1000} 1000,1000`
    let new_wave_path_upper_d = `M00,00 C${x / domrect.width * 1000},${y / domrect.height * 1000} ${x / domrect.width * 1000},${y / domrect.height * 1000} 1000,00`

    // let new_wave_path_d = `M00,1000 ${x / domrect.width * 1000},${y / domrect.height * 1000}, 1000,000, 000,000 ${x / domrect.width * 1000},${y / domrect.height * 1000}, 1000,1000`




    // let new_wave_path_d = `M00,1000 C300,100 ${x},100 1000,1000`
    // let new_wave_path_d = `M00,1000 C1000,100 300,100 1000,1000`
    wave_path_lower.setAttribute("d", new_wave_path_lower_d)
    wave_path_upper.setAttribute("d", new_wave_path_upper_d)
    // console.log(wave_path_d)
    // console.log(wave_path_d_array)
    // console.log(new_wave_path_d)


}




// event listener for mouse movement
// document.addEventListener("mousemove", create_bubble(event.clientX))

// do things on page load



// function init() {console.log("Init running")}


const wave_container = document.getElementById("wave-container")

// window.onload = init
// window.onmousemove = function (e) { create_bubble(e.clientX) }
console.log(wave_container)


// event listener for mouse movement overs specific element
// bubble_container.addEventListener("mousemove", (e) => { create_bubble(e.clientX) })

wave_container.onmousemove = function (e) { change_paths(e.offsetX, e.offsetY) }
// window.onmousemove = function (e) { create_bubble(e.offsetX) }