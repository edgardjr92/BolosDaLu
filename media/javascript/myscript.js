$(function () {
    activeMenu();
});

function activeMenu() {
    deactivateMenu();
    var currentPage = $("input[name='page']").attr('value');

    $("li[name=" + currentPage + "]").addClass('active');
}

function deactivateMenu() {
    $("li.active").removeClass('active');
}