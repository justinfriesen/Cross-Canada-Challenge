function initMap(teamId) {
  const map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 52.825, lng: -95.217},
    zoom: 4,
    mapId: '6a3c4395688dbd65'
  });
  
  fetch(`/maps/${teamId}`, {method: "POST"})
  .then((res) => res.json()) // wait for response from endpoint, capture response in res variable and then we are returning res.json
      .then((data) => {
        console.log(data["locations"])

        if (data["amount"] === 0){
          new google.maps.Marker({
            position: { lat: 47.561068, lng: -52.712285 },
            map,
          });
        }
        else {
          for (let i = 0; i < data["locations"].length; i++) {
            const location = data["locations"][i];
            
            if (data["amount"] >location[3]){
              new google.maps.Marker({
                position: { lat: location[1], lng: location[2] },
                map,
              });
              break;
            }
        }
        }
          
      }) //ES6 JS functions. data is returned frim res.json. We can then take this and log it to the the console. 
      .catch((e) => alert("Could not like post."));
}

document.onload = initMap(1)



