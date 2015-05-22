$(function () {
    backEventListener();
    deactivateMenu();
    activeMenu();
    backToAlbums();
});


$("#arquivo").change(function () {
    $(this).prev().html($(this).val());
});

$('#clean').click(function(){
    var valueEmpty = 'Selecione uma foto:'
    $('#arquivo').prev().html(valueEmpty);
});


$('.link-gallery').click(function () {
    closeAlbums();
    showPictures();
});

$('#backAlbums').click(function (event) {
    backToAlbums();
    event.preventDefault();
});

// ouvinte quando ação de VOLTAR do browser for realizada
function backEventListener() {
    if (window.history && window.history.pushState) {
        window.history.pushState('forward', null);

        $(window).on('popstate', function () {
            if (getCurrentPage() == 'galeria' && isHidden('#albums')) {
                backToAlbums();
                disableBack();
            }
        });

    }
}

// retorna para os albuns da galeria
function backToAlbums() {
    closePictures();
    showAlbums();
}

// desabilita a ação VOLTAR do navegador
function disableBack() {
    window.history.forward();
}

// abre os albuns da galeria
function showAlbums() {
    $('#albums').show();
}

// fecha os albuns da galeria
function closeAlbums() {
    $('#albums').hide();
}

// abre as fotos da galeria
function showPictures() {
    $('#pictures').show();
}

// fecha as fotos da galeria
function closePictures() {
    $('#pictures').hide();
}

// ativa o menu da pagina
function activeMenu() {
    $("li[name=" + getCurrentPage() + "]").addClass('active');
}

// desativa o menu da pagina
function deactivateMenu() {
    $("li.active").removeClass('active');
}

// retorna a pagina atual
function getCurrentPage() {
    var currentPage = $("input[name='page']").attr('value');

    return currentPage;
}

// verifica se o elemento esta oculto
function isHidden(id) {
    var isHidden = false;
    if ($(id).css('display') == 'none') {
        isHidden = true;
    }
    return isHidden;
}
