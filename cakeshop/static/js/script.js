var form = document.getElementById('cart-item_form')
var input = document.getElementById('amount');
var value = parseInt(input.value);

function handelMinus() {
    value--;
    input.value = value < 1 ? 1 : value
    form.submit()
}

function handelPlus() {
    value++;
    input.value = value
    form.submit()
}

