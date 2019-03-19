'use strict';

var requestForm = document.forms.ApplicationForm;
requestForm.addEventListener('submit', function(e) {
    var userPhone = document.getElementById('phoneNumber');
    if (userPhone.value[userPhone.value.length - 1] == '_') {
        e.preventDefault();
        userPhone.style.borderColor = 'red';
    }
})

var purchaseOrRentSelect = requestForm.elements.purchase_or_rent;
var serviceTypeSelect = requestForm.elements.service_type;

purchaseOrRentSelect.addEventListener("change", function () {
    var rentPeriod = document.getElementById("rentPeriodFilter");
    var selectedValue = this.options[this.selectedIndex].value;
    rentPeriod.hidden = (selectedValue == "Аренда" ? false : true);
});

serviceTypeSelect.addEventListener("change", function () {
    var selectedValue = this.options[this.selectedIndex].value;
    var roomCountFilter = document.getElementById("roomCountFilter");
    var floorNumberFilter = document.getElementById("floorNumberFilter");
    var floorCountFilter = document.getElementById("floorCountFilter")

    function showServiceFilters(roomCount, floorNumber, floorCount) {
        roomCountFilter.hidden = !roomCount;
        floorNumberFilter.hidden = !floorNumber;
        floorCountFilter.hidden = !floorCount;
    };

    if (selectedValue == "Квартира")
        showServiceFilters(true, true, false);
    else if (selectedValue == "Дом/Дача")
        showServiceFilters(true, false, true);
    else if (selectedValue == "Земля")
        showServiceFilters(false, false, false);
    else if (selectedValue == "Гараж")
        showServiceFilters(false, false, false);
});
