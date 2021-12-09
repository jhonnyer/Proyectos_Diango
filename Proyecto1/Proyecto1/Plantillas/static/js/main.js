$(document).ready(function(){

	// Slider
	if(window.location.href.indexOf('tecnologias') > -1){
	  
	  $('.galeria').bxSlider({
	    mode: 'fade',
	    captions: false,
	    slideWidth: 1200,
	    responsive: true,
	    pager: true
	  });

	}




	// Acordeon

	if(window.location.href.indexOf('games') > -1){
		$("#acordeon").accordion();
	}


	// Reloj
	if(window.location.href.indexOf('musica') > -1){

		setInterval(function(){
				var reloj = moment().format("hh:mm:ss");
				$('#reloj').html(reloj);
		}, 1000);
		
	
	}


	

});