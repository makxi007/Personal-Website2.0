
var nav = document.getElementById('navbar-fixed-top');

window.onscroll = function (){
	"use strict";
	if (document.body.scrollTop >= 200 || document.documentElement.scrollTop >= 200){
		nav.classList.add("nav-colored");
		nav.classList.remove("nav-transparent");
	}
	else{
		nav.classList.add("nav-transparent");
		nav.classList.remove("nav-colored");
	}
}
