(function($, document, window){

	$(document).ready(function(){

		// Cloning main navigation for mobile menu
		$(".mobile-navigation").append($(".main-navigation .menu").clone());

		// Mobile menu toggle
		$(".menu-toggle").click(function(){
			$(".mobile-navigation").slideToggle();
		});

		// Format dates in forecast headers
		formatForecastDates();

		var map = $(".map");
		var latitude = map.data("latitude");
		var longitude = map.data("longitude");
		if( map.length ){

			map.gmap3({
				map:{
					options:{
						center: [latitude,longitude],
						zoom: 15,
						scrollwheel: false
					}
				},
				marker:{
					latLng: [latitude,longitude],
				}
			});

		}

		// Add hover effect to forecast items
		$(".forecast").hover(function(){
			$(this).addClass("forecast-hover");
		}, function(){
			$(this).removeClass("forecast-hover");
		});
	});

	// Function to format dates in a more user-friendly way
	function formatForecastDates() {
		$(".forecast-header .day").each(function() {
			var dateText = $(this).text();
			if (dateText && dateText.includes("-")) {
				try {
					// Parse the date string (format: YYYY-MM-DD HH:MM:SS)
					var dateParts = dateText.split(" ");
					if (dateParts.length >= 2) {
						var date = new Date(dateText);
						var options = { weekday: 'short', month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' };
						var formattedDate = date.toLocaleDateString('en-US', options);
						$(this).text(formattedDate);
					}
				} catch (e) {
					console.log("Error formatting date: " + e.message);
				}
			}
		});
	}

	// Add a function to refresh weather data
	function refreshWeather() {
		var city = $(".location").text().split(",")[0];
		if (city) {
			$("form.find-location input[name='city']").val(city);
			$("form.find-location").submit();
		}
	}

	// Add a refresh button if it doesn't exist
	function addRefreshButton() {
		if ($(".refresh-weather").length === 0 && $(".forecast-container").length > 0) {
			var refreshBtn = $('<button class="refresh-weather button">Refresh Weather</button>');
			refreshBtn.click(function(e) {
				e.preventDefault();
				refreshWeather();
			});
			$(".forecast-container").before(refreshBtn);
		}
	}

	$(window).load(function(){
		// Format dates after window loads
		formatForecastDates();

		// Add refresh button
		addRefreshButton();
	});

})(jQuery, document, window);