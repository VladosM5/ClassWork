// function triangleArea(a, b, c) {
//   let S = a * b * c;
//   return S;
// }

// triangleArea(2, 5, 3);

// triangleArea(23, 56, 24);

// function rectangleArea(a, b, c, d) {
//   return a * b * c * d;
// }

// console.log(rectangleArea(1, 2, 3, 4))

// function smallAndBig(a, b) {
//    if (a > b){
//       return b
//    }
//    else if(a < b){
//       return a
//    }
// }
// console.log(smallAndBig(5, 10));

// function min(a, b){
//    return ((a<b)? a:b);
// }

// console.log('Минимальное значение: ' + min(4, 78))

// function exponentiation(c, d) {
//    let e = c ** d
//    return e
// }

// console.log(exponentiation(5, 2))

// function pow(c, d){
//    st = 1;
//    for (; d >= 1; d--){
//       st*=c;
//    }
//    return st;
// }

// let c = 3;
// let d = 5;
// console.log(`${c} в степени ${d} = ${pow(c, d)}`);

// function matVicheslenie(a, b, c) {
//   if (c == "+") {
//     return (d = a + b);
//   } else if (c == "-") {
//     return (d = a - b);
//   } else if (c == "*") {
//     return (d = a * b);
//   } else if (c == "/") {
//     return (d = a / b);
//   }
// }
// console.log(matVicheslenie(25, 30, "+"));

// let num = 15;

// let flag = true;

// function primeNumber(n) {
//   for (let i = 2; i < n / 2; i++) {
//     if (n % i == 0) {
//       return false;
//     }
//   }
//   return true;
// }

// let n = 5;

// console.log()

// let a = 7;

// function multiplicationTable(){
//    for (let i = 0; i < 10; i++){
//       console.log(`${a} * ${i} = ${a * i}`)
//    }
// }

// console.log(multiplicationTable(`${a}*1=${a*1}`))

// let a = 15;
// let n = 4;
// console.log(a / n);
// let i = 1;
// while (i < a / n) {
//   i++;
// }
// i--;
// console.log(i);
// console.log(a - i * n);

// Написать функцию, которая выводит все четные или нечетные числа в указанно диапазоне. true - четные, false - нечетные

// function evenOrOdd(a, b, flag) {
//   for (let i = a; i <= b; i++) {
//     if (flag && i % 2 == 0) console.log(i);
//     else if (!flag && i % 2) console.log(i);
//   }
// }
// console.log(evenOrOdd(2, 18, false))

// function all(...a) {
//   let summ = 0;
//   for (let i in a) {
//     summ += a[i];
//   }
//   return summ;
// }

// console.log(all(1, 2, 3, 4, 5));

// function all(...a) {
//   let max = a[0];
//   for (let i in a) {
//     if (max < a[i]){
//       max = a[i];
//     }
//   }
//   return max
// }

// console.log(all(5, 10, 2, 7, 9))