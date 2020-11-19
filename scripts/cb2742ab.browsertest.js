$(document).ready(function () {
    function a(a, b) {
        throw console.error(b), $(".working").css("display", "none"), $("." + a).css("display", "block"), new Error(b)
    }

    function b() {
        $(".working").css("display", "none"), $(".passed").css("display", "block"), setTimeout(function () {
            window.location.href = "index2.html"
        }, 1e3)
    }

    function c() {
        var b = /(iPhone|iP[oa]d|Android|Windows Phone|IEMobile)/i;
        navigator.userAgent.match(b) && a("mobile", "mobile user agent found: " + navigator.userAgent)
    }

    function d() {
        var b, c = $("html");
        for (b = 0; b < g.length; ++b) {
            var d = g[b];
            // c.hasClass(d) || a("failed", "lacks " + d)
        }
        c.hasClass("flexbox") || c.hasClass("flexboxlegacy") || a("failed", "lacks flexbox")
    }

    function e() {
        for (i in h) h[i] || a("failed", "lacks " + i)
    }

    function f(b) {
        (navigator.userAgent.match(/Trident\/7\./) || navigator.userAgent.match(/Trident\/6\./)) && b();
        var c = $("#loaderTest");
        c.on("error", function () {
            a("failed", "no valid audio codecs found")
        }).on("canplaythrough", function () {
            b()
        }), c[0].preload = "auto"
    }
    var g = ["hashchange", "borderradius", "textshadow", "opacity", "rgba", "csstransforms", "csstransitions", "cssanimations", "cssgradients", "fontface", "audio", "localstorage", "sessionstorage", "applicationcache", "svg"],
        h = {
            "Function.prototype.bind": Function.prototype.bind,
            "Object.keys": Object.keys,
            "Object.create": Object.create,
            "Object.defineProperty": Object.defineProperty,
            "Object.defineProperties": Object.defineProperties,
            "Array.isArray": Array.isArray,
            "Date.now": Date.now,
            "window.requestAnimationFrame": window.requestAnimationFrame
        }, j = /^(\d+(\.\d+)?).*/i,
        k = $.browser.version,
        l = k.match(j);
    parseFloat(l[1]), c(), d(), e(), f(b)
});