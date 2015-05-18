$(function () {
    deactivateMenu();
    activeMenu();
    backAlbuns();
    getBackEvent();
});

$('.link-gallery').click(function () {
    closeAlbuns();
    showPictures();
});

$('#backAlbuns').click(function(event){
   backAlbuns();
   event.preventDefault();
});

function getBackEvent() {
    if (window.history && window.history.pushState) {

        window.history.pushState('forward', null);

        $(window).on('popstate', function (event) {
            if (getCurrentPage() == 'galeria' && isHidden('#albuns')) {
                returnForGaleria();
                disableBack();
            }
        });

    }
}

function backAlbuns(){
    closePictures();
    showAlbuns();
}

function returnForGaleria() {
    closePictures();
    showAlbuns();
}

function disableBack(){
    window.history.forward();
}

function showAlbuns() {
    $('#albuns').show();
}

function closeAlbuns() {
    $('#albuns').hide();
}

function showPictures() {
    $('#pictures').show();
}

function closePictures() {
    $('#pictures').hide();
}

function activeMenu() {
    $("li[name=" + getCurrentPage() + "]").addClass('active');
}

function deactivateMenu() {
    $("li.active").removeClass('active');
}

function getCurrentPage() {
    var currentPage = $("input[name='page']").attr('value');

    return currentPage;
}

function isHidden(id) {
    var isHidden = false;
    if ($(id).css('display') == 'none') {
        isHidden = true;
    }
    return isHidden;
}