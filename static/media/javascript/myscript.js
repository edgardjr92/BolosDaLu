$(function () {
    backEventListener();
    deactivateMenu();
    activeMenu();
//    backToAlbums();
});

$("#arquivo").change(function () {
    $(this).prev().html($(this).val());
});

$('#clean').click(function () {
    var valueEmpty = 'Selecione uma foto:'
    $('#arquivo').prev().html(valueEmpty);
});


$('.link-gallery').click(function (event) {
    getFotos($(this));
    event.preventDefault();
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

function getFotos(self) {
    var url = self.attr("atr-url");
    requestAjax(url, "json", "GET", getFotosAjaxSucess, getFotosAjaxComplete);
}

function getFotosAjaxSucess(data) {
    if (data != '') {
        $("#fotos > li").remove();
        $.each(data, function (key, value) {
            $("#fotos").append(generateHtmlFotos(value));
        });
    }
}

//exibe as fotos do album
function getFotosAjaxComplete() {
    closeAlbums();
    showPictures();
}

//gera o html para criacao das fotos da galeria
function generateHtmlFotos(value) {
    var html = '<li>' + '<a href="/static/media/' + value.fields.imagem +
        '" rel="lightbox[ultimas-fotos]"' + ' title="' + value.fields.legenda + '">'+
        '<span class="wrapper">' +
        '<img src="/static/media/'+ value.fields.imagem_min +'"' +
        ' alt="' + value.fields.legenda + '" width="252"  height="161">' +
        '<div class="shade-a"></div>' +
        '<div class="shade-b"></div>' +
        '<div class="shade-c"></div>' +
        '</span>' +
        value.fields.legenda + '</a></li>'

    return html
}

//realiza uma requisicao ajax
function requestAjax(url, dataType, type, functionSucess, functionComplete) {
    $.ajax({
        url: url,
        dataType: dataType,
        type: type,
        success: function (result) {
            functionSucess(result);
        },
        beforeSend: function () {
//            onAjaxBeforeSend();
        },
        complete: function () {
            functionComplete();
        }
    });
}