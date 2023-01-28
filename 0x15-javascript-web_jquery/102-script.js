$('document').ready(function () {
  $('INPUT#btn_translate').click(function () {
    const lng = document.getElementById('language_code').value;
    const url = 'https://fourtonfish.com/hellosalut/?lang=' + lng;
    $.get(url, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
