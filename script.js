fetch('http://ec2-65-2-111-197.ap-south-1.compute.amazonaws.com:8888/')
  .then(response => {console.log(response);
        return response.json()
    })
  .then(data => {
          console.log(data);
          document.getElementById('loading').
          innerHTML=data[0].name;
          document.getElementById('Linux').
          innerHTML=data[0].last;

        })

  .catch(error => {
      console.log("error!")
      console.error(error)
  })
