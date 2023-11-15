let infomarker = [];
const modal = document.getElementById("miModal");

function modalxd() {
  modal.classList.remove("hidden");
}

const unp = {
  north: 13.663107128422704,
  south: 11.244178967486436,
  west: -87.95878829611368,
  east: -83.74827831043596,
};
const unpcenter = { lat: 12.137797, lng: -86.221002 };
let infoWindow;
let map;
let userMarker;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: unpcenter,
    restriction: {
      latLngBounds: unp,
      strictBounds: false,
    },
    zoom: 5,
    mapId: "663481e2c353fdbc",
  });
  const infomarker1 = new google.maps.InfoWindow({
    content:
      '<div id="content">' +
      '<div id="bodyContent">' +
      ' <p> <a onclick="modalxd()" class="url" type="button"> <b>Fruta Polar</b> </a> </p>' +
      "</div>" +
      "</div>",
  });
  infomarker.push(infomarker1);
  const infomarker2 = new google.maps.InfoWindow({
    content:
      '<div id="content">' +
      '<div id="bodyContent">' +
      ' <p> <a href="/sitio/1" class="url"> <b>Fruta Polar</b> </a> </p>' +
      "</div>" +
      "</div>",
  });

  window.addEventListener("load", function () {
    const infomarker1 = new google.maps.InfoWindow({
      content:
        '<div id="content">' +
        '<div id="bodyContent">' +
        ' <p> <a href="/sitio/1" class="url"> <b>Fruta Polar</b> </a> </p>' +
        "</div>" +
        "</div>",
    });
    infomarker.push(infomarker1);
  });

  //marcador
  const marker1 = new google.maps.Marker({
    position: { lat: 12.851501799791537, lng: -86.10779737099169 },
    map,
    title: "Fruta Polar",
    animation: google.maps.Animation.DROP,
  });

  //animation
  marker1.addListener("click", () => {
    toggleBounce(1);
  });
  marker1.addListener("click", toggleBounce);

  //contenido del marcador
  marker1.addListener("click", () => {
    for (let i = 1; i < infomarker.length; i++) {
      eval("infomarker" + i + ".close();");
    }
    infomarker1.open({
      anchor: marker1,
      map,
      shouldFocus: false,
    });
  });
  //-----------
  //marcador2
  const marker2 = new google.maps.Marker({
    position: { lat: 12.932908048600105, lng: -85.88639493891249 },
    map,
    title: "Fruta Polar",
    animation: google.maps.Animation.DROP,
  });

  //animation
  marker2.addListener("click", () => {
    toggleBounce(2);
  });
  marker2.addListener("click", toggleBounce);

  //contenido del marcador
  marker2.addListener("click", () => {
    for (let i = 1; i < infomarker.length; i++) {
      eval("infomarker" + i + ".close();");
    }
    infomarker2.open({
      anchor: marker2,
      map,
      shouldFocus: false,
    });
  });
  //-------
  //marcador3
  const marker3 = new google.maps.Marker({
    position: { lat: 12.418938727741981, lng: -86.94812073336354 },
    map,
    title: "Fruta Polar",
    animation: google.maps.Animation.DROP,
  });

  //animation
  marker3.addListener("click", () => {
    toggleBounce(3);
  });
  marker3.addListener("click", toggleBounce);

  //contenido del marcador
  marker3.addListener("click", () => {
    for (let i = 1; i < infomarker.length; i++) {
      eval("infomarker" + i + ".close();");
    }
    infomarker3.open({
      anchor: marker2,
      map,
      shouldFocus: false,
    });
  });
  //-------
  //marcador4
  const marker4 = new google.maps.Marker({
    position: { lat: 12.386748953795879, lng: -85.53088453819333 },
    map,
    title: "Fruta Polar",
    animation: google.maps.Animation.DROP,
  });

  //animation
  marker4.addListener("click", () => {
    toggleBounce(4);
  });
  marker4.addListener("click", toggleBounce);

  //contenido del marcador
  marker4.addListener("click", () => {
    for (let i = 1; i < infomarker.length; i++) {
      eval("infomarker" + i + ".close();");
    }
    infomarker3.open({
      anchor: marker2,
      map,
      shouldFocus: false,
    });
  });
  //marcador5
  const marker5 = new google.maps.Marker({
    position: { lat: 11.981358016164375, lng: -84.85247884011766 },
    map,
    title: "Fruta Polar",
    animation: google.maps.Animation.DROP,
  });

  //animation
  marker5.addListener("click", () => {
    toggleBounce(5);
  });
  marker5.addListener("click", toggleBounce);

  //contenido del marcador
  marker5.addListener("click", () => {
    for (let i = 1; i < infomarker.length; i++) {
      eval("infomarker" + i + ".close();");
    }
    infomarker5.open({
      anchor: marker5,
      map,
      shouldFocus: false,
    });
  });

  //marcador6
  const marker6 = new google.maps.Marker({
    position: { lat: 11.437955820274741, lng: -85.82335920908731 },
    map,
    title: "Fruta Polar",
    animation: google.maps.Animation.DROP,
  });

  //animation
  marker6.addListener("click", () => {
    toggleBounce(6);
  });
  marker6.addListener("click", toggleBounce);

  //contenido del marcador
  marker6.addListener("click", () => {
    for (let i = 1; i < infomarker.length; i++) {
      eval("infomarker" + i + ".close();");
    }
    infomarker6.open({
      anchor: marker6,
      map,
      shouldFocus: false,
    });
  });

  //marcador6
  const marker7 = new google.maps.Marker({
    position: { lat: 12.95202411539313, lng: -85.19713858429218 },
    map,
    title: "Fruta Polar",
    animation: google.maps.Animation.DROP,
  });

  //animation
  marker7.addListener("click", () => {
    toggleBounce(7);
  });
  marker7.addListener("click", toggleBounce);

  //contenido del marcador
  marker7.addListener("click", () => {
    for (let i = 1; i < infomarker.length; i++) {
      eval("infomarker" + i + ".close();");
    }
    infomarker7.open({
      anchor: marker7,
      map,
      shouldFocus: false,
    });
  });

  //marcador8
  const marker8 = new google.maps.Marker({
    position: { lat: 11.214429320876844, lng: -84.66704826256752 },
    map,
    title: "Fruta Polar",
    animation: google.maps.Animation.DROP,
  });

  //animation
  marker8.addListener("click", () => {
    toggleBounce(8);
  });
  marker8.addListener("click", toggleBounce);

  //contenido del marcador
  marker8.addListener("click", () => {
    for (let i = 1; i < infomarker.length; i++) {
      eval("infomarker" + i + ".close();");
    }
    infomarker8.open({
      anchor: marker8,
      map,
      shouldFocus: false,
    });
  });

  //marcador9
  const marker9 = new google.maps.Marker({
    position: { lat: 13.34785830892888, lng: -85.37841300170432 },
    map,
    title: "Fruta Polar",
    animation: google.maps.Animation.DROP,
  });

  //animation
  marker9.addListener("click", () => {
    toggleBounce(9);
  });
  marker9.addListener("click", toggleBounce);

  //contenido del marcador
  marker9.addListener("click", () => {
    for (let i = 1; i < infomarker.length; i++) {
      eval("infomarker" + i + ".close();");
    }
    infomarker9.open({
      anchor: marker9,
      map,
      shouldFocus: false,
    });
  });

  //marcador10
  const marker10 = new google.maps.Marker({
    position: { lat: 13.19281030552884, lng: -84.96367915389288 },
    map,
    title: "Fruta Polar",
    animation: google.maps.Animation.DROP,
  });

  //animation
  marker10.addListener("click", () => {
    toggleBounce(9);
  });
  marker9.addListener("click", toggleBounce);

  //contenido del marcador
  marker10.addListener("click", () => {
    for (let i = 1; i < infomarker.length; i++) {
      eval("infomarker" + i + ".close();");
    }
    infomarker10.open({
      anchor: marker9,
      map,
      shouldFocus: false,
    });
  });

  //marcador11
  const marker11 = new google.maps.Marker({
    position: { lat: 12.756548482361596, lng: -85.62835194284297 },
    map,
    title: "Fruta Polar",
    animation: google.maps.Animation.DROP,
  });

  //animation
  marker11.addListener("click", () => {
    toggleBounce(11);
  });
  marker11.addListener("click", toggleBounce);

  //contenido del marcador
  marker11.addListener("click", () => {
    for (let i = 1; i < infomarker.length; i++) {
      eval("infomarker" + i + ".close();");
    }
    infomarker10.open({
      anchor: marker9,
      map,
      shouldFocus: false,
    });
  });

  function toggleBounce(x) {
    //animacion de los
    if (isNaN(x) == false) {
      for (let i = 1; i < 12; i++) {
        eval("marker" + i + ".setAnimation(null);");
      }

      eval(
        "if (marker" +
          x +
          ".getAnimation() !== null) {" +
          "marker" +
          x +
          ".setAnimation(null);" +
          "} else {" +
          "marker" +
          x +
          ".setAnimation(google.maps.Animation.BOUNCE);" +
          "}"
      );
    }
    x = 0;
  }
}

//marcador2

//,
//,
//,
//,
//,
//,
//,
//,
//,
//,
//,
//12.263177209156106, -86.07604479306596

//animation
