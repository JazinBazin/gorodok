'use strict';

var phoneNumber = document.getElementById('phoneNumber');
phoneNumber.addEventListener('keydown', function (e) {
    if ((e.key < '0' || e.key > '9') && !(e.key == 'Backspace' || e.key == 'Delete'))
        e.preventDefault();
});

/*
phoneNumber.value = "+_ (___) __-__-___";
var cursorPositions = [1, 4, 5, 6, 9, 10, 12, 13, 15, 16, 17];
var digitNumber = 0;

phoneNumber.addEventListener('keydown', function (e) {
    var self = this;
    function replaceCharacter(character) {
        var phone = self.value.split('');
        phone.splice(cursorPositions[digitNumber], 1, character);
        self.value = phone.join('');
    }

    e.preventDefault();
    if (e.key == 'Backspace') {
        if (digitNumber > 0) {
            --digitNumber;
            replaceCharacter('_');
        }
        return;
    }
    if (digitNumber == 11 || e.key < '0' || e.key > '9')
        return;
    replaceCharacter(e.key);
    ++digitNumber;
});
*/