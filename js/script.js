var ANIMATION_DELAY = 300;

var quotes = [];
var isFirst = true;
var curidx = 0;
function new_quote(){
	if(isFirst){
		var rand = Math.random();
		var len = quotes.length;
		curidx = Math.floor(rand*len);
		isFirst = false;
		return quotes[curidx];
	}
	if(curidx < quotes.length-1){
		curidx++;
	}
	else{
		curidx = 0;
	}
	return quotes[curidx];
}
function change_quote(){
	var q = new_quote();
	var g = $("#genquote");
	g.finish();
	g.fadeOut(ANIMATION_DELAY);
	g.queue(function(next){
		g.text(q)
		next();
	});
	g.fadeIn(ANIMATION_DELAY);
	set_tweet_text(q);
}

function tweet_text(generated) {
    var prefix;
    prefix = "Inspirotron: " + generated;
    return prefix;
}

function set_tweet_text(generated) {
    var text = tweet_text(generated);
    if (text) { 
        $('#tweet').attr("href", ("https://twitter.com/share" +
                "?url=" + window.location.href +
                "&text=" + encodeURIComponent(text)
        ));
    }
}

$(document).ready(function(e) {
    var data_url = $("body").data("namesource");
	
	$.ajax({
		url: data_url,
		type: 'GET',
		dataType: 'json',
		error: function(data) {},
		success: function(data){
			quotes = data.quotes;
			change_quote();
		}
		});
	
	$("#myButton").click(function(e) {
        change_quote();
    });
});