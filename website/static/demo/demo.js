/*
Theme Name: Nantria
Description: Multi-Purpose HTML Site Template
Author: erilisdesign
Theme URI: https://preview.erilisdesign.com/html/nantria/
Author URI: https://themeforest.net/user/erilisdesign
Version: 1.0
*/

(function($) {
	"use strict";

	// Refresh Waypoints
	var refreshWaypoints_timeout;

	function refreshWaypoints() {
		clearTimeout(refreshWaypoints_timeout);
		refreshWaypoints_timeout = setTimeout(function() {
			Waypoint.refreshAll();
		}, 1000);
	}
	
	// Portfolio
	function initIntroMasonryLayout() {
		if ($('.isotope-container').length) {
			var $isotopeContainer = $('.isotope-container');
			var $columnWidth = $isotopeContainer.data('column-width');
			
			if($columnWidth == null){
				var $columnWidth = '.isotope-item';
			}
			
			$isotopeContainer.isotope({
				filter: '*',
				animationEngine: 'best-available',
				resizable: false,
				itemSelector : '.isotope-item',
				masonry: {
					columnWidth: $columnWidth
				},
				animationOptions: {
					duration: 750,
					easing: 'linear',
					queue: false
				}
			}, refreshWaypoints());
		}

		$('.demo-filter ul a').on('click', function() {
			var selector = $(this).attr('data-filter');
			$isotopeContainer.isotope({ filter: selector }, refreshWaypoints());
			$('.demo-filter ul a').removeClass('active');
			$(this).addClass('active');
			return false;
		});

	}
	
	// DOCUMENT.READY FUNCTION
	jQuery(document).ready(function($) {
		initIntroMasonryLayout();
	});

})(jQuery);