//Some stuff.
var script = document.createElement('script');
script.src = 'http://code.jquery.com/jquery-3.2.1.min.js';
document.getElementsByTagName('head')[0].appendChild(script);

$(document).ready(function () {
  const para = document.querySelector('header');
  para.style.color = '#FF0000';
});
