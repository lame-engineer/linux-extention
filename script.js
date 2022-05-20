fetch('')   //Add the url of your API
  .then(response => {console.log(response);
        return response.json()
    })
  .then(data => {
          console.log(data);
          document.getElementById('').  //Add HTML element ID
          innerHTML=data[0].name;
          document.getElementById('').  //Add HTML element ID
          innerHTML=data[0].last;

        })

  .catch(error => {
      console.log("error!")
      console.error(error)
  })
    