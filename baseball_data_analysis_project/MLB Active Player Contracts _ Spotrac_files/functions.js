(function($) {
    "use strict";
    
 
    // Navigation Menu Expander
    $('#nav-expander').sidr({
        side: 'right'
    });
	

    $('#sidr li a.more').click(function(e) {
        e.preventDefault();
        $(this).parent().find('ul.subnav-menu').toggle();
    });
	
	$('#sidr li a.moremore').click(function(f) {
        f.preventDefault();
        $(this).parent().find('ul.subsubnav').toggle();
    });
    
    // Subnav article loader
    $('#menu .subnav-menu li').hover(function() {
        $(this).parent().find('li').removeClass('current');
        $(this).addClass('current');
    });
    
    // Homepage slider
    /*
	$('#slider-carousel').carouFredSel({
        width: '100%',
        height: 'auto',
        prev: '#slider-prev',
        next: '#slider-next',
        auto: false,
        responsive: true,
        transition: true,
        swipe: {
                onMouse: true,
                onTouch: true
        },
        scroll : {
            items           : 1,
            easing          : "quadratic",
            duration        : 1000,                         
            pauseOnHover    : true
        }      
    });
    
    // Init photobox
    $('#weekly-gallery').photobox('a',{ time:0 });
    $('#article-gallery').photobox('a',{ time:0 });
	
    
    // Init datepicker for archive page
    $('#archive-date-picker').datepicker({
        format: 'mm/dd/yyyy'
    });
    */
	
    //Click event to scroll to top
    $('.scrollToTop').click(function(){
        $('html, body').animate({scrollTop : 0},800);
        return false;
    });
    
    //Contact form
    /*
	var contactForm = $('#contactForm');
    var successForm = $('.alert-success', contactForm);
    var errorForm = $('.alert-danger', contactForm);
    
    $("#contactForm").validate({
        submitHandler: function (form) {
            successForm.removeClass('hide').show();
            errorForm.hide();            
        }
    });
	*/
 /*
 $(window).touchwipe({
        wipeLeft: function() {
          // Close
          $.sidr('open', 'sidr');
        },
        wipeRight: function() {
          // Open
          $.sidr('close', 'sidr');
        },
        preventDefaultEvents: false
      }); 
*/  

})(jQuery);

/*
 * Dropit v1.1.0
 * http://dev7studios.com/dropit
 *
 * Copyright 2012, Dev7studios
 * Free to use and abuse under the MIT license.
 * http://www.opensource.org/licenses/mit-license.php
 */

(function($) {

    $.fn.dropit = function(method) {

        var methods = {

            init : function(options) {
                this.dropit.settings = $.extend({}, this.dropit.defaults, options);
                return this.each(function() {
                    var $el = $(this),
                         el = this,
                         settings = $.fn.dropit.settings;

                    // Hide initial submenus
                    $el.addClass('dropit')
                    .find('>'+ settings.triggerParentEl +':has('+ settings.submenuEl +')').addClass('dropit-trigger')
                    .find(settings.submenuEl).addClass('dropit-submenu').hide();

                    // Open on click
                    $el.off(settings.action).on(settings.action, settings.triggerParentEl +':has('+ settings.submenuEl +') > '+ settings.triggerEl +'', function(){
                        // Close click menu's if clicked again
                        if(settings.action == 'click' && $(this).parents(settings.triggerParentEl).hasClass('dropit-open')){
                            settings.beforeHide.call(this);
                            $(this).parents(settings.triggerParentEl).removeClass('dropit-open').find(settings.submenuEl).hide();
                            settings.afterHide.call(this);
														
                            return false;
                        }

                        // Hide open menus
                        settings.beforeHide.call(this);
                        $('.dropit-open').removeClass('dropit-open').find('.dropit-submenu').hide();
                        settings.afterHide.call(this);

                        // Open this menu
                        settings.beforeShow.call(this);
                        $(this).parents(settings.triggerParentEl).addClass('dropit-open').find(settings.submenuEl).show();
                        settings.afterShow.call(this);

                        return false;
                    });

                    // Close if outside click
                    $(document).on('click', function(){
                        settings.beforeHide.call(this);
                        $('.dropit-open').removeClass('dropit-open').find('.dropit-submenu').hide();
                        settings.afterHide.call(this);
                    });

                    // If hover
                    if(settings.action == 'mouseenter'){
                        $el.on('mouseleave', '.dropit-open', function(){
                            settings.beforeHide.call(this);
                            $(this).removeClass('dropit-open').find(settings.submenuEl).hide();
                            settings.afterHide.call(this);
                        });
                    }

                    settings.afterLoad.call(this);
                });
            }

        };

        if (methods[method]) {
            return methods[method].apply(this, Array.prototype.slice.call(arguments, 1));
        } else if (typeof method === 'object' || !method) {
            return methods.init.apply(this, arguments);
        } else {
            $.error( 'Method "' +  method + '" does not exist in dropit plugin!');
        }

    };

    $.fn.dropit.defaults = {
        action: 'click', // The open action for the trigger
        submenuEl: 'ul', // The submenu element
        triggerEl: 'a', // The trigger element
        triggerParentEl: 'li', // The trigger parent element
        afterLoad: function(){}, // Triggers when plugin has loaded
        beforeShow: function(){}, // Triggers before submenu is shown
        afterShow: function(){}, // Triggers after submenu is shown
        beforeHide: function(){}, // Triggers before submenu is hidden
        afterHide: function(){} // Triggers before submenu is hidden
    };

    $.fn.dropit.settings = {};

 $('.menu').dropit();

})(jQuery);
  
  
$(document).ready(function(){
	"use strict";
	
	$("nav.cat-nfl, nav.cat-nhl, nav.cat-mlb, nav.cat-epl, nav.cat-nba").css("overflow","visible");
		
});


var justClicked = "";
$(document).ready(function(){
	$("a.clickable").click(function(){
		
		$(".subnav-container").hide();
		$(this).siblings(".subnav-container").show();	
		
		if(justClicked==$(this).parents("li").attr("class"))
		{
			justClicked = "";
			$(this).siblings(".subnav-container").hide();
			
		}
		else
		{
			justClicked = $(this).parents("li").attr("class")	
		}
		
		

		return false;
	});
	
	
	$("body:not(a.clickable)").click(function(){
		
		justClicked = "";

		$(".subnav-container").hide();

	});
	
});


/*** PREMIUM ***/

$(document).ready(function(){
	$(".premiumheader.ad").slideToggle('slow', function(){
		$.ajax({
			  type: 'post',
			  //url: 'http://localhost:8888/spotrac.com/premium/hideAd/',
			  url: 'https://www.spotrac.com/premium/hideAd/',
			  success: function(data)
			  {
				  //$(".premiumheader").slideUp('slow');
			  }
		  });
	});
	
	$(".premiumheaderclose").click(function(){
		 $.ajax({
			  type: 'post',
			  //url: 'http://localhost:8888/spotrac.com/premium/hideAd/',
			  url: 'https://www.spotrac.com/premium/hideAd/',
			  success: function(data)
			  {
				  $(".premiumheader").slideUp('slow');
			  }
		  });
	})
})



/*** COOKIES ***/

$(document).ready(function(){
	
	$(".cookie-alert-settings").click(function(e){
		$("#cookies").modal('show');
	});
	
	$(".cookie-alert-close").click(function(e){
		e.preventDefault();
		$(".optanon-alert-box-wrapper").slideToggle();
	})
	
	$(".cookie-alert-accept").click(function(e){
		e.preventDefault();
		$.ajax({
			  type: 'post',
			  ///url: 'http://localhost:8888/spotrac.com/cookies/accept/',
			  url: 'https://www.spotrac.com/cookies/accept/',
			  success: function(data)
			  {
				$(".optanon-alert-box-wrapper").slideToggle();
			  }
		  });
	});
	
});
