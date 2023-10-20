const unp = {
    north: 12.13844,
    south: 12.136232,
    west: -86.221658,
    east: -86.218874,
  };
  const unpcenter = { lat: 12.137797, lng: -86.221002 };
  let infoWindow;
  let map;
  let userMarker; 
  
  function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
      center: unpcenter,
      zoom: 19,
      mapId: "663481e2c353fdbc",
    });
  
    infoWindow = new google.maps.InfoWindow();

    function addMarkerOnMap(event) {
      const pos = event.latLng;
  
      if (!userMarker) {
        userMarker = new google.maps.Marker({
          position: pos,
          map: map,
          title: "Tu ubicación",
        });
      } else {
        userMarker.setPosition(pos);
      }
  
      infoWindow.close();
      map.setCenter(pos);
    }
  
    map.addListener("click", addMarkerOnMap);
    function requestLocation() {
      if (navigator.geolocation) {
        if (window.confirm("¿Permitir acceso a tu ubicación?")) {
          navigator.geolocation.getCurrentPosition(
            (position) => {
              const pos = {
                lat: position.coords.latitude,
                lng: position.coords.longitude,
              };
  
              if (!userMarker) {
                userMarker = new google.maps.Marker({
                  position: pos,
                  map: map,
                  title: "Tu ubicación",
                });
              } else {
                userMarker.setPosition(pos);
              }
  
              infoWindow.close();
              map.setCenter(pos);
            },
            () => {
              handleLocationError(true, infoWindow, map.getCenter());
            }
          );
        }
      } else {
        handleLocationError(false, infoWindow, map.getCenter());
      }
    }
  
    requestLocation();
  
const locationButton1 = document.createElement("button");
locationButton1.textContent = "Mi Ubicación";
locationButton1.classList.add(
  "custom-map-control-button",
  "bg-gray-50",
  "hover:bg-gray-50",
  "shadow-md", 
  "text-black",
  "font-bold",
  "py-2",
  "px-4",
  "rounded",
  "mt-4",
  "mr-4",
  "ml-4", 
);

const locationButton2 = document.createElement("button");
locationButton2.textContent = "Segundo Botón";
locationButton2.classList.add(
  "custom-map-control-button",
  "bg-gray-50",
  "hover:bg-gray-50",
  "shadow-md", 
  "text-black",
  "font-bold",
  "py-2",
  "px-4",
  "rounded",
  "mt-4",
  "mr-4",
  "enviarserver", 
);
  
    map.controls[google.maps.ControlPosition.TOP_LEFT].push(locationButton1);
    map.controls[google.maps.ControlPosition.TOP_LEFT].push(locationButton2);
  

     locationButton1.addEventListener("click", () => {
        if (userMarker) {
          map.setCenter(userMarker.getPosition());
        }
      });

    locationButton2.addEventListener("click", () => {
      if (userMarker) {
        const latitud = userMarker.getPosition().lat();
        const longitud = userMarker.getPosition().lng();
        
        // Ahora puedes enviar la latitud y longitud al servidor
        console(latitud, longitud);
      }
    });
  }
  
  function handleLocationError(browserHasGeolocation, infoWindow, pos) {
    infoWindow.setPosition(pos);
    infoWindow.setContent(
      browserHasGeolocation
        ? "Error: The Geolocation service failed."
        : "Error: Your browser doesn't support geolocation."
    );
    infoWindow.open(map);
  }

  document.querySelector(".enviarserver").addEventListener("click", function() {
   
  });
  
  