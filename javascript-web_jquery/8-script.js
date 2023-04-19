$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    const movies = data.results;
    for (let i = 0; i < movies.length; ++i) {
      const title = `<li>${movies[i].title}</li>`;
      $("UL#list_movies").append(title);
  }
});
