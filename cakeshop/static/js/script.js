let amountElement = document.getElementById('amount');
let amount = amountElement.value; //amount lay gia tri tu phan tu co id ('amount')
//in gia tri  
let render = (amount) =>{
    amountElement.value = amount;
}
//handel PLUS
let handelPlus = () =>{
    amount++
    render(amount);
}

let handelMinus = () =>{
    if(amount > 1)
        amount--;
    render(amount);
}

amountElement.addEventListener('input', () =>{

});