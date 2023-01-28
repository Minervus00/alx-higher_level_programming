$('document').ready(function () {
  const lng = document.getElementById('language_code').value;
  const url = 'https://fourtonfish.com/hellosalut/?lang=' + lng;

  var input = document.getElementById("language_code");

  // Execute a function when the user presses a key on the keyboard
  input.addEventListener("keypress", function(event) {
    // If the user presses the "Enter" key on the keyboard
    if (event.key === "Enter") {
      // Trigger the button element with a click
      document.getElementById("btn_translate").click();
    }
  });

  // $(document).keypress(function(e) {
  //   var keycode = (e.keyCode ? e.keyCode : e.which);
  //   if (keycode == '13') {
  //     $.get(url, function (data) {
  //       $('DIV#hello').text(data.hello);
  //     });
  //   }
  // });

  $('INPUT#btn_translate').click(function () {
    $.get(url, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
