$(function () {
    var selectField = $('#id_product_type'),
        clothingStock = $('.field-stock_xs, .field-stock_s, .field-stock_m, .field-stock_l, .field-stock_xl, .field-stock_xxl, .field-stock_xxxl');
    stock = $('.field-stock');

    function toggleVerified(value) {
        if (value == 1) {
            clothingStock.show();
            stock.hide();
        } else {
            clothingStock.hide();
            stock.show();
        }
    }

    // show/hide on load based on pervious value of selectField
    toggleVerified(selectField.val());

    // show/hide on change
    selectField.change(function () {
        toggleVerified($(this).val());
    });
});
