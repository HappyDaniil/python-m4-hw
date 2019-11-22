advice_url="http://sf-pyw.mosyag.in/m04/api/forecasts"
$('#main-header').click(function() {
	
	$.getJSON(advice_url, function(data) {
		paragraphs=data["prophecies"]
		set_content_in_divs(paragraphs) 
	});
	$("h1").css("background-color","lightblue")
})


function set_content_in_divs(paragraphs) {
  $.each(paragraphs, function(i, d) {
    p = $("#p-" + i)
    p.html("<p>" + d + "</p>")
  })
}
