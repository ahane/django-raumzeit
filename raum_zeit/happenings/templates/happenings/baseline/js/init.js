{% load staticfiles %}
/* skel-baseline v2.0.2 | (c) n33 | getskel.com | MIT licensed */

		(function($) {
			var prefix = "{% static 'happenings/baseline/css/' %}";
			skel.init({
				reset: 'full',
				breakpoints: {
					global: {
						href: prefix + 'style.css',
						containers: 1400,
						grid: { gutters: ['2em', 0] }
					},
					xlarge: {
						media: '(max-width: 1680px)',
						href: prefix + 'style-xlarge.css',
						containers: 1200
					},
					large: {
						media: '(max-width: 1280px)',
						href: prefix + 'style-large.css',
						containers: 960,
						grid: { gutters: ['1.5em', 0] },
						viewport: { scalable: false }
					},
					medium: {
						media: '(max-width: 980px)',
						href: prefix + 'style-medium.css',
						containers: '90%'
					},
					small: {
						media: '(max-width: 736px)',
						href: prefix + 'style-small.css',
						containers: '90%',
						grid: { gutters: ['1.25em', 0] }
					},
					xsmall: {
						media: '(max-width: 480px)',
						href: prefix + 'style-xsmall.css'
					}
				},
				plugins: {
					layers: {
						// infoBoxSmall: {
						// 	position: 'bottom',
						// 	width: '400',
						// 	maxWidth: '30%',
						// 	height: '150',

						// 	//animation: 'overlayY',
						// 	//hidden: true,
						// 	html: '<div id="skel-layers-fixed"><div class="paper"><p>dd</p><p></p></div></div>'
						// },
						

						streamBox: {
							position: 'bottom',
							width: '80%',
							height: '7em',
							//hidden: true,
							animation: 'overlayY',					
						},
						infoBox: {
							position: 'bottom',
							width: '80%',
							height: '7em',
							animation: 'overlayY',					
						},


						config: {
							mode: 'transform'
						},
						navPanel: {
							animation: 'pushX',
							breakpoints: 'medium',
							clickToHide: true,
							height: '100%',
							hidden: true,
							html: '<div data-action="moveElement" data-args="nav"></div>',
							orientation: 'vertical',
							position: 'top-left',
							side: 'left',
							width: 250
						},
						navButton: {
							breakpoints: 'medium',
							height: '4em',
							html: '<span class="toggle" data-action="toggleLayer" data-args="navPanel"></span>',
							position: 'top-left',
							side: 'top',
							width: '6em'
						}
					}
				}
			});

			$(function() {

				// jQuery ready stuff.

			});

		})(jQuery);