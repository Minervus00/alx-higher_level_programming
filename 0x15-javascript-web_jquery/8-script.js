const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$.get(url, function(data, textStatus) {
  data.results.forEach(element => {
    const newTag = "<li>"+ element.title + "</li>";
    $("UL#list_movies").append(newTag);
  });
});
