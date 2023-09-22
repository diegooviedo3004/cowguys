const unp = {
    north: 12.13844,
    south: 12.136232,
    west: -86.221658,
    east: -86.218874,
  };
  const unpcenter = { lat: 12.137797, lng: -86.221002 };
  let infoWindow;
  let map;
  let userMarker; // Variable para almacenar el marcador del usuario
  
  function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
      center: unpcenter,
      zoom: 19,
      mapId: "663481e2c353fdbc",
    });
  
    infoWindow = new google.maps.InfoWindow();
  
    // Función para agregar un marcador en el mapa cuando el usuario hace clic
    function addMarkerOnMap(event) {
      const pos = event.latLng;
  
      // Crear un nuevo marcador personalizado para la ubicación del usuario
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
  
    // Agregar un evento de clic al mapa
    map.addListener("click", addMarkerOnMap);
  
    // Función para solicitar la ubicación del usuario
    function requestLocation() {
      if (navigator.geolocation) {
        if (window.confirm("¿Permitir acceso a tu ubicación?")) {
          navigator.geolocation.getCurrentPosition(
            (position) => {
              const pos = {
                lat: position.coords.latitude,
                lng: position.coords.longitude,
              };
  
              // Crear un marcador personalizado para la ubicación del usuario
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
        // Browser doesn't support Geolocation
        handleLocationError(false, infoWindow, map.getCenter());
      }
    }
  
    // Solicitar la ubicación cuando se inicia el mapa
    requestLocation();
  
    // Crear el botón en la esquina superior izquierda del mapa
    const locationButton = document.createElement("button");
    locationButton.textContent = "Mi Ubicación";
    locationButton.classList.add("custom-map-control-button");
    map.controls[google.maps.ControlPosition.TOP_LEFT].push(locationButton);
  
    // Agregar un evento de clic al botón para centrar el mapa en la ubicación del usuario
    locationButton.addEventListener("click", () => {
      if (userMarker) {
        map.setCenter(userMarker.getPosition());
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
  