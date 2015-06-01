/**    Head JS     The only script in your <HEAD>    Copyright   Tero Piirainen (tipiirai)    License     MIT / http://bit.ly/mit-license    Version     0.96    http://headjs.com*/(function (a) {
    function l() {
        var a = window.outerWidth || b.clientWidth;
        b.className = b.className.replace(/ (w|lt)-\d+/g, ""), f("w-" + Math.round(a / 100) * 100), h(c.screens, function (b) {
            a <= b && f("lt-" + b)
        }), i.feature()
    }

    function h(a, b) {
        for (var c = 0, d = a.length; c < d; c++)b.call(a, a[c], c)
    }

    function g(a) {
        var c = new RegExp("\\b" + a + "\\b");
        b.className = b.className.replace(c, "")
    }

    function f(a) {
        d[d.length] = a
    }

    var b = a.documentElement, c = {screens: [320, 480, 640, 768, 1024, 1280, 1440, 1680, 1920], section: "-section", page: "-page", head: "head"}, d = [];
    if (window.head_conf)for (var e in head_conf)head_conf[e] !== undefined && (c[e] = head_conf[e]);
    var i = window[c.head] = function () {
        i.ready.apply(null, arguments)
    };
    i.feature = function (a, c, e) {
        if (!a)b.className += " " + d.join(" "), d = []; else {
            Object.prototype.toString.call(c) == "[object Function]" && (c = c.call()), f((c ? "" : "no-") + a), i[a] = !!c, e || (g("no-" + a), g(a), i.feature());
            return i
        }
    };
    var j = navigator.userAgent.toLowerCase();
    j = /(webkit)[ \/]([\w.]+)/.exec(j) || /(opera)(?:.*version)?[ \/]([\w.]+)/.exec(j) || /(msie) ([\w.]+)/.exec(j) || !/compatible/.test(j) && /(mozilla)(?:.*? rv:([\w.]+))?/.exec(j) || [], j[1] == "msie" && (j[1] = "ie", j[2] = document.documentMode || j[2]), f(j[1]), i.browser = {version: j[2]}, i.browser[j[1]] = !0;
    if (i.browser.ie) {
        f("ie" + parseFloat(j[2]));
        for (var k = 3; k < 11; k++)parseFloat(j[2]) < k && f("lt-ie" + k);
        h("abbr|article|aside|audio|canvas|details|figcaption|figure|footer|header|hgroup|mark|meter|nav|output|progress|section|summary|time|video".split("|"), function (b) {
            a.createElement(b)
        })
    }
    h(location.pathname.split("/"), function (a, d) {
        if (this.length > 2 && this[d + 1] !== undefined)d && f(this.slice(1, d + 1).join("-") + c.section); else {
            var e = a || "index", g = e.indexOf(".");
            g > 0 && (e = e.substring(0, g)), b.id = e + c.page, d || f("root" + c.section)
        }
    }), l(), window.onresize = l, i.feature("js", !0).feature()
})(document), function () {
    function h(a) {
        var b = a.charAt(0).toUpperCase() + a.substr(1), c = (a + " " + d.join(b + " ") + b).split(" ");
        return!!g(c)
    }

    function g(a) {
        for (var c in a)if (b[a[c]] !== undefined)return!0
    }

    var a = document.createElement("i"), b = a.style, c = " -o- -moz- -ms- -webkit- -khtml- ".split(" "), d = "Webkit Moz O ms Khtml".split(" "), e = window.head_conf && head_conf.head || "head", f = window[e], i = {gradient: function () {
        var a = "background-image:", d = "gradient(linear,left top,right bottom,from(#9f9),to(#fff));", e = "linear-gradient(left top,#eee,#fff);";
        b.cssText = (a + c.join(d + a) + c.join(e + a)).slice(0, -a.length);
        return!!b.backgroundImage
    }, rgba: function () {
        b.cssText = "background-color:rgba(0,0,0,0.5)";
        return!!b.backgroundColor
    }, opacity: function () {
        return a.style.opacity === ""
    }, textshadow: function () {
        return b.textShadow === ""
    }, multiplebgs: function () {
        b.cssText = "background:url(//:),url(//:),red url(//:)";
        return(new RegExp("(url\\s*\\(.*?){3}")).test(b.background)
    }, boxshadow: function () {
        return h("boxShadow")
    }, borderimage: function () {
        return h("borderImage")
    }, borderradius: function () {
        return h("borderRadius")
    }, cssreflections: function () {
        return h("boxReflect")
    }, csstransforms: function () {
        return h("transform")
    }, csstransitions: function () {
        return h("transition")
    }, fontface: function () {
        var a = navigator.userAgent, b;
        if (0)return!0;
        if (b = a.match(/Chrome\/(\d+\.\d+\.\d+\.\d+)/))return b[1] >= "4.0.249.4" || 1 * b[1].split(".")[0] > 5;
        if ((b = a.match(/Safari\/(\d+\.\d+)/)) && !/iPhone/.test(a))return b[1] >= "525.13";
        if (/Opera/.test({}.toString.call(window.opera)))return opera.version() >= "10.00";
        if (b = a.match(/rv:(\d+\.\d+\.\d+)[^b].*Gecko\//))return b[1] >= "1.9.1";
        return!1
    }};
    for (var j in i)i[j] && f.feature(j, i[j].call(), !0);
    f.feature()
}(), function (a) {
    function z() {
        d || (d = !0, s(e, function (a) {
            p(a)
        }))
    }

    function y(c, d) {
        var e = a.createElement("script");
        e.type = "text/" + (c.type || "javascript"), e.src = c.src || c, e.async = !1, e.onreadystatechange = e.onload = function () {
            var a = e.readyState;
            !d.done && (!a || /loaded|complete/.test(a)) && (d.done = !0, d())
        }, (a.body || b).appendChild(e)
    }

    function x(a, b) {
        if (a.state == o)return b && b();
        if (a.state == n)return k.ready(a.name, b);
        if (a.state == m)return a.onpreload.push(function () {
            x(a, b)
        });
        a.state = n, y(a.url, function () {
            a.state = o, b && b(), s(g[a.name], function (a) {
                p(a)
            }), u() && d && s(g.ALL, function (a) {
                p(a)
            })
        })
    }

    function w(a, b) {
        a.state === undefined && (a.state = m, a.onpreload = [], y({src: a.url, type: "cache"}, function () {
            v(a)
        }))
    }

    function v(a) {
        a.state = l, s(a.onpreload, function (a) {
            a.call()
        })
    }

    function u(a) {
        a = a || h;
        var b;
        for (var c in a) {
            if (a.hasOwnProperty(c) && a[c].state != o)return!1;
            b = !0
        }
        return b
    }

    function t(a) {
        return Object.prototype.toString.call(a) == "[object Function]"
    }

    function s(a, b) {
        if (!!a) {
            typeof a == "object" && (a = [].slice.call(a));
            for (var c = 0; c < a.length; c++)b.call(a, a[c], c)
        }
    }

    function r(a) {
        var b;
        if (typeof a == "object")for (var c in a)a[c] && (b = {name: c, url: a[c]}); else b = {name: q(a), url: a};
        var d = h[b.name];
        if (d && d.url === b.url)return d;
        h[b.name] = b;
        return b
    }

    function q(a) {
        var b = a.split("/"), c = b[b.length - 1], d = c.indexOf("?");
        return d != -1 ? c.substring(0, d) : c
    }

    function p(a) {
        a._done || (a(), a._done = 1)
    }

    var b = a.documentElement, c, d, e = [], f = [], g = {}, h = {}, i = a.createElement("script").async === !0 || "MozAppearance"in a.documentElement.style || window.opera, j = window.head_conf && head_conf.head || "head", k = window[j] = window[j] || function () {
        k.ready.apply(null, arguments)
    }, l = 1, m = 2, n = 3, o = 4;
    i ? k.js = function () {
        var a = arguments, b = a[a.length - 1], c = {};
        t(b) || (b = null), s(a, function (d, e) {
            d != b && (d = r(d), c[d.name] = d, x(d, b && e == a.length - 2 ? function () {
                u(c) && p(b)
            } : null))
        });
        return k
    } : k.js = function () {
        var a = arguments, b = [].slice.call(a, 1), d = b[0];
        if (!c) {
            f.push(function () {
                k.js.apply(null, a)
            });
            return k
        }
        d ? (s(b, function (a) {
            t(a) || w(r(a))
        }), x(r(a[0]), t(d) ? d : function () {
            k.js.apply(null, b)
        })) : x(r(a[0]));
        return k
    }, k.ready = function (b, c) {
        if (b == a) {
            d ? p(c) : e.push(c);
            return k
        }
        t(b) && (c = b, b = "ALL");
        if (typeof b != "string" || !t(c))return k;
        var f = h[b];
        if (f && f.state == o || b == "ALL" && u() && d) {
            p(c);
            return k
        }
        var i = g[b];
        i ? i.push(c) : i = g[b] = [c];
        return k
    }, k.ready(a, function () {
        u() && s(g.ALL, function (a) {
            p(a)
        }), k.feature && k.feature("domloaded", !0)
    });
    if (window.addEventListener)a.addEventListener("DOMContentLoaded", z, !1), window.addEventListener("load", z, !1); else if (window.attachEvent) {
        a.attachEvent("onreadystatechange", function () {
            a.readyState === "complete" && z()
        });
        var A = 1;
        try {
            A = window.frameElement
        } catch (B) {
        }
        !A && b.doScroll && function () {
            try {
                b.doScroll("left"), z()
            } catch (a) {
                setTimeout(arguments.callee, 1);
                return
            }
        }(), window.attachEvent("onload", z)
    }
    !a.readyState && a.addEventListener && (a.readyState = "loading", a.addEventListener("DOMContentLoaded", handler = function () {
        a.removeEventListener("DOMContentLoaded", handler, !1), a.readyState = "complete"
    }, !1)), setTimeout(function () {
        c = !0, s(f, function (a) {
            a()
        })
    }, 300)
}(document);
