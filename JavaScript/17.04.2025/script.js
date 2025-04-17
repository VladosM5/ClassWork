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

// let elNum = document.getElementsByClassName("num")[0];
// console.log(elNum.textContent);

// function up() {
//    elNum.textContent++;
// }

// function down() {
//    elNum.textContent--;
// }

// let a = 3348639469681305789684747n;
// let b = a + 3348639469681305n;
// console.log(typeof b + " " + b);

// let b = "dfggsf";
// b = b.indexOf("w");
// console.log(typeof b + " " + b);

// let a;
// console.log(typeof a);
// console.log(Math)


num = 0
q1 = confirm("2 * 2 = 4?");
if (q1) {
   num++;
   alert("верно")
} else {
   alert("не верно")
}
q1 = confirm("2 * 2 = 5?");
if (!q1) {
   num++;
   alert("верно");
} else {
   alert("не верно");
}
q1 = confirm("2 * 3 = 4?");
if (!q1) {
  num++;
  alert("верно");
} else {
  alert("не верно");
}

if(num==0) alert("лузер");
if (num == 1) alert("плоховато");
if (num == 2) alert("хорошо");
if (num == 3) alert("отлично");