

$(document).ready(function() {

	$("#styleA").on("click", function() {
		$("link[href='styleB.css']").remove();
		$('head').append('<link rel="stylesheet" type="text/css" href="styleA.css">');
	});	

	$("#styleB").on("click", function() {
		$("link[href='styleA.css']").remove();
		$('head').append('<link rel="stylesheet" type="text/css" href="styleB.css">');
	});	

});