
    // gogle maps funcion 
    function iniciarMap(){
      var coord = {lat:-40.15313425841268, lng: -71.35092948261295};
      var map = new google.maps.Map(document.getElementById('map'),{
        zoom: 19,
        center: coord
      });
      var marker = new google.maps.Marker({
        position: coord,
        map: map
      });
  }

  
// Agrega un evento de clic al elemento que activa el menú desplegable

function showLoader() {
    // Mostrar la nueva capa de superposición y el loader
    document.getElementById('overlayLoader').style.display = 'block';
    document.getElementById('loader').style.display = 'flex';
}

// Agregar evento click a todos los enlaces con clase 'one' y 'two'
document.querySelectorAll('.one, .two').forEach(item => {
    item.addEventListener('click', function() {
        // Mostrar el loader al hacer clic en un enlace
        showLoader();
    });
});

// Ocultar el loader y la nueva capa de superposición cuando se ha cargado completamente una nueva página
window.addEventListener('load', function() {
    document.getElementById('overlayLoader').style.display = 'none';
    document.getElementById('loader').style.display = 'none';
});





//funcion para mostrar o esconder secciones en la pagina de programas
var currentSection = 0;

function showSection(sectionNumber) {
    var allSections = document.querySelectorAll('.section');
    allSections.forEach(function(section) {
        section.classList.remove('active');
    });

    var selectedSection = document.getElementById('section' + sectionNumber);
    selectedSection.classList.add('active');
    currentSection = sectionNumber;
}

function previousSection() {
  var allSections = document.querySelectorAll('.section');
  allSections.forEach(function(section) {
      section.classList.remove('active');
  });

  var firstSection = document.getElementById('section0');
  firstSection.classList.add('active');
  currentSection = 0;
}



//calendario
