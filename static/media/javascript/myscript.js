$(function () {
    backEventListener();
    deactivateMenu();
    activeMenu();
    activeFirstPagination();
//    backToAlbums();
});


$('.page').click(function (event) {
    event.preventDefault();
    var self = $(this);
    var url = self.attr('href');
    activeCurrentPagination(self);

    requestAjax(url, 'json', 'GET', null, paginationAjaxSucess, paginationAjaxComplete);
});

$('.btn_page').click(function (event) {
    event.preventDefault();
    var self = $(this);
    var url = self.attr('href');
    var pageCurrent = url.split("/")[2]
    activeCurrentPagination($('a[name=' + pageCurrent + ']'));

    requestAjax(url, 'json', 'GET', null, paginationAjaxSucess, paginationAjaxComplete);
});


function activeCurrentPagination(self) {
    $('.pagination-a li').removeClass('active');
    self.parent().addClass('active');
}

function activeFirstPagination() {
    $('.pagination-a li:eq(1)').first().addClass('active');
}

function paginationAjaxSucess(data) {
    $('#depoimentos li').remove();
    if (data != '') {
        $.each(data, function (key, value) {
            $("#depoimentos").append(generateHtmlPagination(value));
        });
    }

    createButtonsPagination();
}

function paginationAjaxComplete() {

}

function createButtonsPagination() {
    var pageCurrent = $('.pagination-a li.active');

    if(hasPrev()){
        $('#prev').children().attr('href', pageCurrent.prev().children().attr('href'));
        $('#prev').css('display', 'inline');
    }else{
        $('#prev').hide();
    }

    if(hasNext()){
        $('#next').children().attr('href', pageCurrent.next().children().attr('href'));
        $('#next').show();
    }else{
        $('#next').hide();
    }
}

function hasNext() {
    var pageCurrent = $('.pagination-a li.active');
    return pageCurrent.next().children().html() != 'Próxima' && pageCurrent.next().children().html() != null;
}


function hasPrev() {
    var pageCurrent = $('.pagination-a li.active');
    return pageCurrent.children().html() != '1'
}

function generateHtmlPagination(value) {
    var html = '<li><span>' + value.fields.nome + ':</span> ' + value.fields.descricao + '</li>'

    return html
}

$("#form_testimonials").submit(function (event) {
    addDepoimento($(this));
    event.preventDefault();

});

function addDepoimento(self) {
    var data = self.serialize();
    var url = self.attr('action');
    var method = self.attr('method').toUpperCase();

    requestAjax(url, "json", method, data, addDepoimentoAjaxSucess, addDepoimentoAjaxComplete);
}


function addDepoimentoAjaxSucess(data) {
    if (data != '' && data == 'success') {
        showAlert('success', 'Seu depoimento foi criado com sucesso, logo será aprovado.');
    } else {
        showAlert('error', 'Falha de acesso a dados.');
    }
}

function addDepoimentoAjaxComplete() {
    clearForm('#form_testimonials');
}


function clearForm(idForm) {
    $(idForm).find("input[type=text],input[type=email], textarea").val("");
}

function showAlert(type, message) {
    $('#alert').addClass('alert-' + type);
    $('#alert p').html(message);
    $('#alert').fadeIn();

    setTimeout(closeAlert, 10000);
}

$(function () {
    $('#alert').click(function () {
        closeAlert();
    });
});

function closeAlert() {
    $('#alert').fadeOut();
}

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
    requestAjax(url, "json", "GET", null, getFotosAjaxSucess, getFotosAjaxComplete);
}

function getFotosAjaxSucess(data) {
    $("#fotos > li").remove();
    if (data != '') {
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
        '" rel="lightbox[ultimas-fotos]"' + ' title="' + value.fields.legenda + '">' +
        '<span class="wrapper">' +
        '<img src="/static/media/' + value.fields.imagem_min + '"' +
        ' alt="' + value.fields.legenda + '" width="252"  height="161">' +
        '<div class="shade-a"></div>' +
        '<div class="shade-b"></div>' +
        '<div class="shade-c"></div>' +
        '</span>' +
        value.fields.legenda + '</a></li>'

    return html
}

//realiza uma requisicao ajax
function requestAjax(url, dataType, method, data, functionSucess, functionComplete) {
    $.ajax({
        url: url,
        dataType: dataType,
        type: method,
        data: data,
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