$('document').ready(function () {
  const lng = document.getElementById('language_code').value;
  const url = 'https://fourtonfish.com/hellosalut/?lang=' + lng;

  $(document).keypress(function(e) {
    var keycode = (e.keyCode ? e.keyCode : e.which);
    if (keycode == '13') {
      $.get(url, function (data) {
        $('DIV#hello').text(data.hello);
      });
    }
  });

  $('INPUT#btn_translate').click(function () {
    $.get(url, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
