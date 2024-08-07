const $ = window.$;
function getHello () {
  $.ajax({
    type: 'GET',
    data: {
      lang: $('#language_code').val()
    },
    url: 'https://fourtonfish.com/hellosalut/',
    success: function (data) {
      $('#hello').text(data.hello);
    }
  });
}

$(document).ready(function () {
  $('#btn_translate').click(function () {
    getHello();
  });

  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      getHello();
    }
  });
});
