'use strict';

/*
-
-
THIS FILE COMPUTES THE TIME ON THE MARKET FOR A SPECIFIC GROUP OF PROPERTIES
BASED ON A SET OF A FEATURES OBTAINED FROM THE DATA AND DISPLAYS A BAR CHART
OF DIFFERENT PROPERTIES WITH EACH PROPERTY REPRESENTING A COLUMN.
-
-
*/

// IIFE
(function () {


//Missing Data Connection

	// Init data
	let data = [];

	// Fetch json data

		createVis();
	}).catch((err) => {

		console.error(err);
	});


	//Compute Data to know the time on the market (listDate-SoldDate)

	//data = d.list_date - d.sold_date;

 //data = data.days;

	function createVis() {

		// Get svg
		const svg = d3.select('#barChart');

		// Config
		const margin = {
			'top': 25,
			'right': 54,
			'bottom': 50,
			'left': 10
		};
		const width = +svg.attr('width') - (margin.right + margin.left);
		const height = +svg.attr('height') - (margin.top + margin.bottom);

		// Create and position container
		const container = svg.append('g')
			.attr('class', 'container')
			.style('transform', `translate(${margin.left}px, ${margin.top}px)`);

		// Set DataMap
		const dataMap = data.map(function (d, i) {
			return d.;
		});

		// X Scale
		const scX = d3.scaleLinear()
			.domain(d3.extent(dataMap, (d) => {
				return d;
			}))
			.range([0, width]);

		// Histogram and bins
		const histogram = d3.histogram()
			.domain(scX.domain())
			.thresholds(scX.ticks(10));

		const bins = histogram(dataMap);

		// Y Scale
		const scY = d3.scaleLinear()
			.domain([0, d3.max(bins, function (d) {
				return d.length;
			})])
			.range([0, height]);

		// Config transition
		const t = d3.transition()
			.duration(250)
			.ease(d3.easeLinear);

		// Create bars
		const bars = container.selectAll('.bar')
			.data(bins)
			.enter()
			.append('g')
			.attr('class', 'bar')
			.style('transform', (d, i) => {
				return `translate(${i * Math.floor(width / bins.length)}px, ${height - scY(d.length)}px)`;
			});

		// Create rects
		bars.append('rect')
			.attr('width', () => {
				return Math.floor(width / bins.length);
			})
			.attr('height', (d) => {
				return scY(d.length);
			})
			.attr('fill', '#111E32')
			.on('mouseover', function () {
				d3.select(this)
					.attr('fill', '#111E32')
			})
			.on('mouseout', function () {
				d3.select(this)
					.attr('fill', '#111E32');
			});


		// Add y-label
		const yLabels = bars.append('text')
			.text(function (d) {
				return d.length;
			})
			.attr('class', 'yLabel')
			.attr('y', -5)
			.attr('x', Math.floor(width / bins.length) / 2)
			.attr('text-anchor', 'middle');

		// Add x-axis
		const xAxis = container.append('g')
			.attr('transform', `translate(0, ${height + 5})`)
			.call(d3.axisBottom(scX).ticks(5));


		// Add x-label
		container.append('text')
			.attr('transform', `translate(${width/2}, ${height + 45})`)
			.attr('text-anchor', 'middle')
			.text('Days on Sale of Similar Properties');


	}


})();
