$(function () {    
    console.log("Init...")
    
    let first_run_state = 1;
    if (localStorage.getItem('isblur') == null) {
        console.log('blur state new');
        localStorage.setItem('isblur', first_run_state);
        var is_blur = first_run_state;
    }
    else {
        var is_blur = localStorage.getItem('isblur');
    }
    console.log(is_blur);
    if (is_blur == false){
        console.log('pre blur is false');
        is_blur=false;
        $('#switch').text('OFF');
        $("img").each(function () {
            $(this).css('filter', 'blur(0px)');
        });
    }
    else {
        console.log('pre blur is true');
        is_blur=true;
        $('#switch').text('ON');
        $("img").each(function () {
            $(this).css('filter', 'blur(10px)');
        });
    }
    
    $('a[href="/random/"]').prepend('');
    $('.thumbs').css('max-height', 'none')
    $('span.count').before('|');
    
    var  thing = "<button type='button' id='switch'>OFF</button>";
    $('li').eq(7).before(thing);
    
    $("img").each(function () {
        $(this).wrap("<div class='blur'></div>");
        var imgsrc = $(this).attr("data-src");
        $(this).attr("src", imgsrc);
        console.log(imgsrc);
    });
    
    $('#switch').click(function(){
        if (is_blur){
            localStorage.setItem('isblur', 0);
            console.log('blur switched to false');
            is_blur=false;
            $('#switch').text('OFF');
            $("img").each(function () {
                $(this).css('filter', 'blur(0px)');
            });
        }
        else {
            localStorage.setItem('isblur', 1);
            console.log('blur switched to true');
            is_blur=true;
            $('#switch').text('ON');
            $("img").each(function () {
                $(this).css('filter', 'blur(10px)');
            });
        }
    });
    
});

