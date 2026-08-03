fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    const list = document.querySelector('#list_movies');
    for (const movie of data.results) {
      const item = document.createElement('li');
      item.textContent = movie.title;
      list.appendChild(item);
    }
  });
