// let a = +prompt('введите число');

// if(a > 0){
//    alert('больше нуля');
// }
// else if(a < 0){
//    alert('меньше нуля');
// }
// else{
//    alert('равно нулю');
// }

// let day = prompt('введите день недели');

// if(day=='понедельник'){
//    alert('пн');
// }
// else if(day=='вторник'){
//    alert('вт');
// }
// else if(day=='среда'){
//    alert('ср');
// }
// else if(day=='четверг'){
//    alert('чт');
// }
// else if(day=='пятница'){
//    alert('пт');
// }
// else if(day=='суббота'){
//    alert('сб');
// }
// else if(day=='воскресенье'){
//    alert('вс');
// }
// else{
//    alert('некорректные данные');
// }

// switch (day) {
//   case "понедельник":
//     alert("пн");
//     break;
//   case "вторник":
//     alert("вт");
//     break;
//   case "среда":
//     alert("ср");
//     break;
//   case "четверг":
//     alert("чт");
//     break;
//   case "пятница":
//     alert("пт");
//     break;
//   case "суббота":
//     alert("сб");
//     break;
//   case "воскресенье":
//     alert("вс");
//     break;
//   default:
//     alert('некорректные данные')
// }

// let age = +prompt('введите свой возвраст');

// if(age>0 && age<120){
//    alert('данные корректны');
// }
// else if(age<0 && age>120){
//    alert('некорректные данные');
// }

// let hours = +prompt('введите часы');
// let minutes = +prompt('введите минуты');
// let seconds = +prompt('введите секунды');

// if(hours<0 && hours>23){
//    alert('данные корректны');
// }
// else if(minutes<0 && minutes>59){
//    alert('данные корректны');
// }
// else if(seconds<0 && seconds>59){
//    alert('данные корректны');
// }
// else{
//    alert('некорректные данные');
// }

// let flag = true;
// if (hours<0 || hours>23) flag = false;
// if (minutes < 0 || minutes > 59) flag = false;
// if (seconds < 0 || seconds > 59) flag = false;

// if (flag) alert('данные корректны');
// else alert('данные не корректны');

// alert(flag ? 'данные корректны' : 'данные не корректны');

// let num1 = +prompt('введите первое число');
// let num2 = +prompt('введите второе число');

// alert(num1>num2 ? num1 : num2);

// let num1 = +prompt('введите первое число');
// let num2 = +prompt("введите второе число");
// let opper = prompt ('введите одну из операций: + - * /');

// switch(opper){
//    case '+':
//       alert(num1 + num2);
//       break;
//    case '-':
//       alert(num1 - num2);
//       break;
//    case '*':
//       alert(num1 * num2);
//       break;
//    case '/':
//       alert(num1 / num2);
//       break;
//    default:
//       alert('некорретные данные')
// }

// let count = 0;
// while (count < 10) {
//   console.log(count++);
// }

// let count = 0;
// do {
//   let num = +prompt("введите число: ");
//   count++;
// } while (num != 0);
// console.log(count);

// Вывести # столько раз, сколько указал пользователь.
// let count = 0;
// let a = +prompt("введите кол-во раз: ");
// do {
//   count++;
// } while (a > count);
// console.log(count);

// Пользователь ввел число, а на экран вывелись все числа от введеного до 0
// let a = +prompt('введите число: ');
// do {
//    alert(a);
//    a--;
// }while(a >= 0);

// Запросить число и степень. Возвести число в указанную степень и вывести результат
// let a = +prompt('введите число: ');
// let b = +prompt('введите степень: ');

// count = 1;
// ab = a;
// do {
//    ab = ab * a;
//    count++;
// }while(count < b);
// console.log(ab)


let a = +prompt('введите первое число: ');
let b = +prompt('введите второе число: ');

