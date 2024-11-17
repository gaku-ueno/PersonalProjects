// Tablesorter - responsive table layout
	if($("table.responsive").length>0)
	{
		
		$("table.responsive").tablesorter({
			textExtraction: function(node){ 
				return  $(node).text().replace(/[,$%]/g,'') //.replace("-",'0');				
			},
			sortInitialOrder: 'desc',
  			sortRestart: true
				/*
			,
			widgets : ["columns"],
			widgetOptions : {
			  // change the default column class names
			  // primary is the first column sorted, secondary is the second, etc
			  columns : [ "result" ],
			  // include thead when adding class names
			  columns_thead : true,
			  // include tfoot when adding class names
			  columns_tfoot : true
			}
			*/
		});	
	}

// Tablesorter - datatable table layout
	if($("table.datatable:not(.captotal)").length>0)
	{				

		$("table.datatable:not(.captotal)").tablesorter({
			textExtraction: function(node){ 
				return $(node).text().replace(/[,$%]/g,''); //.replace("-",'0');
			},
			sortInitialOrder: 'desc',
  			sortRestart: true
			/*
			,
			widgets : ["columns"],
			widgetOptions : {
			  // change the default column class names
			  // primary is the first column sorted, secondary is the second, etc
			  columns : [ "result" ],
			  // include thead when adding class names
			  columns_thead : true,
			  // include tfoot when adding class names
			  columns_tfoot : true
			}
			*/
		});
	}
	
	// Tablesorter - datatable.captracker re-sort ranks accordingly
	if($("table.datatable.captracker").length>0)
	{
		$("table.datatable.captracker").bind("sortStart",function() { 
		}).bind("sortEnd",function() { 	
			c = 0;
			$("table.datatable tbody tr").each(function(i){
				 if(!$(this).is(".average"))
				 {
					 $(this).find("td:eq(0)").html(c+1);
					 c++;
				 }
			});
		});
	}
	
// Responsive Menu
	$("select.dropdown").change(function(){
		document.location.href = $(this).val();
	});
	

// Initialize bootstrap tooltip
	$('a.info, span.info, i.info, sup.info').tooltip({html: true});


// Ajax - Rankings (load the rest)
	if(typeof ajax!=='undefined' && ajax=="rankings")
	{
		mobile = "false"; if($(window).width()<=480)	mobile = "true";
		
		$.ajax({
			type: 'post',
			url: ajaxUrl,
			data: 'ajax=true&mobile='+mobile,
			success: function(data)
			{
				$( "div.ranklist" ).html( data );

				// Initialize bootstrap tooltip
				$('a.info, span.info').tooltip();
				
				
				$("table.datatable").tablesorter({
					textExtraction: function(node){ 
						return $(node).text().replace(/[,$%]/g,''); //.replace("-",'0');
					},
					sortInitialOrder: 'desc'
				});

			}
		})
	}


// Forms onchange - depreciated
/*
$("form#filter select").change(function(){
	$("form#filter").submit();
});
*/

