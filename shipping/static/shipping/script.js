const values = [...document.querySelectorAll('.price')]
        .map(element => element.innerText.replace('.', '').replace(',00', '')) 

total = 0
for(i = 0; i <values.length; i++){
    console.log(values[i])
    total += Number(values[i]);
}
console.log(total)

console.log(typeof (total))
let bil = total.toString()
console.log(typeof(bil))
console.log(bil)

let reverse = bil.toString().split('').reverse().join('')
let ribuan 	= reverse.match(/\d{1,3}/g);
let bil_ribuan	= ribuan.join('.').split('').reverse().join('');     

document.getElementById("hasil").innerHTML = "Total = Rp. " + bil_ribuan + ",00";

        