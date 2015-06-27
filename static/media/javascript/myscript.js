$(function () {
    deactivateMenu();
    activeMenu();

    if (getCurrentPage() == 'depoimentos' || getCurrentPage() == 'galeria') {
        activePagination();
    }
});


function activePagination() {
    var page = getUrlParameter('page');

    if (page) {
        $('.pagination-a li a[name=' + page + ']').parent().addClass('active');
    } else {
        $('.pagination-a li').first().addClass('active');
    }
}

function getUrlParameter(sParam) {
    var sPageURL = window.location.search.substring(1);
    var sURLVariables = sPageURL.split('&');
    for (var i = 0; i < sURLVariables.length; i++) {
        var sParameterName = sURLVariables[i].split('=');
        if (sParameterName[0] == sParam) {
            return sParameterName[1];
        }
    }
}

function validFile(valueFile) {
    switch (valueFile.substring(valueFile.lastIndexOf('.') + 1).toLowerCase()) {
        case 'jpg':
        case 'png':
            closeAlert();
            break
        default :
            cleanInputFile();
            showAlert('warning', 'Formato de arquivo inválido.')
            break
    }
}


$("#form_testimonials").submit(function (event) {
    addDepoimento($(this));
    event.preventDefault();

});


$("#form_contact").submit(function () {
    $('#send').attr('disabled', true);
});


function addDepoimento(self) {
    var data = self.serialize();
    var url = self.attr('action');
    var method = self.attr('method').toUpperCase();

    requestAjax(url, "json", method, data, addDepoimentoAjaxSucess, addDepoimentoAjaxComplete, null);
}

function addDepoimentoAjaxSucess(data) {
    if (data != '' && data == 'success') {
        showAlert('success', 'Seu depoimento foi criado com sucesso, logo será aprovado.');
    } else {
        showAlert('error', 'Falha de acesso a dados, tente novamente mais tarde.');
    }
}

function addDepoimentoAjaxComplete() {
    clearForm('#form_testimonials');
    cleanInputFile();
}


function clearForm(idForm) {
    $(idForm).find("input[type=text],input[type=email], textarea").val("");
}

function showAlert(type, message) {
    $('#alert_ajax').addClass(type);
    $('#alert_ajax p').html(message);
    $('#alert_ajax').fadeIn();

}

$('.alert').click(function () {
    closeAlert();
});

function closeAlert() {
    $('.alert').fadeOut();
}

$("#arquivo").change(function () {
    $(this).prev().html($(this).val());
    validFile($(this).val())
});

$('#clean').click(function () {
    cleanInputFile();
});


function cleanInputFile() {
    var valueEmpty = 'Selecione uma foto (JPEG ou PNG):'
    $('#arquivo').val('');
    $('#arquivo').prev().html(valueEmpty);
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


//realiza uma requisicao ajax
function requestAjax(url, dataType, method, data, functionSucess, functionComplete, functionBeforeSend) {
    $.ajax({
        url: url,
        dataType: dataType,
        type: method,
        data: data,
        success: function (result) {
            functionSucess(result);
        },
        beforeSend: function () {
            if (functionBeforeSend) {
                functionBeforeSend();
            }
        },
        complete: function () {
            functionComplete();
        }
    });
}