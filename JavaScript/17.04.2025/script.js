/* a = 5
let b = 67
var c = 23



name = prompt('введите имя'); 
alert('Привет' + name); */


// function line() {
//    for(let i = 0; i < 5; i++) {
//    console.log('-----')
//    }
// }

// console.log("1");
// line();
// console.log("1");
// line();
// console.log("1");
// line();

let elNum = document.getElementsByClassName("num")[0];
console.log(elNum.textContent);

function up() {
   elNum.textContent++;
}

function down() {
   elNum.textContent--;
}