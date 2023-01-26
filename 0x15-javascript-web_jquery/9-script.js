const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

$(function () {
  $.get(url, function (data, textStatus) {
    $('DIV#hello').text(data.hello);
  });
});
