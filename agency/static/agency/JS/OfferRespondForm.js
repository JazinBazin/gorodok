'use strict';

var form = document.forms.OfferResponseForm;
form.addEventListener('submit', function (e) {
    if (phoneNumber.value[phoneNumber.value.length - 1] == '_') {
        e.preventDefault();
        phoneNumber.style.borderColor = 'red';
    }
})