// HERO MENU
$("#navbarBurger").click(function(event) {
    event.preventDefault();
    $(".hero-nav").toggleClass("show");
    $("body").addClass("overflow-active");
    $("html").addClass("html-overflow-active");
    $("#aside-menu").addClass("aside-overflow-active");
});

$(".hero-nav-close").click(function(event) {
    event.preventDefault();
    $(".hero-nav").removeClass("show");
    $("body").removeClass("overflow-active");
    $("html").removeClass("html-overflow-active");
    $("#aside-menu").removeClass("aside-overflow-active");
});


// MASONRY
    $('.grid').masonry({
        // options
        columnWidth: '.grid-sizer',
        itemSelector: '.grid-item',
        percentPosition: true,
        horizontalOrder: true
    });


// TABS
    $(function() {
        $(".tab-menu li a").click(function(event) {
            event.preventDefault();
            $(this).parent().addClass("current");
            $(this).parent().siblings().removeClass("current");
            var tab = $(this).attr("href");
            $(".tab-content").not(tab).css({"display": "block", "height": "0", "overflow": "hidden", "opacity" : "0"});
            $(tab).css({"display": "block", "height": "auto", "overflow": "auto", "opacity" : "1" });
        });
    });

    $(".tab-content:first-child").css({"display": "block"});
    $(".tab-menu li:first-child").addClass("current");


// RANGE
    $(window).on("load resize", function() {
        // Get the current width of the slider
        var sliderWidth = $('[type=range]').width();
        // Remove previously created style elements
        $('.custom-style-element-related-to-range').remove();
        // Add our updated styling
        $('<style class="custom-style-element-related-to-range">input[type="range"]::-webkit-slider-thumb { box-shadow: -' + sliderWidth + 'px 0 0 ' + sliderWidth + 'px;}<style/>').appendTo('head');
    });

    function outputUpdate(vol) {
        document.querySelector('#volume').value = vol;
    }

// ATTACH FILE INPUT
    $('#input-file').change(function() {
        var i = $(this).prev('label').clone();
        var file = $('#input-file')[0].files[0].name;
        $(this).prev('label').text(file);
    });
