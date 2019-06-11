/** *************Init JS*********************
	
    TABLE OF CONTENTS
	---------------------------
	1.Ready function
	2.Load function
	3.Full height function
	4.Griffin function
	5.Chat App function
	6.Resize function
 ** ***************************************/

"use strict";
/*****Ready function start*****/
$(document).ready(function() {
    griffin();
    emailApp();
    chatApp();
    calendarApp();
    fmApp();
    languageInit();
    /*Disabled*/
    $(document).on("click", "a.disabled,a:disabled", function(e) {
        return false;
    });
});
/*****Ready function end*****/

/*****Load function start*****/
$(window).on("load", function() {
    $(".preloader-it").delay(500).fadeOut("slow");
});
/*****Load function* end*****/

/*Variables*/
var height, width,
    $wrapper = $(".hk-wrapper"),
    $nav = $(".hk-nav"),
    $vertnaltNav = $(".hk-wrapper.hk-vertical-nav,.hk-wrapper.hk-alt-nav"),
    $horizontalNav = $(".hk-wrapper.hk-horizontal-nav"),
    $navbar = $(".hk-navbar");

/***** griffin function start *****/
var griffin = function() {

    /*Feather Icon*/
    var featherIcon = $('.feather-icon');
    if (featherIcon.length > 0) {
        feather.replace();
    }


    /*Counter Animation*/
    var counterAnim = $('.counter-anim');
    if (counterAnim.length > 0) {
        counterAnim.counterUp({
            delay: 10,
            time: 1000
        });
    }

    /*Tooltip*/
    if ($('[data-toggle="tooltip"]').length > 0)
        $('[data-toggle="tooltip"]').tooltip();

    /*Popover*/
    if ($('[data-toggle="popover"]').length > 0)
        $('[data-toggle="popover"]').popover()

    /*Navbar Collapse Animation*/
    var navbarNavCollapse = $('.hk-nav .navbar-nav  li');
    var navbarNavAnchor = '.hk-nav .navbar-nav  li a';
    $(document).on("click", navbarNavAnchor, function(e) {
        if ($(this).attr('aria-expanded') === "false")
            $(this).blur();
        $(this).parent().siblings().find('.collapse').collapse('hide');
        $(this).parent().find('.collapse').collapse('hide');
    });

    /*Card Remove*/
    $(document).on('click', '.card-close', function(e) {
        var effect = $(this).data('effect');
        $(this).closest('.card')[effect]();
        return false;
    });

    /*Accordion js*/
    $(document).on('show.bs.collapse', '.accordion .collapse', function(e) {
        $(this).siblings('.card-header').addClass('activestate');
    });

    $(document).on('hide.bs.collapse', '.accordion .collapse', function(e) {
        $(this).siblings('.card-header').removeClass('activestate');
    });

    /*Navbar Toggle*/
    $(document).on('click', '#navbar_toggle_btn', function(e) {
        $wrapper.toggleClass('hk-nav-toggle');
        $(window).trigger("resize");
        return false;
    });
    $(document).on('click', '#hk_nav_backdrop,#hk_nav_close', function(e) {
        $wrapper.removeClass('hk-nav-toggle');
        return false;
    });

    /*Search form Collapse*/
    $(document).on('click', '#navbar_search_btn', function(e) {
        $('html,body').animate({ scrollTop: 0 }, 'slow');
        $(".navbar-search input").focus();
        $wrapper.addClass('navbar-search-toggle');
        $(window).trigger("resize");
    });
    $(document).on('click', '#navbar_search_close', function(e) {
        $wrapper.removeClass('navbar-search-toggle');
        $(window).trigger("resize");
        return false;
    });

    /*Slimscroll*/
    $('.nicescroll-bar').slimscroll({ height: '100%', color: '#d6d9da', disableFadeOut: true, borderRadius: 0, size: '6px', enableKeyNavigation: true, opacity: .8 });
    $('.notifications-nicescroll-bar').slimscroll({ height: '330px', size: '6px', color: '#d6d9da', disableFadeOut: true, borderRadius: 0, enableKeyNavigation: true, opacity: .8 });


    /*Slimscroll Key Control*/
    $(".slimScrollDiv").hover(function() {
        $(this).find('[class*="nicescroll-bar"]').focus();
    }, function() {
        $(this).find('[class*="nicescroll-bar"]').blur();
    });

    /*Refresh Init Js*/
    var refreshMe = '.refresh';
    $(document).on("click", refreshMe, function(e) {
        var panelToRefresh = $(this).closest('.card').find('.refresh-container');
        var dataToRefresh = $(this).closest('.card').find('.panel-wrapper');
        var loadingAnim = panelToRefresh.find('.la-anim-1');
        panelToRefresh.show();
        setTimeout(function() {
            loadingAnim.addClass('la-animate');
        }, 100);

        function started() {} //function before timeout
        setTimeout(function() {
            function completed() {} //function after timeout
            panelToRefresh.fadeOut(800);
            setTimeout(function() {
                loadingAnim.removeClass('la-animate');
            }, 800);
        }, 1500);
        return false;
    });

    /*Fullscreen Init Js*/
    $(document).on("click", ".full-screen", function(e) {
        $(this).parents('.card').toggleClass('fullscreen');
        $(window).trigger("resize");
        return false;
    });

};
/***** griffin function end *****/

/***** Full height function start *****/
var setHeightWidth = function() {
    height = window.innerHeight;
    width = window.innerWidth;
    $('.full-height').css('height', (height));
    $('.hk-pg-wrapper').css('min-height', (height));

    /*****App Height for differnt brekpoints with Vertical & Alt menu*****/

    /*ChatApp Height for differnt brekpoints with Vertical & Alt menu*/
    if ($vertnaltNav.hasClass('navbar-search-toggle'))
        $vertnaltNav.find('.chatapp-users-list,.chat-body').css('height', (height - 240));
    else
        $vertnaltNav.find('.chatapp-users-list,.chat-body').css('height', (height - 190));

    /*EmailApp Height for differnt brekpoints with Vertical & Alt menu*/
    if ($vertnaltNav.hasClass('navbar-search-toggle')) {
        $vertnaltNav.find('.emailapp-emails-list').css('height', (height - 240));
        $vertnaltNav.find('.email-body').css('height', (height - 179));
        $vertnaltNav.find('.emailapp-sidebar').css('height', (height - 107));
    } else {
        $vertnaltNav.find('.emailapp-emails-list').css('height', (height - 190));
        $vertnaltNav.find('.email-body').css('height', (height - 129));
        $vertnaltNav.find('.emailapp-sidebar').css('height', (height - 57));
    }
    /*FilemanagerApp Height for differnt brekpoints with Vertical & Alt menu*/
    if ($vertnaltNav.hasClass('navbar-search-toggle')) {
        $vertnaltNav.find('.fm-body').css('height', (height - 179));
        $vertnaltNav.find('.fmapp-sidebar').css('height', (height - 107));
    } else {
        $vertnaltNav.find('.fm-body').css('height', (height - 129));
        $vertnaltNav.find('.fmapp-sidebar').css('height', (height - 57));
    }
    /*CalendarApp Height for differnt brekpoints with Vertical & Alt menu*/
    if ($vertnaltNav.hasClass('navbar-search-toggle'))
        $vertnaltNav.find('.calendarapp-sidebar,.calendar-wrap').css('height', (height - 107));
    else
        $vertnaltNav.find('.calendarapp-sidebar,.calendar-wrap').css('height', (height - 57));

    /*GmapApp Height for differnt brekpoints with Vertical & Alt menu*/
    if ($vertnaltNav.hasClass('navbar-search-toggle'))
        $vertnaltNav.find('.gmap').css('height', (height - 107));
    else
        $vertnaltNav.find('.gmap').css('height', (height - 57));


    /*****App Height for differnt brekpoints with Horizontal menu*****/

    /*ChatApp Height for differnt brekpoints with Horizontal menu*/
    if (width > 1024) {
        if ($horizontalNav.hasClass('hk-nav-toggle') && !($horizontalNav.hasClass('navbar-search-toggle')))
            $horizontalNav.find('.chatapp-users-list,.chat-body').css('height', (height - 190));
        else if (!($horizontalNav.hasClass('hk-nav-toggle')) && $horizontalNav.hasClass('navbar-search-toggle'))
            $horizontalNav.find('.chatapp-users-list,.chat-body').css('height', (height - 290));
        else
            $horizontalNav.find('.chatapp-users-list,.chat-body').css('height', (height - 240));
    } else {
        if ($horizontalNav.hasClass('navbar-search-toggle'))
            $horizontalNav.find('.chatapp-users-list,.chat-body').css('height', (height - 240));
        else
            $horizontalNav.find('.chatapp-users-list,.chat-body').css('height', (height - 190));
    }

    /*EmailApp Height for differnt brekpoints with Horizontal menu*/
    if (width > 1024) {
        if ($horizontalNav.hasClass('hk-nav-toggle') && !($horizontalNav.hasClass('navbar-search-toggle'))) {
            $horizontalNav.find('.emailapp-emails-list').css('height', (height - 190));
            $horizontalNav.find('.email-body').css('height', (height - 129));
            $horizontalNav.find('.emailapp-sidebar').css('height', (height - 57));
        } else if (!($horizontalNav.hasClass('hk-nav-toggle')) && $horizontalNav.hasClass('navbar-search-toggle')) {
            $horizontalNav.find('.emailapp-emails-list').css('height', (height - 290));
            $horizontalNav.find('.email-body').css('height', (height - 229));
            $horizontalNav.find('.emailapp-sidebar').css('height', (height - 157));
        } else {
            $horizontalNav.find('.emailapp-emails-list').css('height', (height - 240));
            $horizontalNav.find('.email-body').css('height', (height - 179));
            $horizontalNav.find('.emailapp-sidebar').css('height', (height - 107));
        }
    } else {
        if ($horizontalNav.hasClass('navbar-search-toggle')) {
            $horizontalNav.find('.emailapp-emails-list').css('height', (height - 240));
            $horizontalNav.find('.email-body').css('height', (height - 179));
            $horizontalNav.find('.emailapp-sidebar').css('height', (height - 107));
        } else {
            $horizontalNav.find('.emailapp-emails-list').css('height', (height - 190));
            $horizontalNav.find('.email-body').css('height', (height - 129));
            $horizontalNav.find('.emailapp-sidebar').css('height', (height - 57));
        }
    }

    /*FilemanagerApp Height for differnt brekpoints with Horizontal menu*/
    if (width > 1024) {
        if ($horizontalNav.hasClass('hk-nav-toggle') && !($horizontalNav.hasClass('navbar-search-toggle'))) {
            $horizontalNav.find('.fm-body').css('height', (height - 129));
            $horizontalNav.find('.fmapp-sidebar').css('height', (height - 57));
        } else if (!($horizontalNav.hasClass('hk-nav-toggle')) && $horizontalNav.hasClass('navbar-search-toggle')) {
            $horizontalNav.find('.fm-body').css('height', (height - 229));
            $horizontalNav.find('.fmapp-sidebar').css('height', (height - 157));
        } else {
            $horizontalNav.find('.fm-body').css('height', (height - 179));
            $horizontalNav.find('.fmapp-sidebar').css('height', (height - 107));
        }
    } else {
        if ($horizontalNav.hasClass('navbar-search-toggle')) {
            $horizontalNav.find('.fm-body').css('height', (height - 179));
            $horizontalNav.find('.fmapp-sidebar').css('height', (height - 107));
        } else {
            $horizontalNav.find('.fm-body').css('height', (height - 129));
            $horizontalNav.find('.fmapp-sidebar').css('height', (height - 57));
        }
    }

    /*CalendarApp Height for differnt brekpoints with Horizontal menu*/
    if (width > 1024) {
        if ($horizontalNav.hasClass('hk-nav-toggle') && !($horizontalNav.hasClass('navbar-search-toggle')))
            $horizontalNav.find('.calendarapp-sidebar,.calendar-wrap').css('height', (height - 57));
        else if (!($horizontalNav.hasClass('hk-nav-toggle')) && $horizontalNav.hasClass('navbar-search-toggle'))
            $horizontalNav.find('.calendarapp-sidebar,.calendar-wrap').css('height', (height - 157));
        else
            $horizontalNav.find('.calendarapp-sidebar,.calendar-wrap').css('height', (height - 107));
    } else {
        if ($horizontalNav.hasClass('navbar-search-toggle'))
            $horizontalNav.find('.calendarapp-sidebar,.calendar-wrap').css('height', (height - 107));
        else
            $horizontalNav.find('.calendarapp-sidebar,.calendar-wrap').css('height', (height - 57));
    }

    /*GmapApp Height for differnt brekpoints with Horizontal menu*/
    if (width > 1024) {
        if ($horizontalNav.hasClass('hk-nav-toggle') && !($horizontalNav.hasClass('navbar-search-toggle')))
            $horizontalNav.find('.gmap').css('height', (height - 57));
        else if (!($horizontalNav.hasClass('hk-nav-toggle')) && $horizontalNav.hasClass('navbar-search-toggle'))
            $horizontalNav.find('.gmap').css('height', (height - 157));
        else
            $horizontalNav.find('.gmap').css('height', (height - 107));

    } else {
        if ($horizontalNav.hasClass('navbar-search-toggle'))
            $horizontalNav.find('.gmap').css('height', (height - 107));
        else
            $horizontalNav.find('.gmap').css('height', (height - 57));
    }
};
/***** Full height function end *****/

/***** Chat App function start *****/
var chatAppTarget = $('.chatapp-wrap');
var chatApp = function() {
    if (width > 1024)
        chatAppTarget.removeClass('chatapp-slide');
    $(document).on("click", ".chatapp-wrap .chatapp-users-list a.media", function(e) {
        if (width <= 1024) {
            chatAppTarget.addClass('chatapp-slide');
        }
        return false;
    });
    $(document).on("click", "#back_user_list", function(e) {
        if (width <= 1024) {
            chatAppTarget.removeClass('chatapp-slide');
        }
        return false;
    });
    $(document).on("keypress", "#input_msg_send_chatapp", function(e) {
        if ((e.which == 13) && (!$(this).val().length == 0)) {
            $('<li class="media sent"><div class="media-body"><div class="msg-box"><div><p>' + $(this).val() + '</p><span class="chat-time">8:00 pm</span><div class="arrow-triangle-wrap"><div class="arrow-triangle left"></div></div></div></div></div></li>').insertAfter(".chatapp-right  ul li.media:last-child");
            $(this).val('');
        } else if (e.which == 13) {
            alert('Please type asomthing!');
        }
        return;
    });
};
/***** Chat App function end *****/

/***** Email App function start *****/
var emailAppTarget = $('.emailapp-wrap');
var emailApp = function() {
    if (width > 1024)
        emailAppTarget.removeClass('emailapp-slide');
    $(document).on("click", ".emailapp-wrap .emailapp-emails-list a.media", function(e) {
        if (width <= 1024) {
            emailAppTarget.addClass('emailapp-slide');
        }
        return;
    });
    $(document).on("click", "#back_email_list", function(e) {
        if (width <= 1024) {
            emailAppTarget.removeClass('emailapp-slide');
        }
        return false;
    });
    $(document).on("click", "#emailapp_sidebar_move", function(e) {
        emailAppTarget.toggleClass('emailapp-sidebar-toggle');
        return false;
    });
    $(document).on("click", "#close_emailapp_sidebar", function(e) {
        if (width <= 1400) {
            emailAppTarget.removeClass('emailapp-sidebar-toggle');
        }
        return false;
    });
};
/***** Email App function end *****/

/***** Email App function start *****/
var fmAppTarget = $('.fmapp-wrap');
var fmApp = function() {
    $(document).on('click', '#fm_view_switcher', function(e) {
        $(this).closest('.fmapp-main').toggleClass('fmapp-view-switch');
        return false;
    });
    $(document).on("click", "#fmapp_sidebar_move", function(e) {
        fmAppTarget.toggleClass('fmapp-sidebar-toggle');
        return false;
    });
    $(document).on("click", "#close_fmapp_sidebar", function(e) {
        if (width <= 1400) {
            fmAppTarget.removeClass('fmapp-sidebar-toggle');
        }
        return false;
    });
};
/***** Email App function end *****/


/***** Calendar App function start *****/
var calendarAppTarget = $('.calendarapp-wrap');
var calendarApp = function() {
    $(document).on("click", "#calendarapp_sidebar_move", function(e) {
        calendarAppTarget.toggleClass('calendarapp-sidebar-toggle');
        return false;
    });
    $(document).on("click", "#close_calendarapp_sidebar", function(e) {
        if (width <= 1024) {
            calendarAppTarget.removeClass('calendarapp-sidebar-toggle');
        }
        return false;
    });
};
/***** Calendar App function end *****/

/***** Resize function start *****/
$(window).on("resize", function() {
    setHeightWidth();
});
$(window).trigger("resize");
/***** Resize function end *****/

/***** language init start *****/
var languageInit = function() {
    var dict = {};

    $(function() {
        registerWords();
        if (getCookieVal("lang") == "en") {
            setLanguage("en");
        } else if (getCookieVal("lang") == "cn") {
            setLanguage("cn");
        } else if (getCookieVal("lang") == "fr") {
            setLanguage("fr");
        } else {
            setLanguage("en");
        }

        // 切换语言事件 根据自己业务而定
        $("#langEN").bind("click", function() {
            setLanguage("en");
            //这里也可以写一些其他操作，比如加载语言对应的css
        });

        $("#langCN").bind("click", function() {
            sessionStorage.removeItem("cnData")
            setLanguage("cn");
        });

        $("#langFR").bind("click", function() {
            sessionStorage.removeItem("frData")
            setLanguage("fr");
        });

    });

    function setLanguage(lang) {
        setCookie("lang=" + lang + "; path=/;");
        translate(lang);
    }

    function getCookieVal(name) {
        var items = document.cookie.split(";");
        for (var i in items) {
            var cookie = $.trim(items[i]);
            var eqIdx = cookie.indexOf("=");
            var key = cookie.substring(0, eqIdx);
            if (name == $.trim(key)) {
                return $.trim(cookie.substring(eqIdx + 1));
            }
        }
        return null;
    }

    function setCookie(cookie) {
        var Days = 30; //此 cookie 将被保存 30 天
        var exp = new Date(); //new Date("December 31, 9998");
        exp.setTime(exp.getTime() + Days * 24 * 60 * 60 * 1000);
        document.cookie = cookie + ";expires=" + exp.toGMTString();
    }

    function translate(lang) {
        if (sessionStorage.getItem(lang + "Data") != null) {
            dict = JSON.parse(sessionStorage.getItem(lang + "Data"));
            console.log(dict)
        } else {
            loadDict();
        }

        $("[lang]").each(function() {
            switch (this.tagName.toLowerCase()) {
                case "input":
                    $(this).val(__tr($(this).attr("lang").toLowerCase()));
                    break;
                default:
                    $(this).text(__tr($(this).attr("lang").toLowerCase()));
            }
        });
    }

    function __tr(src) {
        return (dict[src] || src);
    }

    function loadDict() {
        var lang = (getCookieVal("lang") || "en");
        if (lang == "en") {
            dict = {};
            return;
        }
        console.log("dsd")
        $.ajax({
            async: false,
            type: "GET",
            url: "/lang/" + lang + ".json",
            success: function(msg) {
                dict = msg;
                sessionStorage.setItem(lang + 'Data', JSON.stringify(dict));
            },
            error: function(error) {
                console.log(error.responseText);
            }
        });

    }

    // 遍历所有lang属性的标签赋值
    function registerWords() {
        $("[lang]").each(function() {
            switch (this.tagName.toLowerCase()) {
                case "input":
                    if ($(this).attr("lang") == "") {
                        $(this).attr("lang", $(this).val());
                    }
                    break;
                default:
                    if ($(this).attr("lang") == "") {
                        $(this).attr("lang", $(this).text());
                    }
            }
        });
    }
};
/***** language init end *****/