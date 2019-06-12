var getLangNail = function() {
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

    if (getCookieVal("lang") == "en") {
        return ".html";
    } else if (getCookieVal("lang") == "cn") {
        return "-cn.html";
    } else if (getCookieVal("lang") == "fr") {
        return "-fr.html";
    } else {
        return ".html";
    }
}