fetch('')   //Add the url of your API
  .then(response => {console.log(response);
        return response.json()
    })
  .then(data => {
          console.log(data);
          document.getElementById('').  //Add HTML element ID
          innerHTML=data;
        })

  .catch(error => {
      console.log("error!")
      console.error(error)
  })
    
