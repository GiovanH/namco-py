! function () {
    ! function (a, b) {
        "use strict";

        function c(a) {
            var b = a.length,
                c = fb.type(a);
            return fb.isWindow(a) ? false : 1 === a.nodeType && b ? true : "array" === c || "function" !== c && (0 === b || "number" == typeof b && b > 0 && b - 1 in a)
        }

        function d(a) {
            var b = ob[a] = {};
            return fb.each(a.match(hb) || [], function (a, c) {
                b[c] = true
            }), b
        }

        function e() {
            Object.defineProperty(this.cache = {}, 0, {
                get: function () {
                    return {}
                }
            }), this.expando = fb.expando + Math.random()
        }

        function f(a, c, d) {
            var e;
            if (d === b && 1 === a.nodeType)
                if (e = "data-" + c.replace(sb, "-$1").toLowerCase(), d = a.getAttribute(e), "string" == typeof d) {
                    try {
                        d = "true" === d ? true : "false" === d ? false : "null" === d ? null : +d + "" === d ? +d : rb.test(d) ? JSON.parse(d) : d
                    } catch (f) {}
                    pb.set(a, c, d)
                } else d = b;
            return d
        }

        function g() {
            return true
        }

        function h() {
            return false
        }

        function i() {
            try {
                return T.activeElement
            } catch (a) {}
        }

        function j(a, b) {
            for (;
                (a = a[b]) && 1 !== a.nodeType;);
            return a
        }

        function k(a, b, c) {
            if (fb.isFunction(b)) return fb.grep(a, function (a, d) {
                return !!b.call(a, d, a) !== c
            });
            if (b.nodeType) return fb.grep(a, function (a) {
                return a === b !== c
            });
            if ("string" == typeof b) {
                if (Cb.test(b)) return fb.filter(b, a, c);
                b = fb.filter(b, a)
            }
            return fb.grep(a, function (a) {
                return bb.call(b, a) >= 0 !== c
            })
        }

        function l(a, b) {
            return fb.nodeName(a, "table") && fb.nodeName(1 === b.nodeType ? b : b.firstChild, "tr") ? a.getElementsByTagName("tbody")[0] || a.appendChild(a.ownerDocument.createElement("tbody")) : a
        }

        function m(a) {
            return a.type = (null !== a.getAttribute("type")) + "/" + a.type, a
        }

        function n(a) {
            var b = Nb.exec(a.type);
            return b ? a.type = b[1] : a.removeAttribute("type"), a
        }

        function o(a, b) {
            for (var c = a.length, d = 0; c > d; d++) qb.set(a[d], "globalEval", !b || qb.get(b[d], "globalEval"))
        }

        function p(a, b) {
            var c, d, e, f, g, h, i, j;
            if (1 === b.nodeType) {
                if (qb.hasData(a) && (f = qb.access(a), g = qb.set(b, f), j = f.events)) {
                    delete g.handle, g.events = {};
                    for (e in j)
                        for (c = 0, d = j[e].length; d > c; c++) fb.event.add(b, e, j[e][c])
                }
                pb.hasData(a) && (h = pb.access(a), i = fb.extend({}, h), pb.set(b, i))
            }
        }

        function q(a, c) {
            var d = a.getElementsByTagName ? a.getElementsByTagName(c || "*") : a.querySelectorAll ? a.querySelectorAll(c || "*") : [];
            return c === b || c && fb.nodeName(a, c) ? fb.merge([a], d) : d
        }

        function r(a, b) {
            var c = b.nodeName.toLowerCase();
            "input" === c && Kb.test(a.type) ? b.checked = a.checked : ("input" === c || "textarea" === c) && (b.defaultValue = a.defaultValue)
        }

        function s(a, b) {
            if (b in a) return b;
            for (var c = b.charAt(0).toUpperCase() + b.slice(1), d = b, e = _b.length; e--;)
                if (b = _b[e] + c, b in a) return b;
            return d
        }

        function t(a, b) {
            return a = b || a, "none" === fb.css(a, "display") || !fb.contains(a.ownerDocument, a)
        }

        function u(b) {
            return a.getComputedStyle(b, null)
        }

        function v(a, b) {
            for (var c, d, e, f = [], g = 0, h = a.length; h > g; g++) d = a[g], d.style && (f[g] = qb.get(d, "olddisplay"), c = d.style.display, b ? (f[g] || "none" !== c || (d.style.display = ""), "" === d.style.display && t(d) && (f[g] = qb.access(d, "olddisplay", z(d.nodeName)))) : f[g] || (e = t(d), (c && "none" !== c || !e) && qb.set(d, "olddisplay", e ? c : fb.css(d, "display"))));
            for (g = 0; h > g; g++) d = a[g], d.style && (b && "none" !== d.style.display && "" !== d.style.display || (d.style.display = b ? f[g] || "" : "none"));
            return a
        }

        function w(a, b, c) {
            var d = Ub.exec(b);
            return d ? Math.max(0, d[1] - (c || 0)) + (d[2] || "px") : b
        }

        function x(a, b, c, d, e) {
            for (var f = c === (d ? "border" : "content") ? 4 : "width" === b ? 1 : 0, g = 0; 4 > f; f += 2) "margin" === c && (g += fb.css(a, c + $b[f], true, e)), d ? ("content" === c && (g -= fb.css(a, "padding" + $b[f], true, e)), "margin" !== c && (g -= fb.css(a, "border" + $b[f] + "Width", true, e))) : (g += fb.css(a, "padding" + $b[f], true, e), "padding" !== c && (g += fb.css(a, "border" + $b[f] + "Width", true, e)));
            return g
        }

        function y(a, b, c) {
            var d = true,
                e = "width" === b ? a.offsetWidth : a.offsetHeight,
                f = u(a),
                g = fb.support.boxSizing && "border-box" === fb.css(a, "boxSizing", false, f);
            if (0 >= e || null == e) {
                if (e = Qb(a, b, f), (0 > e || null == e) && (e = a.style[b]), Vb.test(e)) return e;
                d = g && (fb.support.boxSizingReliable || e === a.style[b]), e = parseFloat(e) || 0
            }
            return e + x(a, b, c || (g ? "border" : "content"), d, f) + "px"
        }

        function z(a) {
            var b = T,
                c = Xb[a];
            return c || (c = A(a, b), "none" !== c && c || (Rb = (Rb || fb("<iframe frameborder='0' width='0' height='0'/>").css("cssText", "display:block !important")).appendTo(b.documentElement), b = (Rb[0].contentWindow || Rb[0].contentDocument).document, b.write("<!doctype html><html><body>"), b.close(), c = A(a, b), Rb.detach()), Xb[a] = c), c
        }

        function A(a, b) {
            var c = fb(b.createElement(a)).appendTo(b.body),
                d = fb.css(c[0], "display");
            return c.remove(), d
        }

        function B(a, b, c, d) {
            var e;
            if (fb.isArray(b)) fb.each(b, function (b, e) {
                c || bc.test(a) ? d(a, e) : B(a + "[" + ("object" == typeof e ? b : "") + "]", e, c, d)
            });
            else if (c || "object" !== fb.type(b)) d(a, b);
            else
                for (e in b) B(a + "[" + e + "]", b[e], c, d)
        }

        function C(a) {
            return function (b, c) {
                "string" != typeof b && (c = b, b = "*");
                var d, e = 0,
                    f = b.toLowerCase().match(hb) || [];
                if (fb.isFunction(c))
                    for (; d = f[e++];) "+" === d[0] ? (d = d.slice(1) || "*", (a[d] = a[d] || []).unshift(c)) : (a[d] = a[d] || []).push(c)
            }
        }

        function D(a, b, c, d) {
            function e(h) {
                var i;
                return f[h] = true, fb.each(a[h] || [], function (a, h) {
                    var j = h(b, c, d);
                    return "string" != typeof j || g || f[j] ? g ? !(i = j) : void 0 : (b.dataTypes.unshift(j), e(j), false)
                }), i
            }
            var f = {}, g = a === sc;
            return e(b.dataTypes[0]) || !f["*"] && e("*")
        }

        function E(a, c) {
            var d, e, f = fb.ajaxSettings.flatOptions || {};
            for (d in c) c[d] !== b && ((f[d] ? a : e || (e = {}))[d] = c[d]);
            return e && fb.extend(true, a, e), a
        }

        function F(a, c, d) {
            for (var e, f, g, h, i = a.contents, j = a.dataTypes;
                "*" === j[0];) j.shift(), e === b && (e = a.mimeType || c.getResponseHeader("Content-Type"));
            if (e)
                for (f in i)
                    if (i[f] && i[f].test(e)) {
                        j.unshift(f);
                        break
                    }
            if (j[0] in d) g = j[0];
            else {
                for (f in d) {
                    if (!j[0] || a.converters[f + " " + j[0]]) {
                        g = f;
                        break
                    }
                    h || (h = f)
                }
                g = g || h
            }
            return g ? (g !== j[0] && j.unshift(g), d[g]) : void 0
        }

        function G(a, b, c, d) {
            var e, f, g, h, i, j = {}, k = a.dataTypes.slice();
            if (k[1])
                for (g in a.converters) j[g.toLowerCase()] = a.converters[g];
            for (f = k.shift(); f;)
                if (a.responseFields[f] && (c[a.responseFields[f]] = b), !i && d && a.dataFilter && (b = a.dataFilter(b, a.dataType)), i = f, f = k.shift())
                    if ("*" === f) f = i;
                    else if ("*" !== i && i !== f) {
                if (g = j[i + " " + f] || j["* " + f], !g)
                    for (e in j)
                        if (h = e.split(" "), h[1] === f && (g = j[i + " " + h[0]] || j["* " + h[0]])) {
                            g === true ? g = j[e] : j[e] !== true && (f = h[0], k.unshift(h[1]));
                            break
                        }
                if (g !== true)
                    if (g && a["throws"]) b = g(b);
                    else try {
                        b = g(b)
                    } catch (l) {
                        return {
                            state: "parsererror",
                            error: g ? l : "No conversion from " + i + " to " + f
                        }
                    }
            }
            return {
                state: "success",
                data: b
            }
        }

        function H() {
            return setTimeout(function () {
                Bc = b
            }), Bc = fb.now()
        }

        function I(a, b, c) {
            for (var d, e = (Hc[b] || []).concat(Hc["*"]), f = 0, g = e.length; g > f; f++)
                if (d = e[f].call(c, b, a)) return d
        }

        function J(a, b, c) {
            var d, e, f = 0,
                g = Gc.length,
                h = fb.Deferred().always(function () {
                    delete i.elem
                }),
                i = function () {
                    if (e) return false;
                    for (var b = Bc || H(), c = Math.max(0, j.startTime + j.duration - b), d = c / j.duration || 0, f = 1 - d, g = 0, i = j.tweens.length; i > g; g++) j.tweens[g].run(f);
                    return h.notifyWith(a, [j, f, c]), 1 > f && i ? c : (h.resolveWith(a, [j]), false)
                }, j = h.promise({
                    elem: a,
                    props: fb.extend({}, b),
                    opts: fb.extend(true, {
                        specialEasing: {}
                    }, c),
                    originalProperties: b,
                    originalOptions: c,
                    startTime: Bc || H(),
                    duration: c.duration,
                    tweens: [],
                    createTween: function (b, c) {
                        var d = fb.Tween(a, j.opts, b, c, j.opts.specialEasing[b] || j.opts.easing);
                        return j.tweens.push(d), d
                    },
                    stop: function (b) {
                        var c = 0,
                            d = b ? j.tweens.length : 0;
                        if (e) return this;
                        for (e = true; d > c; c++) j.tweens[c].run(1);
                        return b ? h.resolveWith(a, [j, b]) : h.rejectWith(a, [j, b]), this
                    }
                }),
                k = j.props;
            for (K(k, j.opts.specialEasing); g > f; f++)
                if (d = Gc[f].call(j, a, k, j.opts)) return d;
            return fb.map(k, I, j), fb.isFunction(j.opts.start) && j.opts.start.call(a, j), fb.fx.timer(fb.extend(i, {
                elem: a,
                anim: j,
                queue: j.opts.queue
            })), j.progress(j.opts.progress).done(j.opts.done, j.opts.complete).fail(j.opts.fail).always(j.opts.always)
        }

        function K(a, b) {
            var c, d, e, f, g;
            for (c in a)
                if (d = fb.camelCase(c), e = b[d], f = a[c], fb.isArray(f) && (e = f[1], f = a[c] = f[0]), c !== d && (a[d] = f, delete a[c]), g = fb.cssHooks[d], g && "expand" in g) {
                    f = g.expand(f), delete a[d];
                    for (c in f) c in a || (a[c] = f[c], b[c] = e)
                } else b[d] = e
        }

        function L(a, c, d) {
            var e, f, g, h, i, j, k = this,
                l = {}, m = a.style,
                n = a.nodeType && t(a),
                o = qb.get(a, "fxshow");
            d.queue || (i = fb._queueHooks(a, "fx"), null == i.unqueued && (i.unqueued = 0, j = i.empty.fire, i.empty.fire = function () {
                i.unqueued || j()
            }), i.unqueued++, k.always(function () {
                k.always(function () {
                    i.unqueued--, fb.queue(a, "fx").length || i.empty.fire()
                })
            })), 1 === a.nodeType && ("height" in c || "width" in c) && (d.overflow = [m.overflow, m.overflowX, m.overflowY], "inline" === fb.css(a, "display") && "none" === fb.css(a, "float") && (m.display = "inline-block")), d.overflow && (m.overflow = "hidden", k.always(function () {
                m.overflow = d.overflow[0], m.overflowX = d.overflow[1], m.overflowY = d.overflow[2]
            }));
            for (e in c)
                if (f = c[e], Dc.exec(f)) {
                    if (delete c[e], g = g || "toggle" === f, f === (n ? "hide" : "show")) {
                        if ("show" !== f || !o || o[e] === b) continue;
                        n = true
                    }
                    l[e] = o && o[e] || fb.style(a, e)
                }
            if (!fb.isEmptyObject(l)) {
                o ? "hidden" in o && (n = o.hidden) : o = qb.access(a, "fxshow", {}), g && (o.hidden = !n), n ? fb(a).show() : k.done(function () {
                    fb(a).hide()
                }), k.done(function () {
                    var b;
                    qb.remove(a, "fxshow");
                    for (b in l) fb.style(a, b, l[b])
                });
                for (e in l) h = I(n ? o[e] : 0, e, k), e in o || (o[e] = h.start, n && (h.end = h.start, h.start = "width" === e || "height" === e ? 1 : 0))
            }
        }

        function M(a, b, c, d, e) {
            return new M.prototype.init(a, b, c, d, e)
        }

        function N(a, b) {
            var c, d = {
                    height: a
                }, e = 0;
            for (b = b ? 1 : 0; 4 > e; e += 2 - b) c = $b[e], d["margin" + c] = d["padding" + c] = a;
            return b && (d.opacity = d.width = a), d
        }

        function O(a) {
            return fb.isWindow(a) ? a : 9 === a.nodeType && a.defaultView
        }
        var P, Q, R = typeof b,
            S = a.location,
            T = a.document,
            U = T.documentElement,
            V = a.jQuery,
            W = a.$,
            X = {}, Y = [],
            Z = "2.0.3",
            $ = Y.concat,
            _ = Y.push,
            ab = Y.slice,
            bb = Y.indexOf,
            cb = X.toString,
            db = X.hasOwnProperty,
            eb = Z.trim,
            fb = function (a, b) {
                return new fb.fn.init(a, b, P)
            }, gb = /[+-]?(?:\d*\.|)\d+(?:[eE][+-]?\d+|)/.source,
            hb = /\S+/g,
            ib = /^(?:\s*(<[\w\W]+>)[^>]*|#([\w-]*))$/,
            jb = /^<(\w+)\s*\/?>(?:<\/\1>|)$/,
            kb = /^-ms-/,
            lb = /-([\da-z])/gi,
            mb = function (a, b) {
                return b.toUpperCase()
            }, nb = function () {
                T.removeEventListener("DOMContentLoaded", nb, false), a.removeEventListener("load", nb, false), fb.ready()
            };
        fb.fn = fb.prototype = {
            jquery: Z,
            constructor: fb,
            init: function (a, c, d) {
                var e, f;
                if (!a) return this;
                if ("string" == typeof a) {
                    if (e = "<" === a.charAt(0) && ">" === a.charAt(a.length - 1) && a.length >= 3 ? [null, a, null] : ib.exec(a), !e || !e[1] && c) return !c || c.jquery ? (c || d).find(a) : this.constructor(c).find(a);
                    if (e[1]) {
                        if (c = c instanceof fb ? c[0] : c, fb.merge(this, fb.parseHTML(e[1], c && c.nodeType ? c.ownerDocument || c : T, true)), jb.test(e[1]) && fb.isPlainObject(c))
                            for (e in c) fb.isFunction(this[e]) ? this[e](c[e]) : this.attr(e, c[e]);
                        return this
                    }
                    return f = T.getElementById(e[2]), f && f.parentNode && (this.length = 1, this[0] = f), this.context = T, this.selector = a, this
                }
                return a.nodeType ? (this.context = this[0] = a, this.length = 1, this) : fb.isFunction(a) ? d.ready(a) : (a.selector !== b && (this.selector = a.selector, this.context = a.context), fb.makeArray(a, this))
            },
            selector: "",
            length: 0,
            toArray: function () {
                return ab.call(this)
            },
            get: function (a) {
                return null == a ? this.toArray() : 0 > a ? this[this.length + a] : this[a]
            },
            pushStack: function (a) {
                var b = fb.merge(this.constructor(), a);
                return b.prevObject = this, b.context = this.context, b
            },
            each: function (a, b) {
                return fb.each(this, a, b)
            },
            ready: function (a) {
                return fb.ready.promise().done(a), this
            },
            slice: function () {
                return this.pushStack(ab.apply(this, arguments))
            },
            first: function () {
                return this.eq(0)
            },
            last: function () {
                return this.eq(-1)
            },
            eq: function (a) {
                var b = this.length,
                    c = +a + (0 > a ? b : 0);
                return this.pushStack(c >= 0 && b > c ? [this[c]] : [])
            },
            map: function (a) {
                return this.pushStack(fb.map(this, function (b, c) {
                    return a.call(b, c, b)
                }))
            },
            end: function () {
                return this.prevObject || this.constructor(null)
            },
            push: _,
            sort: [].sort,
            splice: [].splice
        }, fb.fn.init.prototype = fb.fn, fb.extend = fb.fn.extend = function () {
            var a, c, d, e, f, g, h = arguments[0] || {}, i = 1,
                j = arguments.length,
                k = false;
            for ("boolean" == typeof h && (k = h, h = arguments[1] || {}, i = 2), "object" == typeof h || fb.isFunction(h) || (h = {}), j === i && (h = this, --i); j > i; i++)
                if (null != (a = arguments[i]))
                    for (c in a) d = h[c], e = a[c], h !== e && (k && e && (fb.isPlainObject(e) || (f = fb.isArray(e))) ? (f ? (f = false, g = d && fb.isArray(d) ? d : []) : g = d && fb.isPlainObject(d) ? d : {}, h[c] = fb.extend(k, g, e)) : e !== b && (h[c] = e));
            return h
        }, fb.extend({
            expando: "jQuery" + (Z + Math.random()).replace(/\D/g, ""),
            noConflict: function (b) {
                return a.$ === fb && (a.$ = W), b && a.jQuery === fb && (a.jQuery = V), fb
            },
            isReady: false,
            readyWait: 1,
            holdReady: function (a) {
                a ? fb.readyWait++ : fb.ready(true)
            },
            ready: function (a) {
                (a === true ? --fb.readyWait : fb.isReady) || (fb.isReady = true, a !== true && --fb.readyWait > 0 || (Q.resolveWith(T, [fb]), fb.fn.trigger && fb(T).trigger("ready").off("ready")))
            },
            isFunction: function (a) {
                return "function" === fb.type(a)
            },
            isArray: Array.isArray,
            isWindow: function (a) {
                return null != a && a === a.window
            },
            isNumeric: function (a) {
                return !isNaN(parseFloat(a)) && isFinite(a)
            },
            type: function (a) {
                return null == a ? String(a) : "object" == typeof a || "function" == typeof a ? X[cb.call(a)] || "object" : typeof a
            },
            isPlainObject: function (a) {
                if ("object" !== fb.type(a) || a.nodeType || fb.isWindow(a)) return false;
                try {
                    if (a.constructor && !db.call(a.constructor.prototype, "isPrototypeOf")) return false
                } catch (b) {
                    return false
                }
                return true
            },
            isEmptyObject: function (a) {
                var b;
                for (b in a) return false;
                return true
            },
            error: function (a) {
                throw new Error(a)
            },
            parseHTML: function (a, b, c) {
                if (!a || "string" != typeof a) return null;
                "boolean" == typeof b && (c = b, b = false), b = b || T;
                var d = jb.exec(a),
                    e = !c && [];
                return d ? [b.createElement(d[1])] : (d = fb.buildFragment([a], b, e), e && fb(e).remove(), fb.merge([], d.childNodes))
            },
            parseJSON: JSON.parse,
            parseXML: function (a) {
                var c, d;
                if (!a || "string" != typeof a) return null;
                try {
                    d = new DOMParser, c = d.parseFromString(a, "text/xml")
                } catch (e) {
                    c = b
                }
                return (!c || c.getElementsByTagName("parsererror").length) && fb.error("Invalid XML: " + a), c
            },
            noop: function () {},
            globalEval: function (a) {
                var b, c = eval;
                a = fb.trim(a), a && (1 === a.indexOf("use strict") ? (b = T.createElement("script"), b.text = a, T.head.appendChild(b).parentNode.removeChild(b)) : c(a))
            },
            camelCase: function (a) {
                return a.replace(kb, "ms-").replace(lb, mb)
            },
            nodeName: function (a, b) {
                return a.nodeName && a.nodeName.toLowerCase() === b.toLowerCase()
            },
            each: function (a, b, d) {
                var e, f = 0,
                    g = a.length,
                    h = c(a);
                if (d) {
                    if (h)
                        for (; g > f && (e = b.apply(a[f], d), e !== false); f++);
                    else
                        for (f in a)
                            if (e = b.apply(a[f], d), e === false) break
                } else if (h)
                    for (; g > f && (e = b.call(a[f], f, a[f]), e !== false); f++);
                else
                    for (f in a)
                        if (e = b.call(a[f], f, a[f]), e === false) break; return a
            },
            trim: function (a) {
                return null == a ? "" : eb.call(a)
            },
            makeArray: function (a, b) {
                var d = b || [];
                return null != a && (c(Object(a)) ? fb.merge(d, "string" == typeof a ? [a] : a) : _.call(d, a)), d
            },
            inArray: function (a, b, c) {
                return null == b ? -1 : bb.call(b, a, c)
            },
            merge: function (a, c) {
                var d = c.length,
                    e = a.length,
                    f = 0;
                if ("number" == typeof d)
                    for (; d > f; f++) a[e++] = c[f];
                else
                    for (; c[f] !== b;) a[e++] = c[f++];
                return a.length = e, a
            },
            grep: function (a, b, c) {
                var d, e = [],
                    f = 0,
                    g = a.length;
                for (c = !! c; g > f; f++) d = !! b(a[f], f), c !== d && e.push(a[f]);
                return e
            },
            map: function (a, b, d) {
                var e, f = 0,
                    g = a.length,
                    h = c(a),
                    i = [];
                if (h)
                    for (; g > f; f++) e = b(a[f], f, d), null != e && (i[i.length] = e);
                else
                    for (f in a) e = b(a[f], f, d), null != e && (i[i.length] = e);
                return $.apply([], i)
            },
            guid: 1,
            proxy: function (a, c) {
                var d, e, f;
                return "string" == typeof c && (d = a[c], c = a, a = d), fb.isFunction(a) ? (e = ab.call(arguments, 2), f = function () {
                    return a.apply(c || this, e.concat(ab.call(arguments)))
                }, f.guid = a.guid = a.guid || fb.guid++, f) : b
            },
            access: function (a, c, d, e, f, g, h) {
                var i = 0,
                    j = a.length,
                    k = null == d;
                if ("object" === fb.type(d)) {
                    f = true;
                    for (i in d) fb.access(a, c, i, d[i], true, g, h)
                } else if (e !== b && (f = true, fb.isFunction(e) || (h = true), k && (h ? (c.call(a, e), c = null) : (k = c, c = function (a, b, c) {
                    return k.call(fb(a), c)
                })), c))
                    for (; j > i; i++) c(a[i], d, h ? e : e.call(a[i], i, c(a[i], d)));
                return f ? a : k ? c.call(a) : j ? c(a[0], d) : g
            },
            now: Date.now,
            swap: function (a, b, c, d) {
                var e, f, g = {};
                for (f in b) g[f] = a.style[f], a.style[f] = b[f];
                e = c.apply(a, d || []);
                for (f in b) a.style[f] = g[f];
                return e
            }
        }), fb.ready.promise = function (b) {
            return Q || (Q = fb.Deferred(), "complete" === T.readyState ? setTimeout(fb.ready) : (T.addEventListener("DOMContentLoaded", nb, false), a.addEventListener("load", nb, false))), Q.promise(b)
        }, fb.each("Boolean Number String Function Array Date RegExp Object Error".split(" "), function (a, b) {
            X["[object " + b + "]"] = b.toLowerCase()
        }), P = fb(T),
        function (a, b) {
            function c(a, b, c, d) {
                var e, f, g, h, i, j, k, l, o, p;
                if ((b ? b.ownerDocument || b : O) !== G && F(b), b = b || G, c = c || [], !a || "string" != typeof a) return c;
                if (1 !== (h = b.nodeType) && 9 !== h) return [];
                if (I && !d) {
                    if (e = tb.exec(a))
                        if (g = e[1]) {
                            if (9 === h) {
                                if (f = b.getElementById(g), !f || !f.parentNode) return c;
                                if (f.id === g) return c.push(f), c
                            } else if (b.ownerDocument && (f = b.ownerDocument.getElementById(g)) && M(b, f) && f.id === g) return c.push(f), c
                        } else {
                            if (e[2]) return ab.apply(c, b.getElementsByTagName(a)), c;
                            if ((g = e[3]) && x.getElementsByClassName && b.getElementsByClassName) return ab.apply(c, b.getElementsByClassName(g)), c
                        }
                    if (x.qsa && (!J || !J.test(a))) {
                        if (l = k = N, o = b, p = 9 === h && a, 1 === h && "object" !== b.nodeName.toLowerCase()) {
                            for (j = m(a), (k = b.getAttribute("id")) ? l = k.replace(wb, "\\$&") : b.setAttribute("id", l), l = "[id='" + l + "'] ", i = j.length; i--;) j[i] = l + n(j[i]);
                            o = nb.test(a) && b.parentNode || b, p = j.join(",")
                        }
                        if (p) try {
                            return ab.apply(c, o.querySelectorAll(p)), c
                        } catch (q) {} finally {
                            k || b.removeAttribute("id")
                        }
                    }
                }
                return v(a.replace(kb, "$1"), b, c, d)
            }

            function d() {
                function a(c, d) {
                    return b.push(c += " ") > z.cacheLength && delete a[b.shift()], a[c] = d
                }
                var b = [];
                return a
            }

            function e(a) {
                return a[N] = true, a
            }

            function f(a) {
                var b = G.createElement("div");
                try {
                    return !!a(b)
                } catch (c) {
                    return false
                } finally {
                    b.parentNode && b.parentNode.removeChild(b), b = null
                }
            }

            function g(a, b) {
                for (var c = a.split("|"), d = a.length; d--;) z.attrHandle[c[d]] = b
            }

            function h(a, b) {
                var c = b && a,
                    d = c && 1 === a.nodeType && 1 === b.nodeType && (~b.sourceIndex || X) - (~a.sourceIndex || X);
                if (d) return d;
                if (c)
                    for (; c = c.nextSibling;)
                        if (c === b) return -1;
                return a ? 1 : -1
            }

            function i(a) {
                return function (b) {
                    var c = b.nodeName.toLowerCase();
                    return "input" === c && b.type === a
                }
            }

            function j(a) {
                return function (b) {
                    var c = b.nodeName.toLowerCase();
                    return ("input" === c || "button" === c) && b.type === a
                }
            }

            function k(a) {
                return e(function (b) {
                    return b = +b, e(function (c, d) {
                        for (var e, f = a([], c.length, b), g = f.length; g--;) c[e = f[g]] && (c[e] = !(d[e] = c[e]))
                    })
                })
            }

            function l() {}

            function m(a, b) {
                var d, e, f, g, h, i, j, k = S[a + " "];
                if (k) return b ? 0 : k.slice(0);
                for (h = a, i = [], j = z.preFilter; h;) {
                    (!d || (e = lb.exec(h))) && (e && (h = h.slice(e[0].length) || h), i.push(f = [])), d = false, (e = mb.exec(h)) && (d = e.shift(), f.push({
                        value: d,
                        type: e[0].replace(kb, " ")
                    }), h = h.slice(d.length));
                    for (g in z.filter)!(e = rb[g].exec(h)) || j[g] && !(e = j[g](e)) || (d = e.shift(), f.push({
                        value: d,
                        type: g,
                        matches: e
                    }), h = h.slice(d.length));
                    if (!d) break
                }
                return b ? h.length : h ? c.error(a) : S(a, i).slice(0)
            }

            function n(a) {
                for (var b = 0, c = a.length, d = ""; c > b; b++) d += a[b].value;
                return d
            }

            function o(a, b, c) {
                var d = b.dir,
                    e = c && "parentNode" === d,
                    f = Q++;
                return b.first ? function (b, c, f) {
                    for (; b = b[d];)
                        if (1 === b.nodeType || e) return a(b, c, f)
                } : function (b, c, g) {
                    var h, i, j, k = P + " " + f;
                    if (g) {
                        for (; b = b[d];)
                            if ((1 === b.nodeType || e) && a(b, c, g)) return true
                    } else
                        for (; b = b[d];)
                            if (1 === b.nodeType || e)
                                if (j = b[N] || (b[N] = {}), (i = j[d]) && i[0] === k) {
                                    if ((h = i[1]) === true || h === y) return h === true
                                } else if (i = j[d] = [k], i[1] = a(b, c, g) || y, i[1] === true) return true
                }
            }

            function p(a) {
                return a.length > 1 ? function (b, c, d) {
                    for (var e = a.length; e--;)
                        if (!a[e](b, c, d)) return false;
                    return true
                } : a[0]
            }

            function q(a, b, c, d, e) {
                for (var f, g = [], h = 0, i = a.length, j = null != b; i > h; h++)(f = a[h]) && (!c || c(f, d, e)) && (g.push(f), j && b.push(h));
                return g
            }

            function r(a, b, c, d, f, g) {
                return d && !d[N] && (d = r(d)), f && !f[N] && (f = r(f, g)), e(function (e, g, h, i) {
                    var j, k, l, m = [],
                        n = [],
                        o = g.length,
                        p = e || u(b || "*", h.nodeType ? [h] : h, []),
                        r = !a || !e && b ? p : q(p, m, a, h, i),
                        s = c ? f || (e ? a : o || d) ? [] : g : r;
                    if (c && c(r, s, h, i), d)
                        for (j = q(s, n), d(j, [], h, i), k = j.length; k--;)(l = j[k]) && (s[n[k]] = !(r[n[k]] = l));
                    if (e) {
                        if (f || a) {
                            if (f) {
                                for (j = [], k = s.length; k--;)(l = s[k]) && j.push(r[k] = l);
                                f(null, s = [], j, i)
                            }
                            for (k = s.length; k--;)(l = s[k]) && (j = f ? cb.call(e, l) : m[k]) > -1 && (e[j] = !(g[j] = l))
                        }
                    } else s = q(s === g ? s.splice(o, s.length) : s), f ? f(null, g, s, i) : ab.apply(g, s)
                })
            }

            function s(a) {
                for (var b, c, d, e = a.length, f = z.relative[a[0].type], g = f || z.relative[" "], h = f ? 1 : 0, i = o(function (a) {
                        return a === b
                    }, g, true), j = o(function (a) {
                        return cb.call(b, a) > -1
                    }, g, true), k = [
                        function (a, c, d) {
                            return !f && (d || c !== D) || ((b = c).nodeType ? i(a, c, d) : j(a, c, d))
                        }
                    ]; e > h; h++)
                    if (c = z.relative[a[h].type]) k = [o(p(k), c)];
                    else {
                        if (c = z.filter[a[h].type].apply(null, a[h].matches), c[N]) {
                            for (d = ++h; e > d && !z.relative[a[d].type]; d++);
                            return r(h > 1 && p(k), h > 1 && n(a.slice(0, h - 1).concat({
                                value: " " === a[h - 2].type ? "*" : ""
                            })).replace(kb, "$1"), c, d > h && s(a.slice(h, d)), e > d && s(a = a.slice(d)), e > d && n(a))
                        }
                        k.push(c)
                    }
                return p(k)
            }

            function t(a, b) {
                var d = 0,
                    f = b.length > 0,
                    g = a.length > 0,
                    h = function (e, h, i, j, k) {
                        var l, m, n, o = [],
                            p = 0,
                            r = "0",
                            s = e && [],
                            t = null != k,
                            u = D,
                            v = e || g && z.find.TAG("*", k && h.parentNode || h),
                            w = P += null == u ? 1 : Math.random() || .1;
                        for (t && (D = h !== G && h, y = d); null != (l = v[r]); r++) {
                            if (g && l) {
                                for (m = 0; n = a[m++];)
                                    if (n(l, h, i)) {
                                        j.push(l);
                                        break
                                    }
                                t && (P = w, y = ++d)
                            }
                            f && ((l = !n && l) && p--, e && s.push(l))
                        }
                        if (p += r, f && r !== p) {
                            for (m = 0; n = b[m++];) n(s, o, h, i);
                            if (e) {
                                if (p > 0)
                                    for (; r--;) s[r] || o[r] || (o[r] = $.call(j));
                                o = q(o)
                            }
                            ab.apply(j, o), t && !e && o.length > 0 && p + b.length > 1 && c.uniqueSort(j)
                        }
                        return t && (P = w, D = u), s
                    };
                return f ? e(h) : h
            }

            function u(a, b, d) {
                for (var e = 0, f = b.length; f > e; e++) c(a, b[e], d);
                return d
            }

            function v(a, b, c, d) {
                var e, f, g, h, i, j = m(a);
                if (!d && 1 === j.length) {
                    if (f = j[0] = j[0].slice(0), f.length > 2 && "ID" === (g = f[0]).type && x.getById && 9 === b.nodeType && I && z.relative[f[1].type]) {
                        if (b = (z.find.ID(g.matches[0].replace(xb, yb), b) || [])[0], !b) return c;
                        a = a.slice(f.shift().value.length)
                    }
                    for (e = rb.needsContext.test(a) ? 0 : f.length; e-- && (g = f[e], !z.relative[h = g.type]);)
                        if ((i = z.find[h]) && (d = i(g.matches[0].replace(xb, yb), nb.test(f[0].type) && b.parentNode || b))) {
                            if (f.splice(e, 1), a = d.length && n(f), !a) return ab.apply(c, d), c;
                            break
                        }
                }
                return C(a, j)(d, b, !I, c, nb.test(a)), c
            }
            var w, x, y, z, A, B, C, D, E, F, G, H, I, J, K, L, M, N = "sizzle" + -new Date,
                O = a.document,
                P = 0,
                Q = 0,
                R = d(),
                S = d(),
                T = d(),
                U = false,
                V = function (a, b) {
                    return a === b ? (U = true, 0) : 0
                }, W = typeof b,
                X = 1 << 31,
                Y = {}.hasOwnProperty,
                Z = [],
                $ = Z.pop,
                _ = Z.push,
                ab = Z.push,
                bb = Z.slice,
                cb = Z.indexOf || function (a) {
                    for (var b = 0, c = this.length; c > b; b++)
                        if (this[b] === a) return b;
                    return -1
                }, db = "checked|selected|async|autofocus|autoplay|controls|defer|disabled|hidden|ismap|loop|multiple|open|readonly|required|scoped",
                eb = "[\\x20\\t\\r\\n\\f]",
                gb = "(?:\\\\.|[\\w-]|[^\\x00-\\xa0])+",
                hb = gb.replace("w", "w#"),
                ib = "\\[" + eb + "*(" + gb + ")" + eb + "*(?:([*^$|!~]?=)" + eb + "*(?:(['\"])((?:\\\\.|[^\\\\])*?)\\3|(" + hb + ")|)|)" + eb + "*\\]",
                jb = ":(" + gb + ")(?:\\(((['\"])((?:\\\\.|[^\\\\])*?)\\3|((?:\\\\.|[^\\\\()[\\]]|" + ib.replace(3, 8) + ")*)|.*)\\)|)",
                kb = new RegExp("^" + eb + "+|((?:^|[^\\\\])(?:\\\\.)*)" + eb + "+$", "g"),
                lb = new RegExp("^" + eb + "*," + eb + "*"),
                mb = new RegExp("^" + eb + "*([>+~]|" + eb + ")" + eb + "*"),
                nb = new RegExp(eb + "*[+~]"),
                ob = new RegExp("=" + eb + "*([^\\]'\"]*)" + eb + "*\\]", "g"),
                pb = new RegExp(jb),
                qb = new RegExp("^" + hb + "$"),
                rb = {
                    ID: new RegExp("^#(" + gb + ")"),
                    CLASS: new RegExp("^\\.(" + gb + ")"),
                    TAG: new RegExp("^(" + gb.replace("w", "w*") + ")"),
                    ATTR: new RegExp("^" + ib),
                    PSEUDO: new RegExp("^" + jb),
                    CHILD: new RegExp("^:(only|first|last|nth|nth-last)-(child|of-type)(?:\\(" + eb + "*(even|odd|(([+-]|)(\\d*)n|)" + eb + "*(?:([+-]|)" + eb + "*(\\d+)|))" + eb + "*\\)|)", "i"),
                    bool: new RegExp("^(?:" + db + ")$", "i"),
                    needsContext: new RegExp("^" + eb + "*[>+~]|:(even|odd|eq|gt|lt|nth|first|last)(?:\\(" + eb + "*((?:-\\d)?\\d*)" + eb + "*\\)|)(?=[^-]|$)", "i")
                }, sb = /^[^{]+\{\s*\[native \w/,
                tb = /^(?:#([\w-]+)|(\w+)|\.([\w-]+))$/,
                ub = /^(?:input|select|textarea|button)$/i,
                vb = /^h\d$/i,
                wb = /'|\\/g,
                xb = new RegExp("\\\\([\\da-f]{1,6}" + eb + "?|(" + eb + ")|.)", "ig"),
                yb = function (a, b, c) {
                    var d = "0x" + b - 65536;
                    return d !== d || c ? b : 0 > d ? String.fromCharCode(d + 65536) : String.fromCharCode(55296 | d >> 10, 56320 | 1023 & d)
                };
            try {
                ab.apply(Z = bb.call(O.childNodes), O.childNodes), Z[O.childNodes.length].nodeType
            } catch (zb) {
                ab = {
                    apply: Z.length ? function (a, b) {
                        _.apply(a, bb.call(b))
                    } : function (a, b) {
                        for (var c = a.length, d = 0; a[c++] = b[d++];);
                        a.length = c - 1
                    }
                }
            }
            B = c.isXML = function (a) {
                var b = a && (a.ownerDocument || a).documentElement;
                return b ? "HTML" !== b.nodeName : false
            }, x = c.support = {}, F = c.setDocument = function (a) {
                var b = a ? a.ownerDocument || a : O,
                    c = b.defaultView;
                return b !== G && 9 === b.nodeType && b.documentElement ? (G = b, H = b.documentElement, I = !B(b), c && c.attachEvent && c !== c.top && c.attachEvent("onbeforeunload", function () {
                    F()
                }), x.attributes = f(function (a) {
                    return a.className = "i", !a.getAttribute("className")
                }), x.getElementsByTagName = f(function (a) {
                    return a.appendChild(b.createComment("")), !a.getElementsByTagName("*").length
                }), x.getElementsByClassName = f(function (a) {
                    return a.innerHTML = "<div class='a'></div><div class='a i'></div>", a.firstChild.className = "i", 2 === a.getElementsByClassName("i").length
                }), x.getById = f(function (a) {
                    return H.appendChild(a).id = N, !b.getElementsByName || !b.getElementsByName(N).length
                }), x.getById ? (z.find.ID = function (a, b) {
                    if (typeof b.getElementById !== W && I) {
                        var c = b.getElementById(a);
                        return c && c.parentNode ? [c] : []
                    }
                }, z.filter.ID = function (a) {
                    var b = a.replace(xb, yb);
                    return function (a) {
                        return a.getAttribute("id") === b
                    }
                }) : (delete z.find.ID, z.filter.ID = function (a) {
                    var b = a.replace(xb, yb);
                    return function (a) {
                        var c = typeof a.getAttributeNode !== W && a.getAttributeNode("id");
                        return c && c.value === b
                    }
                }), z.find.TAG = x.getElementsByTagName ? function (a, b) {
                    return typeof b.getElementsByTagName !== W ? b.getElementsByTagName(a) : void 0
                } : function (a, b) {
                    var c, d = [],
                        e = 0,
                        f = b.getElementsByTagName(a);
                    if ("*" === a) {
                        for (; c = f[e++];) 1 === c.nodeType && d.push(c);
                        return d
                    }
                    return f
                }, z.find.CLASS = x.getElementsByClassName && function (a, b) {
                    return typeof b.getElementsByClassName !== W && I ? b.getElementsByClassName(a) : void 0
                }, K = [], J = [], (x.qsa = sb.test(b.querySelectorAll)) && (f(function (a) {
                    a.innerHTML = "<select><option selected=''></option></select>", a.querySelectorAll("[selected]").length || J.push("\\[" + eb + "*(?:value|" + db + ")"), a.querySelectorAll(":checked").length || J.push(":checked")
                }), f(function (a) {
                    var c = b.createElement("input");
                    c.setAttribute("type", "hidden"), a.appendChild(c).setAttribute("t", ""), a.querySelectorAll("[t^='']").length && J.push("[*^$]=" + eb + "*(?:''|\"\")"), a.querySelectorAll(":enabled").length || J.push(":enabled", ":disabled"), a.querySelectorAll("*,:x"), J.push(",.*:")
                })), (x.matchesSelector = sb.test(L = H.webkitMatchesSelector || H.mozMatchesSelector || H.oMatchesSelector || H.msMatchesSelector)) && f(function (a) {
                    x.disconnectedMatch = L.call(a, "div"), L.call(a, "[s!='']:x"), K.push("!=", jb)
                }), J = J.length && new RegExp(J.join("|")), K = K.length && new RegExp(K.join("|")), M = sb.test(H.contains) || H.compareDocumentPosition ? function (a, b) {
                    var c = 9 === a.nodeType ? a.documentElement : a,
                        d = b && b.parentNode;
                    return a === d || !(!d || 1 !== d.nodeType || !(c.contains ? c.contains(d) : a.compareDocumentPosition && 16 & a.compareDocumentPosition(d)))
                } : function (a, b) {
                    if (b)
                        for (; b = b.parentNode;)
                            if (b === a) return true;
                    return false
                }, V = H.compareDocumentPosition ? function (a, c) {
                    if (a === c) return U = true, 0;
                    var d = c.compareDocumentPosition && a.compareDocumentPosition && a.compareDocumentPosition(c);
                    return d ? 1 & d || !x.sortDetached && c.compareDocumentPosition(a) === d ? a === b || M(O, a) ? -1 : c === b || M(O, c) ? 1 : E ? cb.call(E, a) - cb.call(E, c) : 0 : 4 & d ? -1 : 1 : a.compareDocumentPosition ? -1 : 1
                } : function (a, c) {
                    var d, e = 0,
                        f = a.parentNode,
                        g = c.parentNode,
                        i = [a],
                        j = [c];
                    if (a === c) return U = true, 0;
                    if (!f || !g) return a === b ? -1 : c === b ? 1 : f ? -1 : g ? 1 : E ? cb.call(E, a) - cb.call(E, c) : 0;
                    if (f === g) return h(a, c);
                    for (d = a; d = d.parentNode;) i.unshift(d);
                    for (d = c; d = d.parentNode;) j.unshift(d);
                    for (; i[e] === j[e];) e++;
                    return e ? h(i[e], j[e]) : i[e] === O ? -1 : j[e] === O ? 1 : 0
                }, b) : G
            }, c.matches = function (a, b) {
                return c(a, null, null, b)
            }, c.matchesSelector = function (a, b) {
                if ((a.ownerDocument || a) !== G && F(a), b = b.replace(ob, "='$1']"), !(!x.matchesSelector || !I || K && K.test(b) || J && J.test(b))) try {
                    var d = L.call(a, b);
                    if (d || x.disconnectedMatch || a.document && 11 !== a.document.nodeType) return d
                } catch (e) {}
                return c(b, G, null, [a]).length > 0
            }, c.contains = function (a, b) {
                return (a.ownerDocument || a) !== G && F(a), M(a, b)
            }, c.attr = function (a, c) {
                (a.ownerDocument || a) !== G && F(a);
                var d = z.attrHandle[c.toLowerCase()],
                    e = d && Y.call(z.attrHandle, c.toLowerCase()) ? d(a, c, !I) : b;
                return e === b ? x.attributes || !I ? a.getAttribute(c) : (e = a.getAttributeNode(c)) && e.specified ? e.value : null : e
            }, c.error = function (a) {
                throw new Error("Syntax error, unrecognized expression: " + a)
            }, c.uniqueSort = function (a) {
                var b, c = [],
                    d = 0,
                    e = 0;
                if (U = !x.detectDuplicates, E = !x.sortStable && a.slice(0), a.sort(V), U) {
                    for (; b = a[e++];) b === a[e] && (d = c.push(e));
                    for (; d--;) a.splice(c[d], 1)
                }
                return a
            }, A = c.getText = function (a) {
                var b, c = "",
                    d = 0,
                    e = a.nodeType;
                if (e) {
                    if (1 === e || 9 === e || 11 === e) {
                        if ("string" == typeof a.textContent) return a.textContent;
                        for (a = a.firstChild; a; a = a.nextSibling) c += A(a)
                    } else if (3 === e || 4 === e) return a.nodeValue
                } else
                    for (; b = a[d]; d++) c += A(b);
                return c
            }, z = c.selectors = {
                cacheLength: 50,
                createPseudo: e,
                match: rb,
                attrHandle: {},
                find: {},
                relative: {
                    ">": {
                        dir: "parentNode",
                        first: true
                    },
                    " ": {
                        dir: "parentNode"
                    },
                    "+": {
                        dir: "previousSibling",
                        first: true
                    },
                    "~": {
                        dir: "previousSibling"
                    }
                },
                preFilter: {
                    ATTR: function (a) {
                        return a[1] = a[1].replace(xb, yb), a[3] = (a[4] || a[5] || "").replace(xb, yb), "~=" === a[2] && (a[3] = " " + a[3] + " "), a.slice(0, 4)
                    },
                    CHILD: function (a) {
                        return a[1] = a[1].toLowerCase(), "nth" === a[1].slice(0, 3) ? (a[3] || c.error(a[0]), a[4] = +(a[4] ? a[5] + (a[6] || 1) : 2 * ("even" === a[3] || "odd" === a[3])), a[5] = +(a[7] + a[8] || "odd" === a[3])) : a[3] && c.error(a[0]), a
                    },
                    PSEUDO: function (a) {
                        var c, d = !a[5] && a[2];
                        return rb.CHILD.test(a[0]) ? null : (a[3] && a[4] !== b ? a[2] = a[4] : d && pb.test(d) && (c = m(d, true)) && (c = d.indexOf(")", d.length - c) - d.length) && (a[0] = a[0].slice(0, c), a[2] = d.slice(0, c)), a.slice(0, 3))
                    }
                },
                filter: {
                    TAG: function (a) {
                        var b = a.replace(xb, yb).toLowerCase();
                        return "*" === a ? function () {
                            return true
                        } : function (a) {
                            return a.nodeName && a.nodeName.toLowerCase() === b
                        }
                    },
                    CLASS: function (a) {
                        var b = R[a + " "];
                        return b || (b = new RegExp("(^|" + eb + ")" + a + "(" + eb + "|$)")) && R(a, function (a) {
                            return b.test("string" == typeof a.className && a.className || typeof a.getAttribute !== W && a.getAttribute("class") || "")
                        })
                    },
                    ATTR: function (a, b, d) {
                        return function (e) {
                            var f = c.attr(e, a);
                            return null == f ? "!=" === b : b ? (f += "", "=" === b ? f === d : "!=" === b ? f !== d : "^=" === b ? d && 0 === f.indexOf(d) : "*=" === b ? d && f.indexOf(d) > -1 : "$=" === b ? d && f.slice(-d.length) === d : "~=" === b ? (" " + f + " ").indexOf(d) > -1 : "|=" === b ? f === d || f.slice(0, d.length + 1) === d + "-" : false) : true
                        }
                    },
                    CHILD: function (a, b, c, d, e) {
                        var f = "nth" !== a.slice(0, 3),
                            g = "last" !== a.slice(-4),
                            h = "of-type" === b;
                        return 1 === d && 0 === e ? function (a) {
                            return !!a.parentNode
                        } : function (b, c, i) {
                            var j, k, l, m, n, o, p = f !== g ? "nextSibling" : "previousSibling",
                                q = b.parentNode,
                                r = h && b.nodeName.toLowerCase(),
                                s = !i && !h;
                            if (q) {
                                if (f) {
                                    for (; p;) {
                                        for (l = b; l = l[p];)
                                            if (h ? l.nodeName.toLowerCase() === r : 1 === l.nodeType) return false;
                                        o = p = "only" === a && !o && "nextSibling"
                                    }
                                    return true
                                }
                                if (o = [g ? q.firstChild : q.lastChild], g && s) {
                                    for (k = q[N] || (q[N] = {}), j = k[a] || [], n = j[0] === P && j[1], m = j[0] === P && j[2], l = n && q.childNodes[n]; l = ++n && l && l[p] || (m = n = 0) || o.pop();)
                                        if (1 === l.nodeType && ++m && l === b) {
                                            k[a] = [P, n, m];
                                            break
                                        }
                                } else if (s && (j = (b[N] || (b[N] = {}))[a]) && j[0] === P) m = j[1];
                                else
                                    for (;
                                        (l = ++n && l && l[p] || (m = n = 0) || o.pop()) && ((h ? l.nodeName.toLowerCase() !== r : 1 !== l.nodeType) || !++m || (s && ((l[N] || (l[N] = {}))[a] = [P, m]), l !== b)););
                                return m -= e, m === d || 0 === m % d && m / d >= 0
                            }
                        }
                    },
                    PSEUDO: function (a, b) {
                        var d, f = z.pseudos[a] || z.setFilters[a.toLowerCase()] || c.error("unsupported pseudo: " + a);
                        return f[N] ? f(b) : f.length > 1 ? (d = [a, a, "", b], z.setFilters.hasOwnProperty(a.toLowerCase()) ? e(function (a, c) {
                            for (var d, e = f(a, b), g = e.length; g--;) d = cb.call(a, e[g]), a[d] = !(c[d] = e[g])
                        }) : function (a) {
                            return f(a, 0, d)
                        }) : f
                    }
                },
                pseudos: {
                    not: e(function (a) {
                        var b = [],
                            c = [],
                            d = C(a.replace(kb, "$1"));
                        return d[N] ? e(function (a, b, c, e) {
                            for (var f, g = d(a, null, e, []), h = a.length; h--;)(f = g[h]) && (a[h] = !(b[h] = f))
                        }) : function (a, e, f) {
                            return b[0] = a, d(b, null, f, c), !c.pop()
                        }
                    }),
                    has: e(function (a) {
                        return function (b) {
                            return c(a, b).length > 0
                        }
                    }),
                    contains: e(function (a) {
                        return function (b) {
                            return (b.textContent || b.innerText || A(b)).indexOf(a) > -1
                        }
                    }),
                    lang: e(function (a) {
                        return qb.test(a || "") || c.error("unsupported lang: " + a), a = a.replace(xb, yb).toLowerCase(),
                        function (b) {
                            var c;
                            do
                                if (c = I ? b.lang : b.getAttribute("xml:lang") || b.getAttribute("lang")) return c = c.toLowerCase(), c === a || 0 === c.indexOf(a + "-"); while ((b = b.parentNode) && 1 === b.nodeType);
                            return false
                        }
                    }),
                    target: function (b) {
                        var c = a.location && a.location.hash;
                        return c && c.slice(1) === b.id
                    },
                    root: function (a) {
                        return a === H
                    },
                    focus: function (a) {
                        return a === G.activeElement && (!G.hasFocus || G.hasFocus()) && !! (a.type || a.href || ~a.tabIndex)
                    },
                    enabled: function (a) {
                        return a.disabled === false
                    },
                    disabled: function (a) {
                        return a.disabled === true
                    },
                    checked: function (a) {
                        var b = a.nodeName.toLowerCase();
                        return "input" === b && !! a.checked || "option" === b && !! a.selected
                    },
                    selected: function (a) {
                        return a.parentNode && a.parentNode.selectedIndex, a.selected === true
                    },
                    empty: function (a) {
                        for (a = a.firstChild; a; a = a.nextSibling)
                            if (a.nodeName > "@" || 3 === a.nodeType || 4 === a.nodeType) return false;
                        return true
                    },
                    parent: function (a) {
                        return !z.pseudos.empty(a)
                    },
                    header: function (a) {
                        return vb.test(a.nodeName)
                    },
                    input: function (a) {
                        return ub.test(a.nodeName)
                    },
                    button: function (a) {
                        var b = a.nodeName.toLowerCase();
                        return "input" === b && "button" === a.type || "button" === b
                    },
                    text: function (a) {
                        var b;
                        return "input" === a.nodeName.toLowerCase() && "text" === a.type && (null == (b = a.getAttribute("type")) || b.toLowerCase() === a.type)
                    },
                    first: k(function () {
                        return [0]
                    }),
                    last: k(function (a, b) {
                        return [b - 1]
                    }),
                    eq: k(function (a, b, c) {
                        return [0 > c ? c + b : c]
                    }),
                    even: k(function (a, b) {
                        for (var c = 0; b > c; c += 2) a.push(c);
                        return a
                    }),
                    odd: k(function (a, b) {
                        for (var c = 1; b > c; c += 2) a.push(c);
                        return a
                    }),
                    lt: k(function (a, b, c) {
                        for (var d = 0 > c ? c + b : c; --d >= 0;) a.push(d);
                        return a
                    }),
                    gt: k(function (a, b, c) {
                        for (var d = 0 > c ? c + b : c; ++d < b;) a.push(d);
                        return a
                    })
                }
            }, z.pseudos.nth = z.pseudos.eq;
            for (w in {
                radio: true,
                checkbox: true,
                file: true,
                password: true,
                image: true
            }) z.pseudos[w] = i(w);
            for (w in {
                submit: true,
                reset: true
            }) z.pseudos[w] = j(w);
            l.prototype = z.filters = z.pseudos, z.setFilters = new l, C = c.compile = function (a, b) {
                var c, d = [],
                    e = [],
                    f = T[a + " "];
                if (!f) {
                    for (b || (b = m(a)), c = b.length; c--;) f = s(b[c]), f[N] ? d.push(f) : e.push(f);
                    f = T(a, t(e, d))
                }
                return f
            }, x.sortStable = N.split("").sort(V).join("") === N, x.detectDuplicates = U, F(), x.sortDetached = f(function (a) {
                return 1 & a.compareDocumentPosition(G.createElement("div"))
            }), f(function (a) {
                return a.innerHTML = "<a href='#'></a>", "#" === a.firstChild.getAttribute("href")
            }) || g("type|href|height|width", function (a, b, c) {
                return c ? void 0 : a.getAttribute(b, "type" === b.toLowerCase() ? 1 : 2)
            }), x.attributes && f(function (a) {
                return a.innerHTML = "<input/>", a.firstChild.setAttribute("value", ""), "" === a.firstChild.getAttribute("value")
            }) || g("value", function (a, b, c) {
                return c || "input" !== a.nodeName.toLowerCase() ? void 0 : a.defaultValue
            }), f(function (a) {
                return null == a.getAttribute("disabled")
            }) || g(db, function (a, b, c) {
                var d;
                return c ? void 0 : (d = a.getAttributeNode(b)) && d.specified ? d.value : a[b] === true ? b.toLowerCase() : null
            }), fb.find = c, fb.expr = c.selectors, fb.expr[":"] = fb.expr.pseudos, fb.unique = c.uniqueSort, fb.text = c.getText, fb.isXMLDoc = c.isXML, fb.contains = c.contains
        }(a);
        var ob = {};
        fb.Callbacks = function (a) {
            a = "string" == typeof a ? ob[a] || d(a) : fb.extend({}, a);
            var c, e, f, g, h, i, j = [],
                k = !a.once && [],
                l = function (b) {
                    for (c = a.memory && b, e = true, i = g || 0, g = 0, h = j.length, f = true; j && h > i; i++)
                        if (j[i].apply(b[0], b[1]) === false && a.stopOnFalse) {
                            c = false;
                            break
                        }
                    f = false, j && (k ? k.length && l(k.shift()) : c ? j = [] : m.disable())
                }, m = {
                    add: function () {
                        if (j) {
                            var b = j.length;
                            ! function d(b) {
                                fb.each(b, function (b, c) {
                                    var e = fb.type(c);
                                    "function" === e ? a.unique && m.has(c) || j.push(c) : c && c.length && "string" !== e && d(c)
                                })
                            }(arguments), f ? h = j.length : c && (g = b, l(c))
                        }
                        return this
                    },
                    remove: function () {
                        return j && fb.each(arguments, function (a, b) {
                            for (var c;
                                (c = fb.inArray(b, j, c)) > -1;) j.splice(c, 1), f && (h >= c && h--, i >= c && i--)
                        }), this
                    },
                    has: function (a) {
                        return a ? fb.inArray(a, j) > -1 : !(!j || !j.length)
                    },
                    empty: function () {
                        return j = [], h = 0, this
                    },
                    disable: function () {
                        return j = k = c = b, this
                    },
                    disabled: function () {
                        return !j
                    },
                    lock: function () {
                        return k = b, c || m.disable(), this
                    },
                    locked: function () {
                        return !k
                    },
                    fireWith: function (a, b) {
                        return !j || e && !k || (b = b || [], b = [a, b.slice ? b.slice() : b], f ? k.push(b) : l(b)), this
                    },
                    fire: function () {
                        return m.fireWith(this, arguments), this
                    },
                    fired: function () {
                        return !!e
                    }
                };
            return m
        }, fb.extend({
            Deferred: function (a) {
                var b = [
                    ["resolve", "done", fb.Callbacks("once memory"), "resolved"],
                    ["reject", "fail", fb.Callbacks("once memory"), "rejected"],
                    ["notify", "progress", fb.Callbacks("memory")]
                ],
                    c = "pending",
                    d = {
                        state: function () {
                            return c
                        },
                        always: function () {
                            return e.done(arguments).fail(arguments), this
                        },
                        then: function () {
                            var a = arguments;
                            return fb.Deferred(function (c) {
                                fb.each(b, function (b, f) {
                                    var g = f[0],
                                        h = fb.isFunction(a[b]) && a[b];
                                    e[f[1]](function () {
                                        var a = h && h.apply(this, arguments);
                                        a && fb.isFunction(a.promise) ? a.promise().done(c.resolve).fail(c.reject).progress(c.notify) : c[g + "With"](this === d ? c.promise() : this, h ? [a] : arguments)
                                    })
                                }), a = null
                            }).promise()
                        },
                        promise: function (a) {
                            return null != a ? fb.extend(a, d) : d
                        }
                    }, e = {};
                return d.pipe = d.then, fb.each(b, function (a, f) {
                    var g = f[2],
                        h = f[3];
                    d[f[1]] = g.add, h && g.add(function () {
                        c = h
                    }, b[1 ^ a][2].disable, b[2][2].lock), e[f[0]] = function () {
                        return e[f[0] + "With"](this === e ? d : this, arguments), this
                    }, e[f[0] + "With"] = g.fireWith
                }), d.promise(e), a && a.call(e, e), e
            },
            when: function (a) {
                var b, c, d, e = 0,
                    f = ab.call(arguments),
                    g = f.length,
                    h = 1 !== g || a && fb.isFunction(a.promise) ? g : 0,
                    i = 1 === h ? a : fb.Deferred(),
                    j = function (a, c, d) {
                        return function (e) {
                            c[a] = this, d[a] = arguments.length > 1 ? ab.call(arguments) : e, d === b ? i.notifyWith(c, d) : --h || i.resolveWith(c, d)
                        }
                    };
                if (g > 1)
                    for (b = new Array(g), c = new Array(g), d = new Array(g); g > e; e++) f[e] && fb.isFunction(f[e].promise) ? f[e].promise().done(j(e, d, f)).fail(i.reject).progress(j(e, c, b)) : --h;
                return h || i.resolveWith(d, f), i.promise()
            }
        }), fb.support = function (b) {
            var c = T.createElement("input"),
                d = T.createDocumentFragment(),
                e = T.createElement("div"),
                f = T.createElement("select"),
                g = f.appendChild(T.createElement("option"));
            return c.type ? (c.type = "checkbox", b.checkOn = "" !== c.value, b.optSelected = g.selected, b.reliableMarginRight = true, b.boxSizingReliable = true, b.pixelPosition = false, c.checked = true, b.noCloneChecked = c.cloneNode(true).checked, f.disabled = true, b.optDisabled = !g.disabled, c = T.createElement("input"), c.value = "t", c.type = "radio", b.radioValue = "t" === c.value, c.setAttribute("checked", "t"), c.setAttribute("name", "t"), d.appendChild(c), b.checkClone = d.cloneNode(true).cloneNode(true).lastChild.checked, b.focusinBubbles = "onfocusin" in a, e.style.backgroundClip = "content-box", e.cloneNode(true).style.backgroundClip = "", b.clearCloneStyle = "content-box" === e.style.backgroundClip, fb(function () {
                var c, d, f = "padding:0;margin:0;border:0;display:block;-webkit-box-sizing:content-box;-moz-box-sizing:content-box;box-sizing:content-box",
                    g = T.getElementsByTagName("body")[0];
                g && (c = T.createElement("div"), c.style.cssText = "border:0;width:0;height:0;position:absolute;top:0;left:-9999px;margin-top:1px", g.appendChild(c).appendChild(e), e.innerHTML = "", e.style.cssText = "-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;padding:1px;border:1px;display:block;width:4px;margin-top:1%;position:absolute;top:1%", fb.swap(g, null != g.style.zoom ? {
                    zoom: 1
                } : {}, function () {
                    b.boxSizing = 4 === e.offsetWidth
                }), a.getComputedStyle && (b.pixelPosition = "1%" !== (a.getComputedStyle(e, null) || {}).top, b.boxSizingReliable = "4px" === (a.getComputedStyle(e, null) || {
                    width: "4px"
                }).width, d = e.appendChild(T.createElement("div")), d.style.cssText = e.style.cssText = f, d.style.marginRight = d.style.width = "0", e.style.width = "1px", b.reliableMarginRight = !parseFloat((a.getComputedStyle(d, null) || {}).marginRight)), g.removeChild(c))
            }), b) : b
        }({});
        var pb, qb, rb = /(?:\{[\s\S]*\}|\[[\s\S]*\])$/,
            sb = /([A-Z])/g;
        e.uid = 1, e.accepts = function (a) {
            return a.nodeType ? 1 === a.nodeType || 9 === a.nodeType : true
        }, e.prototype = {
            key: function (a) {
                if (!e.accepts(a)) return 0;
                var b = {}, c = a[this.expando];
                if (!c) {
                    c = e.uid++;
                    try {
                        b[this.expando] = {
                            value: c
                        }, Object.defineProperties(a, b)
                    } catch (d) {
                        b[this.expando] = c, fb.extend(a, b)
                    }
                }
                return this.cache[c] || (this.cache[c] = {}), c
            },
            set: function (a, b, c) {
                var d, e = this.key(a),
                    f = this.cache[e];
                if ("string" == typeof b) f[b] = c;
                else if (fb.isEmptyObject(f)) fb.extend(this.cache[e], b);
                else
                    for (d in b) f[d] = b[d];
                return f
            },
            get: function (a, c) {
                var d = this.cache[this.key(a)];
                return c === b ? d : d[c]
            },
            access: function (a, c, d) {
                var e;
                return c === b || c && "string" == typeof c && d === b ? (e = this.get(a, c), e !== b ? e : this.get(a, fb.camelCase(c))) : (this.set(a, c, d), d !== b ? d : c)
            },
            remove: function (a, c) {
                var d, e, f, g = this.key(a),
                    h = this.cache[g];
                if (c === b) this.cache[g] = {};
                else {
                    fb.isArray(c) ? e = c.concat(c.map(fb.camelCase)) : (f = fb.camelCase(c), c in h ? e = [c, f] : (e = f, e = e in h ? [e] : e.match(hb) || [])), d = e.length;
                    for (; d--;) delete h[e[d]]
                }
            },
            hasData: function (a) {
                return !fb.isEmptyObject(this.cache[a[this.expando]] || {})
            },
            discard: function (a) {
                a[this.expando] && delete this.cache[a[this.expando]]
            }
        }, pb = new e, qb = new e, fb.extend({
            acceptData: e.accepts,
            hasData: function (a) {
                return pb.hasData(a) || qb.hasData(a)
            },
            data: function (a, b, c) {
                return pb.access(a, b, c)
            },
            removeData: function (a, b) {
                pb.remove(a, b)
            },
            _data: function (a, b, c) {
                return qb.access(a, b, c)
            },
            _removeData: function (a, b) {
                qb.remove(a, b)
            }
        }), fb.fn.extend({
            data: function (a, c) {
                var d, e, g = this[0],
                    h = 0,
                    i = null;
                if (a === b) {
                    if (this.length && (i = pb.get(g), 1 === g.nodeType && !qb.get(g, "hasDataAttrs"))) {
                        for (d = g.attributes; h < d.length; h++) e = d[h].name, 0 === e.indexOf("data-") && (e = fb.camelCase(e.slice(5)), f(g, e, i[e]));
                        qb.set(g, "hasDataAttrs", true)
                    }
                    return i
                }
                return "object" == typeof a ? this.each(function () {
                    pb.set(this, a)
                }) : fb.access(this, function (c) {
                    var d, e = fb.camelCase(a);
                    if (g && c === b) {
                        if (d = pb.get(g, a), d !== b) return d;
                        if (d = pb.get(g, e), d !== b) return d;
                        if (d = f(g, e, b), d !== b) return d
                    } else this.each(function () {
                        var d = pb.get(this, e);
                        pb.set(this, e, c), -1 !== a.indexOf("-") && d !== b && pb.set(this, a, c)
                    })
                }, null, c, arguments.length > 1, null, true)
            },
            removeData: function (a) {
                return this.each(function () {
                    pb.remove(this, a)
                })
            }
        }), fb.extend({
            queue: function (a, b, c) {
                var d;
                return a ? (b = (b || "fx") + "queue", d = qb.get(a, b), c && (!d || fb.isArray(c) ? d = qb.access(a, b, fb.makeArray(c)) : d.push(c)), d || []) : void 0
            },
            dequeue: function (a, b) {
                b = b || "fx";
                var c = fb.queue(a, b),
                    d = c.length,
                    e = c.shift(),
                    f = fb._queueHooks(a, b),
                    g = function () {
                        fb.dequeue(a, b)
                    };
                "inprogress" === e && (e = c.shift(), d--), e && ("fx" === b && c.unshift("inprogress"), delete f.stop, e.call(a, g, f)), !d && f && f.empty.fire()
            },
            _queueHooks: function (a, b) {
                var c = b + "queueHooks";
                return qb.get(a, c) || qb.access(a, c, {
                    empty: fb.Callbacks("once memory").add(function () {
                        qb.remove(a, [b + "queue", c])
                    })
                })
            }
        }), fb.fn.extend({
            queue: function (a, c) {
                var d = 2;
                return "string" != typeof a && (c = a, a = "fx", d--), arguments.length < d ? fb.queue(this[0], a) : c === b ? this : this.each(function () {
                    var b = fb.queue(this, a, c);
                    fb._queueHooks(this, a), "fx" === a && "inprogress" !== b[0] && fb.dequeue(this, a)
                })
            },
            dequeue: function (a) {
                return this.each(function () {
                    fb.dequeue(this, a)
                })
            },
            delay: function (a, b) {
                return a = fb.fx ? fb.fx.speeds[a] || a : a, b = b || "fx", this.queue(b, function (b, c) {
                    var d = setTimeout(b, a);
                    c.stop = function () {
                        clearTimeout(d)
                    }
                })
            },
            clearQueue: function (a) {
                return this.queue(a || "fx", [])
            },
            promise: function (a, c) {
                var d, e = 1,
                    f = fb.Deferred(),
                    g = this,
                    h = this.length,
                    i = function () {
                        --e || f.resolveWith(g, [g])
                    };
                for ("string" != typeof a && (c = a, a = b), a = a || "fx"; h--;) d = qb.get(g[h], a + "queueHooks"), d && d.empty && (e++, d.empty.add(i));
                return i(), f.promise(c)
            }
        });
        var tb, ub, vb = /[\t\r\n\f]/g,
            wb = /\r/g,
            xb = /^(?:input|select|textarea|button)$/i;
        fb.fn.extend({
            attr: function (a, b) {
                return fb.access(this, fb.attr, a, b, arguments.length > 1)
            },
            removeAttr: function (a) {
                return this.each(function () {
                    fb.removeAttr(this, a)
                })
            },
            prop: function (a, b) {
                return fb.access(this, fb.prop, a, b, arguments.length > 1)
            },
            removeProp: function (a) {
                return this.each(function () {
                    delete this[fb.propFix[a] || a]
                })
            },
            addClass: function (a) {
                var b, c, d, e, f, g = 0,
                    h = this.length,
                    i = "string" == typeof a && a;
                if (fb.isFunction(a)) return this.each(function (b) {
                    fb(this).addClass(a.call(this, b, this.className))
                });
                if (i)
                    for (b = (a || "").match(hb) || []; h > g; g++)
                        if (c = this[g], d = 1 === c.nodeType && (c.className ? (" " + c.className + " ").replace(vb, " ") : " ")) {
                            for (f = 0; e = b[f++];) d.indexOf(" " + e + " ") < 0 && (d += e + " ");
                            c.className = fb.trim(d)
                        }
                return this
            },
            removeClass: function (a) {
                var b, c, d, e, f, g = 0,
                    h = this.length,
                    i = 0 === arguments.length || "string" == typeof a && a;
                if (fb.isFunction(a)) return this.each(function (b) {
                    fb(this).removeClass(a.call(this, b, this.className))
                });
                if (i)
                    for (b = (a || "").match(hb) || []; h > g; g++)
                        if (c = this[g], d = 1 === c.nodeType && (c.className ? (" " + c.className + " ").replace(vb, " ") : "")) {
                            for (f = 0; e = b[f++];)
                                for (; d.indexOf(" " + e + " ") >= 0;) d = d.replace(" " + e + " ", " ");
                            c.className = a ? fb.trim(d) : ""
                        }
                return this
            },
            toggleClass: function (a, b) {
                var c = typeof a;
                return "boolean" == typeof b && "string" === c ? b ? this.addClass(a) : this.removeClass(a) : fb.isFunction(a) ? this.each(function (c) {
                    fb(this).toggleClass(a.call(this, c, this.className, b), b)
                }) : this.each(function () {
                    if ("string" === c)
                        for (var b, d = 0, e = fb(this), f = a.match(hb) || []; b = f[d++];) e.hasClass(b) ? e.removeClass(b) : e.addClass(b);
                    else(c === R || "boolean" === c) && (this.className && qb.set(this, "__className__", this.className), this.className = this.className || a === false ? "" : qb.get(this, "__className__") || "")
                })
            },
            hasClass: function (a) {
                for (var b = " " + a + " ", c = 0, d = this.length; d > c; c++)
                    if (1 === this[c].nodeType && (" " + this[c].className + " ").replace(vb, " ").indexOf(b) >= 0) return true;
                return false
            },
            val: function (a) {
                var c, d, e, f = this[0]; {
                    if (arguments.length) return e = fb.isFunction(a), this.each(function (d) {
                        var f;
                        1 === this.nodeType && (f = e ? a.call(this, d, fb(this).val()) : a, null == f ? f = "" : "number" == typeof f ? f += "" : fb.isArray(f) && (f = fb.map(f, function (a) {
                            return null == a ? "" : a + ""
                        })), c = fb.valHooks[this.type] || fb.valHooks[this.nodeName.toLowerCase()], c && "set" in c && c.set(this, f, "value") !== b || (this.value = f))
                    });
                    if (f) return c = fb.valHooks[f.type] || fb.valHooks[f.nodeName.toLowerCase()], c && "get" in c && (d = c.get(f, "value")) !== b ? d : (d = f.value, "string" == typeof d ? d.replace(wb, "") : null == d ? "" : d)
                }
            }
        }), fb.extend({
            valHooks: {
                option: {
                    get: function (a) {
                        var b = a.attributes.value;
                        return !b || b.specified ? a.value : a.text
                    }
                },
                select: {
                    get: function (a) {
                        for (var b, c, d = a.options, e = a.selectedIndex, f = "select-one" === a.type || 0 > e, g = f ? null : [], h = f ? e + 1 : d.length, i = 0 > e ? h : f ? e : 0; h > i; i++)
                            if (c = d[i], !(!c.selected && i !== e || (fb.support.optDisabled ? c.disabled : null !== c.getAttribute("disabled")) || c.parentNode.disabled && fb.nodeName(c.parentNode, "optgroup"))) {
                                if (b = fb(c).val(), f) return b;
                                g.push(b)
                            }
                        return g
                    },
                    set: function (a, b) {
                        for (var c, d, e = a.options, f = fb.makeArray(b), g = e.length; g--;) d = e[g], (d.selected = fb.inArray(fb(d).val(), f) >= 0) && (c = true);
                        return c || (a.selectedIndex = -1), f
                    }
                }
            },
            attr: function (a, c, d) {
                var e, f, g = a.nodeType;
                if (a && 3 !== g && 8 !== g && 2 !== g) return typeof a.getAttribute === R ? fb.prop(a, c, d) : (1 === g && fb.isXMLDoc(a) || (c = c.toLowerCase(), e = fb.attrHooks[c] || (fb.expr.match.bool.test(c) ? ub : tb)), d === b ? e && "get" in e && null !== (f = e.get(a, c)) ? f : (f = fb.find.attr(a, c), null == f ? b : f) : null !== d ? e && "set" in e && (f = e.set(a, d, c)) !== b ? f : (a.setAttribute(c, d + ""), d) : (fb.removeAttr(a, c), void 0))
            },
            removeAttr: function (a, b) {
                var c, d, e = 0,
                    f = b && b.match(hb);
                if (f && 1 === a.nodeType)
                    for (; c = f[e++];) d = fb.propFix[c] || c, fb.expr.match.bool.test(c) && (a[d] = false), a.removeAttribute(c)
            },
            attrHooks: {
                type: {
                    set: function (a, b) {
                        if (!fb.support.radioValue && "radio" === b && fb.nodeName(a, "input")) {
                            var c = a.value;
                            return a.setAttribute("type", b), c && (a.value = c), b
                        }
                    }
                }
            },
            propFix: {
                "for": "htmlFor",
                "class": "className"
            },
            prop: function (a, c, d) {
                var e, f, g, h = a.nodeType;
                if (a && 3 !== h && 8 !== h && 2 !== h) return g = 1 !== h || !fb.isXMLDoc(a), g && (c = fb.propFix[c] || c, f = fb.propHooks[c]), d !== b ? f && "set" in f && (e = f.set(a, d, c)) !== b ? e : a[c] = d : f && "get" in f && null !== (e = f.get(a, c)) ? e : a[c]
            },
            propHooks: {
                tabIndex: {
                    get: function (a) {
                        return a.hasAttribute("tabindex") || xb.test(a.nodeName) || a.href ? a.tabIndex : -1
                    }
                }
            }
        }), ub = {
            set: function (a, b, c) {
                return b === false ? fb.removeAttr(a, c) : a.setAttribute(c, c), c
            }
        }, fb.each(fb.expr.match.bool.source.match(/\w+/g), function (a, c) {
            var d = fb.expr.attrHandle[c] || fb.find.attr;
            fb.expr.attrHandle[c] = function (a, c, e) {
                var f = fb.expr.attrHandle[c],
                    g = e ? b : (fb.expr.attrHandle[c] = b) != d(a, c, e) ? c.toLowerCase() : null;
                return fb.expr.attrHandle[c] = f, g
            }
        }), fb.support.optSelected || (fb.propHooks.selected = {
            get: function (a) {
                var b = a.parentNode;
                return b && b.parentNode && b.parentNode.selectedIndex, null
            }
        }), fb.each(["tabIndex", "readOnly", "maxLength", "cellSpacing", "cellPadding", "rowSpan", "colSpan", "useMap", "frameBorder", "contentEditable"], function () {
            fb.propFix[this.toLowerCase()] = this
        }), fb.each(["radio", "checkbox"], function () {
            fb.valHooks[this] = {
                set: function (a, b) {
                    return fb.isArray(b) ? a.checked = fb.inArray(fb(a).val(), b) >= 0 : void 0
                }
            }, fb.support.checkOn || (fb.valHooks[this].get = function (a) {
                return null === a.getAttribute("value") ? "on" : a.value
            })
        });
        var yb = /^key/,
            zb = /^(?:mouse|contextmenu)|click/,
            Ab = /^(?:focusinfocus|focusoutblur)$/,
            Bb = /^([^.]*)(?:\.(.+)|)$/;
        fb.event = {
            global: {},
            add: function (a, c, d, e, f) {
                var g, h, i, j, k, l, m, n, o, p, q, r = qb.get(a);
                if (r) {
                    for (d.handler && (g = d, d = g.handler, f = g.selector), d.guid || (d.guid = fb.guid++), (j = r.events) || (j = r.events = {}), (h = r.handle) || (h = r.handle = function (a) {
                        return typeof fb === R || a && fb.event.triggered === a.type ? b : fb.event.dispatch.apply(h.elem, arguments)
                    }, h.elem = a), c = (c || "").match(hb) || [""], k = c.length; k--;) i = Bb.exec(c[k]) || [], o = q = i[1], p = (i[2] || "").split(".").sort(), o && (m = fb.event.special[o] || {}, o = (f ? m.delegateType : m.bindType) || o, m = fb.event.special[o] || {}, l = fb.extend({
                        type: o,
                        origType: q,
                        data: e,
                        handler: d,
                        guid: d.guid,
                        selector: f,
                        needsContext: f && fb.expr.match.needsContext.test(f),
                        namespace: p.join(".")
                    }, g), (n = j[o]) || (n = j[o] = [], n.delegateCount = 0, m.setup && m.setup.call(a, e, p, h) !== false || a.addEventListener && a.addEventListener(o, h, false)), m.add && (m.add.call(a, l), l.handler.guid || (l.handler.guid = d.guid)), f ? n.splice(n.delegateCount++, 0, l) : n.push(l), fb.event.global[o] = true);
                    a = null
                }
            },
            remove: function (a, b, c, d, e) {
                var f, g, h, i, j, k, l, m, n, o, p, q = qb.hasData(a) && qb.get(a);
                if (q && (i = q.events)) {
                    for (b = (b || "").match(hb) || [""], j = b.length; j--;)
                        if (h = Bb.exec(b[j]) || [], n = p = h[1], o = (h[2] || "").split(".").sort(), n) {
                            for (l = fb.event.special[n] || {}, n = (d ? l.delegateType : l.bindType) || n, m = i[n] || [], h = h[2] && new RegExp("(^|\\.)" + o.join("\\.(?:.*\\.|)") + "(\\.|$)"), g = f = m.length; f--;) k = m[f], !e && p !== k.origType || c && c.guid !== k.guid || h && !h.test(k.namespace) || d && d !== k.selector && ("**" !== d || !k.selector) || (m.splice(f, 1), k.selector && m.delegateCount--, l.remove && l.remove.call(a, k));
                            g && !m.length && (l.teardown && l.teardown.call(a, o, q.handle) !== false || fb.removeEvent(a, n, q.handle), delete i[n])
                        } else
                            for (n in i) fb.event.remove(a, n + b[j], c, d, true);
                    fb.isEmptyObject(i) && (delete q.handle, qb.remove(a, "events"))
                }
            },
            trigger: function (c, d, e, f) {
                var g, h, i, j, k, l, m, n = [e || T],
                    o = db.call(c, "type") ? c.type : c,
                    p = db.call(c, "namespace") ? c.namespace.split(".") : [];
                if (h = i = e = e || T, 3 !== e.nodeType && 8 !== e.nodeType && !Ab.test(o + fb.event.triggered) && (o.indexOf(".") >= 0 && (p = o.split("."), o = p.shift(), p.sort()), k = o.indexOf(":") < 0 && "on" + o, c = c[fb.expando] ? c : new fb.Event(o, "object" == typeof c && c), c.isTrigger = f ? 2 : 3, c.namespace = p.join("."), c.namespace_re = c.namespace ? new RegExp("(^|\\.)" + p.join("\\.(?:.*\\.|)") + "(\\.|$)") : null, c.result = b, c.target || (c.target = e), d = null == d ? [c] : fb.makeArray(d, [c]), m = fb.event.special[o] || {}, f || !m.trigger || m.trigger.apply(e, d) !== false)) {
                    if (!f && !m.noBubble && !fb.isWindow(e)) {
                        for (j = m.delegateType || o, Ab.test(j + o) || (h = h.parentNode); h; h = h.parentNode) n.push(h), i = h;
                        i === (e.ownerDocument || T) && n.push(i.defaultView || i.parentWindow || a)
                    }
                    for (g = 0;
                        (h = n[g++]) && !c.isPropagationStopped();) c.type = g > 1 ? j : m.bindType || o, l = (qb.get(h, "events") || {})[c.type] && qb.get(h, "handle"), l && l.apply(h, d), l = k && h[k], l && fb.acceptData(h) && l.apply && l.apply(h, d) === false && c.preventDefault();
                    return c.type = o, f || c.isDefaultPrevented() || m._default && m._default.apply(n.pop(), d) !== false || !fb.acceptData(e) || k && fb.isFunction(e[o]) && !fb.isWindow(e) && (i = e[k], i && (e[k] = null), fb.event.triggered = o, e[o](), fb.event.triggered = b, i && (e[k] = i)), c.result
                }
            },
            dispatch: function (a) {
                a = fb.event.fix(a);
                var c, d, e, f, g, h = [],
                    i = ab.call(arguments),
                    j = (qb.get(this, "events") || {})[a.type] || [],
                    k = fb.event.special[a.type] || {};
                if (i[0] = a, a.delegateTarget = this, !k.preDispatch || k.preDispatch.call(this, a) !== false) {
                    for (h = fb.event.handlers.call(this, a, j), c = 0;
                        (f = h[c++]) && !a.isPropagationStopped();)
                        for (a.currentTarget = f.elem, d = 0;
                            (g = f.handlers[d++]) && !a.isImmediatePropagationStopped();)(!a.namespace_re || a.namespace_re.test(g.namespace)) && (a.handleObj = g, a.data = g.data, e = ((fb.event.special[g.origType] || {}).handle || g.handler).apply(f.elem, i), e !== b && (a.result = e) === false && (a.preventDefault(), a.stopPropagation()));
                    return k.postDispatch && k.postDispatch.call(this, a), a.result
                }
            },
            handlers: function (a, c) {
                var d, e, f, g, h = [],
                    i = c.delegateCount,
                    j = a.target;
                if (i && j.nodeType && (!a.button || "click" !== a.type))
                    for (; j !== this; j = j.parentNode || this)
                        if (j.disabled !== true || "click" !== a.type) {
                            for (e = [], d = 0; i > d; d++) g = c[d], f = g.selector + " ", e[f] === b && (e[f] = g.needsContext ? fb(f, this).index(j) >= 0 : fb.find(f, this, null, [j]).length), e[f] && e.push(g);
                            e.length && h.push({
                                elem: j,
                                handlers: e
                            })
                        }
                return i < c.length && h.push({
                    elem: this,
                    handlers: c.slice(i)
                }), h
            },
            props: "altKey bubbles cancelable ctrlKey currentTarget eventPhase metaKey relatedTarget shiftKey target timeStamp view which".split(" "),
            fixHooks: {},
            keyHooks: {
                props: "char charCode key keyCode".split(" "),
                filter: function (a, b) {
                    return null == a.which && (a.which = null != b.charCode ? b.charCode : b.keyCode), a
                }
            },
            mouseHooks: {
                props: "button buttons clientX clientY offsetX offsetY pageX pageY screenX screenY toElement".split(" "),
                filter: function (a, c) {
                    var d, e, f, g = c.button;
                    return null == a.pageX && null != c.clientX && (d = a.target.ownerDocument || T, e = d.documentElement, f = d.body, a.pageX = c.clientX + (e && e.scrollLeft || f && f.scrollLeft || 0) - (e && e.clientLeft || f && f.clientLeft || 0), a.pageY = c.clientY + (e && e.scrollTop || f && f.scrollTop || 0) - (e && e.clientTop || f && f.clientTop || 0)), a.which || g === b || (a.which = 1 & g ? 1 : 2 & g ? 3 : 4 & g ? 2 : 0), a
                }
            },
            fix: function (a) {
                if (a[fb.expando]) return a;
                var b, c, d, e = a.type,
                    f = a,
                    g = this.fixHooks[e];
                for (g || (this.fixHooks[e] = g = zb.test(e) ? this.mouseHooks : yb.test(e) ? this.keyHooks : {}), d = g.props ? this.props.concat(g.props) : this.props, a = new fb.Event(f), b = d.length; b--;) c = d[b], a[c] = f[c];
                return a.target || (a.target = T), 3 === a.target.nodeType && (a.target = a.target.parentNode), g.filter ? g.filter(a, f) : a
            },
            special: {
                load: {
                    noBubble: true
                },
                focus: {
                    trigger: function () {
                        return this !== i() && this.focus ? (this.focus(), false) : void 0
                    },
                    delegateType: "focusin"
                },
                blur: {
                    trigger: function () {
                        return this === i() && this.blur ? (this.blur(), false) : void 0
                    },
                    delegateType: "focusout"
                },
                click: {
                    trigger: function () {
                        return "checkbox" === this.type && this.click && fb.nodeName(this, "input") ? (this.click(), false) : void 0
                    },
                    _default: function (a) {
                        return fb.nodeName(a.target, "a")
                    }
                },
                beforeunload: {
                    postDispatch: function (a) {
                        a.result !== b && (a.originalEvent.returnValue = a.result)
                    }
                }
            },
            simulate: function (a, b, c, d) {
                var e = fb.extend(new fb.Event, c, {
                    type: a,
                    isSimulated: true,
                    originalEvent: {}
                });
                d ? fb.event.trigger(e, null, b) : fb.event.dispatch.call(b, e), e.isDefaultPrevented() && c.preventDefault()
            }
        }, fb.removeEvent = function (a, b, c) {
            a.removeEventListener && a.removeEventListener(b, c, false)
        }, fb.Event = function (a, b) {
            return this instanceof fb.Event ? (a && a.type ? (this.originalEvent = a, this.type = a.type, this.isDefaultPrevented = a.defaultPrevented || a.getPreventDefault && a.getPreventDefault() ? g : h) : this.type = a, b && fb.extend(this, b), this.timeStamp = a && a.timeStamp || fb.now(), this[fb.expando] = true, void 0) : new fb.Event(a, b)
        }, fb.Event.prototype = {
            isDefaultPrevented: h,
            isPropagationStopped: h,
            isImmediatePropagationStopped: h,
            preventDefault: function () {
                var a = this.originalEvent;
                this.isDefaultPrevented = g, a && a.preventDefault && a.preventDefault()
            },
            stopPropagation: function () {
                var a = this.originalEvent;
                this.isPropagationStopped = g, a && a.stopPropagation && a.stopPropagation()
            },
            stopImmediatePropagation: function () {
                this.isImmediatePropagationStopped = g, this.stopPropagation()
            }
        }, fb.each({
            mouseenter: "mouseover",
            mouseleave: "mouseout"
        }, function (a, b) {
            fb.event.special[a] = {
                delegateType: b,
                bindType: b,
                handle: function (a) {
                    var c, d = this,
                        e = a.relatedTarget,
                        f = a.handleObj;
                    return (!e || e !== d && !fb.contains(d, e)) && (a.type = f.origType, c = f.handler.apply(this, arguments), a.type = b), c
                }
            }
        }), fb.support.focusinBubbles || fb.each({
            focus: "focusin",
            blur: "focusout"
        }, function (a, b) {
            var c = 0,
                d = function (a) {
                    fb.event.simulate(b, a.target, fb.event.fix(a), true)
                };
            fb.event.special[b] = {
                setup: function () {
                    0 === c++ && T.addEventListener(a, d, true)
                },
                teardown: function () {
                    0 === --c && T.removeEventListener(a, d, true)
                }
            }
        }), fb.fn.extend({
            on: function (a, c, d, e, f) {
                var g, i;
                if ("object" == typeof a) {
                    "string" != typeof c && (d = d || c, c = b);
                    for (i in a) this.on(i, c, d, a[i], f);
                    return this
                }
                if (null == d && null == e ? (e = c, d = c = b) : null == e && ("string" == typeof c ? (e = d, d = b) : (e = d, d = c, c = b)), e === false) e = h;
                else if (!e) return this;
                return 1 === f && (g = e, e = function (a) {
                    return fb().off(a), g.apply(this, arguments)
                }, e.guid = g.guid || (g.guid = fb.guid++)), this.each(function () {
                    fb.event.add(this, a, e, d, c)
                })
            },
            one: function (a, b, c, d) {
                return this.on(a, b, c, d, 1)
            },
            off: function (a, c, d) {
                var e, f;
                if (a && a.preventDefault && a.handleObj) return e = a.handleObj, fb(a.delegateTarget).off(e.namespace ? e.origType + "." + e.namespace : e.origType, e.selector, e.handler), this;
                if ("object" == typeof a) {
                    for (f in a) this.off(f, c, a[f]);
                    return this
                }
                return (c === false || "function" == typeof c) && (d = c, c = b), d === false && (d = h), this.each(function () {
                    fb.event.remove(this, a, d, c)
                })
            },
            trigger: function (a, b) {
                return this.each(function () {
                    fb.event.trigger(a, b, this)
                })
            },
            triggerHandler: function (a, b) {
                var c = this[0];
                return c ? fb.event.trigger(a, b, c, true) : void 0
            }
        });
        var Cb = /^.[^:#\[\.,]*$/,
            Db = /^(?:parents|prev(?:Until|All))/,
            Eb = fb.expr.match.needsContext,
            Fb = {
                children: true,
                contents: true,
                next: true,
                prev: true
            };
        fb.fn.extend({
            find: function (a) {
                var b, c = [],
                    d = this,
                    e = d.length;
                if ("string" != typeof a) return this.pushStack(fb(a).filter(function () {
                    for (b = 0; e > b; b++)
                        if (fb.contains(d[b], this)) return true
                }));
                for (b = 0; e > b; b++) fb.find(a, d[b], c);
                return c = this.pushStack(e > 1 ? fb.unique(c) : c), c.selector = this.selector ? this.selector + " " + a : a, c
            },
            has: function (a) {
                var b = fb(a, this),
                    c = b.length;
                return this.filter(function () {
                    for (var a = 0; c > a; a++)
                        if (fb.contains(this, b[a])) return true
                })
            },
            not: function (a) {
                return this.pushStack(k(this, a || [], true))
            },
            filter: function (a) {
                return this.pushStack(k(this, a || [], false))
            },
            is: function (a) {
                return !!k(this, "string" == typeof a && Eb.test(a) ? fb(a) : a || [], false).length
            },
            closest: function (a, b) {
                for (var c, d = 0, e = this.length, f = [], g = Eb.test(a) || "string" != typeof a ? fb(a, b || this.context) : 0; e > d; d++)
                    for (c = this[d]; c && c !== b; c = c.parentNode)
                        if (c.nodeType < 11 && (g ? g.index(c) > -1 : 1 === c.nodeType && fb.find.matchesSelector(c, a))) {
                            c = f.push(c);
                            break
                        }
                return this.pushStack(f.length > 1 ? fb.unique(f) : f)
            },
            index: function (a) {
                return a ? "string" == typeof a ? bb.call(fb(a), this[0]) : bb.call(this, a.jquery ? a[0] : a) : this[0] && this[0].parentNode ? this.first().prevAll().length : -1
            },
            add: function (a, b) {
                var c = "string" == typeof a ? fb(a, b) : fb.makeArray(a && a.nodeType ? [a] : a),
                    d = fb.merge(this.get(), c);
                return this.pushStack(fb.unique(d))
            },
            addBack: function (a) {
                return this.add(null == a ? this.prevObject : this.prevObject.filter(a))
            }
        }), fb.each({
            parent: function (a) {
                var b = a.parentNode;
                return b && 11 !== b.nodeType ? b : null
            },
            parents: function (a) {
                return fb.dir(a, "parentNode")
            },
            parentsUntil: function (a, b, c) {
                return fb.dir(a, "parentNode", c)
            },
            next: function (a) {
                return j(a, "nextSibling")
            },
            prev: function (a) {
                return j(a, "previousSibling")
            },
            nextAll: function (a) {
                return fb.dir(a, "nextSibling")
            },
            prevAll: function (a) {
                return fb.dir(a, "previousSibling")
            },
            nextUntil: function (a, b, c) {
                return fb.dir(a, "nextSibling", c)
            },
            prevUntil: function (a, b, c) {
                return fb.dir(a, "previousSibling", c)
            },
            siblings: function (a) {
                return fb.sibling((a.parentNode || {}).firstChild, a)
            },
            children: function (a) {
                return fb.sibling(a.firstChild)
            },
            contents: function (a) {
                return a.contentDocument || fb.merge([], a.childNodes)
            }
        }, function (a, b) {
            fb.fn[a] = function (c, d) {
                var e = fb.map(this, b, c);
                return "Until" !== a.slice(-5) && (d = c), d && "string" == typeof d && (e = fb.filter(d, e)), this.length > 1 && (Fb[a] || fb.unique(e), Db.test(a) && e.reverse()), this.pushStack(e)
            }
        }), fb.extend({
            filter: function (a, b, c) {
                var d = b[0];
                return c && (a = ":not(" + a + ")"), 1 === b.length && 1 === d.nodeType ? fb.find.matchesSelector(d, a) ? [d] : [] : fb.find.matches(a, fb.grep(b, function (a) {
                    return 1 === a.nodeType
                }))
            },
            dir: function (a, c, d) {
                for (var e = [], f = d !== b;
                    (a = a[c]) && 9 !== a.nodeType;)
                    if (1 === a.nodeType) {
                        if (f && fb(a).is(d)) break;
                        e.push(a)
                    }
                return e
            },
            sibling: function (a, b) {
                for (var c = []; a; a = a.nextSibling) 1 === a.nodeType && a !== b && c.push(a);
                return c
            }
        });
        var Gb = /<(?!area|br|col|embed|hr|img|input|link|meta|param)(([\w:]+)[^>]*)\/>/gi,
            Hb = /<([\w:]+)/,
            Ib = /<|&#?\w+;/,
            Jb = /<(?:script|style|link)/i,
            Kb = /^(?:checkbox|radio)$/i,
            Lb = /checked\s*(?:[^=]|=\s*.checked.)/i,
            Mb = /^$|\/(?:java|ecma)script/i,
            Nb = /^true\/(.*)/,
            Ob = /^\s*<!(?:\[CDATA\[|--)|(?:\]\]|--)>\s*$/g,
            Pb = {
                option: [1, "<select multiple='multiple'>", "</select>"],
                thead: [1, "<table>", "</table>"],
                col: [2, "<table><colgroup>", "</colgroup></table>"],
                tr: [2, "<table><tbody>", "</tbody></table>"],
                td: [3, "<table><tbody><tr>", "</tr></tbody></table>"],
                _default: [0, "", ""]
            };
        Pb.optgroup = Pb.option, Pb.tbody = Pb.tfoot = Pb.colgroup = Pb.caption = Pb.thead, Pb.th = Pb.td, fb.fn.extend({
            text: function (a) {
                return fb.access(this, function (a) {
                    return a === b ? fb.text(this) : this.empty().append((this[0] && this[0].ownerDocument || T).createTextNode(a))
                }, null, a, arguments.length)
            },
            append: function () {
                return this.domManip(arguments, function (a) {
                    if (1 === this.nodeType || 11 === this.nodeType || 9 === this.nodeType) {
                        var b = l(this, a);
                        b.appendChild(a)
                    }
                })
            },
            prepend: function () {
                return this.domManip(arguments, function (a) {
                    if (1 === this.nodeType || 11 === this.nodeType || 9 === this.nodeType) {
                        var b = l(this, a);
                        b.insertBefore(a, b.firstChild)
                    }
                })
            },
            before: function () {
                return this.domManip(arguments, function (a) {
                    this.parentNode && this.parentNode.insertBefore(a, this)
                })
            },
            after: function () {
                return this.domManip(arguments, function (a) {
                    this.parentNode && this.parentNode.insertBefore(a, this.nextSibling)
                })
            },
            remove: function (a, b) {
                for (var c, d = a ? fb.filter(a, this) : this, e = 0; null != (c = d[e]); e++) b || 1 !== c.nodeType || fb.cleanData(q(c)), c.parentNode && (b && fb.contains(c.ownerDocument, c) && o(q(c, "script")), c.parentNode.removeChild(c));
                return this
            },
            empty: function () {
                for (var a, b = 0; null != (a = this[b]); b++) 1 === a.nodeType && (fb.cleanData(q(a, false)), a.textContent = "");
                return this
            },
            clone: function (a, b) {
                return a = null == a ? false : a, b = null == b ? a : b, this.map(function () {
                    return fb.clone(this, a, b)
                })
            },
            html: function (a) {
                return fb.access(this, function (a) {
                    var c = this[0] || {}, d = 0,
                        e = this.length;
                    if (a === b && 1 === c.nodeType) return c.innerHTML;
                    if ("string" == typeof a && !Jb.test(a) && !Pb[(Hb.exec(a) || ["", ""])[1].toLowerCase()]) {
                        a = a.replace(Gb, "<$1></$2>");
                        try {
                            for (; e > d; d++) c = this[d] || {}, 1 === c.nodeType && (fb.cleanData(q(c, false)), c.innerHTML = a);
                            c = 0
                        } catch (f) {}
                    }
                    c && this.empty().append(a)
                }, null, a, arguments.length)
            },
            replaceWith: function () {
                var a = fb.map(this, function (a) {
                    return [a.nextSibling, a.parentNode]
                }),
                    b = 0;
                return this.domManip(arguments, function (c) {
                    var d = a[b++],
                        e = a[b++];
                    e && (d && d.parentNode !== e && (d = this.nextSibling), fb(this).remove(), e.insertBefore(c, d))
                }, true), b ? this : this.remove()
            },
            detach: function (a) {
                return this.remove(a, true)
            },
            domManip: function (a, b, c) {
                a = $.apply([], a);
                var d, e, f, g, h, i, j = 0,
                    k = this.length,
                    l = this,
                    o = k - 1,
                    p = a[0],
                    r = fb.isFunction(p);
                if (r || !(1 >= k || "string" != typeof p || fb.support.checkClone) && Lb.test(p)) return this.each(function (d) {
                    var e = l.eq(d);
                    r && (a[0] = p.call(this, d, e.html())), e.domManip(a, b, c)
                });
                if (k && (d = fb.buildFragment(a, this[0].ownerDocument, false, !c && this), e = d.firstChild, 1 === d.childNodes.length && (d = e), e)) {
                    for (f = fb.map(q(d, "script"), m), g = f.length; k > j; j++) h = d, j !== o && (h = fb.clone(h, true, true), g && fb.merge(f, q(h, "script"))), b.call(this[j], h, j);
                    if (g)
                        for (i = f[f.length - 1].ownerDocument, fb.map(f, n), j = 0; g > j; j++) h = f[j], Mb.test(h.type || "") && !qb.access(h, "globalEval") && fb.contains(i, h) && (h.src ? fb._evalUrl(h.src) : fb.globalEval(h.textContent.replace(Ob, "")))
                }
                return this
            }
        }), fb.each({
            appendTo: "append",
            prependTo: "prepend",
            insertBefore: "before",
            insertAfter: "after",
            replaceAll: "replaceWith"
        }, function (a, b) {
            fb.fn[a] = function (a) {
                for (var c, d = [], e = fb(a), f = e.length - 1, g = 0; f >= g; g++) c = g === f ? this : this.clone(true), fb(e[g])[b](c), _.apply(d, c.get());
                return this.pushStack(d)
            }
        }), fb.extend({
            clone: function (a, b, c) {
                var d, e, f, g, h = a.cloneNode(true),
                    i = fb.contains(a.ownerDocument, a);
                if (!(fb.support.noCloneChecked || 1 !== a.nodeType && 11 !== a.nodeType || fb.isXMLDoc(a)))
                    for (g = q(h), f = q(a), d = 0, e = f.length; e > d; d++) r(f[d], g[d]);
                if (b)
                    if (c)
                        for (f = f || q(a), g = g || q(h), d = 0, e = f.length; e > d; d++) p(f[d], g[d]);
                    else p(a, h);
                return g = q(h, "script"), g.length > 0 && o(g, !i && q(a, "script")), h
            },
            buildFragment: function (a, b, c, d) {
                for (var e, f, g, h, i, j, k = 0, l = a.length, m = b.createDocumentFragment(), n = []; l > k; k++)
                    if (e = a[k], e || 0 === e)
                        if ("object" === fb.type(e)) fb.merge(n, e.nodeType ? [e] : e);
                        else if (Ib.test(e)) {
                    for (f = f || m.appendChild(b.createElement("div")), g = (Hb.exec(e) || ["", ""])[1].toLowerCase(), h = Pb[g] || Pb._default, f.innerHTML = h[1] + e.replace(Gb, "<$1></$2>") + h[2], j = h[0]; j--;) f = f.lastChild;
                    fb.merge(n, f.childNodes), f = m.firstChild, f.textContent = ""
                } else n.push(b.createTextNode(e));
                for (m.textContent = "", k = 0; e = n[k++];)
                    if ((!d || -1 === fb.inArray(e, d)) && (i = fb.contains(e.ownerDocument, e), f = q(m.appendChild(e), "script"), i && o(f), c))
                        for (j = 0; e = f[j++];) Mb.test(e.type || "") && c.push(e);
                return m
            },
            cleanData: function (a) {
                for (var c, d, f, g, h, i, j = fb.event.special, k = 0;
                    (d = a[k]) !== b; k++) {
                    if (e.accepts(d) && (h = d[qb.expando], h && (c = qb.cache[h]))) {
                        if (f = Object.keys(c.events || {}), f.length)
                            for (i = 0;
                                (g = f[i]) !== b; i++) j[g] ? fb.event.remove(d, g) : fb.removeEvent(d, g, c.handle);
                        qb.cache[h] && delete qb.cache[h]
                    }
                    delete pb.cache[d[pb.expando]]
                }
            },
            _evalUrl: function (a) {
                return fb.ajax({
                    url: a,
                    type: "GET",
                    dataType: "script",
                    async: false,
                    global: false,
                    "throws": true
                })
            }
        }), fb.fn.extend({
            wrapAll: function (a) {
                var b;
                return fb.isFunction(a) ? this.each(function (b) {
                    fb(this).wrapAll(a.call(this, b))
                }) : (this[0] && (b = fb(a, this[0].ownerDocument).eq(0).clone(true), this[0].parentNode && b.insertBefore(this[0]), b.map(function () {
                    for (var a = this; a.firstElementChild;) a = a.firstElementChild;
                    return a
                }).append(this)), this)
            },
            wrapInner: function (a) {
                return fb.isFunction(a) ? this.each(function (b) {
                    fb(this).wrapInner(a.call(this, b))
                }) : this.each(function () {
                    var b = fb(this),
                        c = b.contents();
                    c.length ? c.wrapAll(a) : b.append(a)
                })
            },
            wrap: function (a) {
                var b = fb.isFunction(a);
                return this.each(function (c) {
                    fb(this).wrapAll(b ? a.call(this, c) : a)
                })
            },
            unwrap: function () {
                return this.parent().each(function () {
                    fb.nodeName(this, "body") || fb(this).replaceWith(this.childNodes)
                }).end()
            }
        });
        var Qb, Rb, Sb = /^(none|table(?!-c[ea]).+)/,
            Tb = /^margin/,
            Ub = new RegExp("^(" + gb + ")(.*)$", "i"),
            Vb = new RegExp("^(" + gb + ")(?!px)[a-z%]+$", "i"),
            Wb = new RegExp("^([+-])=(" + gb + ")", "i"),
            Xb = {
                BODY: "block"
            }, Yb = {
                position: "absolute",
                visibility: "hidden",
                display: "block"
            }, Zb = {
                letterSpacing: 0,
                fontWeight: 400
            }, $b = ["Top", "Right", "Bottom", "Left"],
            _b = ["Webkit", "O", "Moz", "ms"];
        fb.fn.extend({
            css: function (a, c) {
                return fb.access(this, function (a, c, d) {
                    var e, f, g = {}, h = 0;
                    if (fb.isArray(c)) {
                        for (e = u(a), f = c.length; f > h; h++) g[c[h]] = fb.css(a, c[h], false, e);
                        return g
                    }
                    return d !== b ? fb.style(a, c, d) : fb.css(a, c)
                }, a, c, arguments.length > 1)
            },
            show: function () {
                return v(this, true)
            },
            hide: function () {
                return v(this)
            },
            toggle: function (a) {
                return "boolean" == typeof a ? a ? this.show() : this.hide() : this.each(function () {
                    t(this) ? fb(this).show() : fb(this).hide()
                })
            }
        }), fb.extend({
            cssHooks: {
                opacity: {
                    get: function (a, b) {
                        if (b) {
                            var c = Qb(a, "opacity");
                            return "" === c ? "1" : c
                        }
                    }
                }
            },
            cssNumber: {
                columnCount: true,
                fillOpacity: true,
                fontWeight: true,
                lineHeight: true,
                opacity: true,
                order: true,
                orphans: true,
                widows: true,
                zIndex: true,
                zoom: true
            },
            cssProps: {
                "float": "cssFloat"
            },
            style: function (a, c, d, e) {
                if (a && 3 !== a.nodeType && 8 !== a.nodeType && a.style) {
                    var f, g, h, i = fb.camelCase(c),
                        j = a.style;
                    return c = fb.cssProps[i] || (fb.cssProps[i] = s(j, i)), h = fb.cssHooks[c] || fb.cssHooks[i], d === b ? h && "get" in h && (f = h.get(a, false, e)) !== b ? f : j[c] : (g = typeof d, "string" === g && (f = Wb.exec(d)) && (d = (f[1] + 1) * f[2] + parseFloat(fb.css(a, c)), g = "number"), null == d || "number" === g && isNaN(d) || ("number" !== g || fb.cssNumber[i] || (d += "px"), fb.support.clearCloneStyle || "" !== d || 0 !== c.indexOf("background") || (j[c] = "inherit"), h && "set" in h && (d = h.set(a, d, e)) === b || (j[c] = d)), void 0)
                }
            },
            css: function (a, c, d, e) {
                var f, g, h, i = fb.camelCase(c);
                return c = fb.cssProps[i] || (fb.cssProps[i] = s(a.style, i)), h = fb.cssHooks[c] || fb.cssHooks[i], h && "get" in h && (f = h.get(a, true, d)), f === b && (f = Qb(a, c, e)), "normal" === f && c in Zb && (f = Zb[c]), "" === d || d ? (g = parseFloat(f), d === true || fb.isNumeric(g) ? g || 0 : f) : f
            }
        }), Qb = function (a, c, d) {
            var e, f, g, h = d || u(a),
                i = h ? h.getPropertyValue(c) || h[c] : b,
                j = a.style;
            return h && ("" !== i || fb.contains(a.ownerDocument, a) || (i = fb.style(a, c)), Vb.test(i) && Tb.test(c) && (e = j.width, f = j.minWidth, g = j.maxWidth, j.minWidth = j.maxWidth = j.width = i, i = h.width, j.width = e, j.minWidth = f, j.maxWidth = g)), i
        }, fb.each(["height", "width"], function (a, b) {
            fb.cssHooks[b] = {
                get: function (a, c, d) {
                    return c ? 0 === a.offsetWidth && Sb.test(fb.css(a, "display")) ? fb.swap(a, Yb, function () {
                        return y(a, b, d)
                    }) : y(a, b, d) : void 0
                },
                set: function (a, c, d) {
                    var e = d && u(a);
                    return w(a, c, d ? x(a, b, d, fb.support.boxSizing && "border-box" === fb.css(a, "boxSizing", false, e), e) : 0)
                }
            }
        }), fb(function () {
            fb.support.reliableMarginRight || (fb.cssHooks.marginRight = {
                get: function (a, b) {
                    return b ? fb.swap(a, {
                        display: "inline-block"
                    }, Qb, [a, "marginRight"]) : void 0
                }
            }), !fb.support.pixelPosition && fb.fn.position && fb.each(["top", "left"], function (a, b) {
                fb.cssHooks[b] = {
                    get: function (a, c) {
                        return c ? (c = Qb(a, b), Vb.test(c) ? fb(a).position()[b] + "px" : c) : void 0
                    }
                }
            })
        }), fb.expr && fb.expr.filters && (fb.expr.filters.hidden = function (a) {
            return a.offsetWidth <= 0 && a.offsetHeight <= 0
        }, fb.expr.filters.visible = function (a) {
            return !fb.expr.filters.hidden(a)
        }), fb.each({
            margin: "",
            padding: "",
            border: "Width"
        }, function (a, b) {
            fb.cssHooks[a + b] = {
                expand: function (c) {
                    for (var d = 0, e = {}, f = "string" == typeof c ? c.split(" ") : [c]; 4 > d; d++) e[a + $b[d] + b] = f[d] || f[d - 2] || f[0];
                    return e
                }
            }, Tb.test(a) || (fb.cssHooks[a + b].set = w)
        });
        var ac = /%20/g,
            bc = /\[\]$/,
            cc = /\r?\n/g,
            dc = /^(?:submit|button|image|reset|file)$/i,
            ec = /^(?:input|select|textarea|keygen)/i;
        fb.fn.extend({
            serialize: function () {
                return fb.param(this.serializeArray())
            },
            serializeArray: function () {
                return this.map(function () {
                    var a = fb.prop(this, "elements");
                    return a ? fb.makeArray(a) : this
                }).filter(function () {
                    var a = this.type;
                    return this.name && !fb(this).is(":disabled") && ec.test(this.nodeName) && !dc.test(a) && (this.checked || !Kb.test(a))
                }).map(function (a, b) {
                    var c = fb(this).val();
                    return null == c ? null : fb.isArray(c) ? fb.map(c, function (a) {
                        return {
                            name: b.name,
                            value: a.replace(cc, "\r\n")
                        }
                    }) : {
                        name: b.name,
                        value: c.replace(cc, "\r\n")
                    }
                }).get()
            }
        }), fb.param = function (a, c) {
            var d, e = [],
                f = function (a, b) {
                    b = fb.isFunction(b) ? b() : null == b ? "" : b, e[e.length] = encodeURIComponent(a) + "=" + encodeURIComponent(b)
                };
            if (c === b && (c = fb.ajaxSettings && fb.ajaxSettings.traditional), fb.isArray(a) || a.jquery && !fb.isPlainObject(a)) fb.each(a, function () {
                f(this.name, this.value)
            });
            else
                for (d in a) B(d, a[d], c, f);
            return e.join("&").replace(ac, "+")
        }, fb.each("blur focus focusin focusout load resize scroll unload click dblclick mousedown mouseup mousemove mouseover mouseout mouseenter mouseleave change select submit keydown keypress keyup error contextmenu".split(" "), function (a, b) {
            fb.fn[b] = function (a, c) {
                return arguments.length > 0 ? this.on(b, null, a, c) : this.trigger(b)
            }
        }), fb.fn.extend({
            hover: function (a, b) {
                return this.mouseenter(a).mouseleave(b || a)
            },
            bind: function (a, b, c) {
                return this.on(a, null, b, c)
            },
            unbind: function (a, b) {
                return this.off(a, null, b)
            },
            delegate: function (a, b, c, d) {
                return this.on(b, a, c, d)
            },
            undelegate: function (a, b, c) {
                return 1 === arguments.length ? this.off(a, "**") : this.off(b, a || "**", c)
            }
        });
        var fc, gc, hc = fb.now(),
            ic = /\?/,
            jc = /#.*$/,
            kc = /([?&])_=[^&]*/,
            lc = /^(.*?):[ \t]*([^\r\n]*)$/gm,
            mc = /^(?:about|app|app-storage|.+-extension|file|res|widget):$/,
            nc = /^(?:GET|HEAD)$/,
            oc = /^\/\//,
            pc = /^([\w.+-]+:)(?:\/\/([^\/?#:]*)(?::(\d+)|)|)/,
            qc = fb.fn.load,
            rc = {}, sc = {}, tc = "*/".concat("*");
        try {
            gc = S.href
        } catch (uc) {
            gc = T.createElement("a"), gc.href = "", gc = gc.href
        }
        fc = pc.exec(gc.toLowerCase()) || [], fb.fn.load = function (a, c, d) {
            if ("string" != typeof a && qc) return qc.apply(this, arguments);
            var e, f, g, h = this,
                i = a.indexOf(" ");
            return i >= 0 && (e = a.slice(i), a = a.slice(0, i)), fb.isFunction(c) ? (d = c, c = b) : c && "object" == typeof c && (f = "POST"), h.length > 0 && fb.ajax({
                url: a,
                type: f,
                dataType: "html",
                data: c
            }).done(function (a) {
                g = arguments, h.html(e ? fb("<div>").append(fb.parseHTML(a)).find(e) : a)
            }).complete(d && function (a, b) {
                h.each(d, g || [a.responseText, b, a])
            }), this
        }, fb.each(["ajaxStart", "ajaxStop", "ajaxComplete", "ajaxError", "ajaxSuccess", "ajaxSend"], function (a, b) {
            fb.fn[b] = function (a) {
                return this.on(b, a)
            }
        }), fb.extend({
            active: 0,
            lastModified: {},
            etag: {},
            ajaxSettings: {
                url: gc,
                type: "GET",
                isLocal: mc.test(fc[1]),
                global: true,
                processData: true,
                async: true,
                contentType: "application/x-www-form-urlencoded; charset=UTF-8",
                accepts: {
                    "*": tc,
                    text: "text/plain",
                    html: "text/html",
                    xml: "application/xml, text/xml",
                    json: "application/json, text/javascript"
                },
                contents: {
                    xml: /xml/,
                    html: /html/,
                    json: /json/
                },
                responseFields: {
                    xml: "responseXML",
                    text: "responseText",
                    json: "responseJSON"
                },
                converters: {
                    "* text": String,
                    "text html": true,
                    "text json": fb.parseJSON,
                    "text xml": fb.parseXML
                },
                flatOptions: {
                    url: true,
                    context: true
                }
            },
            ajaxSetup: function (a, b) {
                return b ? E(E(a, fb.ajaxSettings), b) : E(fb.ajaxSettings, a)
            },
            ajaxPrefilter: C(rc),
            ajaxTransport: C(sc),
            ajax: function (a, c) {
                function d(a, c, d, h) {
                    var j, l, s, t, v, x = c;
                    2 !== u && (u = 2, i && clearTimeout(i), e = b, g = h || "", w.readyState = a > 0 ? 4 : 0, j = a >= 200 && 300 > a || 304 === a, d && (t = F(m, w, d)), t = G(m, t, w, j), j ? (m.ifModified && (v = w.getResponseHeader("Last-Modified"), v && (fb.lastModified[f] = v), v = w.getResponseHeader("etag"), v && (fb.etag[f] = v)), 204 === a || "HEAD" === m.type ? x = "nocontent" : 304 === a ? x = "notmodified" : (x = t.state, l = t.data, s = t.error, j = !s)) : (s = x, (a || !x) && (x = "error", 0 > a && (a = 0))), w.status = a, w.statusText = (c || x) + "", j ? p.resolveWith(n, [l, x, w]) : p.rejectWith(n, [w, x, s]), w.statusCode(r), r = b, k && o.trigger(j ? "ajaxSuccess" : "ajaxError", [w, m, j ? l : s]), q.fireWith(n, [w, x]), k && (o.trigger("ajaxComplete", [w, m]), --fb.active || fb.event.trigger("ajaxStop")))
                }
                "object" == typeof a && (c = a, a = b), c = c || {};
                var e, f, g, h, i, j, k, l, m = fb.ajaxSetup({}, c),
                    n = m.context || m,
                    o = m.context && (n.nodeType || n.jquery) ? fb(n) : fb.event,
                    p = fb.Deferred(),
                    q = fb.Callbacks("once memory"),
                    r = m.statusCode || {}, s = {}, t = {}, u = 0,
                    v = "canceled",
                    w = {
                        readyState: 0,
                        getResponseHeader: function (a) {
                            var b;
                            if (2 === u) {
                                if (!h)
                                    for (h = {}; b = lc.exec(g);) h[b[1].toLowerCase()] = b[2];
                                b = h[a.toLowerCase()]
                            }
                            return null == b ? null : b
                        },
                        getAllResponseHeaders: function () {
                            return 2 === u ? g : null
                        },
                        setRequestHeader: function (a, b) {
                            var c = a.toLowerCase();
                            return u || (a = t[c] = t[c] || a, s[a] = b), this
                        },
                        overrideMimeType: function (a) {
                            return u || (m.mimeType = a), this
                        },
                        statusCode: function (a) {
                            var b;
                            if (a)
                                if (2 > u)
                                    for (b in a) r[b] = [r[b], a[b]];
                                else w.always(a[w.status]);
                            return this
                        },
                        abort: function (a) {
                            var b = a || v;
                            return e && e.abort(b), d(0, b), this
                        }
                    };
                if (p.promise(w).complete = q.add, w.success = w.done, w.error = w.fail, m.url = ((a || m.url || gc) + "").replace(jc, "").replace(oc, fc[1] + "//"), m.type = c.method || c.type || m.method || m.type, m.dataTypes = fb.trim(m.dataType || "*").toLowerCase().match(hb) || [""], null == m.crossDomain && (j = pc.exec(m.url.toLowerCase()), m.crossDomain = !(!j || j[1] === fc[1] && j[2] === fc[2] && (j[3] || ("http:" === j[1] ? "80" : "443")) === (fc[3] || ("http:" === fc[1] ? "80" : "443")))), m.data && m.processData && "string" != typeof m.data && (m.data = fb.param(m.data, m.traditional)), D(rc, m, c, w), 2 === u) return w;
                k = m.global, k && 0 === fb.active++ && fb.event.trigger("ajaxStart"), m.type = m.type.toUpperCase(), m.hasContent = !nc.test(m.type), f = m.url, m.hasContent || (m.data && (f = m.url += (ic.test(f) ? "&" : "?") + m.data, delete m.data), m.cache === false && (m.url = kc.test(f) ? f.replace(kc, "$1_=" + hc++) : f + (ic.test(f) ? "&" : "?") + "_=" + hc++)), m.ifModified && (fb.lastModified[f] && w.setRequestHeader("If-Modified-Since", fb.lastModified[f]), fb.etag[f] && w.setRequestHeader("If-None-Match", fb.etag[f])), (m.data && m.hasContent && m.contentType !== false || c.contentType) && w.setRequestHeader("Content-Type", m.contentType), w.setRequestHeader("Accept", m.dataTypes[0] && m.accepts[m.dataTypes[0]] ? m.accepts[m.dataTypes[0]] + ("*" !== m.dataTypes[0] ? ", " + tc + "; q=0.01" : "") : m.accepts["*"]);
                for (l in m.headers) w.setRequestHeader(l, m.headers[l]);
                if (m.beforeSend && (m.beforeSend.call(n, w, m) === false || 2 === u)) return w.abort();
                v = "abort";
                for (l in {
                    success: 1,
                    error: 1,
                    complete: 1
                }) w[l](m[l]);
                if (e = D(sc, m, c, w)) {
                    w.readyState = 1, k && o.trigger("ajaxSend", [w, m]), m.async && m.timeout > 0 && (i = setTimeout(function () {
                        w.abort("timeout")
                    }, m.timeout));
                    try {
                        u = 1, e.send(s, d)
                    } catch (x) {
                        if (!(2 > u)) throw x;
                        d(-1, x)
                    }
                } else d(-1, "No Transport");
                return w
            },
            getJSON: function (a, b, c) {
                return fb.get(a, b, c, "json")
            },
            getScript: function (a, c) {
                return fb.get(a, b, c, "script")
            }
        }), fb.each(["get", "post"], function (a, c) {
            fb[c] = function (a, d, e, f) {
                return fb.isFunction(d) && (f = f || e, e = d, d = b), fb.ajax({
                    url: a,
                    type: c,
                    dataType: f,
                    data: d,
                    success: e
                })
            }
        }), fb.ajaxSetup({
            accepts: {
                script: "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript"
            },
            contents: {
                script: /(?:java|ecma)script/
            },
            converters: {
                "text script": function (a) {
                    return fb.globalEval(a), a
                }
            }
        }), fb.ajaxPrefilter("script", function (a) {
            a.cache === b && (a.cache = false), a.crossDomain && (a.type = "GET")
        }), fb.ajaxTransport("script", function (a) {
            if (a.crossDomain) {
                var b, c;
                return {
                    send: function (d, e) {
                        b = fb("<script>").prop({
                            async: true,
                            charset: a.scriptCharset,
                            src: a.url
                        }).on("load error", c = function (a) {
                            b.remove(), c = null, a && e("error" === a.type ? 404 : 200, a.type)
                        }), T.head.appendChild(b[0])
                    },
                    abort: function () {
                        c && c()
                    }
                }
            }
        });
        var vc = [],
            wc = /(=)\?(?=&|$)|\?\?/;
        fb.ajaxSetup({
            jsonp: "callback",
            jsonpCallback: function () {
                var a = vc.pop() || fb.expando + "_" + hc++;
                return this[a] = true, a
            }
        }), fb.ajaxPrefilter("json jsonp", function (c, d, e) {
            var f, g, h, i = c.jsonp !== false && (wc.test(c.url) ? "url" : "string" == typeof c.data && !(c.contentType || "").indexOf("application/x-www-form-urlencoded") && wc.test(c.data) && "data");
            return i || "jsonp" === c.dataTypes[0] ? (f = c.jsonpCallback = fb.isFunction(c.jsonpCallback) ? c.jsonpCallback() : c.jsonpCallback, i ? c[i] = c[i].replace(wc, "$1" + f) : c.jsonp !== false && (c.url += (ic.test(c.url) ? "&" : "?") + c.jsonp + "=" + f), c.converters["script json"] = function () {
                return h || fb.error(f + " was not called"), h[0]
            }, c.dataTypes[0] = "json", g = a[f], a[f] = function () {
                h = arguments
            }, e.always(function () {
                a[f] = g, c[f] && (c.jsonpCallback = d.jsonpCallback, vc.push(f)), h && fb.isFunction(g) && g(h[0]), h = g = b
            }), "script") : void 0
        }), fb.ajaxSettings.xhr = function () {
            try {
                return new XMLHttpRequest
            } catch (a) {}
        };
        var xc = fb.ajaxSettings.xhr(),
            yc = {
                0: 200,
                1223: 204
            }, zc = 0,
            Ac = {};
        a.ActiveXObject && fb(a).on("unload", function () {
            for (var a in Ac) Ac[a]();
            Ac = b
        }), fb.support.cors = !! xc && "withCredentials" in xc, fb.support.ajax = xc = !! xc, fb.ajaxTransport(function (a) {
            var c;
            return fb.support.cors || xc && !a.crossDomain ? {
                send: function (d, e) {
                    var f, g, h = a.xhr();
                    if (h.open(a.type, a.url, a.async, a.username, a.password), a.xhrFields)
                        for (f in a.xhrFields) h[f] = a.xhrFields[f];
                    a.mimeType && h.overrideMimeType && h.overrideMimeType(a.mimeType), a.crossDomain || d["X-Requested-With"] || (d["X-Requested-With"] = "XMLHttpRequest");
                    for (f in d) h.setRequestHeader(f, d[f]);
                    c = function (a) {
                        return function () {
                            c && (delete Ac[g], c = h.onload = h.onerror = null, "abort" === a ? h.abort() : "error" === a ? e(h.status || 404, h.statusText) : e(yc[h.status] || h.status, h.statusText, "string" == typeof h.responseText ? {
                                text: h.responseText
                            } : b, h.getAllResponseHeaders()))
                        }
                    }, h.onload = c(), h.onerror = c("error"), c = Ac[g = zc++] = c("abort"), h.send(a.hasContent && a.data || null)
                },
                abort: function () {
                    c && c()
                }
            } : void 0
        });
        var Bc, Cc, Dc = /^(?:toggle|show|hide)$/,
            Ec = new RegExp("^(?:([+-])=|)(" + gb + ")([a-z%]*)$", "i"),
            Fc = /queueHooks$/,
            Gc = [L],
            Hc = {
                "*": [
                    function (a, b) {
                        var c = this.createTween(a, b),
                            d = c.cur(),
                            e = Ec.exec(b),
                            f = e && e[3] || (fb.cssNumber[a] ? "" : "px"),
                            g = (fb.cssNumber[a] || "px" !== f && +d) && Ec.exec(fb.css(c.elem, a)),
                            h = 1,
                            i = 20;
                        if (g && g[3] !== f) {
                            f = f || g[3], e = e || [], g = +d || 1;
                            do h = h || ".5", g /= h, fb.style(c.elem, a, g + f); while (h !== (h = c.cur() / d) && 1 !== h && --i)
                        }
                        return e && (g = c.start = +g || +d || 0, c.unit = f, c.end = e[1] ? g + (e[1] + 1) * e[2] : +e[2]), c
                    }
                ]
            };
        fb.Animation = fb.extend(J, {
            tweener: function (a, b) {
                fb.isFunction(a) ? (b = a, a = ["*"]) : a = a.split(" ");
                for (var c, d = 0, e = a.length; e > d; d++) c = a[d], Hc[c] = Hc[c] || [], Hc[c].unshift(b)
            },
            prefilter: function (a, b) {
                b ? Gc.unshift(a) : Gc.push(a)
            }
        }), fb.Tween = M, M.prototype = {
            constructor: M,
            init: function (a, b, c, d, e, f) {
                this.elem = a, this.prop = c, this.easing = e || "swing", this.options = b, this.start = this.now = this.cur(), this.end = d, this.unit = f || (fb.cssNumber[c] ? "" : "px")
            },
            cur: function () {
                var a = M.propHooks[this.prop];
                return a && a.get ? a.get(this) : M.propHooks._default.get(this)
            },
            run: function (a) {
                var b, c = M.propHooks[this.prop];
                return this.pos = b = this.options.duration ? fb.easing[this.easing](a, this.options.duration * a, 0, 1, this.options.duration) : a, this.now = (this.end - this.start) * b + this.start, this.options.step && this.options.step.call(this.elem, this.now, this), c && c.set ? c.set(this) : M.propHooks._default.set(this), this
            }
        }, M.prototype.init.prototype = M.prototype, M.propHooks = {
            _default: {
                get: function (a) {
                    var b;
                    return null == a.elem[a.prop] || a.elem.style && null != a.elem.style[a.prop] ? (b = fb.css(a.elem, a.prop, ""), b && "auto" !== b ? b : 0) : a.elem[a.prop]
                },
                set: function (a) {
                    fb.fx.step[a.prop] ? fb.fx.step[a.prop](a) : a.elem.style && (null != a.elem.style[fb.cssProps[a.prop]] || fb.cssHooks[a.prop]) ? fb.style(a.elem, a.prop, a.now + a.unit) : a.elem[a.prop] = a.now
                }
            }
        }, M.propHooks.scrollTop = M.propHooks.scrollLeft = {
            set: function (a) {
                a.elem.nodeType && a.elem.parentNode && (a.elem[a.prop] = a.now)
            }
        }, fb.each(["toggle", "show", "hide"], function (a, b) {
            var c = fb.fn[b];
            fb.fn[b] = function (a, d, e) {
                return null == a || "boolean" == typeof a ? c.apply(this, arguments) : this.animate(N(b, true), a, d, e)
            }
        }), fb.fn.extend({
            fadeTo: function (a, b, c, d) {
                return this.filter(t).css("opacity", 0).show().end().animate({
                    opacity: b
                }, a, c, d)
            },
            animate: function (a, b, c, d) {
                var e = fb.isEmptyObject(a),
                    f = fb.speed(b, c, d),
                    g = function () {
                        var b = J(this, fb.extend({}, a), f);
                        (e || qb.get(this, "finish")) && b.stop(true)
                    };
                return g.finish = g, e || f.queue === false ? this.each(g) : this.queue(f.queue, g)
            },
            stop: function (a, c, d) {
                var e = function (a) {
                    var b = a.stop;
                    delete a.stop, b(d)
                };
                return "string" != typeof a && (d = c, c = a, a = b), c && a !== false && this.queue(a || "fx", []), this.each(function () {
                    var b = true,
                        c = null != a && a + "queueHooks",
                        f = fb.timers,
                        g = qb.get(this);
                    if (c) g[c] && g[c].stop && e(g[c]);
                    else
                        for (c in g) g[c] && g[c].stop && Fc.test(c) && e(g[c]);
                    for (c = f.length; c--;) f[c].elem !== this || null != a && f[c].queue !== a || (f[c].anim.stop(d), b = false, f.splice(c, 1));
                    (b || !d) && fb.dequeue(this, a)
                })
            },
            finish: function (a) {
                return a !== false && (a = a || "fx"), this.each(function () {
                    var b, c = qb.get(this),
                        d = c[a + "queue"],
                        e = c[a + "queueHooks"],
                        f = fb.timers,
                        g = d ? d.length : 0;
                    for (c.finish = true, fb.queue(this, a, []), e && e.stop && e.stop.call(this, true), b = f.length; b--;) f[b].elem === this && f[b].queue === a && (f[b].anim.stop(true), f.splice(b, 1));
                    for (b = 0; g > b; b++) d[b] && d[b].finish && d[b].finish.call(this);
                    delete c.finish
                })
            }
        }), fb.each({
            slideDown: N("show"),
            slideUp: N("hide"),
            slideToggle: N("toggle"),
            fadeIn: {
                opacity: "show"
            },
            fadeOut: {
                opacity: "hide"
            },
            fadeToggle: {
                opacity: "toggle"
            }
        }, function (a, b) {
            fb.fn[a] = function (a, c, d) {
                return this.animate(b, a, c, d)
            }
        }), fb.speed = function (a, b, c) {
            var d = a && "object" == typeof a ? fb.extend({}, a) : {
                complete: c || !c && b || fb.isFunction(a) && a,
                duration: a,
                easing: c && b || b && !fb.isFunction(b) && b
            };
            return d.duration = fb.fx.off ? 0 : "number" == typeof d.duration ? d.duration : d.duration in fb.fx.speeds ? fb.fx.speeds[d.duration] : fb.fx.speeds._default, (null == d.queue || d.queue === true) && (d.queue = "fx"), d.old = d.complete, d.complete = function () {
                fb.isFunction(d.old) && d.old.call(this), d.queue && fb.dequeue(this, d.queue)
            }, d
        }, fb.easing = {
            linear: function (a) {
                return a
            },
            swing: function (a) {
                return .5 - Math.cos(a * Math.PI) / 2
            }
        }, fb.timers = [], fb.fx = M.prototype.init, fb.fx.tick = function () {
            var a, c = fb.timers,
                d = 0;
            for (Bc = fb.now(); d < c.length; d++) a = c[d], a() || c[d] !== a || c.splice(d--, 1);
            c.length || fb.fx.stop(), Bc = b
        }, fb.fx.timer = function (a) {
            a() && fb.timers.push(a) && fb.fx.start()
        }, fb.fx.interval = 13, fb.fx.start = function () {
            Cc || (Cc = setInterval(fb.fx.tick, fb.fx.interval))
        }, fb.fx.stop = function () {
            clearInterval(Cc), Cc = null
        }, fb.fx.speeds = {
            slow: 600,
            fast: 200,
            _default: 400
        }, fb.fx.step = {}, fb.expr && fb.expr.filters && (fb.expr.filters.animated = function (a) {
            return fb.grep(fb.timers, function (b) {
                return a === b.elem
            }).length
        }), fb.fn.offset = function (a) {
            if (arguments.length) return a === b ? this : this.each(function (b) {
                fb.offset.setOffset(this, a, b)
            });
            var c, d, e = this[0],
                f = {
                    top: 0,
                    left: 0
                }, g = e && e.ownerDocument;
            if (g) return c = g.documentElement, fb.contains(c, e) ? (typeof e.getBoundingClientRect !== R && (f = e.getBoundingClientRect()), d = O(g), {
                top: f.top + d.pageYOffset - c.clientTop,
                left: f.left + d.pageXOffset - c.clientLeft
            }) : f
        }, fb.offset = {
            setOffset: function (a, b, c) {
                var d, e, f, g, h, i, j, k = fb.css(a, "position"),
                    l = fb(a),
                    m = {};
                "static" === k && (a.style.position = "relative"), h = l.offset(), f = fb.css(a, "top"), i = fb.css(a, "left"), j = ("absolute" === k || "fixed" === k) && (f + i).indexOf("auto") > -1, j ? (d = l.position(), g = d.top, e = d.left) : (g = parseFloat(f) || 0, e = parseFloat(i) || 0), fb.isFunction(b) && (b = b.call(a, c, h)), null != b.top && (m.top = b.top - h.top + g), null != b.left && (m.left = b.left - h.left + e), "using" in b ? b.using.call(a, m) : l.css(m)
            }
        }, fb.fn.extend({
            position: function () {
                if (this[0]) {
                    var a, b, c = this[0],
                        d = {
                            top: 0,
                            left: 0
                        };
                    return "fixed" === fb.css(c, "position") ? b = c.getBoundingClientRect() : (a = this.offsetParent(), b = this.offset(), fb.nodeName(a[0], "html") || (d = a.offset()), d.top += fb.css(a[0], "borderTopWidth", true), d.left += fb.css(a[0], "borderLeftWidth", true)), {
                        top: b.top - d.top - fb.css(c, "marginTop", true),
                        left: b.left - d.left - fb.css(c, "marginLeft", true)
                    }
                }
            },
            offsetParent: function () {
                return this.map(function () {
                    for (var a = this.offsetParent || U; a && !fb.nodeName(a, "html") && "static" === fb.css(a, "position");) a = a.offsetParent;
                    return a || U
                })
            }
        }), fb.each({
            scrollLeft: "pageXOffset",
            scrollTop: "pageYOffset"
        }, function (c, d) {
            var e = "pageYOffset" === d;
            fb.fn[c] = function (f) {
                return fb.access(this, function (c, f, g) {
                    var h = O(c);
                    return g === b ? h ? h[d] : c[f] : (h ? h.scrollTo(e ? a.pageXOffset : g, e ? g : a.pageYOffset) : c[f] = g, void 0)
                }, c, f, arguments.length, null)
            }
        }), fb.each({
            Height: "height",
            Width: "width"
        }, function (a, c) {
            fb.each({
                padding: "inner" + a,
                content: c,
                "": "outer" + a
            }, function (d, e) {
                fb.fn[e] = function (e, f) {
                    var g = arguments.length && (d || "boolean" != typeof e),
                        h = d || (e === true || f === true ? "margin" : "border");
                    return fb.access(this, function (c, d, e) {
                        var f;
                        return fb.isWindow(c) ? c.document.documentElement["client" + a] : 9 === c.nodeType ? (f = c.documentElement, Math.max(c.body["scroll" + a], f["scroll" + a], c.body["offset" + a], f["offset" + a], f["client" + a])) : e === b ? fb.css(c, d, h) : fb.style(c, d, e, h)
                    }, c, g ? e : b, g, null)
                }
            })
        }), fb.fn.size = function () {
            return this.length
        }, fb.fn.andSelf = fb.fn.addBack, "object" == typeof module && module && "object" == typeof module.exports ? module.exports = fb : "function" == typeof define && define.amd && define("jquery", [], function () {
            return fb
        }), "object" == typeof a && "object" == typeof a.document && (a.jQuery = a.$ = fb)
    }(window), define("htmlvn/lib/utils", ["jquery"], function (a) {
        "use strict";

        // Try
        function b(a) {
            try {
                a()
            } catch (b) {
                console.error(b)
            }
        }

        // to number
        function c(b) {
            return v.test(b) ? null : t.test(b) ? true : u.test(b) ? false : a.isNumeric(b) ? parseFloat(b) : b
        }

        function d(a, b, c, d, e) {
            for (var f = 0; f < d.length; ++f) {
                var g = d[f];
                // For g in d
                if (g in c) return a[b] = c[g], void 0
            }
            5 === arguments.length && (a[b] = e)
        }

        function e(a, b, c) {
            for (var d = 0; d < b.length; ++d) {
                var e = b[d];
                if (e in a) return a[e]
            }
            return c
        }

        // return the one that exists
        function f(a, b) {
            return "undefined" == typeof a ? b : a
        }

        function g(a, b) {
            var c = a[b];
            return delete a[b], c
        }

        function h() {
            w = false
        }

        function i() {
            w = true
        }

        function j() {}

        function k(a) {}

        function l() {}

        function m(a) {}

        function n(a) {}

        function o(a, b, c, d) {}

        function p(a) {
            var b = null;
            return b
        }

        function q(a) {
            return false
        }

        function r() {}

        function s() {
            for (var a = arguments[0], b = 0; b < arguments.length - 1; b++) {
                var c = new RegExp("\\{" + b + "\\}", "gm");
                a = a.replace(c, arguments[b + 1])
            }
            return a
        }
        String.prototype.startsWith || (String.prototype.startsWith = function (a) {
            return this.slice(0, a.length) == a
        }), String.prototype.endsWith || (String.prototype.endsWith = function (a) {
            return this.slice(-a.length) == a
        }), String.prototype.trim || (String.prototype.trim = function () {
            return this.replace(/^\s+|\s+$/gm, "")
        });
        var t = /^true$/i,
            u = /^false$/i,
            v = /^null$/i,
            w = true,
            x = "animationstart animationStart webkitAnimationStart oanimationstart oAnimationStart MSAnimationStart",
            y = "animationend animationEnd webkitAnimationEnd oanimationend oAnimationEnd MSAnimationEnd",
            z = "transitionend transitionEnd webkitTransitionEnd otransitionend oTransitionEnd MSTransitionEnd";
        return {
            pick: f,
            pickIn: e,
            pickInAndSet: d,
            getAndDelete: g,
            transitionend: z,
            animationstart: x,
            animationend: y,
            coerceType: c,
            blockHashUpdate: h,
            resumeHashUpdate: i,
            getHashParams: j,
            setHashParams: k,
            removeHashParam: m,
            updateHashParams: n,
            removeAllHashParams: l,
            saveGameState: o,
            getGameState: p,
            hasGameState: q,
            clearGameState: r,
            format: s,
            runSafe: b
        }
    }),
    function () {
        function a() {}

        function b() {
            WAssert(false, "Not implemented")()
        }
        if (!String.prototype.format) {
            var c = {};
            String.prototype.format = function () {
                for (var a = this, b = arguments, d = b.length; --d >= 0;) a = a.replace(c[d] || (c[d] = RegExp("\\{" + d + "\\}", "gm")), b[d]);
                return a
            }, String.format || (String.format = function (a) {
                for (var b = arguments, d = b.length; --d;) a = a.replace(c[d - 1] || (c[d - 1] = RegExp("\\{" + (d - 1) + "\\}", "gm")), b[d]);
                return a
            })
        }
        window.WAssert = function (b, c) {
            if ("function" == typeof c && (c = c.apply(this, arguments) || ""), "function" == typeof b ? !b.apply(this, arguments) : !b) {
                var d = Array.prototype.slice.call(arguments, 1),
                    e = "string" == typeof c ? String.format.apply(c, d) : c;
                return window.console && !console.__throwErrorOnAssert && console.assert && console.assert.bind && console.assert.bind(console, b, e) || function () {
                    throw e
                }
            }
            return a
        };
        var d = Function.prototype,
            e = Array.prototype,
            f = e.forEach,
            g = Object.defineProperty,
            h = "function" == typeof Object.defineProperties,
            i = {};
        if (i = i.__proto__ === Object.prototype) try {
            i = {}, i.__proto__ = {
                Object: 1
            }, i = 1 === i.Object
        } catch (j) {
            i = false
        }
        if ("function" != typeof Object.getPrototypeOf && (Object.getPrototypeOf = i ? function (a) {
            return a.__proto__
        } : function (a) {
            return null != a && a.constructor && a !== Object.prototype ? a.constructor.prototype === a ? Object.prototype : a.constructor.prototype : null
        }), f || (e.forEach = f = function (a, b) {
            for (var c = 0, d = this.length; d > c; ++c) a.call(b || this, this[c], c, this)
        }), d.fastClass = function (a) {
            var b = this,
                c = this.prototype;
            a = a || function () {
                this.constructor = function () {
                    b.apply(this, arguments)
                }
            }, a.prototype = c;
            var e, f = new a(c, this);
            return f.hasOwnProperty("constructor") || (f.constructor = function () {
                b.apply(this, arguments)
            }), e = f.constructor, e.prototype = f, WAssert(false, window.intellisense && function () {
                var c = f;
                intellisense.redirectDefinition(e, c.hasOwnProperty("constructor") ? c.constructor : a), intellisense.annotate(e, c.hasOwnProperty("constructor") ? c.constructor : baseCtor), c.constructor = e, Object.getOwnPropertyNames(c).forEach(function (a) {
                    var d = c[a];
                    "function" == typeof d && intellisense.addEventListener("signaturehelp", function (c) {
                        if (c.target == d) {
                            for (var e = [c.functionHelp], f = b.prototype; f != Object.prototype;) e.push(f.hasOwnProperty(a) ? f[a] : null), f = Object.getPrototypeOf(f);
                            intellisense.inheritXMLDoc.apply(null, e)
                        }
                    })
                })
            }), a = null, arguments.length > 1 && d.define.apply(e, arguments), e
        }, d.inheritWith = i ? function (a) {
            var b = this,
                c = ("function" == typeof a ? a.call(this, this.prototype, this) : a) || {}, e = c.hasOwnProperty("constructor") ? c.constructor : function () {
                    b.apply(this, arguments)
                };
            return e.prototype = c, c.__proto__ = this.prototype, a = null, arguments.length > 1 && d.define.apply(e, arguments), e
        } : function (b) {
            var c = this,
                e = ("function" == typeof b ? b.call(this, this.prototype, this) : b) || {}, f = e.hasOwnProperty("constructor") ? e.constructor : function () {
                    c.apply(this, arguments)
                };
            WAssert(false, window.intellisense && function () {
                intellisense.redirectDefinition(f, e.hasOwnProperty("constructor") ? e.constructor : b), intellisense.annotate(f, e.hasOwnProperty("constructor") ? e.constructor : c), e.constructor = f, Object.getOwnPropertyNames(e).forEach(function (a) {
                    var b = e[a];
                    "function" == typeof b && intellisense.addEventListener("signaturehelp", function (d) {
                        if (d.target == b) {
                            for (var e = [d.functionHelp], f = c.prototype; f != Object.prototype;) e.push(f.hasOwnProperty(a) ? f[a] : null), f = Object.getPrototypeOf(f);
                            intellisense.inheritXMLDoc.apply(null, e)
                        }
                    })
                })
            });
            var g;
            return a.prototype = this.prototype, f.prototype = g = new a, b = e, d.define.apply(f, arguments), f
        }, d.define = function (b, c) {
            var d = this,
                e = this.prototype,
                i = b;
            if (b) {
                "function" == typeof b && (b = b.call(e, this.prototype, this));
                for (var j in b) e[j] = b[j]
            }
            return b = null, (arguments.length > 2 || c) && (e.hasOwnProperty("__mixins__") || (h ? g(e, "__mixins__", {
                enumerable: false,
                value: [],
                writeable: false
            }).__mixins__.__hidden = true : e.__mixins__ = [])) && f.call(arguments, function (b, c, f, g) {
                if (g = "function" == typeof b, g ? (a.prototype = b.prototype, f = new b(e, d)) : f = b, f) {
                    g && e.__mixins__.push(b);
                    for (var h in f) "constructor" != h && "prototype" != h && (WAssert(true, function () {
                        if (h in e) {
                            if (e[h] && e[h].abstract) return;
                            var a = "The '{0}' mixin defines a '{1}' named '{2}' which is already defined on the class {3}!".format(g && b.name || c - 1, "function" == typeof f[h] ? "function" : "member", h, d.name ? "'" + d.name + "'" : "");
                            throw console.log(a), window.intellisense && intellisense.logMessage(a), a
                        }
                        "function" == typeof f[h] && b != f[h] && b != d && b !== e && (f[h].__glyph = "GlyphCppProject")
                    }), e[h] = f[h])
                }
            }), WAssert(true, window.intellisense && function () {
                a.prototype = e;
                var b = new a;
                d.call(b);
                for (var c in b) "constructor" !== c && (i.hasOwnProperty(c) || (i[c] = b[c]))
            }), this
        }, Function.define = function (a, b) {
            var c, e = a || function () {}, f = arguments.length > 1;
            return "function" != typeof a ? (e = a.hasOwnProperty("constructor") ? a.constructor : function () {}, e.prototype = a, WAssert(true, window.intellisense && function () {
                function b() {
                    for (var b in a) a.hasOwnProperty(b) && (this[b] = a[b])
                }
                b.prototype = Object.getPrototypeOf(a), e.prototype = new b
            }), f = true) : (a = b, b = null), f && d.define.apply(e, arguments), c = function () {
                Function.initMixins(this), e.apply(this, arguments)
            }, c.prototype = e.prototype, WAssert(true, window.intellisense && function () {
                window.intellisense && intellisense.redirectDefinition(c, e)
            }), c
        }, d.defineStatic = function (a) {
            if (a)
                for (var b in a) this[b] = a[b];
            return this
        }, b.defineStatic({
            "abstract": true
        }), Function.abstract = function (a, c) {
            var d = a || c ? function () {
                    "function" == typeof a && a.apply(this, arguments), "function" == typeof c && c.apply(this, arguments), "string" == typeof a ? WAssert(false, a)() : b()
                }.defineStatic({
                    "abstract": true
                }) : b;
            return WAssert(true, window.intellisense && function () {
                d != b && ("function" == typeof a && intellisense.redirectDefinition(d, a), "function" == typeof c && intellisense.redirectDefinition(d, c))
            }), d
        }, Function.initMixins = function (a) {
            if (a && !a.__initMixins__) {
                var b, c, d, e, f = a,
                    g = {};
                for (a.__initMixins__ = 1, WAssert(true, window.intellisense && function () {
                    a.__initMixins__ = {
                        __hidden: true
                    }
                }); f;)
                    if (f = i ? f.__proto__ : Object.getPrototypeOf(f), f && f.hasOwnProperty("__mixins__") && (b = f.__mixins__) && (c = b.length))
                        for (d = 0; e = b[d], c > d; d++) e in g || (g[e] = 1, e.call(a, f, f.constructor));
                delete a.__initMixins__
            }
        }, h) {
            var k = {
                0: [Function, "initMixins", "define", "abstract"],
                1: [d, "fastClass", "inheritWith", "define", "defineStatic"]
            };
            for (var l in k)
                for (var m, n = k[l], o = n[0], p = 1; m = n[p], p < n.length; p++) g(o, m, {
                    enumerable: false,
                    value: o[m]
                })
        }
    }(), define("FastClass", function (a) {
        return function () {
            var b;
            return b || a.Function.define
        }
    }(this)), define("htmlvn/lib/Class", ["FastClass"], function () {
        var a = Function.define({
            constructor: function () {}
        });
        return a
    }), define("htmlvn/Game", ["htmlvn/lib/utils", "htmlvn/lib/Class"], function (a, b) {
        var c = {
            parallelLoads: 3,
            canvasWidth: 1024,
            canvasHeight: 768,
            language: "en"
        }, d = null,
            e = b.inheritWith(function () {
                return {
                    constructor: function (a) {
                        this.__options = $.extend({}, c, a), this.__identifier = a.identifier, this.__defaultScene = a.defaultScene, d = this;
                        var b = this.__identifier.split(".");
                        this.__finalComponent = b[b.length - 1]
                    },
                    getIdentifier: function () {
                        return this.__identifier
                    },
                    getLanguage: function () {
                        return this.getOption("language", "en")
                    },
                    getDefaultScene: function () {
                        return this.__defaultScene
                    },
                    getOptions: function () {
                        return $.extend({}, this.__options)
                    },
                    getOption: function (a, b) {
                        return this.__options.hasOwnProperty(a) ? this.__options[a] : b
                    }
                }
            }).defineStatic({
                defaults: c,
                getAll: function () {
                    return d.getOptions()
                },
                get: function (a, b) {
                    return d.getOption(a, b)
                },
                getDefaultScene: function () {
                    return d.getDefaultScene()
                },
                getLanguage: function () {
                    return d.getLanguage()
                }
            });
        return e
    }),
    function (a) {
        if ("function" == typeof bootstrap) bootstrap("promise", a);
        else if ("object" == typeof exports) module.exports = a();
        else if ("function" == typeof define && define.amd) define("Q", a);
        else if ("undefined" != typeof ses) {
            if (!ses.ok()) return;
            ses.makeQ = a
        } else Q = a()
    }(function () {
        "use strict";

        function a(a) {
            return function () {
                return X.apply(a, arguments)
            }
        }

        function b(a) {
            return a === Object(a)
        }

        function c(a) {
            return "[object StopIteration]" === db(a) || a instanceof T
        }

        function d(a, b) {
            if (Q && b.stack && "object" == typeof a && null !== a && a.stack && -1 === a.stack.indexOf(fb)) {
                for (var c = [], d = b; d; d = d.source) d.stack && c.unshift(d.stack);
                c.unshift(a.stack);
                var f = c.join("\n" + fb + "\n");
                a.stack = e(f)
            }
        }

        function e(a) {
            for (var b = a.split("\n"), c = [], d = 0; d < b.length; ++d) {
                var e = b[d];
                h(e) || f(e) || !e || c.push(e)
            }
            return c.join("\n")
        }

        function f(a) {
            return -1 !== a.indexOf("(module.js:") || -1 !== a.indexOf("(node.js:")
        }

        function g(a) {
            var b = /at .+ \((.+):(\d+):(?:\d+)\)$/.exec(a);
            if (b) return [b[1], Number(b[2])];
            var c = /at ([^ ]+):(\d+):(?:\d+)$/.exec(a);
            if (c) return [c[1], Number(c[2])];
            var d = /.*@(.+):(\d+)$/.exec(a);
            return d ? [d[1], Number(d[2])] : void 0
        }

        function h(a) {
            var b = g(a);
            if (!b) return false;
            var c = b[0],
                d = b[1];
            return c === S && d >= U && kb >= d
        }

        function i() {
            if (Q) try {
                throw new Error
            } catch (a) {
                var b = a.stack.split("\n"),
                    c = b[0].indexOf("@") > 0 ? b[1] : b[2],
                    d = g(c);
                if (!d) return;
                return S = d[0], d[1]
            }
        }

        function j(a, b, c) {
            return function () {
                return "undefined" != typeof console && "function" == typeof console.warn && console.warn(b + " is deprecated, use " + c + " instead.", new Error("").stack), a.apply(a, arguments)
            }
        }

        function k(a) {
            return r(a) ? a : s(a) ? D(a) : C(a)
        }

        function l() {
            function a(a) {
                b = a, f.source = a, Z(c, function (b, c) {
                    W(function () {
                        a.promiseDispatch.apply(a, c)
                    })
                }, void 0), c = void 0, d = void 0
            }
            var b, c = [],
                d = [],
                e = ab(l.prototype),
                f = ab(o.prototype);
            if (f.promiseDispatch = function (a, e, f) {
                var g = Y(arguments);
                c ? (c.push(g), "when" === e && f[1] && d.push(f[1])) : W(function () {
                    b.promiseDispatch.apply(b, g)
                })
            }, f.valueOf = j(function () {
                if (c) return f;
                var a = q(b);
                return r(a) && (b = a), a
            }, "valueOf", "inspect"), f.inspect = function () {
                return b ? b.inspect() : {
                    state: "pending"
                }
            }, k.longStackSupport && Q) try {
                throw new Error
            } catch (g) {
                f.stack = g.stack.substring(g.stack.indexOf("\n") + 1)
            }
            return e.promise = f, e.resolve = function (c) {
                b || a(k(c))
            }, e.fulfill = function (c) {
                b || a(C(c))
            }, e.reject = function (c) {
                b || a(B(c))
            }, e.notify = function (a) {
                b || Z(d, function (b, c) {
                    W(function () {
                        c(a)
                    })
                }, void 0)
            }, e
        }

        function m(a) {
            if ("function" != typeof a) throw new TypeError("resolver must be a function.");
            var b = l();
            try {
                a(b.resolve, b.reject, b.notify)
            } catch (c) {
                b.reject(c)
            }
            return b.promise
        }

        function n(a) {
            return m(function (b, c) {
                for (var d = 0, e = a.length; e > d; d++) k(a[d]).then(b, c)
            })
        }

        function o(a, b, c) {
            void 0 === b && (b = function (a) {
                return B(new Error("Promise does not support operation: " + a))
            }), void 0 === c && (c = function () {
                return {
                    state: "unknown"
                }
            });
            var d = ab(o.prototype);
            if (d.promiseDispatch = function (c, e, f) {
                var g;
                try {
                    g = a[e] ? a[e].apply(d, f) : b.call(d, e, f)
                } catch (h) {
                    g = B(h)
                }
                c && c(g)
            }, d.inspect = c, c) {
                var e = c();
                "rejected" === e.state && (d.exception = e.reason), d.valueOf = j(function () {
                    var a = c();
                    return "pending" === a.state || "rejected" === a.state ? d : a.value
                })
            }
            return d
        }

        function p(a, b, c, d) {
            return k(a).then(b, c, d)
        }

        function q(a) {
            if (r(a)) {
                var b = a.inspect();
                if ("fulfilled" === b.state) return b.value
            }
            return a
        }

        function r(a) {
            return b(a) && "function" == typeof a.promiseDispatch && "function" == typeof a.inspect
        }

        function s(a) {
            return b(a) && "function" == typeof a.then
        }

        function t(a) {
            return r(a) && "pending" === a.inspect().state
        }

        function u(a) {
            return !r(a) || "fulfilled" === a.inspect().state
        }

        function v(a) {
            return r(a) && "rejected" === a.inspect().state
        }

        function w() {
            ib || "undefined" == typeof window || window.Touch || !window.console || console.warn("[Q] Unhandled rejection reasons (should be empty):", gb), ib = true
        }

        function x() {
            for (var a = 0; a < gb.length; a++) {
                var b = gb[a];
                console.warn("Unhandled rejection reason:", b)
            }
        }

        function y() {
            gb.length = 0, hb.length = 0, ib = false, jb || (jb = true, "undefined" != typeof process && process.on && process.on("exit", x))
        }

        function z(a, b) {
            jb && (hb.push(a), b && "undefined" != typeof b.stack ? gb.push(b.stack) : gb.push("(no stack) " + b), w())
        }

        function A(a) {
            if (jb) {
                var b = $(hb, a); - 1 !== b && (hb.splice(b, 1), gb.splice(b, 1))
            }
        }

        function B(a) {
            var b = o({
                when: function (b) {
                    return b && A(this), b ? b(a) : this
                }
            }, function () {
                return this
            }, function () {
                return {
                    state: "rejected",
                    reason: a
                }
            });
            return z(b, a), b
        }

        function C(a) {
            return o({
                when: function () {
                    return a
                },
                get: function (b) {
                    return a[b]
                },
                set: function (b, c) {
                    a[b] = c
                },
                "delete": function (b) {
                    delete a[b]
                },
                post: function (b, c) {
                    return null === b || void 0 === b ? a.apply(void 0, c) : a[b].apply(a, c)
                },
                apply: function (b, c) {
                    return a.apply(b, c)
                },
                keys: function () {
                    return cb(a)
                }
            }, void 0, function () {
                return {
                    state: "fulfilled",
                    value: a
                }
            })
        }

        function D(a) {
            var b = l();
            return W(function () {
                try {
                    a.then(b.resolve, b.reject, b.notify)
                } catch (c) {
                    b.reject(c)
                }
            }), b.promise
        }

        function E(a) {
            return o({
                isDef: function () {}
            }, function (b, c) {
                return K(a, b, c)
            }, function () {
                return k(a).inspect()
            })
        }

        function F(a, b, c) {
            return k(a).spread(b, c)
        }

        function G(a) {
            return function () {
                function b(a, b) {
                    var g;
                    if (eb) {
                        try {
                            g = d[a](b)
                        } catch (h) {
                            return B(h)
                        }
                        return g.done ? g.value : p(g.value, e, f)
                    }
                    try {
                        g = d[a](b)
                    } catch (h) {
                        return c(h) ? h.value : B(h)
                    }
                    return p(g, e, f)
                }
                var d = a.apply(this, arguments),
                    e = b.bind(b, "next"),
                    f = b.bind(b, "throw");
                return e()
            }
        }

        function H(a) {
            k.done(k.async(a)())
        }

        function I(a) {
            throw new T(a)
        }

        function J(a) {
            return function () {
                return F([this, L(arguments)], function (b, c) {
                    return a.apply(b, c)
                })
            }
        }

        function K(a, b, c) {
            return k(a).dispatch(b, c)
        }

        function L(a) {
            return p(a, function (a) {
                var b = 0,
                    c = l();
                return Z(a, function (d, e, f) {
                    var g;
                    r(e) && "fulfilled" === (g = e.inspect()).state ? a[f] = g.value : (++b, p(e, function (d) {
                        a[f] = d, 0 === --b && c.resolve(a)
                    }, c.reject, function (a) {
                        c.notify({
                            index: f,
                            value: a
                        })
                    }))
                }, void 0), 0 === b && c.resolve(a), c.promise
            })
        }

        function M(a) {
            return p(a, function (a) {
                return a = _(a, k), p(L(_(a, function (a) {
                    return p(a, V, V)
                })), function () {
                    return a
                })
            })
        }

        function N(a) {
            return k(a).allSettled()
        }

        function O(a, b) {
            return k(a).then(void 0, void 0, b)
        }

        function P(a, b) {
            return k(a).nodeify(b)
        }
        var Q = false;
        try {
            throw new Error
        } catch (R) {
            Q = !! R.stack
        }
        var S, T, U = i(),
            V = function () {}, W = function () {
                function a() {
                    for (; b.next;) {
                        b = b.next;
                        var c = b.task;
                        b.task = void 0;
                        var e = b.domain;
                        e && (b.domain = void 0, e.enter());
                        try {
                            c()
                        } catch (g) {
                            if (f) throw e && e.exit(), setTimeout(a, 0), e && e.enter(), g;
                            setTimeout(function () {
                                throw g
                            }, 0)
                        }
                        e && e.exit()
                    }
                    d = false
                }
                var b = {
                    task: void 0,
                    next: null
                }, c = b,
                    d = false,
                    e = void 0,
                    f = false;
                if (W = function (a) {
                    c = c.next = {
                        task: a,
                        domain: f && process.domain,
                        next: null
                    }, d || (d = true, e())
                }, "undefined" != typeof process && process.nextTick) f = true, e = function () {
                    process.nextTick(a)
                };
                else if ("function" == typeof setImmediate) e = "undefined" != typeof window ? setImmediate.bind(window, a) : function () {
                    setImmediate(a)
                };
                else if ("undefined" != typeof MessageChannel) {
                    var g = new MessageChannel;
                    g.port1.onmessage = function () {
                        e = h, g.port1.onmessage = a, a()
                    };
                    var h = function () {
                        g.port2.postMessage(0)
                    };
                    e = function () {
                        setTimeout(a, 0), h()
                    }
                } else e = function () {
                    setTimeout(a, 0)
                };
                return W
            }(),
            X = Function.call,
            Y = a(Array.prototype.slice),
            Z = a(Array.prototype.reduce || function (a, b) {
                var c = 0,
                    d = this.length;
                if (1 === arguments.length)
                    for (;;) {
                        if (c in this) {
                            b = this[c++];
                            break
                        }
                        if (++c >= d) throw new TypeError
                    }
                for (; d > c; c++) c in this && (b = a(b, this[c], c));
                return b
            }),
            $ = a(Array.prototype.indexOf || function (a) {
                for (var b = 0; b < this.length; b++)
                    if (this[b] === a) return b;
                return -1
            }),
            _ = a(Array.prototype.map || function (a, b) {
                var c = this,
                    d = [];
                return Z(c, function (e, f, g) {
                    d.push(a.call(b, f, g, c))
                }, void 0), d
            }),
            ab = Object.create || function (a) {
                function b() {}
                return b.prototype = a, new b
            }, bb = a(Object.prototype.hasOwnProperty),
            cb = Object.keys || function (a) {
                var b = [];
                for (var c in a) bb(a, c) && b.push(c);
                return b
            }, db = a(Object.prototype.toString);
        T = "undefined" != typeof ReturnValue ? ReturnValue : function (a) {
            this.value = a
        };
        var eb;
        try {
            new Function("(function* (){ yield 1; })"), eb = true
        } catch (R) {
            eb = false
        }
        var fb = "From previous event:";
        k.resolve = k, k.nextTick = W, k.longStackSupport = false, k.defer = l, l.prototype.makeNodeResolver = function () {
            var a = this;
            return function (b, c) {
                b ? a.reject(b) : arguments.length > 2 ? a.resolve(Y(arguments, 1)) : a.resolve(c)
            }
        }, k.promise = m, k.passByCopy = function (a) {
            return a
        }, o.prototype.passByCopy = function () {
            return this
        }, k.join = function (a, b) {
            return k(a).join(b)
        }, o.prototype.join = function (a) {
            return k([this, a]).spread(function (a, b) {
                if (a === b) return a;
                throw new Error("Can't join: not the same: " + a + " " + b)
            })
        }, k.race = n, o.prototype.race = function () {
            return this.then(k.race)
        }, k.makePromise = o, o.prototype.toString = function () {
            return "[object Promise]"
        }, o.prototype.then = function (a, b, c) {
            function e(b) {
                try {
                    return "function" == typeof a ? a(b) : b
                } catch (c) {
                    return B(c)
                }
            }

            function f(a) {
                if ("function" == typeof b) {
                    d(a, h);
                    try {
                        return b(a)
                    } catch (c) {
                        return B(c)
                    }
                }
                return B(a)
            }

            function g(a) {
                return "function" == typeof c ? c(a) : a
            }
            var h = this,
                i = l(),
                j = false;
            return W(function () {
                h.promiseDispatch(function (a) {
                    j || (j = true, i.resolve(e(a)))
                }, "when", [
                    function (a) {
                        j || (j = true, i.resolve(f(a)))
                    }
                ])
            }), h.promiseDispatch(void 0, "when", [void 0,
                function (a) {
                    var b, c = false;
                    try {
                        b = g(a)
                    } catch (d) {
                        if (c = true, !k.onerror) throw d;
                        k.onerror(d)
                    }
                    c || i.notify(b)
                }
            ]), i.promise
        }, k.when = p, o.prototype.thenResolve = function (a) {
            return this.then(function () {
                return a
            })
        }, k.thenResolve = function (a, b) {
            return k(a).thenResolve(b)
        }, o.prototype.thenReject = function (a) {
            return this.then(function () {
                throw a
            })
        }, k.thenReject = function (a, b) {
            return k(a).thenReject(b)
        }, k.nearer = q, k.isPromise = r, k.isPromiseAlike = s, k.isPending = t, o.prototype.isPending = function () {
            return "pending" === this.inspect().state
        }, k.isFulfilled = u, o.prototype.isFulfilled = function () {
            return "fulfilled" === this.inspect().state
        }, k.isRejected = v, o.prototype.isRejected = function () {
            return "rejected" === this.inspect().state
        };
        var gb = [],
            hb = [],
            ib = false,
            jb = true;
        k.resetUnhandledRejections = y, k.getUnhandledReasons = function () {
            return gb.slice()
        }, k.stopUnhandledRejectionTracking = function () {
            y(), "undefined" != typeof process && process.on && process.removeListener("exit", x), jb = false
        }, y(), k.reject = B, k.fulfill = C, k.master = E, k.spread = F, o.prototype.spread = function (a, b) {
            return this.all().then(function (b) {
                return a.apply(void 0, b)
            }, b)
        }, k.async = G, k.spawn = H, k["return"] = I, k.promised = J, k.dispatch = K, o.prototype.dispatch = function (a, b) {
            var c = this,
                d = l();
            return W(function () {
                c.promiseDispatch(d.resolve, a, b)
            }), d.promise
        }, k.get = function (a, b) {
            return k(a).dispatch("get", [b])
        }, o.prototype.get = function (a) {
            return this.dispatch("get", [a])
        }, k.set = function (a, b, c) {
            return k(a).dispatch("set", [b, c])
        }, o.prototype.set = function (a, b) {
            return this.dispatch("set", [a, b])
        }, k.del = k["delete"] = function (a, b) {
            return k(a).dispatch("delete", [b])
        }, o.prototype.del = o.prototype["delete"] = function (a) {
            return this.dispatch("delete", [a])
        }, k.mapply = k.post = function (a, b, c) {
            return k(a).dispatch("post", [b, c])
        }, o.prototype.mapply = o.prototype.post = function (a, b) {
            return this.dispatch("post", [a, b])
        }, k.send = k.mcall = k.invoke = function (a, b) {
            return k(a).dispatch("post", [b, Y(arguments, 2)])
        }, o.prototype.send = o.prototype.mcall = o.prototype.invoke = function (a) {
            return this.dispatch("post", [a, Y(arguments, 1)])
        }, k.fapply = function (a, b) {
            return k(a).dispatch("apply", [void 0, b])
        }, o.prototype.fapply = function (a) {
            return this.dispatch("apply", [void 0, a])
        }, k["try"] = k.fcall = function (a) {
            return k(a).dispatch("apply", [void 0, Y(arguments, 1)])
        }, o.prototype.fcall = function () {
            return this.dispatch("apply", [void 0, Y(arguments)])
        }, k.fbind = function (a) {
            var b = k(a),
                c = Y(arguments, 1);
            return function () {
                return b.dispatch("apply", [this, c.concat(Y(arguments))])
            }
        }, o.prototype.fbind = function () {
            var a = this,
                b = Y(arguments);
            return function () {
                return a.dispatch("apply", [this, b.concat(Y(arguments))])
            }
        }, k.keys = function (a) {
            return k(a).dispatch("keys", [])
        }, o.prototype.keys = function () {
            return this.dispatch("keys", [])
        }, k.all = L, o.prototype.all = function () {
            return L(this)
        }, k.allResolved = j(M, "allResolved", "allSettled"), o.prototype.allResolved = function () {
            return M(this)
        }, k.allSettled = N, o.prototype.allSettled = function () {
            return this.then(function (a) {
                return L(_(a, function (a) {
                    function b() {
                        return a.inspect()
                    }
                    return a = k(a), a.then(b, b)
                }))
            })
        }, k.fail = k["catch"] = function (a, b) {
            return k(a).then(void 0, b)
        }, o.prototype.fail = o.prototype["catch"] = function (a) {
            return this.then(void 0, a)
        }, k.progress = O, o.prototype.progress = function (a) {
            return this.then(void 0, void 0, a)
        }, k.fin = k["finally"] = function (a, b) {
            return k(a)["finally"](b)
        }, o.prototype.fin = o.prototype["finally"] = function (a) {
            return a = k(a), this.then(function (b) {
                return a.fcall().then(function () {
                    return b
                })
            }, function (b) {
                return a.fcall().then(function () {
                    throw b
                })
            })
        }, k.done = function (a, b, c, d) {
            return k(a).done(b, c, d)
        }, o.prototype.done = function (a, b, c) {
            var e = function (a) {
                W(function () {
                    if (d(a, f), !k.onerror) throw a;
                    k.onerror(a)
                })
            }, f = a || b || c ? this.then(a, b, c) : this;
            "object" == typeof process && process && process.domain && (e = process.domain.bind(e)), f.then(void 0, e)
        }, k.timeout = function (a, b, c) {
            return k(a).timeout(b, c)
        }, o.prototype.timeout = function (a, b) {
            var c = l(),
                d = setTimeout(function () {
                    c.reject(new Error(b || "Timed out after " + a + " ms"))
                }, a);
            return this.then(function (a) {
                clearTimeout(d), c.resolve(a)
            }, function (a) {
                clearTimeout(d), c.reject(a)
            }, c.notify), c.promise
        }, k.delay = function (a, b) {
            return void 0 === b && (b = a, a = void 0), k(a).delay(b)
        }, o.prototype.delay = function (a) {
            return this.then(function (b) {
                var c = l();
                return setTimeout(function () {
                    c.resolve(b)
                }, a), c.promise
            })
        }, k.nfapply = function (a, b) {
            return k(a).nfapply(b)
        }, o.prototype.nfapply = function (a) {
            var b = l(),
                c = Y(a);
            return c.push(b.makeNodeResolver()), this.fapply(c).fail(b.reject), b.promise
        }, k.nfcall = function (a) {
            var b = Y(arguments, 1);
            return k(a).nfapply(b)
        }, o.prototype.nfcall = function () {
            var a = Y(arguments),
                b = l();
            return a.push(b.makeNodeResolver()), this.fapply(a).fail(b.reject), b.promise
        }, k.nfbind = k.denodeify = function (a) {
            var b = Y(arguments, 1);
            return function () {
                var c = b.concat(Y(arguments)),
                    d = l();
                return c.push(d.makeNodeResolver()), k(a).fapply(c).fail(d.reject), d.promise
            }
        }, o.prototype.nfbind = o.prototype.denodeify = function () {
            var a = Y(arguments);
            return a.unshift(this), k.denodeify.apply(void 0, a)
        }, k.nbind = function (a, b) {
            var c = Y(arguments, 2);
            return function () {
                function d() {
                    return a.apply(b, arguments)
                }
                var e = c.concat(Y(arguments)),
                    f = l();
                return e.push(f.makeNodeResolver()), k(d).fapply(e).fail(f.reject), f.promise
            }
        }, o.prototype.nbind = function () {
            var a = Y(arguments, 0);
            return a.unshift(this), k.nbind.apply(void 0, a)
        }, k.nmapply = k.npost = function (a, b, c) {
            return k(a).npost(b, c)
        }, o.prototype.nmapply = o.prototype.npost = function (a, b) {
            var c = Y(b || []),
                d = l();
            return c.push(d.makeNodeResolver()), this.dispatch("post", [a, c]).fail(d.reject), d.promise
        }, k.nsend = k.nmcall = k.ninvoke = function (a, b) {
            var c = Y(arguments, 2),
                d = l();
            return c.push(d.makeNodeResolver()), k(a).dispatch("post", [b, c]).fail(d.reject), d.promise
        }, o.prototype.nsend = o.prototype.nmcall = o.prototype.ninvoke = function (a) {
            var b = Y(arguments, 1),
                c = l();
            return b.push(c.makeNodeResolver()), this.dispatch("post", [a, b]).fail(c.reject), c.promise
        }, k.nodeify = P, o.prototype.nodeify = function (a) {
            return a ? (this.then(function (b) {
                W(function () {
                    a(null, b)
                })
            }, function (b) {
                W(function () {
                    a(b)
                })
            }), void 0) : this
        };
        var kb = i();
        return k
    }), define("htmlvn/assets/AssetType", [], function () {
        "use strict";
        return {
            Image: 0,
            Scene: 1,
            Text: 2,
            Audio: 3
        }
    }), define("htmlvn/assets/Asset", ["Q", "jquery", "htmlvn/lib/utils", "htmlvn/lib/Class"], function (a, b, c, d) {
        "use strict";

        function e() {
            return 0
        }
        var f = {}, g = 0,
            h = d.inheritWith(function () {
                return {
                    __sceneLocal: false,
                    __values: {},
                    constructor: function (a, d, e, i) {
                        this._type = a, this.__assetId = d, e && (this.__values = b.extend({}, e)), i && (this.__sceneLocal = !! i), this.__retainCount = 0, h.isAssetLoaded(d) ? console.warn(c.format("WARNING: asset with ID {0} already registered; refusing to re-register!!!", d)) : (f[d] = this, g += 1)
                    },
                    getAssetId: function () {
                        return this.__assetId
                    },
                    hasValue: function (a) {
                        return a in this.__values
                    },
                    getValue: function (a) {
                        return this.hasValue(a) ? this.__values[a] : null
                    },
                    getPath: function () {
                        return null
                    },
                    getLoadedElement: function () {
                        return null
                    },
                    getLoadingKey: function () {
                        return this.__loadingKey
                    },
                    getLoadingPath: function () {
                        return this.getPath(this.__loadingKey)
                    },
                    getRetainCount: function () {
                        return this.__retainCount
                    },
                    retain: function () {
                        this.__retainCount += 1
                    },
                    release: function (a) {
                        this.isLoaded() && (void 0 === a && (a = true), this.__retainCount -= 1, this.__retainCount <= 0 && a && this.unload(this.__sceneLocal))
                    },
                    load: function (b) {
                        var c = this,
                            d = null;
                        return c.isLoaded() ? d = a(c) : c.isLoading() ? d = c.__loadPromise : (c.__loadingKey = b, c.__loadPromise = d = a.fcall(c._promiseLoad.bind(c), b).delay(e()).then(function () {
                            return c.__loaded = true, c
                        }).fin(function () {
                            delete c.__loadPromise, delete c.__loadingKey
                        })), d
                    },
                    unload: function (a) {
                        this.__loaded = false, this.__retainCount = 0, a && this.unmap()
                    },
                    isSceneLocal: function () {
                        return this.__sceneLocal
                    },
                    isLoading: function () {
                        return !!this.__loadPromise
                    },
                    isLoaded: function () {
                        return !!this.__loaded
                    },
                    unmap: function () {
                        delete f[this.__assetId], g -= 1
                    },
                    _promiseLoad: function () {
                        throw new Error("needs subclass implementation!")
                    }
                }
            }).defineStatic({
                getLoadedAssetList: function () {
                    return Object.keys(f)
                },
                getAssetsOfType: function (a) {
                    var b = [];
                    for (var c in f) {
                        var d = f[c];
                        d instanceof a && b.push(d)
                    }
                    return b
                },
                getLoadedAssetCount: function () {
                    return g
                },
                isAssetLoaded: function (a) {
                    return f.hasOwnProperty(a)
                },
                getAsset: function (a) {
                    if ("string" != typeof a) throw new Error("getAsset requires a string parameter!");
                    return h.isAssetLoaded(a) ? f[a] : null
                },
                tryResolve: function (a, b) {
                    if (!a) return null;
                    if (a instanceof h) return a;
                    var d = null;
                    b = c.pick(b, true);
                    var e = null;
                    if ("@" === a.charAt(0)) {
                        var f = a.substring(1, a.length);
                        d = h.getAsset(f), d && (e = d)
                    } else b && (d = h.getAsset(a), d && (e = d));
                    return e
                }
            });
        return h
    }), define("htmlvn/StepMode", [], function () {
        "use strict";
        return {
            Normal: 0,
            Skip: 2,
            Force: 5,
            Nitro: 10,
            Load: 50,
            Max: 100
        }
    }), define("htmlvn/events/Event", ["jquery", "htmlvn/lib/utils", "htmlvn/StepMode", "htmlvn/lib/Class"], function (a, b, c, d) {
        "use strict";
        var e = null,
            f = [],
            g = null,
            h = d.inheritWith(function () {
                return {
                    _eventName: "",
                    __auto: false,
                    __events: [],
                    __scene: null,
                    __destroyed: false,
                    constructor: function (c) {
                        if (a.isPlainObject(c)) {
                            var d = b.pickInAndSet;
                            d(this, "_eventName", c, ["eventName", "name"]), d(this, "__auto", c, ["auto", "autocomplete"]), d(this, "__events", c, ["events", "ev"]), a.isArray(this.__events) || (this.__events = [this.__events])
                        }
                        for (var e = this.__events, f = 0; f < e.length; ++f) this.__inherit(f, e[f])
                    },
                    isDestroyed: function () {
                        return this.__destroyed
                    },
                    destroy: function () {
                        if (!this.__destroyed) {
                            for (var a = this.__events, b = 0; b < a.length; ++b) a[b].destroy();
                            this.__parent = this.__evPath = null, delete this.__events
                        }
                        this.__destroyed = true
                    },
                    overlayAppeared: function (a) {
                        for (var b = this.__events, c = 0; c < b.length; ++c) b[c].overlayAppeared(a)
                    },
                    overlayDismissed: function (a) {
                        for (var b = this.__events, c = 0; c < b.length; ++c) b[c].overlayDismissed(a)
                    },
                    sceneWarm: function () {
                        for (var a = this.__events, b = 0; b < a.length; ++b) a[b].sceneWarm()
                    },
                    eventWarm: function () {
                        for (var a = this.__events, b = 0; b < a.length; ++b) a[b].eventWarm()
                    },
                    finalize: function () {
                        for (var a = this.__events, b = 0; b < a.length; ++b) a[b].finalize()
                    },
                    isComplete: function () {
                        for (var a = true, b = this.__events, c = 0; a && c < b.length; ++c) a = a && b[c].isComplete();
                        return a
                    },
                    update: function (a) {
                        for (var b = this.__events, c = 0; c < b.length; ++c) b[c].update(a)
                    },
                    step: function (a) {
                        for (var b = true, c = this.__events, d = 0; d < c.length; ++d) b = c[d].step(a) && b;
                        return b
                    },
                    shouldSkip: function (a) {
                        for (var b = a > c.Normal, d = this.__events, e = 0; b && e < d.length; ++e) b = b && d[e].shouldSkip(a);
                        return b
                    },
                    collectAssets: function () {
                        var a = [],
                            b = this.__events;
                        if (b)
                            for (var c = 0; c < b.length; ++c) a = a.concat(b[c].collectAssets());
                        return a
                    },
                    getEventPath: function () {
                        if (!this.__evPath) {
                            for (var a = [this.getEventName()], b = this.getParent(); b;) a.unshift(b.getEventName()), b = b.getParent();
                            this.__evPath = a.join("/")
                        }
                        return this.__evPath
                    },
                    getEventName: function () {
                        var a = this._eventName;
                        return a && 0 !== a.length || !this.__parent || (a = this.__parent.getChildIndex(this) + ""), a
                    },
                    getParent: function () {
                        return this.__parent
                    },
                    doesAutocomplete: function () {
                        return this.__auto
                    },
                    eachChild: function (b) {
                        var c = function (a, c) {
                            b(c)
                        };
                        a.each(this.__events, c)
                    },
                    hasChildren: function () {
                        return this.__events.length > 0
                    },
                    getChildAtIndex: function (a) {
                        return this.__events[a]
                    },
                    getChildByName: function (a) {
                        for (var b = this.__events, c = 0; c < b.length; ++c) {
                            var d = b[c];
                            if (d.getEventName() === a) return d
                        }
                        return null
                    },
                    getChildIndex: function (a) {
                        return this.__events.indexOf(a)
                    },
                    getChildCount: function () {
                        return this.__events.length
                    },
                    getChildEvents: function () {
                        return this.__events
                    },
                    addChild: function (a) {
                        var b = this.__events,
                            c = b.length;
                        b.push(a), this.__inherit(c, a)
                    },
                    insertChild: function (a, b) {
                        var c = this.__events;
                        c.splice(a, 0, b), this.__inherit(a, b)
                    },
                    replaceChild: function (a, b) {
                        var c = this.__events,
                            d = c[a];
                        d._setParent(null), c[a] = b, this.__inherit(a, b)
                    },
                    isLeaf: function () {
                        return 0 === this.getChildCount()
                    },
                    hasChild: function (a) {
                        return -1 !== this.getChildIndex(a)
                    },
                    getScene: function () {
                        return this.__scene ? this.__scene : this.__parent ? this.__parent.getScene() : null
                    },
                    isActive: function () {
                        return e === this
                    },
                    makeActive: function () {
                        this.__parent && this.__parent._childWantsActive(this)
                    },
                    ensurePath: function () {
                        for (var a = true, b = this.__events, c = 0; a && c < b.length; ++c) a = a && b[c].ensurePath();
                        return a
                    },
                    _signalComplete: function () {
                        var a = this.__parent;
                        a && a._childIsComplete(this)
                    },
                    _childIsComplete: function () {
                        var a = this.__parent;
                        this.isComplete() && a._childIsComplete(this)
                    },
                    _childWantsActive: function () {
                        this.__parent && this.__parent._childWantsActive(this)
                    },
                    _setEventName: function (a) {
                        this._eventName = a
                    },
                    _setParent: function (a) {
                        this.__evPath = null, this.__parent = a
                    },
                    _setScene: function (a) {
                        this.__scene = a
                    },
                    __inherit: function (a, b) {
                        b || console.error("WOAH NULL EVENT DUDE"), b._setParent(this)
                    }
                }
            }).defineStatic({
                setStepHandler: function (a) {
                    g = a
                },
                requestStep: function (a) {
                    g && g(a)
                },
                setActiveEvent: function (a) {
                    e = a;
                    for (var c = 0; c < f.length; ++c) {
                        var d = f[c];
                        b.runSafe(function () {
                            d(a)
                        })
                    }
                },
                getActiveEvent: function () {
                    return e
                },
                addChangeListener: function (a) {
                    f.push(a)
                },
                removeChangeListener: function (a) {
                    for (var b = f.length - 1; b >= 0; b--) f[b] === a && f.splice(b, 1)
                }
            });
        return h
    }), define("htmlvn/events/DiscreteEvent", ["htmlvn/lib/utils", "htmlvn/StepMode", "htmlvn/events/Event"], function (a, b, c) {
        "use strict";
        var d = c.inheritWith(function (c, d) {
            return {
                __gotStep: false,
                __canInterrupt: true,
                constructor: function e(b) {
                    d.apply(this, arguments), $.isPlainObject(b) && a.pickInAndSet(this, "__canInterrupt", b, ["allowInterrupt", "canInterrupt", "interruptable", "int"]);
                    for (var c = this.getChildEvents(), f = 0; f < c.length; ++f)
                        if (!(c[f] instanceof e)) throw new Error("Cannot contain non-Discrete event within DiscreteEvent!")
                },
                eventWarm: function () {
                    this.__gotStep = false, c.eventWarm.apply(this, arguments)
                },
                pump: function (a) {
                    for (var b = this.getChildEvents(), c = 0; c < b.length; ++c) b[c].pump(a)
                },
                interrupt: function () {
                    for (var a = false, b = this.getChildEvents(), c = 0; c < b.length; ++c) a = b[c].interrupt() || a;
                    return a
                },
                shouldSkip: function (a) {
                    for (var c = a > b.Skip || a === b.Skip && this.__canInterrupt, d = this.getChildEvents(), e = 0; c && e < d.length; ++e) c = c && d[e].shouldSkip(a);
                    return c
                },
                canInterrupt: function () {
                    return this.__canInterrupt
                },
                step: function (a) {
                    if (this.__gotStep) this.isComplete() || !this.canInterrupt() && !this.shouldSkip(a) || this.interrupt(a);
                    else {
                        this.__gotStep = true;
                        var b = !this.shouldSkip(a);
                        this.pump(b, a)
                    }
                    return this.isComplete()
                }
            }
        });
        return d
    }), define("htmlvn/events/Macro", ["jquery", "htmlvn/lib/utils", "htmlvn/events/Event", "htmlvn/events/DiscreteEvent", "htmlvn/StepMode"], function (a, b, c, d, e) {
        "use strict";
        var f = c.inheritWith(function (b, g) {
            return {
                __idxProtect: false,
                __lastStepMode: e.Normal,
                constructor: function (b) {
                    if (a.isArray(b)) {
                        var c = {
                            events: b
                        };
                        b = c
                    }
                    g.apply(this, arguments)
                },
                eventWarm: function () {
                    this.__event = null, this.__alreadyWarmed = false, this.__idxProtect || (this.__evIdx = 0), this.__nextEvent(false)
                },
                step: function (a) {
                    void 0 === a && (a = this.__lastStepMode), this.__lastStepMode = a, this.__event || console.warn("h-how do we have no ev here ...");
                    var b = this.__event;
                    if (b) {
                        var c = b.step(a);
                        this.__steppedOnce = true, c && this.__progress(false)
                    }
                    return this.isComplete()
                },
                update: function (a) {
                    var b = this.__event;
                    b && this.__steppedOnce && b.update(a)
                },
                isComplete: function () {
                    return !this.__event
                },
                makeActive: function () {
                    this.__events.length > 0 ? this.__events[0].makeActive() : b.makeActive.call(this)
                },
                finalize: function () {
                    this.__event && this.__event.finalize()
                },
                shouldSkip: function (a) {
                    return this.__event ? this.__event.shouldSkip(a) : a > e.Normal
                },
                getNextEvPath: function () {
                    var a = null,
                        b = this.__getNextEvent();
                    return b && (a = b instanceof f ? b.getNextEvPath() : b.getEventPath()), a
                },
                _childWantsActive: function (a) {
                    var b = this.getChildIndex(a);
                    if (-1 != b) {
                        this.__idxProtect = true, this.__evIdx = b;
                        var c = this.getParent();
                        c ? c._childWantsActive(this) : (this.finalize(), this.eventWarm()), delete this.__idxProtect
                    }
                },
                _isRootMacro: function () {
                    return !this.getParent()
                },
                _childIsComplete: function (a) {
                    a === this.__event ? this.__progress(true) : console.warn("won't progess for illegimate children!")
                },
                __progress: function (a) {
                    var b = this.__event;
                    this.__nextEvent(true), this.__event ? b && b.doesAutocomplete() && c.requestStep(this) : a && this._signalComplete()
                },
                __nextEvent: function (a) {
                    void 0 === a && (a = true);
                    var b = this.__event;
                    if (b && a && b.finalize(), this.__alreadyWarmed || this.__warmNextEvent(), this.__alreadyWarmed = false, b = this.__event = this.__getNextEvent()) {
                        if (this.__steppedOnce = false, this.__evIdx += 1, b.doesAutocomplete()) {
                            var e = this.__getNextEvent();
                            e && e instanceof d && (this.__alreadyWarmed = true, this.__warmNextEvent())
                        }
                        b instanceof d && c.setActiveEvent(b)
                    }
                },
                __warmNextEvent: function () {
                    var a = this.__getNextEvent();
                    a && a.eventWarm()
                },
                __getNextEvent: function () {
                    var a = null,
                        b = this.getChildEvents();
                    return this.__evIdx < b.length && (a = b[this.__evIdx]), a
                }
            }
        });
        return f
    }), define("htmlvn/events/DelayEvent", ["htmlvn/lib/utils", "htmlvn/StepMode", "htmlvn/events/DiscreteEvent"], function (a, b, c) {
        "use strict";
        var d = c.inheritWith(function (b, c) {
            return {
                __timeout: null,
                __delay: 0,
                constructor: function (b) {
                    if (c.call(this, b), a.pickInAndSet(this, "__delay", b, ["time", "duration", "delay"]), this.__delay < 0) throw new Error("Delay must be >= 0 to DelayEvent!")
                },
                pump: function (a) {
                    return !a || this.__delay <= 0 ? b.pump.call(this, a) : (this.__timeout = setTimeout(this.__readyToPump.bind(this), 1e3 * this.__delay), void 0)
                },
                interrupt: function () {
                    var a = false;
                    return this.__isTimerRunning() ? (clearTimeout(this.__timeout), this.__timeout = null, a = true, b.pump.call(this, false)) : a = b.interrupt.call(this), a
                },
                isComplete: function () {
                    return this.__isTimerDone() && b.isComplete.call(this)
                },
                update: function (a) {
                    this.__isTimerDone() && b.update.call(this, a)
                },
                shouldSkip: function () {
                    return b.shouldSkip.apply(this, arguments)
                },
                __isTimerRunning: function () {
                    return null !== this.__timeout
                },
                __isTimerDone: function () {
                    return !this.__isTimerRunning()
                },
                __readyToPump: function () {
                    delete this.__timeout, b.pump.call(this, true)
                }
            }
        });
        return d
    }),
    function (a) {
        function b() {
            try {
                return h in a && a[h]
            } catch (b) {
                return false
            }
        }

        function c(a) {
            return function () {
                var b = Array.prototype.slice.call(arguments, 0);
                b.unshift(e), i.appendChild(e), e.addBehavior("#default#userData"), e.load(h);
                var c = a.apply(f, b);
                return i.removeChild(e), c
            }
        }

        function d(a) {
            return a.replace(l, "___")
        }
        var e, f = {}, g = a.document,
            h = "localStorage";
        if (f.disabled = false, f.set = function () {}, f.get = function () {}, f.remove = function () {}, f.clear = function () {}, f.transact = function (a, b, c) {
            var d = f.get(a);
            null == c && (c = b, b = null), "undefined" == typeof d && (d = b || {}), c(d), f.set(a, d)
        }, f.getAll = function () {}, f.forEach = function () {}, f.serialize = function (a) {
            return JSON.stringify(a)
        }, f.deserialize = function (a) {
            if ("string" != typeof a) return void 0;
            try {
                return JSON.parse(a)
            } catch (b) {
                return a || void 0
            }
        }, b()) e = a[h], f.set = function (a, b) {
            return void 0 === b ? f.remove(a) : (e.setItem(a, f.serialize(b)), b)
        }, f.get = function (a) {
            return f.deserialize(e.getItem(a))
        }, f.remove = function (a) {
            e.removeItem(a)
        }, f.clear = function () {
            e.clear()
        }, f.getAll = function () {
            var a = {};
            return f.forEach(function (b, c) {
                a[b] = c
            }), a
        }, f.forEach = function (a) {
            for (var b = 0; b < e.length; b++) {
                var c = e.key(b);
                a(c, f.get(c))
            }
        };
        else if (g.documentElement.addBehavior) {
            var i, j;
            try {
                j = new ActiveXObject("htmlfile"), j.open(), j.write('<script>document.w=window</script><iframe src="/favicon.ico"></iframe>'), j.close(), i = j.w.frames[0].document, e = i.createElement("div")
            } catch (k) {
                e = g.createElement("div"), i = g.body
            }
            var l = new RegExp("[!\"#$%&'()*+,/\\\\:;<=>?@[\\]^`{|}~]", "g");
            f.set = c(function (a, b, c) {
                return b = d(b), void 0 === c ? f.remove(b) : (a.setAttribute(b, f.serialize(c)), a.save(h), c)
            }), f.get = c(function (a, b) {
                return b = d(b), f.deserialize(a.getAttribute(b))
            }), f.remove = c(function (a, b) {
                b = d(b), a.removeAttribute(b), a.save(h)
            }), f.clear = c(function (a) {
                var b = a.XMLDocument.documentElement.attributes;
                a.load(h);
                for (var c, d = 0; c = b[d]; d++) a.removeAttribute(c.name);
                a.save(h)
            }), f.getAll = c(function () {
                var a = {};
                return f.forEach(function (b, c) {
                    a[b] = c
                }), a
            }), f.forEach = c(function (a, b) {
                for (var c, e = a.XMLDocument.documentElement.attributes, g = 0; c = e[g]; ++g) {
                    var h = d(c.name);
                    b(ret[c.name], f.deserialize(a.getAttribute(h)))
                }
            })
        }
        try {
            var m = "__storejs__";
            f.set(m, m), f.get(m) != m && (f.disabled = true), f.remove(m)
        } catch (k) {
            f.disabled = true
        }
        f.enabled = !f.disabled, "undefined" != typeof module && module.exports ? module.exports = f : "function" == typeof define && define.amd ? define("store-js", f) : a.store = f
    }(this.window || global), define("htmlvn/DataStore", ["jquery", "htmlvn/lib/utils", "store-js"], function (a, b, c) {
        "use strict";

        function d(a) {
            return a.replace(v, "")
        }

        function e(a) {
            return "vol_" + a
        }

        function f(a) {
            var b = null;
            if (-1 != a.search(t)) {
                var c = a.match(u);
                5 === c.length && (b = {
                    store: c[3],
                    key: c[4]
                })
            }
            return b
        }

        function g(a) {
            return void 0 === a && (a = A), i(a)
        }

        function h() {
            if (!F) throw new Error("DataStore not yet initialized!!!")
        }

        function i(a) {
            var b = j(a);
            if (!b) throw new Error("Could not get store with name " + b);
            return b
        }

        function j(a) {
            var b = null;
            return a in x && (b = x[a]), b
        }

        function k() {
            return "system:" + z
        }

        function l() {
            return 0 === G.length ? "game:" : "game:" + G + ":"
        }

        function m() {
            return l() + D.getIdentifier()
        }

        function n() {
            return m() + ":local"
        }

        function o() {
            return 0 === H.length ? "save:" + D.getIdentifier() + ":" : "save:" + H + ":" + D.getIdentifier() + ":"
        }

        function p(a) {
            return o() + a
        }

        function q(a) {
            return p(a) + ":scene"
        }

        function r(a) {
            return p(a) + ":meta"
        }
        var s = [],
            t = /(\$\{?[0-9a-zA-Z_:]{2,}\}?)/g,
            u = /\$\{?((([0-9a-zA-Z]+):)?([0-9a-zA-Z_]+))\}?/,
            v = /^\@?(t_)/,
            w = {
                Slot: "slot",
                Scene: "scene",
                Game: "game",
                GameLocal: "gameLocal",
                System: "system"
            }, x = {
                slot: {},
                game: {},
                gameLocal: {},
                system: {},
                scene: {}
            }, y = Date.now,
            z = "com.datenighto.htmlvn",
            A = "slot",
            B = "gameLocal",
            C = "gameLocal",
            D = null,
            E = {}, F = false,
            G = "",
            H = "",
            I = null,
            J = {
                Store: w,
                init: function (a, b, d, e) {
                    var f = false;
                    if (D = a || D, 2 === arguments.length ? f = b : 3 === arguments.length ? (f = d, G = b, H = b) : 4 === arguments.length && (f = e, G = b, H = d), F && !f) throw new Error("DataStore already initialized; cowardly refusing to reinit! Use forceReinit = true to avoid this!");
                    var g = m(),
                        h = n(),
                        i = k();
                    x.system = c.get(i) || {}, x.game = c.get(g) || {}, x.gameLocal = c.get(h) || {}, x.slot = {}, x.scene = {};
                    var j = E = c.getAll();
                    delete j[i], delete j[g], delete j[h];
                    for (var l in j) j[l] = true;
                    return F = true
                },
                newGame: function () {
                    h(), I = null, x.slot = {}, x.scene = {}
                },
                isInitialized: function () {
                    return !!F
                },
                hasSave: function (a) {
                    h();
                    var b = p(a);
                    return b in E
                },
                getSaveMeta: function (a) {
                    h();
                    var b = r(a);
                    return b in E ? c.get(b) : null
                },
                load: function (a) {
                    h();
                    var b = p(a);
                    if (!(b in E)) throw new Error("Cannot find saved game with name " + a);
                    I = a, x.slot = c.get(b), b = q(a), x.scene = c.get(b), this.__signalChanged(a)
                },
                save: function (a, b) {
                    h();
                    var d = y();
                    b = b || {};
                    var e = p(a);
                    x.slot.timestamp = d, E[e] = true, c.set(e, x.slot), e = r(a), b.timestamp = d, b.name = a, E[e] = true, c.set(e, b), e = q(a), x.scene.timestamp = d, E[e] = true, c.set(e, x.scene), this.saveGameData(d), this.saveSystemData(d)
                },
                deleteSave: function (a) {
                    h();
                    var b = p(a);
                    if (b in E) {
                        var d = r(a),
                            e = q(a);
                        delete E[b], delete E[d], delete E[e], c.remove(b), c.remove(d), c.remove(e)
                    }
                },
                clearSceneData: function () {
                    h(), x.scene = {}, this.__signalChanged()
                },
                saveSystemData: function (a) {
                    h(), x.system.timestamp = a || y(), c.set(k(), x.system)
                },
                saveGameData: function (a) {
                    h(), x.game.timestamp = a || y(), c.set(m(), x.game), c.set(n(), x.gameLocal)
                },
                markTextRead: function (a) {
                    h(), a = d(a), a.length > 0 && this.set("tr_" + a, true, B)
                },
                wasTextRead: function (a) {
                    return h(), a = d(a), a.length <= 0 || this.hasKey("tr_" + a, B)
                },
                get: function (a, b) {
                    return h(), g(b)[a]
                },
                set: function (a, b, c) {
                    h(), g(c)[a] = b, this.__signalChanged(a, b, c)
                },
                hasKey: function (a, b) {
                    return h(), a in g(b)
                },
                getVolume: function (a) {
                    h();
                    var b = e(a);
                    return this.hasKey(b, C) ? parseFloat(this.get(b, C)) : 1
                },
                setVolume: function (a, b) {
                    return h(), this.set(e(a), b, C)
                },
                remove: function (a, b) {
                    h(), delete g(b)[a], this.__signalChanged(a, b)
                },
                clearAll: function () {
                    h(), console.warn("CLEARING THE ENTIRE DATA STORE OH GOODNESS!!!"), c.clear(), this.init(D, true)
                },
                clearStore: function (a) {
                    h(), console.warn("CLEARING STORE: " + a + "!!!"), a in x && (x[a] = {})
                },
                replaceVariableTokens: function (a) {
                    h();
                    var b = a.match(t);
                    for (var c in b) {
                        var d = b[c];
                        a = a.replace(d, this.resolve(d))
                    }
                    return a
                },
                resolve: function (a) {
                    if (h(), "string" != typeof a) return a;
                    var c = a.trim();
                    if (!c.length) return a;
                    var d = f(a);
                    return d && (c = this.get(d.key, d.store)), c = b.coerceType(c)
                },
                getRemoteObj: function (a) {
                    h(), (0 === arguments.length || a) && (this.saveSystemData(), this.saveGameData());
                    var b = c.getAll(),
                        d = {}, e = k(),
                        f = m();
                    n(), d[e] = b[e], d[f] = b[f];
                    var g = o();
                    for (var i in b) i.startsWith(g) && (d[i] = b[i]);
                    return d.timestamp = y(), d
                },
                getRemoteJSON: function () {
                    return JSON.stringify(this.getRemoteObj.apply(this, arguments))
                },
                replaceWithIfNewer: function (a) {
                    if (h(), !a) return false;
                    var b = a.timestamp;
                    if (b) {
                        var d = null;
                        if (d = this.get("timestamp", "game"), !(d && d >= b)) {
                            console.log("replacing local data with foreign save data, " + d + " < " + b);
                            for (var e in a) c.set(e, a[e]);
                            return this.init(D, true), true
                        }
                        console.warn("local save is newer than or the save age as foreign save, " + d + " > " + b)
                    } else console.error("couldn't get foreign save date; sorry, but we're failing!!!");
                    return false
                },
                addChangeListener: function (a) {
                    s.push(a)
                },
                removeChangeListener: function (a) {
                    for (var b = s.length - 1; b >= 0; b--) s[b] === a && s.splice(b, 1)
                },
                __signalChanged: function () {
                    for (var a = 0; a < s.length; ++a) try {
                        s[a].apply(null, arguments)
                    } catch (b) {
                        console.error(b)
                    }
                },
                _getDebugRawObj: function () {
                    return x
                }
            };
        return J
    }), define("htmlvn/menu/Screen", ["jquery", "Q", "htmlvn/lib/utils", "htmlvn/lib/Class", "htmlvn/assets/Asset", "htmlvn/DataStore"], function (a, b, c, d, e) {
        "use strict";
        var f = c.runSafe,
            g = ["willPresent", "didPresent", "willDismiss", "didDismiss", "losingFocus", "lostFocus", "gainingFocus", "gainedFocus"],
            h = [],
            i = function (a) {
                var b = m();
                b && f(function () {
                    b._losingFocus()
                }), f(function () {
                    a._gainingFocus()
                }), h.push(a), f(function () {
                    a._gainedFocus()
                }), b && f(function () {
                    b._lostFocus()
                })
            }, j = function () {
                if (0 === h.length) return null;
                var a = h.pop();
                f(function () {
                    a._losingFocus()
                });
                var b = m();
                return b && f(function () {
                    b._gainingFocus()
                }), f(function () {
                    a._lostFocus()
                }), b && f(function () {
                    b._gainedFocus()
                }), a
            }, k = function (a) {
                for (var b = 0; b < h.length; ++b) {
                    var c = h[b];
                    f(function () {
                        c.update(a)
                    })
                }
            }, l = function (a) {
                var b = false,
                    c = h.indexOf(a);
                return c > -1 && (c === h.length - 1 ? (j(), b = true) : (h.splice(c, 1), b = true)), b
            }, m = function () {
                var a = h.length;
                return 0 === a ? null : h[a - 1]
            }, n = function () {
                var a = m();
                return a ? a.eligibleForOverlay() : true
            }, o = d.inheritWith(function () {
                return {
                    __isPresenting: false,
                    __isDismisssing: false,
                    constructor: function (b, d, e) {
                        e = c.pick(e, []);
                        var f = this.__root = a(d);
                        f.find("[data-action]").each(function (b, c) {
                            var d = a(c).attr("data-action"); - 1 === e.indexOf(d) && e.push(d)
                        }), this.__player = b, this.__custom = e, this.__isModal = f.hasClass("modal"), this.__isOverlay = f.hasClass("overlay"), this.__initEvents(g, e), this.__isPresented = false, this.__actionHandler = this.__actionHandler.bind(this)
                    },
                    on: function () {
                        return this.addEventListener.apply(this, arguments)
                    },
                    addEventListener: function (a, b) {
                        a in this.__callbacks && this.__callbacks[a].add(b)
                    },
                    off: function () {
                        return this.removeEventListener.apply(this, arguments)
                    },
                    removeEventListener: function (b, c) {
                        b ? b in this.__callbacks && (c ? this.__callbacks[b].remove(c) : this.__callbacks[b] = a.Callbacks()) : this.__initEvents(g, this.__custom)
                    },
                    show: function () {
                        console.warn("old Screen#show invocation!"), this.present.apply(this, arguments)
                    },
                    update: function () {},
                    present: function (a, c, d) {
                        a = a || {}, c = c || 0, d = d || {};
                        var e = this,
                            f = e.getRoot(),
                            g = null;
                        return e.__isPresented || (e.__isDismisssing && f.stop(), e.__isPresented = true, e._willPresent(a, c), f.css(d).addClass("shown"), e.__isPresenting = true, g = e.__performAnimationAndSignal("willPresent", "didPresent", e._didPresent, a, c, function () {
                            e.__isPresenting = false
                        })), g || b(e)
                    },
                    dismiss: function (a, c) {
                        a = a || {}, c = c || 0;
                        var d = this,
                            e = d.getRoot(),
                            f = null;
                        return this.__isPresented && (this.__isPresenting && e.stop(), this._willDismiss(a, c), this.__isDismisssing = true, f = this.__performAnimationAndSignal("willDismiss", "didDismiss", this._didDismiss, a, c, function () {
                            d.__isDismisssing = false, e.removeClass("shown")
                        }), this.__isPresented = false), f || b(this)
                    },
                    eligibleForOverlay: function () {
                        return !this.isOverlay()
                    },
                    isOverlay: function () {
                        return this.__isOverlay
                    },
                    isModal: function () {
                        return this.__isModal
                    },
                    isPresented: function () {
                        return this.__isPresented
                    },
                    isPresenting: function () {
                        return this.__isPresenting
                    },
                    isDismissing: function () {
                        return this.__isDismisssing
                    },
                    hasFocus: function () {
                        return this.isPresented() && m() === this
                    },
                    getPlayer: function () {
                        return this.__player
                    },
                    getRoot: function () {
                        return this.__root
                    },
                    _willPresent: function () {
                        i(this)
                    },
                    _didPresent: function () {
                        this.__root.find("[data-action]").on("click", this.__actionHandler)
                    },
                    _willDismiss: function () {
                        this.__root.find("[data-action]").off("click", this.__actionHandler)
                    },
                    _didDismiss: function () {
                        l(this)
                    },
                    _losingFocus: function () {
                        this._fireEvent("losingFocus")
                    },
                    _lostFocus: function () {
                        this._fireEvent("lostFocus")
                    },
                    _gainingFocus: function () {
                        this._fireEvent("gainingFocus")
                    },
                    _gainedFocus: function () {
                        this._fireEvent("gainedFocus")
                    },
                    _fireEvent: function (b, d) {
                        if (!(b in this.__callbacks)) throw new Error("Attempted to raise unknown event: " + b);
                        d = c.pick(d, {});
                        var e = a.Event(b);
                        e.menu = this, e = a.extend(e, d), this.__callbacks[b].fire(e)
                    },
                    _setElText: function (a, b) {
                        var c = e.tryResolve(b);
                        "string" == typeof c ? a.attr("data-i18nKey", "").text(c) : a.attr("data-i18nKey", "@" + c.getAssetId()).text(c.getValue())
                    },
                    __actionHandler: function (b) {
                        b.preventDefault();
                        var c = a(b.currentTarget),
                            d = c.attr("data-action");
                        this._fireEvent(d, {
                            target: b.target
                        }), c = null
                    },
                    __initEvents: function (b, c) {
                        this.__callbacks = {};
                        for (var d, e = 0; e < b.length; ++e) d = b[e], this.__callbacks[d] = a.Callbacks();
                        for (var e = 0; e < c.length; ++e) d = c[e], this.__callbacks[d] = a.Callbacks()
                    },
                    __performAnimationAndSignal: function (a, d, e, f, g, h) {
                        var i = null,
                            j = this,
                            k = j.getRoot();
                        e = e.bind(j), f = c.pick(f, {}), j._fireEvent(a, {
                            style: f,
                            duration: g
                        });
                        var l = function () {
                            h && h(), e(), j._fireEvent(d), i && i.resolve(j)
                        }, m = null;
                        return g > 0 && Object.keys(f).length > 0 ? (i = b.defer(), k.animate(f, {
                            duration: 1e3 * g,
                            complete: l
                        }), m = i.promise) : (k.css(f), l(), m = b(j)), m
                    }
                }
            }).defineStatic({
                update: k,
                topCanHaveOverlay: n
            });
        return o
    }), define("htmlvn/assets/TextAsset", ["htmlvn/lib/utils", "htmlvn/assets/AssetType", "htmlvn/assets/Asset", "htmlvn/DataStore"], function (a, b, c, d) {
        "use strict";
        var e = c.inheritWith(function (c, e) {
            return {
                constructor: function (a, c, d) {
                    "string" == typeof c && (c = {
                        en: arguments[1]
                    }), e.call(this, b.Text, a, c, d), this.__loaded = true
                },
                getValue: function (b) {
                    b = a.pick(b, "en"), this.hasValue(b) || (b = "en");
                    var e = c.getValue.call(this, b);
                    return e && (e = d.replaceVariableTokens(e)), e
                },
                isLoading: function () {
                    return false
                },
                isLoaded: function () {
                    return true
                }
            }
        });
        return e
    }), define("htmlvn/assets/ImageAsset", ["Q", "jquery", "htmlvn/lib/utils", "htmlvn/assets/AssetType", "htmlvn/assets/Asset", "FastClass"], function (a, b, c, d, e) {
        "use strict";
        var f = false,
            g = e.inheritWith(function (c, e) {
                return {
                    constructor: function (a, b, c) {
                        "string" == typeof b && (b = {
                            mdpi: arguments[1]
                        }), e.call(this, d.Image, a, b, c)
                    },
                    getValue: function (a) {
                        return a || (a = f && this.hasValue("hdpi") ? "hdpi" : "mdpi"), c.getValue.call(this, a)
                    },
                    getPath: function (a) {
                        return this.getValue(a)
                    },
                    getLoadedElement: function () {
                        return this.__el
                    },
                    unload: function () {
                        b(this.__el).remove(), this.__el = null, delete this.__el, c.unload.call(this)
                    },
                    _promiseLoad: function (c) {
                        var d = a.defer(),
                            e = this,
                            f = this.getPath(c),
                            g = this.__el = new Image;
                        return b(g).attr("draggable", false).on({
                            load: function () {
                                b(g).off(), g = null, d.resolve(e)
                            },
                            error: function () {
                                b(g).off().remove(), e.__el = g = null, d.reject(new Error("Could not load asset of type Image at URL: " + f))
                            },
                            abort: function () {
                                b(g).off().remove(), e.__el = g = null, d.reject(new Error("Could not load asset of type Image at URL: " + f))
                            }
                        }), g.src = f, d.promise
                    }
                }
            });
        return g
    }), define("htmlvn/assets/AudioCodec", [], function () {
        "use strict";
        return {
            m4a: 'audio/mp4; codecs="mp4a.40.2"',
            mp3: "audio/mpeg;",
            ogg: 'audio/ogg; codecs="vorbis"',
            wav: 'audio/wav; codecs="1"'
        }
    }), define("htmlvn/assets/AudioAsset", ["Q", "jquery", "htmlvn/lib/utils", "htmlvn/assets/AssetType", "htmlvn/assets/Asset", "htmlvn/assets/AudioCodec"], function (a, b, c, d, e, f) {
        "use strict";
        var g = {}, h = ["m4a", "ogg", "mp3", "wav"],
            i = e.inheritWith(function (c, e) {
                return {
                    constructor: function (a, b, c, f) {
                        c || (c = ["mp3"]);
                        for (var g = {}, h = 0; h < c.length; ++h) {
                            var i = c[h];
                            g[i] = b + "." + i
                        }
                        e.call(this, d.Audio, a, g, f)
                    },
                    getValue: function (a) {
                        if (!a)
                            for (var b = 0; b < h.length; ++b) {
                                var d = h[b];
                                if (this.hasValue(d) && i.supportsCodec(d)) {
                                    a = d;
                                    break
                                }
                            }
                        return c.getValue.call(this, a)
                    },
                    getLoadedElement: function () {
                        return this.__el
                    },
                    getPath: function (a) {
                        return this.getValue(a)
                    },
                    unload: function () {
                        b(this.__el).remove(), delete this.__el, c.unload.apply(this, arguments)
                    },
                    _promiseLoad: function () {
                        var c = this,
                            d = null,
                            e = a.defer(),
                            f = c.__el = document.createElement("audio");
                        f.autoplay = false;
                        var g = function (a) {
                            b(f).find("source").off().remove(), b(f).off().remove(), f = c.__el = null, e.reject(new Error("el warmup failed for " + c.getAssetId()))
                        }, i = function (a) {
                                f.networkState === HTMLMediaElement.NETWORK_NO_SOURCE && g(a)
                            }, j = function () {
                                b(f).on("error", g)
                            };
                        if (this.__useSrc) b(f).one("canplaythrough", function () {
                            b(f).off(), e.resolve(c)
                        }), j(), b(f).attr("src", this.__useSrc), d = a(this).thenReject(new Error("Could not resolve path for asset " + c.getAssetId()));
                        else {
                            b(f).on("canplaythrough", function () {
                                c.__useSrc = this.currentSrc, b(f).off(), b(f).find("source").off().remove(), b(f).one("canplaythrough", function () {
                                    b(f).off(), e.resolve(c)
                                }), j(), b(f).attr("src", c.__useSrc)
                            }), j(), f.preload = "auto";
                            for (var k = 0; k < h.length; ++k) {
                                var l = this.getPath(h[k]);
                                if (l) {
                                    var m = document.createElement("source");
                                    m.setAttribute("src", l), b(m).on("error", i), f.appendChild(m)
                                }
                            }
                        }
                        return e.promise
                    }
                }
            }).defineStatic({
                supportsCodec: function (a) {
                    if (a in g) return g[a];
                    var b = document.createElement("audio"),
                        c = f[a],
                        d = (b.canPlayType(c), !(!b.canPlayType || !b.canPlayType(c).replace(/no/, "")));
                    return g[a] = d, b = null, d
                }
            });
        return i
    }), define("htmlvn/BasePlayer", ["Q", "jquery", "htmlvn/lib/utils", "htmlvn/lib/Class", "htmlvn/StepMode", "htmlvn/assets/Asset", "htmlvn/events/Event", "htmlvn/events/Macro", "htmlvn/events/DelayEvent", "htmlvn/DataStore", "htmlvn/menu/Screen", "htmlvn/assets/TextAsset", "htmlvn/assets/ImageAsset", "htmlvn/assets/AudioAsset"], function (a, b, c, d, e, f, g, h, i, j, k, l, m, n) {
        var o = null,
            p = {
                TextAsset: l,
                ImageAsset: m,
                AudioAsset: n
            }, q = d.inheritWith(function (a, d) {
                return {
                    __fastforwarding: false,
                    __jumpPath: null,
                    __lastTime: void 0,
                    constructor: function (a, c, e, f, h) {
                        void 0 === h && (h = true), this.__update = this.__update.bind(this), d.call(this), this.__game = a, h && !j.isInitialized() && j.init(a), this.__menuMappings = c, this.__eventMappings = e, this.__assetMappings = b.extend({}, p, f), this.__cachedMenus = {}, o = this, g.setStepHandler(this.requestStep.bind(this)), b(window).ready(this._ready.bind(this))
                    },
                    requestStep: function (a) {
                        this._isFastforwarding() || a.getScene() !== this.__currentScene || this.stepScene(e.Normal)
                    },
                    _ready: function () {
                        this.__update()
                    },
                    play: function () {
                        b(window).ready(this._play.bind(this))
                    },
                    _play: function (a) {
                        this.changeScene(a || this.__currentScene)
                    },
                    showMenu: function () {
                        console.warn("BasePlayer#showMenu!"), this.presentMenu.apply(this, arguments)
                    },
                    presentMenu: function (a, b, c, d) {
                        this._getMenu(a).present(b, c, d)
                    },
                    dismissMenu: function (a, b, c) {
                        this._getMenu(a).dismiss(b, c)
                    },
                    pause: function () {},
                    resume: function () {},
                    getScene: function () {
                        return this.__currentScene
                    },
                    getAsset: function (a, b, c, d) {
                        var e = null,
                            f = this.__assetMappings[a];
                        return f ? e = new f(b, c, d) : console.warn("No asset mapping for event with name " + a), e
                    },
                    saveGame: function (a, c) {
                        c = c || {};
                        var d = g.getActiveEvent(),
                            e = null;
                        d && (e = d.getEventPath()), b.extend(c, {
                            scene: this.getScene().getAssetId(),
                            evPath: e
                        }), j.save(a, c)
                    },
                    getEvent: function (a, b) {
                        var c = null,
                            d = this.__eventMappings[a],
                            e = "delay" in b && b.delay > 0,
                            f = b.name,
                            g = b.auto || false;
                        if (e) {
                            var h = b.delay;
                            delete b.delay, delete b.name, delete b.auto
                        }
                        if (d ? c = new d(b) : console.warn("No event mapping for event with name " + a), e) {
                            var j = {
                                duration: h,
                                auto: g,
                                events: [c]
                            };
                            f && (j.name = f), c = new i(j)
                        }
                        return c
                    },
                    resetStage: function () {},
                    getGame: function () {
                        return this.__game
                    },
                    changeScene: function (a, b, c) {
                        return void 0 === b && (b = true), void 0 === c && (c = true), "string" == typeof a && (a = f.tryResolve(a)), a == this.__currentScene ? false : (c && this.__currentScene && this.__currentScene.isLoaded() && this._unloadScene(), this.__currentScene = a, a && (console.log("Changing to scene with ID: " + a.getAssetId()), a.reset()), b && j.clearSceneData(), true)
                    },
                    updateScene: function (a) {
                        this.__currentScene && this.__currentScene.isLoaded() && (this.__jumpIfNeeded(), this.__currentScene.update(a))
                    },
                    stepScene: function (a) {
                        var b = true;
                        if (this.__currentScene.isLoaded()) {
                            this.__lastStepMode = a, b = this.__currentScene.step(a);
                            var c = this.__jumpIfNeeded();
                            null !== c && (b = c)
                        }
                        return b
                    },
                    jumpToEvent: function (a) {
                        this.__jumpPath = a
                    },
                    debugJump: function (a) {},
                    __restoreSceneFromState: function (a, b, c) {},
                    _isFastforwarding: function () {
                        return this.__fastforwarding
                    },
                    __fastForwardToEvent: function (a) {
                        if (!this.__currentScene.findEvent(a)) return true;
                        this.__fastforwarding = true, c.blockHashUpdate(), this.__currentScene.reset();
                        for (var b = false, d = false, f = null, h = g.getActiveEvent(); !d && h && h.getEventPath() != a;) f = h, d = this.stepScene(e.Load), b = true, h = g.getActiveEvent();
                        c.resumeHashUpdate(), this.__fastforwarding = false, g.setActiveEvent(h);
                        var i = !d && !b || f && f.doesAutocomplete();
                        return i
                    },
                    _getMenu: function (a) {
                        var b = null;
                        if (a in this.__cachedMenus) b = this.__cachedMenus[a];
                        else if (a in this.__menuMappings) {
                            var c = this.__menuMappings[a];
                            c && (b = new c(this), this.__cachedMenus[a] = b)
                        }
                        if (!b) throw new Error("Could not resolve menu with name " + a);
                        return b
                    },
                    _unloadScene: function (a) {
                        var b = this.__currentScene;
                        b && (b.unload(a || false), console.warn("BasePlayer is unloading the current scene!"))
                    },
                    _update: function (a) {
                        try {
                            this.updateScene(a)
                        } catch (b) {
                            console.error(b.stack)
                        }
                        try {
                            k.update(a)
                        } catch (b) {
                            console.error(b.stack)
                        }
                    },
                    __update: function (a) {
                        var b = 0;
                        a && (this.__lastTime && (b = a - this.__lastTime), this.__lastTime = a), b = parseFloat(b) / 1e3, this._update(b), window.requestAnimationFrame(this.__update)
                    },
                    __jumpIfNeeded: function () {
                        return this.__jumpPath && (this.__jumpToEvent(this.__jumpPath), this.__jumpPath = null, !this._isFastforwarding()) ? this.stepScene() : null
                    },
                    __jumpToEvent: function (a) {
                        var b = this.__currentScene,
                            c = b.findEvent(a);
                        c ? c.makeActive() : console.warn("Can't resolve event: " + a + " (current scene: " + b.getAssetId() + ")")
                    }
                }
            }).defineStatic({
                getInstance: function () {
                    return o
                },
                jumpToEvent: function () {
                    return o.jumpToEvent.apply(o, arguments)
                }
            });
        return q
    }), define("htmlvn/assets/parser/Xml", ["jquery", "Q", "htmlvn/lib/utils", "htmlvn/lib/Class", "htmlvn/BasePlayer", "htmlvn/assets/Asset", "htmlvn/assets/TextAsset"], function (a, b, c, d, e) {
        "use strict";

        function f(b, c, d) {
            b.children().each(function (b, e) {
                var f = e.nodeName,
                    g = {}, h = a(e).attr("key");
                a(e).find("value").each(function (b, c) {
                    g[a(c).attr("key")] = a(c).text()
                });
                var i = d.getAsset(f, h, g, true);
                i && c.push(i)
            })
        }

        function g(b, d, e) {
            b.children().each(function (b, f) {
                var h = c.coerceType,
                    i = f.nodeName,
                    j = a(f).attrs();
                for (var k in j) j[k] = h(j[k]);
                a(f).children().each(function (b, c) {
                    var d = a(c),
                        f = c.nodeName;
                    "events" === f ? (j.events = [], g(d, j.events, e)) : "choices" === f ? (j.choices = [], d.children().each(function (b, c) {
                        j.choices.push({
                            text: a(c).text(),
                            value: a(c).attr("value") || b
                        })
                    })) : (j[f] = {}, d.children().each(function (b, c) {
                        j[f][c.nodeName] = h(a(c).text())
                    })), d = null
                });
                var l = e.getEvent(i, j);
                l && d.push(l)
            })
        }
        a.fn.attrs = function (b) {
            var c = a(this);
            if (b) return c.each(function (c, d) {
                var e = a(d);
                for (var f in b) e.attr(f, b[f])
            }), c;
            var d = {}, e = c.get(0);
            if (e) {
                e = e.attributes;
                for (var f in e) {
                    var g = e[f];
                    "undefined" != typeof g.nodeValue && (d[g.nodeName] = g.nodeValue)
                }
            }
            return d
        };
        var h = {
            parse: function (b, c) {
                c || (c = e.getInstance());
                var d = {
                    assets: [],
                    events: []
                }, h = a(b);
                return f(h.find("scene>assets"), d.assets, c), g(h.find("scene>events"), d.events, c), h = null, d
            }
        };
        return h
    }), define("htmlvn/assets/Scene", ["jquery", "Q", "htmlvn/lib/utils", "htmlvn/assets/AssetType", "htmlvn/assets/Asset", "htmlvn/events/Macro", "htmlvn/assets/parser/Xml"], function (a, b, c, d, e, f, g) {
        "use strict";
        var h = e.inheritWith(function (c, i) {
            return {
                __preloaded: false,
                __preloading: false,
                __numLoaded: 0,
                __numToLoad: 1,
                constructor: function (a, b) {
                    i.call(this, d.Scene, a), b instanceof Array && (b = {
                        events: b
                    }), void 0 !== b.events && (this._events = b.events), void 0 !== b.json && (this.__rawJson = b.json), void 0 !== b.xml && (this.__rawXml = b.xml), void 0 !== b.jsonUrl && (this.__jsonUrl = b.jsonUrl), void 0 !== b.xmlUrl && (this.__xmlUrl = b.xmlUrl), this.__sceneWarmed = false, this.__firstStep = true, this.__loadThreads = 0
                },
                update: function (a) {
                    this.__readyToGo() && this.__rootMacro.update(a)
                },
                reset: function () {
                    this.__hasRootMacro() && (this.__sceneWarmed || (this.__sceneWarmed = true, this.__rootMacro.sceneWarm()), this.__firstStep = false, this.__rootMacro.eventWarm())
                },
                step: function (a) {
                    return this.__readyToGo() ? (this.__firstStep && this.reset(), this.__rootMacro.step(a)) : true
                },
                shouldSkip: function (a) {
                    return this.__rootMacro.shouldSkip(a)
                },
                isComplete: function () {
                    return this.__rootMacro.isComplete()
                },
                getPath: function () {
                    return this.__xmlUrl || this.__jsonUrl || null
                },
                getPreloadProgress: function () {
                    return this.isPreloaded() ? 1 : this.isPreloading() ? this.__numLoaded / this.__numToLoad || 0 : 0
                },
                preload: function (a) {
                    void 0 === a && (a = true);
                    var c = this;
                    if (c.isLoaded() && c.__preloaded) return b(c);
                    var d = b();
                    if (c.isLoaded() || (d = d.then(c.load.bind(c))), !c.isPreloaded())
                        if (c.isPreloading()) d = c.__preloadPromise;
                        else {
                            this.__numLoaded = 0, this.__numToLoad = 1, c.__preloading = true;
                            var e = function (a) {
                                return function () {
                                    return c.__assetPreload(a)
                                }
                            };
                            d = d.then(e(a)), c.__preloadPromise = d
                        }
                    return d
                },
                cancelPreload: function () {
                    this.isPreloading()
                },
                isPreloading: function () {
                    return this.__preloading
                },
                isPreloaded: function () {
                    return this.__preloaded
                },
                collectAssets: function () {
                    if (!this.__readyToGo()) return [];
                    var a, b, c = this.__rootMacro.collectAssets(),
                        d = {};
                    for (b = 0; b < c.length; ++b) a = e.tryResolve(c[b]), a && (d[a.getAssetId()] = true);
                    return Object.keys(d)
                },
                unload: function () {
                    return this.__readyToGo() ? (this.releaseAssets(), (this.__xmlUrl || this.__jsonUrl || this.__rawXml || this.__rawJson || this.__rawObjs) && (this.__rootMacro.destroy(), this.__sceneWarmed = false, this.__rootMacro = null, this._events = null, (this.__xmlUrl || this.__jsonUrl) && (this.__rawXml = null, this.__rawJson = null)), this.__firstStep = true, c.unload.call(this, false)) : void 0
                },
                retainAssets: function () {
                    if (this.__readyToGo())
                        for (var a, b = this.collectAssets(), c = 0; c < b.length; ++c) a = e.tryResolve(b[c]), !a || a instanceof h || a.retain()
                },
                releaseAssets: function () {
                    if (this.__readyToGo() && this.isPreloaded()) {
                        console.log("Releasing assets from scene " + this.getAssetId());
                        for (var a, b = this.collectAssets(), c = 0; c < b.length; ++c) a = e.tryResolve(b[c]), !a || a instanceof h || a.release();
                        this.__preloaded = false
                    }
                },
                getRootMacro: function () {
                    return this.__rootMacro
                },
                ensurePaths: function () {
                    return this.__readyToGo() ? this.__rootMacro.ensurePath() : true
                },
                findEvent: function (a) {
                    var b = this.__findEvent(a);
                    if (!b) {
                        var c = this.getAssetId() + "/" + a;
                        b = this.__findEvent(c)
                    }
                    return b
                },
                __findEvent: function (a) {
                    var b = null,
                        c = a.split("/");
                    if (c.length > 0) {
                        var d = c.shift();
                        if (d === this.getAssetId())
                            for (var e = this.__rootMacro; c.length > 0;) {
                                var f = c.shift(),
                                    g = e.getChildByName(f);
                                if (!g) break;
                                0 === c.length ? b = g : e = g
                            }
                    }
                    return b
                },
                _promiseLoad: function () {
                    var c = this,
                        d = null;
                    return c._events ? (c.__createRootMacro(c._events), d = b(c)) : c.__rawObjs ? d = b.reject("Raw obj parse not yet implemented!") : c.__rawXml ? d = b.fcall(c.__parseFromXML.bind(c), c.__rawXml) : c.__rawJson ? d = b.reject("JSON parse not yet implemented!") : c.__xmlUrl ? d = b(a.ajax({
                        url: c.__xmlUrl,
                        dataType: "xml",
                        context: c
                    })).then(function (a) {
                        return c.__parseFromXML(a)
                    }) : c.__jsonUrl && (d = b.reject("JSON fetch+parse not yet implemented!")), d || b.reject("Couldn't start promise load??")
                },
                __createRootMacro: function (a) {
                    return this._events = a, this.__rootMacro = new f({
                        name: this.getAssetId(),
                        ev: this._events
                    }), this.__rootMacro._setScene(this), this
                },
                __parseFromXML: function (a) {
                    var c = this;
                    return b.fcall(function (a) {
                        c.__createRootMacro(a.events)
                    }, g.parse(a))
                },
                __hasEvents: function () {
                    return !!this._events
                },
                __hasRootMacro: function () {
                    return !!this.__rootMacro
                },
                __readyToGo: function () {
                    return this.__hasEvents() && this.__hasRootMacro()
                },
                __assetPreload: function (a) {
                    var c = this;
                    if (c.__preloaded) return b(c);
                    var d, f, g, i = 10,
                        j = c.collectAssets(),
                        k = [],
                        l = [],
                        m = [],
                        n = b(c);
                    for (f = 0; f < j.length; ++f) g = j[f], d = e.tryResolve(g), d && (d instanceof h ? m.push(d) : (a && d.retain(), d.isLoaded() ? k.push(d) : l.push(d)));
                    if (c.__numToLoad = l.length, c.__numLoaded = 0, c.__loadThreads = 0, f = 0, c.__preloading = l.length > 0, c.__preloading) {
                        for (var o = b.defer(), p = function (a, b, d) {
                                console.warn("Failed to load asset path: " + d.getLoadingPath()), o.notify(c), q(a, d)
                            }, q = function (a, b) {
                                if (b && (c.__numLoaded += 1, o.notify(c)), l.length > 0) {
                                    var d = l.shift();
                                    d.load().then(function (b) {
                                        q(a, b)
                                    }, function (b) {
                                        p(a, b, d)
                                    })
                                } else c.__loadThreads -= 1, 0 === c.__loadThreads && (c.__preloaded = true, c.__preloading = false, o.resolve(c))
                            }; i > f && l.length;) c.__loadThreads += 1, q(f), f += 1;
                        n = o.promise
                    } else c.__preloaded = true;
                    return n
                }
            }
        });
        return h
    }), define("htmlvn/menu/MainMenu", ["jquery", "htmlvn/menu/Screen"], function (a, b) {
        "use strict";
        var c = b.inheritWith(function (a, b) {
            return {
                constructor: function (a) {
                    b.call(this, a, "#mainMenu")
                }
            }
        });
        return c
    }), define("htmlvn/menu/LoadingScreen", ["jquery", "htmlvn/menu/Screen"], function (a, b) {
        "use strict";
        var c = b.inheritWith(function (a, b) {
            return {
                constructor: function (a) {
                    b.call(this, a, "#loadingMenu")
                },
                setScene: function (a) {
                    this.__scene = a
                },
                clearScene: function () {
                    this.__scene = null
                },
                _willPresent: function () {
                    a._willPresent.apply(this, arguments), this._setProgressValue(0)
                },
                _didDismiss: function () {
                    this.clearScene(), a._didDismiss.apply(this, arguments)
                },
                startBlockingPreload: function (a) {
                    this.setScene(a);
                    var b = a.preload().then(this._sceneLoadDone.bind(this), this._sceneLoadError.bind(this), this._sceneLoadProgress.bind(this));
                    return this._setProgressValue(Math.round(100 * a.getPreloadProgress())), b
                },
                _setProgressValue: function (a) {
                    this.getRoot().find(".bulb").css("width", a + "%").end().find(".progressText").text(a).end()
                },
                _clearProgressValue: function () {
                    this.getRoot().find("progress").removeAttr("value").end()
                },
                _sceneLoadDone: function () {
                    console.log("Scene preloading complete!")
                },
                _sceneLoadError: function (a) {
                    console.error(a)
                },
                _sceneLoadProgress: function (a) {
                    var b = Math.round(100 * a.getPreloadProgress());
                    this._setProgressValue(b)
                }
            }
        });
        return c
    }), define("htmlvn/menu/GameScreen", ["jquery", "htmlvn/menu/Screen", "htmlvn/StepMode", "htmlvn/events/Event"], function (a, b, c, d) {
        "use strict";
        var e = "#gameButtons .button[data-action=options]",
            f = "#gameButtons .button[data-action=fastForward]",
            g = c.Skip,
            h = b.inheritWith(function (h, i) {
                return {
                    constructor: function (a) {
                        this.__handleKeyDown = this.__handleKeyDown.bind(this), this.__handleKeyUp = this.__handleKeyUp.bind(this), this.__handleTap = this.__handleTap.bind(this), this.__showOptions = this.__showOptions.bind(this), this.__dismissOptions = this.__dismissOptions.bind(this), this.__mainMenuPressed = this.__mainMenuPressed.bind(this), this.__noMainMenu = this.__noMainMenu.bind(this), this.__yesMainMenu = this.__yesMainMenu.bind(this), this.__windowBlurred = this.__windowBlurred.bind(this), this.__tryShowOptions = this.__tryShowOptions.bind(this), this.__toggleSkip = this.__toggleSkip.bind(this), this.__eventChanged = this.__eventChanged.bind(this), i.call(this, a, "#gameScreen", ["step", "update"])
                    },
                    update: function (a) {
                        this.hasFocus() || this.__endSkip();
                        var b = this.getPlayer(),
                            c = b.getScene();
                        if (this.__doUpdate(a), c && c.isLoaded() && this.__skipping)
                            if (c.shouldSkip(g)) try {
                                this.__doStep(g)
                            } catch (d) {
                                console.error(d.stack)
                            } else this.__endSkip()
                    },
                    _didPresent: function () {
                        h._didPresent.apply(this, arguments), a(window).on("keydown", this.__handleKeyDown), a(window).on("keyup", this.__handleKeyUp), a(window).on("blur", this.__windowBlurred), a("#game").on("touchend", this.__handleTap), a("#game").on("click", this.__handleTap), a("#gameButtons").css("display", "block"), a(e).on("click", this.__tryShowOptions), a(f).on("click", this.__toggleSkip), d.addChangeListener(this.__eventChanged)
                    },
                    _losingFocus: function () {
                        h._losingFocus.apply(this, arguments), this.__endSkip(), this.__hideSkipButton()
                    },
                    _gainingFocus: function () {
                        h._gainingFocus.apply(this, arguments), this.__showSkipButton()
                    },
                    _willDismiss: function () {
                        h._willDismiss.apply(this, arguments), this.__endSkip(), a(window).off("keydown", this.__handleKeyDown), a(window).off("keyup", this.__handleKeyUp), a(window).off("blur", this.__windowBlurred), a("#game").off("touchend", this.__handleTap), a("#game").off("click", this.__handleTap), a("#gameButtons").css("display", ""), a(e).off("click", this.__tryShowOptions), a(f).off("click", this.__toggleSkip), d.removeChangeListener(this.__eventChanged)
                    },
                    __handleKeyDown: function (a) {
                        this.__isProcessingInput() && (this.__skipping || (13 === a.which ? this.__doStep(c.Normal) : 83 === a.which && (a.metaKey || a.ctrlKey || a.altKey || this.__startSkip())))
                    },
                    __tryShowOptions: function () {
                        b.topCanHaveOverlay() && this.__showOptions()
                    },
                    __handleKeyUp: function (a) {
                        this.__isProcessingInput() && 83 === a.which && this.__endSkip()
                    },
                    __handleTap: function () {
                        this.__isProcessingInput() && this.__doStep(c.Normal)
                    },
                    __doUpdate: function (a) {
                        this._fireEvent("update", {
                            dt: a
                        })
                    },
                    __doStep: function (a) {
                        return this._fireEvent("step", {
                            mode: a
                        }), this.getPlayer().stepScene(a)
                    },
                    __isProcessingInput: function () {
                        return this.isPresented() && this.hasFocus() && this.getPlayer().getScene().isLoaded()
                    },
                    __showOptions: function () {
                        var a = this.getPlayer(),
                            b = a._getMenu("options");
                        b.isPresented() || (this.__endSkip(), b.on("escape", this.__dismissOptions), b.on("mainMenu", this.__mainMenuPressed), b.present())
                    },
                    __dismissOptions: function () {
                        var a = this.getPlayer(),
                            b = a._getMenu("options");
                        b.off("escape", this.__dismissOptions), b.off("mainMenu", this.__mainMenuPressed), b.dismiss()
                    },
                    __mainMenuPressed: function () {
                        var a = this.getPlayer(),
                            b = a._getMenu("yesno");
                        a._getMenu("options"), b.configure("@t_ui_rusMain"), b.on("yes", this.__yesMainMenu), b.on("no", this.__noMainMenu), this.__dismissOptions(), b.present()
                    },
                    __clearYesNo: function () {
                        var a = this.getPlayer(),
                            b = a._getMenu("yesno");
                        b.off("yes", this.__yesMainMenu), b.off("no", this.__noMainMenu), b.dismiss()
                    },
                    __yesMainMenu: function () {
                        var a = this.getPlayer();
                        this.__clearYesNo(), a.mainMenu()
                    },
                    __noMainMenu: function () {
                        this.__clearYesNo(), this.__showOptions()
                    },
                    __windowBlurred: function () {
                        this.__endSkip()
                    },
                    __toggleSkip: function () {
                        this.__skipping ? this.__endSkip() : this.__startSkip()
                    },
                    __startSkip: function () {
                        this.__skipping || (a(f).addClass("active"), this.__skipping = true)
                    },
                    __endSkip: function () {
                        this.__skipping && (a(f).removeClass("active"), this.__skipping = false)
                    },
                    __isSkipping: function () {
                        return this.__skipping
                    },
                    __showSkipButton: function (b) {
                        b = !! b;
                        var c = d.getActiveEvent(),
                            e = c && !c.isDestroyed() && c.shouldSkip(g);
                        b || e ? a(f).removeClass("disabled") : this.__hideSkipButton()
                    },
                    __hideSkipButton: function () {
                        a(f).addClass("disabled")
                    },
                    __eventChanged: function () {
                        this.__showSkipButton()
                    }
                }
            });
        return h
    }), define("htmlvn/menu/YesNoPrompt", ["jquery", "htmlvn/menu/Screen"], function (a, b) {
        "use strict";
        var c = b.inheritWith(function (a, b) {
            return {
                constructor: function (a) {
                    b.call(this, a, "#yesNoPrompt")
                },
                configure: function (a, b, c) {
                    var d = this._setElText,
                        e = this.getRoot();
                    void 0 === b && (b = "@t_ui_yes"), void 0 === c && (c = "@t_ui_no"), d(e.find("h3"), a), d(e.find(".yes buttonContent"), b), d(e.find(".no buttonContent"), c)
                }
            }
        });
        return c
    }), define("htmlvn/events/ConsoleEvent", ["htmlvn/lib/utils", "htmlvn/events/DiscreteEvent", "htmlvn/DataStore"], function (a, b, c) {
        "use strict";
        var d = b.inheritWith(function (a, b) {
            return {
                constructor: function (a) {
                    this.__severity = a.severity || "log", this.__value = a.value, "auto" in a || (a.auto = true), b.call(this, a)
                },
                pump: function () {
                    console[this.__severity](c.replaceVariableTokens(this.__value))
                },
                interrupt: function () {
                    return false
                },
                isComplete: function () {
                    return true
                }
            }
        });
        return d
    }), define("htmlvn/events/JumpEvent", ["htmlvn/lib/utils", "htmlvn/events/DiscreteEvent", "htmlvn/BasePlayer", "htmlvn/DataStore"], function (a, b, c) {
        "use strict";
        var d = b.inheritWith(function (a, b) {
            return {
                constructor: function (a) {
                    this.__path = a.path, "auto" in a || (a.auto = true), b.call(this, a)
                },
                pump: function (a) {
                    a || console.warn("How did we get a false for runAnim???"), c.jumpToEvent(this.__path)
                },
                interrupt: function () {
                    return false
                },
                isComplete: function () {
                    return false
                },
                shouldSkip: function () {
                    return false
                },
                ensurePath: function () {
                    var a = this.getScene(),
                        b = !! a.findEvent(this.__path);
                    return b
                }
            }
        });
        return d
    }), define("htmlvn/events/MenuEvent", ["jquery", "htmlvn/lib/utils", "htmlvn/StepMode", "htmlvn/BasePlayer", "htmlvn/events/DiscreteEvent"], function (a, b, c, d, e) {
        "use strict";
        var f = d.getInstance,
            g = e.inheritWith(function (a, b) {
                return {
                    constructor: function (a) {
                        this.__menuName = a.menuName, b.call(this, a)
                    },
                    interrupt: function () {
                        return false
                    },
                    pump: function (a) {
                        if (!a) return this.__done = true, true;
                        this._configureMenu(this._getMenu());
                        var b = this._presentScreen();
                        b || console.error("Got a bad return value from showScreen ... not great; proceeding anyway!!")
                    },
                    shouldSkip: function (a) {
                        return a >= c.Load
                    },
                    _configureMenu: function () {},
                    _setMenuName: function (a) {
                        this.__menuName = a
                    },
                    _getMenuName: function () {
                        return this.__menuName
                    },
                    _getMenu: function () {
                        var a = f()._getMenu(this.__menuName);
                        return a || console.error("Got a bad return value from _getMenu ... not great; proceeding anyway!!"), a
                    },
                    _getMenuRoot: function () {
                        var a = this._getMenu();
                        return a ? a.getRoot() : null
                    },
                    _presentScreen: function () {
                        return f().presentMenu(this.__menuName)
                    },
                    _dismissScreen: function () {
                        return f().dismissMenu(this.__menuName)
                    }
                }
            });
        return g
    }),
    function () {
        "use strict";

        function a(b, c) {
            for (var d = b.cssRules || b.rules || [], e = 0; e < d.length; e++) {
                var f = d[e];
                f.type == CSSRule.IMPORT_RULE ? a(f.styleSheet, c) : (f.type === CSSRule.KEYFRAMES_RULE || f.type === CSSRule.MOZ_KEYFRAMES_RULE || f.type === CSSRule.WEBKIT_KEYFRAMES_RULE) && c(f, b, e)
            }
        }

        function b(a) {
            this.original = a, this.keyText = a.keyText, this.css = {};
            for (var b = a.style.cssText.split(";"), c = 0; c < b.length; c++) {
                var d = b[c].split(":");
                if (2 == d.length) {
                    var e = d[0].replace(/^\s+|\s+$/g, ""),
                        f = d[1].replace(/^\s+|\s+$/g, "");
                    this.css[e] = f
                }
            }
        }

        function c(a) {
            this.original = a, this.name = a.name, this.keyframes = [], this.keytexts = [], this.keyframeHash = {}, this.initKeyframes()
        }

        function d() {
            this.animations = {};
            for (var b = document.styleSheets, d = this.animations, e = 0; e < b.length; e++) try {
                a(b[e], function (a) {
                    d[a.name] = new c(a)
                })
            } catch (f) {}
        }
        c.prototype.initKeyframes = function () {
            this.keyframes = [], this.keytexts = [], this.keyframeHash = {};
            for (var a = this.original, c = 0; c < a.cssRules.length; c++) {
                var d = new b(a.cssRules[c]);
                this.keyframes.push(d), this.keytexts.push(d.keyText), this.keyframeHash[d.keyText] = d
            }
        }, c.prototype.getKeyframeTexts = function () {
            return this.keytexts
        }, c.prototype.getKeyframe = function (a) {
            return this.keyframeHash[a]
        }, c.prototype.setKeyframe = function (a, b) {
            var c = a + " {";
            for (var d in b) c += d + ":" + b[d] + ";";
            return c += "}", "appendRule" in this.original ? this.original.appendRule(c) : this.original.insertRule(c), this.initKeyframes(), this
        }, c.prototype.setKeyframes = function (a) {
            for (var b in a) this.setKeyframe(b, a[b])
        }, c.prototype.clear = function () {
            for (var a = 0; a < this.keyframes.length; a++) this.original.deleteRule(this.keyframes[a].keyText)
        }, d.prototype.get = function (a) {
            return this.animations[a]
        }, d.prototype.getDynamicSheet = function () {
            if (!this.dynamicSheet) {
                var a = document.createElement("style");
                a.rel = "stylesheet", a.type = "text/css", document.getElementsByTagName("head")[0].appendChild(a), this.dynamicSheet = a.sheet
            }
            return this.dynamicSheet
        }, d.prototype.create = function (a, b) {
            var d = this.getDynamicSheet();
            "object" == typeof a && (b = a, a = null), a || (a = "anim" + Math.floor(1e5 * Math.random()));
            try {
                var e = d.insertRule("@keyframes " + a + "{}", d.cssRules.length)
            } catch (f) {
                if ("SYNTAX_ERR" != f.name && "SyntaxError" != f.name) throw f;
                e = d.insertRule("@-webkit-keyframes " + a + "{}", d.cssRules.length)
            }
            var g = new c(d.cssRules[e]);
            return this.animations[a] = g, b && g.setKeyframes(b), g
        }, d.prototype.remove = function (b) {
            var d = this.getDynamicSheet();
            b = b instanceof c ? b.name : b, this.animations[b] = null;
            try {
                a(d, function (a, c, d) {
                    a.name == b && c.deleteRule(d)
                })
            } catch (e) {}
        }, "function" == typeof define && define.amd ? define("htmlvn/lib/CSSAnimations", [], function () {
            return new d
        }) : window.CSSAnimations = new d
    }(),
    function (a) {
        var b = {
            vertical: {
                x: false,
                y: true
            },
            horizontal: {
                x: true,
                y: false
            },
            both: {
                x: true,
                y: true
            },
            x: {
                x: true,
                y: false
            },
            y: {
                x: false,
                y: true
            }
        }, c = {
                duration: "fast",
                direction: "both"
            }, d = /^(?:html)$/i,
            e = function (b, c) {
                c = c || (document.defaultView && document.defaultView.getComputedStyle ? document.defaultView.getComputedStyle(b, null) : b.currentStyle);
                var d = document.defaultView && document.defaultView.getComputedStyle ? true : false,
                    e = {
                        top: parseFloat(d ? c.borderTopWidth : a.css(b, "borderTopWidth")) || 0,
                        left: parseFloat(d ? c.borderLeftWidth : a.css(b, "borderLeftWidth")) || 0,
                        bottom: parseFloat(d ? c.borderBottomWidth : a.css(b, "borderBottomWidth")) || 0,
                        right: parseFloat(d ? c.borderRightWidth : a.css(b, "borderRightWidth")) || 0
                    };
                return {
                    top: e.top,
                    left: e.left,
                    bottom: e.bottom,
                    right: e.right,
                    vertical: e.top + e.bottom,
                    horizontal: e.left + e.right
                }
            }, f = function (b) {
                var c = a(window),
                    f = d.test(b[0].nodeName);
                return {
                    border: f ? {
                        top: 0,
                        left: 0,
                        bottom: 0,
                        right: 0
                    } : e(b[0]),
                    scroll: {
                        top: (f ? c : b).scrollTop(),
                        left: (f ? c : b).scrollLeft()
                    },
                    scrollbar: {
                        right: f ? 0 : b.innerWidth() - b[0].clientWidth,
                        bottom: f ? 0 : b.innerHeight() - b[0].clientHeight
                    },
                    rect: function () {
                        var a = b[0].getBoundingClientRect();
                        return {
                            top: f ? 0 : a.top,
                            left: f ? 0 : a.left,
                            bottom: f ? b[0].clientHeight : a.bottom,
                            right: f ? b[0].clientWidth : a.right
                        }
                    }()
                }
            };
        a.fn.extend({
            scrollintoview: function (e) {
                e = a.extend({}, c, e), e.direction = b["string" == typeof e.direction && e.direction.toLowerCase()] || b.both;
                var g = "";
                e.direction.x === true && (g = "horizontal"), e.direction.y === true && (g = g ? "both" : "vertical");
                var h = this.eq(0),
                    i = h.closest(":scrollable(" + g + ")");
                if (i.length > 0) {
                    i = i.eq(0);
                    var j = {
                        e: f(h),
                        s: f(i)
                    }, k = {
                            top: j.e.rect.top - (j.s.rect.top + j.s.border.top),
                            bottom: j.s.rect.bottom - j.s.border.bottom - j.s.scrollbar.bottom - j.e.rect.bottom,
                            left: j.e.rect.left - (j.s.rect.left + j.s.border.left),
                            right: j.s.rect.right - j.s.border.right - j.s.scrollbar.right - j.e.rect.right
                        }, l = {};
                    e.direction.y === true && (k.top < 0 ? l.scrollTop = j.s.scroll.top + k.top : k.top > 0 && k.bottom < 0 && (l.scrollTop = j.s.scroll.top + Math.min(k.top, -k.bottom))), e.direction.x === true && (k.left < 0 ? l.scrollLeft = j.s.scroll.left + k.left : k.left > 0 && k.right < 0 && (l.scrollLeft = j.s.scroll.left + Math.min(k.left, -k.right))), a.isEmptyObject(l) ? a.isFunction(e.complete) && e.complete.call(i[0]) : (d.test(i[0].nodeName) && (i = a("html,body")), i.animate(l, e.duration).eq(0).queue(function (b) {
                        a.isFunction(e.complete) && e.complete.call(i[0]), b()
                    }))
                }
                return this
            }
        });
        var g = {
            auto: true,
            scroll: true,
            visible: false,
            hidden: false
        };
        a.extend(a.expr[":"], {
            scrollable: function (a, c, e) {
                var f = b["string" == typeof e[3] && e[3].toLowerCase()] || b.both,
                    h = document.defaultView && document.defaultView.getComputedStyle ? document.defaultView.getComputedStyle(a, null) : a.currentStyle,
                    i = {
                        x: g[h.overflowX.toLowerCase()] || false,
                        y: g[h.overflowY.toLowerCase()] || false,
                        isRoot: d.test(a.nodeName)
                    };
                if (!i.x && !i.y && !i.isRoot) return false;
                var j = {
                    height: {
                        scroll: a.scrollHeight,
                        client: a.clientHeight
                    },
                    width: {
                        scroll: a.scrollWidth,
                        client: a.clientWidth
                    },
                    scrollableX: function () {
                        return (i.x || i.isRoot) && this.width.scroll > this.width.client
                    },
                    scrollableY: function () {
                        return (i.y || i.isRoot) && this.height.scroll > this.height.client
                    }
                };
                return f.y && j.scrollableY() || f.x && j.scrollableX()
            }
        })
    }(jQuery), define("jquery.scrollintoview", ["jquery"], function () {}), define("htmlvn/events/drivers/dom/DOMTextEvent", ["jquery", "htmlvn/lib/utils", "htmlvn/StepMode", "htmlvn/assets/Asset", "htmlvn/events/DiscreteEvent", "htmlvn/lib/CSSAnimations", "htmlvn/DataStore", "jquery.scrollintoview"], function (a, b, c, d, e, f, g) {
        "use strict";
        var h = {}, i = function (a, b) {
                h[a] = b
            }, j = function () {
                a("#textContent *").remove()
            }, k = function (b, c) {
                a("#textArea").attr("class", "textArea " + b), a("#textContent").attr("class", "textContent " + b), a("#actorName").attr("class", b).text(c)
            }, l = function () {
                a("#textArea").attr("class", "textArea"), a("#textContent").attr("class", "textContent"), a("#actorName").attr("class", "").text("")
            }, m = function (a, b) {
                var c = a;
                if (!a || "string" != typeof a || 0 === a.length) return "";
                if ("$" === a.charAt(0)) c = g.resolve(a);
                else {
                    var e = d.tryResolve(a);
                    c = e ? e.getValue() : a
                }
                return b && b in h && (c = h[b](c)), c
            };
        i("uppercase", function (a) {
            return a.toUpperCase()
        }), i("lowercase", function (a) {
            return a.toLowerCase()
        });
        var n = /[.@ ]/g,
            o = null,
            p = null,
            q = .1,
            r = 0,
            s = e.inheritWith(function (d, e) {
                return {
                    __canceling: false,
                    __letterTag: "span",
                    __wordTag: "span",
                    __textTag: "span",
                    __letterClass: "letterDefault",
                    __wordClass: "wordDefault",
                    __textClass: "textDefault",
                    __letterDelay: .0125,
                    __wordDelay: 0,
                    __append: false,
                    __textId: "",
                    __charId: "",
                    __transformer: null,
                    constructor: function (a) {
                        var c = b.pickInAndSet;
                        e.call(this, a), c(this, "__textId", a, ["text", "txt"]), c(this, "__charId", a, ["actor", "character", "char"]), c(this, "__append", a, ["append"]), c(this, "__letterClass", a, ["letterClass", "lc"]), c(this, "__wordClass", a, ["wordClass", "wc"]), c(this, "__textClass", a, ["textClass", "tc"]), c(this, "__letterTag", a, ["letterTag", "lt"]), c(this, "__wordTag", a, ["wordTag", "wt"]), c(this, "__textTag", a, ["textTag", "tt"]), c(this, "__letterDelay", a, ["letterDelay", "ld"]), c(this, "__wordDelay", a, ["wordDelay", "wd"]), c(this, "__transformer", a, ["transform", "transformer"])
                    },
                    interrupt: function () {
                        var a = !this.isComplete();
                        return a && this.__cancelTransitions(), a
                    },
                    isComplete: function () {
                        return this.__waitingOn <= 0
                    },
                    update: function (a) {
                        null != o && (r += a, r > q && (this.__scrollIntoView(o), o = null, r = 0))
                    },
                    eventWarm: function () {
                        this.__doneTransform = this.__doneTransform.bind(this), this.__startTransform = this.__startTransform.bind(this), d.eventWarm.apply(this, arguments), this.__waitingOn = 0;
                        var b, c, e = this.__textId,
                            f = this.__textId.replace(n, ""),
                            h = this.__charId.replace(n, ""),
                            i = document.createElement(this.__textTag),
                            j = 0,
                            k = 0;
                        r = 0;
                        var l = "unread";
                        g.wasTextRead(e) && (l = "read"), e = m(e, this.__transformer), i.setAttribute("class", ["text", this.__textClass, f, h, l].join(" ")), document.getElementById("textAreaStage").appendChild(i);
                        for (var o = e.split(/\s+/g), p = 0; p < o.length; ++p) {
                            var q = o[p];
                            q += " ";
                            var s = q.split("");
                            b = document.createElement(this.__wordTag), b.setAttribute("class", ["word", "needsWatch", h, f, this.__wordClass, l].join(" ")), i.appendChild(b);
                            for (var t = 0; t < s.length; ++t) {
                                var u = s[t];
                                k = j * this.__letterDelay, j += 1, c = document.createElement(this.__letterTag);
                                var v = ["char", "needsWatch", h, f, this.__letterClass, l];
                                " " === u ? (v.push("empty"), a(c).html("&nbsp")) : a(c).text(u), c.setAttribute("class", v.join(" ")), b.appendChild(a(c).css("animation-delay", k + "s")[0])
                            }
                        }
                        this.__containingEl = i, i = b = c = null
                    },
                    pump: function (c) {
                        var d = this.__charId,
                            e = this.__textId.replace(n, ""),
                            f = this.__charId.replace(n, ""),
                            h = a(this.__containingEl),
                            i = this;
                        this.__append || j(), l(), d && (d = m(d), k(f, d)), g.markTextRead(this.__textId), a("#textArea").addClass(e);
                        var o = this.__textContent = a("#textContent");
                        if (o.append(h.on(b.animationend, ".animating", this.__doneTransform).on(b.animationstart, ".animating", this.__startTransform)), o.find(".needsWatch").removeClass("needsWatch").each(function (a, b) {
                            i.__watchForComplete(b)
                        }), !c) {
                            this.__cancelTransitions();
                            var p = h.children();
                            p.length > 0 && this.__scrollIntoView(p[p.length - 1])
                        }
                    },
                    shouldSkip: function (a) {
                        var b = d.shouldSkip.call(this, a);
                        return b ? a === c.Skip ? !this.__textId || 0 === this.__textId.length || g.wasTextRead(this.__textId) : true : false
                    },
                    finalize: function () {
                        d.finalize.call(this), a(this.__containingEl).off(b.animationstart, ".animating", this.__startTransform), a(this.__containingEl).off(b.animationend, ".animating", this.__doneTransform), this.__containingEl = null, this.__textContent = null, delete this.__doneTransform
                    },
                    collectAssets: function () {
                        var a = [];
                        return this.__charId && a.push(this.__charId), this.__textId && a.push(this.__textId), a
                    },
                    __watchForComplete: function (b) {
                        var c = this.__getAnim(b);
                        c ? (this.__waitingOn += 1, a(b).addClass("animating")) : a(b).addClass("complete")
                    },
                    __startTransform: function (a) {
                        this.__animStart(a.target, true)
                    },
                    __doneTransform: function (a) {
                        this.__animDone(a.target, true)
                    },
                    __animStart: function (a, b) {
                        !this.__canceling && b && (p = o = a)
                    },
                    __scrollIntoView: function (b) {
                        a(b).scrollintoview({
                            duration: 0
                        })
                    },
                    __animDone: function (a) {
                        this.__canceling || (this.__waitingOn -= 1, this.__waitingOn <= 0 && (this.__cancelTransitions(), this.__scrollIntoView(a), p = o = null, this._signalComplete()))
                    },
                    __cancelTransitions: function (c) {
                        var d = this;
                        a(this.__containingEl).off(b.animationstart, ".animating", this.__startTransform), a(this.__containingEl).off(b.animationend, ".animating", this.__doneTransform), this.__canceling = true, c = c || a("#textContent");
                        var e = c.find("*");
                        e.length > 0 && (e.each(function (b, c) {
                            var e = a(c),
                                f = d.__getAnim(e);
                            if (f) {
                                var g = f.getKeyframe("100%"),
                                    h = a.extend({
                                        "animation-name": "none",
                                        "animation-duration": "0s",
                                        "animation-delay": "0s"
                                    }, g.css);
                                e.css(h), d.__animDone(e, false), e = null
                            }
                        }), this.__scrollIntoView(e[e.length - 1])), this.__waitingOn = 0, p = null, o = null, this.__canceling = false
                    },
                    __getAnim: function (b) {
                        var c = null,
                            d = a(b).css("animation-name");
                        if ("string" == typeof d && d.length > 0) {
                            var e = f.get(d);
                            e && (c = e)
                        }
                        return c
                    }
                }
            }).defineStatic({
                resolveText: m,
                clearTextContent: j,
                clearActorName: l,
                setActorName: k,
                getLastAnimated: function () {
                    return p
                },
                registerTransformer: i
            });
        return s
    }), define("htmlvn/events/ChoiceEvent", ["jquery", "htmlvn/lib/utils", "htmlvn/StepMode", "htmlvn/BasePlayer", "htmlvn/events/MenuEvent", "htmlvn/events/Event", "htmlvn/events/Macro", "htmlvn/events/DiscreteEvent", "htmlvn/events/drivers/dom/DOMTextEvent", "htmlvn/DataStore", "htmlvn/assets/Asset"], function (a, b, c, d, e, f, g, h, i, j) {
        "use strict";
        var k = e.inheritWith(function (c, d) {
            return {
                __promptText: null,
                __storeName: "slot",
                __done: false,
                constructor: function (a) {
                    this.__choices = a.choices, this.__varName = a.varName, "auto" in a || (a.auto = true), "promptText" in a && (this.__promptText = a.promptText), "menuName" in a || (a.menuName = "choice"), "storeName" in a && (this.__storeName = a.storeName), a.allowInterrupt = false, a.auto = true, d.call(this, a)
                },
                eventWarm: function () {
                    this.__done = false, this.__boundChoice = this._menuChoice.bind(this), c.eventWarm.apply(this, arguments)
                },
                pump: function () {
                    var b = this.__done = c.pump.apply(this, arguments);
                    if (!b && (i.clearActorName(), i.clearTextContent(), this.__promptText)) {
                        var d = i.resolveText(this.__promptText),
                            e = a('<div class="promptText"></div>');
                        e.text(d), a("#textContent").append(e)
                    }
                    return b
                },
                finalize: function () {
                    var a = this._getMenu();
                    a && a.off("choice", this.__boundChoice), this.__boundChoice = null, c.finalize.apply(this, arguments)
                },
                isComplete: function () {
                    return this.__done
                },
                _configureMenu: function (a) {
                    a && (a.on("choice", this.__boundChoice), a.configure(this, this.__choices))
                },
                _menuChoice: function (a) {
                    function c() {
                        console.log("ChoiceEvent signaling complete!!!"), e.__done = true, e._signalComplete()
                    }
                    var d = b.coerceType(a.value);
                    j.set(this.__varName, d, this.__storeName);
                    var e = this,
                        f = this._dismissScreen();
                    f ? f.then(c) : (console.warn("Didn't get a promise from _dismissScreen; completing immediately!!"), c())
                }
            }
        });
        return k
    }), define("htmlvn/Comparisons", ["htmlvn/DataStore"], function (DataStore) {
        "use strict";
        var eq = function (a, b) {
            return function () {
                return DataStore.resolve(a) == DataStore.resolve(b)
            }
        }, lt = function (a, b) {
                return function () {
                    return DataStore.resolve(a) < DataStore.resolve(b)
                }
            }, gt = function (a, b) {
                return function () {
                    return DataStore.resolve(a) > DataStore.resolve(b)
                }
            }, lte = function (a, b) {
                return function () {
                    return DataStore.resolve(a) <= DataStore.resolve(b)
                }
            }, gte = function (a, b) {
                return function () {
                    return DataStore.resolve(a) >= DataStore.resolve(b)
                }
            }, logicalTrue = function (a) {
                return function () {
                    return !!DataStore.resolve(a)
                }
            }, logicalFalse = function (a) {
                return function () {
                    return !DataStore.resolve(a)
                }
            }, doEval = function doEval(str) {
                return function () {
                    var funcText = DataStore.replaceVariableTokens(str);
                    return eval(funcText)
                }
            };
        return {
            EQ: eq,
            LT: lt,
            GT: gt,
            LTE: lte,
            GTE: gte,
            True: logicalTrue,
            False: logicalFalse,
            Eval: doEval
        }
    }), define("htmlvn/events/ConditionalEvent", ["htmlvn/events/Macro", "htmlvn/DataStore", "htmlvn/Comparisons", "htmlvn/StepMode"], function (a, b, c, d) {
        "use strict";
        var e = a.inheritWith(function (a, b) {
            return {
                __evaluated: false,
                constructor: function (a) {
                    this.__comparison = a.comparison, b.call(this, a)
                },
                doesAutocomplete: function () {
                    return this.__eval() ? a.doesAutocomplete.call(this) : true
                },
                eventWarm: function () {
                    this.__evaluated = false, this.__eval() && a.eventWarm.apply(this, arguments)
                },
                step: function (b) {
                    return this.__eval() ? a.step.call(this, b) : true
                },
                finalize: function () {
                    this.__eval() && a.finalize.call(this)
                },
                isComplete: function () {
                    return this.__eval() ? a.isComplete.call(this) : true
                },
                update: function (b) {
                    this.__eval() && a.update.call(this, b)
                },
                shouldSkip: function (b) {
                    return this.__eval() ? a.shouldSkip.call(this, b) : b > d.Normal
                },
                __eval: function () {
                    if (!this.__evaluated) {
                        var a = typeof this.__comparison;
                        "string" === a ? this.__result = c.Eval(this.__comparison)() : "function" === a && (this.__result = this.__comparison()), this.__evaluated = true
                    }
                    return this.__result
                }
            }
        });
        return e
    }), define("htmlvn/events/drivers/common/BaseImageEvent", ["htmlvn/lib/utils", "htmlvn/events/DiscreteEvent", "htmlvn/assets/Asset", "htmlvn/assets/ImageAsset"], function (a, b, c, d) {
        function e(a) {
            if ("string" == typeof a) {
                var b = a.charAt(0);
                b in h || (a = "#" + a), a = "#game " + a
            }
            return a
        }

        function f(a) {
            if (a instanceof d);
            else if ("string" == typeof a) {
                var b = c.tryResolve(a, false);
                b && (a = b)
            }
            return a
        }

        function g(a) {
            if (a instanceof d) a = a.getPath();
            else {
                if ("string" != typeof a) throw new Error("Bad value passed into image: " + a);
                var b = c.tryResolve(a, false);
                b && (a = b.getPath())
            }
            return a
        }
        var h = {
            ".": true,
            "#": true,
            ":": true,
            "*": true
        }, i = b.inheritWith(function (b, c) {
                return {
                    _duration: 0,
                    _target: null,
                    _ease: "linear",
                    constructor: function d(b) {
                        var e = a.pickInAndSet;
                        c.call(this, b), this._target = d.parseTarget(b.target), e(this, "_style", b, ["style", "styles"], {}), e(this, "_transitions", b, ["transitions", "trans"], {}), e(this, "_animation", b, ["animation", "anim"]), e(this, "_duration", b, ["time", "duration"]), b.ease && (this._ease = b.ease), "string" == typeof this._style && (this._style = {
                            image: this._style
                        }), this._duration <= 0 && ($.extend(this._style, this._transitions), this._duration = 0, this._transitions = {}), this.__transitioning = this._duration > 0 && Object.keys(this._transitions).length > 0, this.__animating = this._duration > 0 && !! this._animation
                    },
                    isComplete: function () {
                        return true
                    },
                    interrupt: function () {
                        return false
                    },
                    collectAssets: function () {
                        return "image" in this._style ? [this._style.image] : null
                    },
                    _resolveImage: function (b) {
                        return g(a.pick(b, this._style.image))
                    },
                    _getImageAsset: function (b) {
                        return f(a.pick(b, this._style.image))
                    }
                }
            }).defineStatic({
                parseTarget: e,
                resolveImage: g,
                getImageAsset: f
            });
        return i
    }),
    function (a) {
        function b(a) {
            if (a in l.style) return a;
            var b = ["Moz", "Webkit", "O", "ms"],
                c = a.charAt(0).toUpperCase() + a.substr(1);
            if (a in l.style) return a;
            for (var d = 0; d < b.length; ++d) {
                var e = b[d] + c;
                if (e in l.style) return e
            }
        }

        function c() {
            return l.style[m.transform] = "", l.style[m.transform] = "rotateY(90deg)", "" !== l.style[m.transform]
        }

        function d(a) {
            return "string" == typeof a && this.parse(a), this
        }

        function e(a, b, c) {
            b === true ? a.queue(c) : b ? a.queue(b, c) : c()
        }

        function f(b) {
            var c = [];
            return a.each(b, function (b) {
                b = a.camelCase(b), b = a.transit.propertyMap[b] || a.cssProps[b] || b, b = i(b), -1 === a.inArray(b, c) && c.push(b)
            }), c
        }

        function g(b, c, d, e) {
            var g = f(b);
            a.cssEase[d] && (d = a.cssEase[d]);
            var h = "" + k(c) + " " + d;
            parseInt(e, 10) > 0 && (h += " " + k(e));
            var i = [];
            return a.each(g, function (a, b) {
                i.push(b + " " + h)
            }), i.join(", ")
        }

        function h(b, c) {
            c || (a.cssNumber[b] = true), a.transit.propertyMap[b] = m.transform, a.cssHooks[b] = {
                get: function (c) {
                    var d = a(c).css("transit:transform");
                    return d.get(b)
                },
                set: function (c, d) {
                    var e = a(c).css("transit:transform");
                    e.setFromString(b, d), a(c).css({
                        "transit:transform": e
                    })
                }
            }
        }

        function i(a) {
            return a.replace(/([A-Z])/g, function (a) {
                return "-" + a.toLowerCase()
            })
        }

        function j(a, b) {
            return "string" != typeof a || a.match(/^[\-0-9\.]+$/) ? "" + a + b : a
        }

        function k(b) {
            var c = b;
            return "string" != typeof c || c.match(/^[\-0-9\.]+/) || (c = a.fx.speeds[c] || a.fx.speeds._default), j(c, "ms")
        }
        a.transit = {
            version: "0.9.9",
            propertyMap: {
                marginLeft: "margin",
                marginRight: "margin",
                marginBottom: "margin",
                marginTop: "margin",
                paddingLeft: "padding",
                paddingRight: "padding",
                paddingBottom: "padding",
                paddingTop: "padding"
            },
            enabled: true,
            useTransitionEnd: false
        };
        var l = document.createElement("div"),
            m = {}, n = navigator.userAgent.toLowerCase().indexOf("chrome") > -1;
        m.transition = b("transition"), m.transitionDelay = b("transitionDelay"), m.transform = b("transform"), m.transformOrigin = b("transformOrigin"), m.transform3d = c();
        var o = m.transitionEnd = "transitionend transitionEnd webkitTransitionEnd otransitionend oTransitionEnd MSTransitionEnd";
        for (var p in m) m.hasOwnProperty(p) && "undefined" == typeof a.support[p] && (a.support[p] = m[p]);
        l = null, a.cssEase = {
            _default: "ease",
            "in": "ease-in",
            out: "ease-out",
            "in-out": "ease-in-out",
            snap: "cubic-bezier(0,1,.5,1)",
            easeOutCubic: "cubic-bezier(.215,.61,.355,1)",
            easeInOutCubic: "cubic-bezier(.645,.045,.355,1)",
            easeInCirc: "cubic-bezier(.6,.04,.98,.335)",
            easeOutCirc: "cubic-bezier(.075,.82,.165,1)",
            easeInOutCirc: "cubic-bezier(.785,.135,.15,.86)",
            easeInExpo: "cubic-bezier(.95,.05,.795,.035)",
            easeOutExpo: "cubic-bezier(.19,1,.22,1)",
            easeInOutExpo: "cubic-bezier(1,0,0,1)",
            easeInQuad: "cubic-bezier(.55,.085,.68,.53)",
            easeOutQuad: "cubic-bezier(.25,.46,.45,.94)",
            easeInOutQuad: "cubic-bezier(.455,.03,.515,.955)",
            easeInQuart: "cubic-bezier(.895,.03,.685,.22)",
            easeOutQuart: "cubic-bezier(.165,.84,.44,1)",
            easeInOutQuart: "cubic-bezier(.77,0,.175,1)",
            easeInQuint: "cubic-bezier(.755,.05,.855,.06)",
            easeOutQuint: "cubic-bezier(.23,1,.32,1)",
            easeInOutQuint: "cubic-bezier(.86,0,.07,1)",
            easeInSine: "cubic-bezier(.47,0,.745,.715)",
            easeOutSine: "cubic-bezier(.39,.575,.565,1)",
            easeInOutSine: "cubic-bezier(.445,.05,.55,.95)",
            easeInBack: "cubic-bezier(.6,-.28,.735,.045)",
            easeOutBack: "cubic-bezier(.175, .885,.32,1.275)",
            easeInOutBack: "cubic-bezier(.68,-.55,.265,1.55)"
        }, a.cssHooks["transit:transform"] = {
            get: function (b) {
                if (!a(b).data("transform")) {
                    var c = window.getComputedStyle(b),
                        e = c[m.transform],
                        f = new d(e);
                    a(b).data("transform", f)
                }
                return a(b).data("transform")
            },
            set: function (b, c) {
                var e = c;
                e instanceof d || (e = new d(e)), b.style[m.transform] = "WebkitTransform" !== m.transform || n ? e.toString() : e.toString(true), a(b).data("transform", e)
            }
        }, a.cssHooks.transform = {
            set: a.cssHooks["transit:transform"].set
        }, a.fn.jquery < "1.8" && (a.cssHooks.transformOrigin = {
            get: function (a) {
                return a.style[m.transformOrigin]
            },
            set: function (a, b) {
                a.style[m.transformOrigin] = b
            }
        }, a.cssHooks.transition = {
            get: function (a) {
                return a.style[m.transition]
            },
            set: function (a, b) {
                a.style[m.transition] = b
            }
        }), h("scale"), h("scaleX"), h("scaleY"), h("translate"), h("rotate"), h("rotateX"), h("rotateY"), h("rotate3d"), h("perspective"), h("skewX"), h("skewY"), h("x", true), h("y", true), d.prototype = {
            setFromString: function (a, b) {
                var c = "string" == typeof b ? b.split(",") : b.constructor === Array ? b : [b];
                c.unshift(a), d.prototype.set.apply(this, c)
            },
            set: function (a) {
                var b = Array.prototype.slice.apply(arguments, [1]);
                this.setter[a] ? this.setter[a].apply(this, b) : this[a] = b.join(",")
            },
            get: function (a) {
                return this.getter[a] ? this.getter[a].apply(this) : this[a] || 0
            },
            setter: {
                rotate: function (a) {
                    this.rotate = j(a, "deg")
                },
                rotateX: function (a) {
                    this.rotateX = j(a, "deg")
                },
                rotateY: function (a) {
                    this.rotateY = j(a, "deg")
                },
                scaleX: function (a) {
                    this.set("scale", a, null)
                },
                scaleY: function (a) {
                    this.set("scale", null, a)
                },
                scale: function (a, b) {
                    if (void 0 === this._scaleX && (this._scaleX = 1), void 0 === this._scaleY && (this._scaleY = 1), 1 === arguments.length)
                        if ("string" == typeof a) {
                            var c = a.split(",");
                            c.length > 1 && (a = parseFloat(c[0]), b = parseFloat(c[1]))
                        } else b = a;
                    null !== a && void 0 !== a && (this._scaleX = parseFloat(a)), null !== b && void 0 !== b && (this._scaleY = parseFloat(b)), this.scale = this._scaleX + "," + this._scaleY
                },
                skewX: function (a) {
                    this.skewX = j(a, "deg")
                },
                skewY: function (a) {
                    this.skewY = j(a, "deg")
                },
                perspective: function (a) {
                    this.perspective = j(a, "px")
                },
                x: function (a) {
                    this.set("translate", a, null)
                },
                y: function (a) {
                    this.set("translate", null, a)
                },
                matrix: function (a, b, c, d, e, f) {
                    this.setter.translate.call(this, e, f), this.setter.scale.call(this, a, d)
                },
                translate: function (a, b) {
                    void 0 === this._translateX && (this._translateX = 0), void 0 === this._translateY && (this._translateY = 0), null !== a && void 0 !== a && (this._translateX = j(a, "px")), null !== b && void 0 !== b && (this._translateY = j(b, "px")), this.translate = this._translateX + "," + this._translateY
                }
            },
            getter: {
                x: function () {
                    return this._translateX || 0
                },
                y: function () {
                    return this._translateY || 0
                },
                scaleX: function () {
                    return this._scaleX || 1
                },
                scaleY: function () {
                    return this._scaleY || 1
                },
                scale: function () {
                    var a = this._scaleX || 1,
                        b = this._scaleY || 1;
                    return a === b ? a : [a, b]
                },
                rotate3d: function () {
                    for (var a = (this.rotate3d || "0,0,0,0deg").split(","), b = 0; 3 >= b; ++b) a[b] && (a[b] = parseFloat(a[b]));
                    return a[3] && (a[3] = j(a[3], "deg")), a
                }
            },
            parse: function (a) {
                var b = this;
                a.replace(/([a-zA-Z0-9]+)\((.*?)\)/g, function (a, c, d) {
                    b.setFromString(c, d)
                })
            },
            toString: function (a) {
                var b = [];
                for (var c in this)
                    if (this.hasOwnProperty(c)) {
                        if (!m.transform3d && ("rotateX" === c || "rotateY" === c || "perspective" === c || "transformOrigin" === c)) continue;
                        "_" !== c[0] && (a && "scale" === c ? b.push(c + "3d(" + this[c] + ",1)") : a && "translate" === c ? b.push(c + "3d(" + this[c] + ",0)") : b.push(c + "(" + this[c] + ")"))
                    }
                return b.join(" ")
            }
        }, a.fn.transition = a.fn.transit = function (b, c, d, f) {
            var h = this,
                i = 0,
                j = true,
                l = jQuery.extend(true, {}, b);
            "function" == typeof c && (f = c, c = void 0), "object" == typeof c && (d = c.easing, i = c.delay || 0, j = c.queue || true, f = c.complete, c = c.duration), "function" == typeof d && (f = d, d = void 0), "undefined" != typeof l.easing && (d = l.easing, delete l.easing), "undefined" != typeof l.duration && (c = l.duration, delete l.duration), "undefined" != typeof l.complete && (f = l.complete, delete l.complete), "undefined" != typeof l.queue && (j = l.queue, delete l.queue), "undefined" != typeof l.delay && (i = l.delay, delete l.delay), "undefined" == typeof c && (c = a.fx.speeds._default), "undefined" == typeof d && (d = a.cssEase._default), c = k(c);
            var n = g(l, c, d, i),
                p = a.transit.enabled && m.transition,
                q = p ? parseInt(c, 10) + parseInt(i, 10) : 0;
            if (0 === q) {
                var r = function (a) {
                    h.css(l), f && f.apply(h), a && a()
                };
                return e(h, j, r), h
            }
            var s = {}, t = function (b) {
                    var c = false,
                        d = function () {
                            c && h.off(o, d), q > 0 && h.each(function () {
                                this.style[m.transition] = s[this] || null
                            }), "function" == typeof f && f.apply(h), "function" == typeof b && b()
                        };
                    q > 0 && o && a.transit.useTransitionEnd ? (c = true, h.on(o, d)) : window.setTimeout(d, q), h.each(function () {
                        q > 0 && (this.style[m.transition] = n), a(this).css(l)
                    })
                }, u = function (a) {
                    this.offsetWidth, t(a)
                };
            return e(h, j, u), this
        }, a.fn.stopTransition = a.fn.stopTransit = function (b, c, d) {
            return "string" != typeof b && (d = c, c = b, b = void 0), c && b !== false && this.queue(b || "fx", []), d ? this.each(function () {
                this.style[m.transition] = "none 0s linear"
            }) : a.error("jumpToEnd=false not yet supported in transit!"), this
        }, a.transit.getTransitionValue = g
    }(jQuery), define("jquery.transit", ["jquery"], function () {}), define("htmlvn/events/drivers/dom/DOMImageEvent", ["jquery", "htmlvn/lib/utils", "htmlvn/events/drivers/common/BaseImageEvent", "htmlvn/lib/CSSAnimations", "jquery.transit"], function (a, b, c, d) {
        "use strict";
        var e = c.inheritWith(function (c, e) {
            return {
                constructor: function () {
                    e.apply(this, arguments)
                },
                eventWarm: function () {
                    if (c.eventWarm.apply(this, arguments), this.__boundAnimDone = this.__animationCallback.bind(this), this.__boundTransDone = this.__transitionCallback.bind(this), this.__finalizeTarget = this._target, this.__transitionsCancelled = false, this.__transitionsDone = false, this.__animationsDone = false, this.__animCancelled = false, "image" in this._style) {
                        if (this.__imageIsEmpty()) return;
                        var b = this._style.image,
                            d = this._getImageAsset(b);
                        if (!d) return console.warn("could not resolve asset named " + b), void 0;
                        for (var e = d.getPath(), f = a(this._target).length, g = 0, h = f - g; h > 0;) {
                            var i = d.getLoadedElement();
                            if (!i) return console.warn("No template loaded for asset: " + d.getAssetId()), void 0;
                            var j = a(d.getLoadedElement().cloneNode()).addClass("image waiting").attr({
                                "data-src": e,
                                src: e,
                                "data-forpath": this.getEventPath()
                            });
                            a("#backstage").append(j), h -= 1
                        }
                    }
                },
                pump: function (c) {
                    var e = a(this._target);
                    if (0 === e.length) return this.__animationsDone = true, this.__transitionsDone = true, true;
                    var f = null;
                    1e3 * this._duration;
                    var g = a.extend({}, this._style);
                    if ("image" in g && (f = g.image, delete g.image), "depth" in g && (g["z-index"] = g.depth, delete g.depth), "id" in g && (e.attr("id", g.id), this.__finalizeTarget = e, delete g.id), e.css(g), this.__transitioning && (c ? (this.__transitionsDone = false, e.transit(this._transitions, 1e3 * this._duration, this._ease, this.__boundTransDone)) : (e.css(this._transitions), this.__transitionsDone = true)), this.__animating) {
                        var h = typeof this._animation,
                            i = null;
                        if ("string" === h ? this.__liveAnim = i = d.get(this._animation) : "object" === h && (this.__liveAnim = this.__createdAnim = i = d.create(this._animation)), i) {
                            var j = i.name;
                            c ? e.on(b.animationend, this.__boundAnimDone).css({
                                "animation-name": j,
                                "animation-fill-mode": "forwards",
                                "animation-iteration-count": 1,
                                "animation-duration": this._duration + "s",
                                "animation-timing-function": this._ease
                            }) : this.__snapAnimToEnd()
                        } else console.warn("Could not resolve animation named " + this._animation)
                    }
                    if (null !== f)
                        if (this.__imageIsEmpty()) e.find(".image.live").removeClass("live").addClass("dead");
                        else {
                            var k = this._resolveImage(f),
                                l = e.find(".image.live"),
                                m = l.attr("data-src");
                            m != k ? (e.find(".image.live").removeClass("live").addClass("dead"), e.append(a("#backstage").find('.image[data-src="' + k + '"][data-forpath="' + this.getEventPath() + '"]').removeClass("waiting").addClass("live"))) : a("#backstage").find('.image[data-src="' + k + '"][data-forpath="' + this.getEventPath() + '"]').remove()
                        }
                    e = null
                },
                finalize: function () {
                    a(this.__finalizeTarget).off(b.animationend, this.__boundAnimDone).find(".image.dead").remove(), this.__createdAnim && (d.remove(this.__createdAnim), delete this.__createdAnim), this.__finalizeTarget = null, this.__liveAnim = null, this.__boundAnimDone = null, this.__boundTransDone = null
                },
                isComplete: function () {
                    return !(this.__transitioning && !this.__transitionsDone || this.__animating && !this.__animationsDone)
                },
                interrupt: function () {
                    var a = false;
                    return this.__transitioning && !this.__transitionsDone && (a = true, this.__stopTransitions()), this.__animating && !this.__animationsDone && (a = true, this.__stopAnimations()), a
                },
                __imageIsEmpty: function () {
                    return "image" in this._style && (!this._style.image || "string" == typeof this._style.image && 0 === this._style.image.length)
                },
                __stopTransitions: function () {
                    this.__transitioning && !this.__transitionsDone && (this.__transitionsCancelled = true, a(this._target).stopTransit(true, true).css(this._transitions), this.__transitionsDone = true)
                },
                __stopAnimations: function () {
                    this.__animating && (this.__animCancelled = true, this.__snapAnimToEnd())
                },
                __transitionCallback: function () {
                    this.__transitionsCancelled || (this.__transitionsDone = true, this.isComplete() && this._signalComplete())
                },
                __animationCallback: function () {
                    this.__snapAnimToEnd(), !this.__animCancelled && this.isComplete() && this._signalComplete()
                },
                __snapAnimToEnd: function () {
                    if (this.__liveAnim) {
                        var b = this.__liveAnim.getKeyframe("100%");
                        a(this._target).css({
                            "animation-name": "emptyAnimation",
                            "animation-duration": "0.001s"
                        }).css(b.css)
                    }
                    this.__animationsDone = true
                }
            }
        });
        return e
    }), define("htmlvn/events/FadeEvent", ["htmlvn/events/drivers/dom/DOMImageEvent"], function (a) {
        "use strict";
        var b = a.inheritWith(function (a, b) {
            return {
                constructor: function (a) {
                    "from" in a && (a.style = {
                        opacity: a.from
                    }, delete a.from), "to" in a && (a.transitions = {
                        opacity: a.to
                    }, delete a.to), b.call(this, a)
                }
            }
        });
        return b
    }), define("htmlvn/events/SceneChangeEvent", ["htmlvn/lib/utils", "htmlvn/events/DiscreteEvent", "htmlvn/BasePlayer"], function (a, b, c) {
        "use strict";
        var d = b.inheritWith(function (b, d) {
            return {
                constructor: function (b) {
                    if ("string" == typeof b) {
                        var c = {
                            scene: b
                        };
                        b = c
                    }
                    this.__sceneId = a.pickIn(b, ["scene", "sceneId", "s"]), d.call(this, b)
                },
                pump: function () {
                    c.getInstance().changeScene(this.__sceneId)
                },
                collectAssets: function () {
                    return [this.__sceneId]
                }
            }
        });
        return d
    }), define("htmlvn/events/vars/VarEvent", ["htmlvn/lib/utils", "htmlvn/events/DiscreteEvent", "htmlvn/DataStore", "htmlvn/StepMode"], function (a, b, c, d) {
        "use strict";
        var e = b.inheritWith(function (a, b) {
            return {
                __storeName: "slot",
                constructor: function (a) {
                    this.__varName = a.varName, "storeName" in a && (this.__storeName = a.storeName), "auto" in a || (a.auto = true), b.call(this, a)
                },
                pump: function () {
                    throw new Error("No default implementation for VarEvent#pump!")
                },
                interrupt: function () {
                    return false
                },
                isComplete: function () {
                    return true
                },
                shouldSkip: function (a) {
                    return a >= d.Load
                },
                _getStoreName: function () {
                    return this.__storeName
                },
                _getVarName: function () {
                    return this.__varName
                }
            }
        });
        return e
    }), define("htmlvn/events/vars/VarDelEvent", ["htmlvn/lib/utils", "htmlvn/events/DiscreteEvent", "htmlvn/DataStore", "htmlvn/events/vars/VarEvent"], function (a, b, c, d) {
        "use strict";
        var e = d.inheritWith(function (a, b) {
            return {
                constructor: function (a) {
                    b.call(this, a)
                },
                pump: function (a) {
                    if (a) {
                        var b = this._getStoreName(),
                            d = this._getVarName();
                        c.remove(d, b)
                    }
                }
            }
        });
        return e
    }), define("htmlvn/events/vars/VarSetEvent", ["htmlvn/lib/utils", "htmlvn/events/DiscreteEvent", "htmlvn/DataStore", "htmlvn/events/vars/VarEvent"], function (a, b, c, d) {
        "use strict";
        var e = d.inheritWith(function (b, d) {
            return {
                constructor: function (a) {
                    this.__value = a.value, d.call(this, a)
                },
                pump: function (b) {
                    b && c.set(this._getVarName(), a.coerceType(this.__value), this._getStoreName())
                }
            }
        });
        return e
    }), define("htmlvn/events/vars/VarIncEvent", ["htmlvn/lib/utils", "htmlvn/events/DiscreteEvent", "htmlvn/DataStore", "htmlvn/events/vars/VarEvent"], function (a, b, c, d) {
        "use strict";
        var e = d.inheritWith(function (a, b) {
            return {
                __amount: 1,
                constructor: function (a) {
                    "amount" in a && (this.__amount = a.amount), b.call(this, a)
                },
                pump: function (a) {
                    if (a) {
                        var b = this._getStoreName(),
                            d = this._getVarName(),
                            e = c.get(this._getVarName(), this._getStoreName()) || 0,
                            f = e + this.__amount;
                        c.set(d, f, b)
                    }
                }
            }
        });
        return e
    }), define("htmlvn/events/vars/VarEnsure", ["htmlvn/lib/utils", "htmlvn/DataStore", "htmlvn/events/vars/VarEvent"], function (a, b, c) {
        "use strict";
        var d = c.inheritWith(function (c, d) {
            return {
                constructor: function (a) {
                    this.__value = a.value, d.call(this, a)
                },
                pump: function (c) {
                    if (c) {
                        var d = this._getStoreName(),
                            e = this._getVarName();
                        b.hasKey(e, d) || b.set(e, a.coerceType(this.__value), d)
                    }
                }
            }
        });
        return d
    }), define("htmlvn/events/cond/IfEqual", ["jquery", "htmlvn/lib/utils", "htmlvn/Comparisons", "htmlvn/StepMode", "htmlvn/events/ConditionalEvent"], function (a, b, c, d, e) {
        "use strict";
        var f = e.inheritWith(function (a, b) {
            return {
                constructor: function (a) {
                    a.comparison = c.EQ(a.lvalue, a.rvalue), b.call(this, a)
                }
            }
        });
        return f
    }), define("htmlvn/events/cond/IfGreater", ["jquery", "htmlvn/lib/utils", "htmlvn/Comparisons", "htmlvn/StepMode", "htmlvn/events/ConditionalEvent"], function (a, b, c, d, e) {
        "use strict";
        var f = e.inheritWith(function (a, b) {
            return {
                constructor: function (a) {
                    a.comparison = c.GT(a.lvalue, a.rvalue), b.call(this, a)
                }
            }
        });
        return f
    }), define("htmlvn/events/cond/IfGTE", ["jquery", "htmlvn/lib/utils", "htmlvn/Comparisons", "htmlvn/StepMode", "htmlvn/events/ConditionalEvent"], function (a, b, c, d, e) {
        "use strict";
        var f = e.inheritWith(function (a, b) {
            return {
                constructor: function (a) {
                    a.comparison = c.GTE(a.lvalue, a.rvalue), b.call(this, a)
                }
            }
        });
        return f
    }), define("htmlvn/events/cond/IfLess", ["jquery", "htmlvn/lib/utils", "htmlvn/Comparisons", "htmlvn/StepMode", "htmlvn/events/ConditionalEvent"], function (a, b, c, d, e) {
        "use strict";
        var f = e.inheritWith(function (a, b) {
            return {
                constructor: function (a) {
                    a.comparison = c.LT(a.lvalue, a.rvalue), b.call(this, a)
                }
            }
        });
        return f
    }), define("htmlvn/events/cond/IfLTE", ["jquery", "htmlvn/lib/utils", "htmlvn/Comparisons", "htmlvn/StepMode", "htmlvn/events/ConditionalEvent"], function (a, b, c, d, e) {
        "use strict";
        var f = e.inheritWith(function (a, b) {
            return {
                constructor: function (a) {
                    a.comparison = c.LTE(a.lvalue, a.rvalue), b.call(this, a)
                }
            }
        });
        return f
    }), define("htmlvn/events/cond/IfTrue", ["jquery", "htmlvn/lib/utils", "htmlvn/Comparisons", "htmlvn/StepMode", "htmlvn/events/ConditionalEvent"], function (a, b, c, d, e) {
        "use strict";
        var f = e.inheritWith(function (a, b) {
            return {
                constructor: function (a) {
                    a.comparison = c.True(a.value), b.call(this, a)
                }
            }
        });
        return f
    }), define("htmlvn/events/cond/IfFalse", ["jquery", "htmlvn/lib/utils", "htmlvn/Comparisons", "htmlvn/StepMode", "htmlvn/events/ConditionalEvent"], function (a, b, c, d, e) {
        "use strict";
        var f = e.inheritWith(function (a, b) {
            return {
                constructor: function (a) {
                    a.comparison = c.False(a.value), b.call(this, a)
                }
            }
        });
        return f
    }), define("htmlvn/events/drivers/dom/DOMImageCreate", ["htmlvn/lib/utils", "htmlvn/events/drivers/dom/DOMImageEvent"], function (a, b) {
        "use strict";
        var c = b.inheritWith(function (b, c) {
            return {
                constructor: function (b, d, e, f, g, h) {
                    if (!$.isPlainObject(b)) {
                        var i = {
                            imageId: b,
                            imageType: d,
                            style: e,
                            transitions: f,
                            transitionDuration: g,
                            transitionEase: h
                        };
                        b = i
                    }
                    var j = a.pickInAndSet;
                    j(this, "__actorId", b, ["imageId", "actorId", "id"]), j(this, "__actorType", b, ["imageType", "actorType", "type"]), "target" in b || (b.target = this.__actorId), c.call(this, b)
                },
                eventWarm: function () {
                    $("#game").append($("<div></div>").attr("id", this.__actorId).addClass("actor " + this.__actorType)), b.eventWarm.apply(this, arguments)
                },
                finalize: function () {
                    b.finalize.call(this)
                }
            }
        });
        return c
    }), define("htmlvn/events/drivers/dom/DOMImageDestroy", ["htmlvn/events/drivers/dom/DOMImageEvent"], function (a) {
        "use strict";
        var b = a.inheritWith(function (a, b) {
            return {
                constructor: function () {
                    b.apply(this, arguments)
                },
                pump: function () {
                    $(this._target).remove()
                }
            }
        });
        return b
    }), define("htmlvn/events/drivers/dom/DOMImageDestroyAll", ["htmlvn/events/drivers/dom/DOMImageDestroy"], function (a) {
        "use strict";
        var b = a.inheritWith(function (a, b) {
            return {
                constructor: function (a) {
                    a || (a = {}), a.target = "*", b.call(this, a)
                }
            }
        });
        return b
    }), define("htmlvn/events/drivers/dom/DOMCrossfadeEvent", ["htmlvn/lib/utils", "htmlvn/events/drivers/dom/DOMImageEvent"], function (a, b) {
        "use strict";
        var c = b.inheritWith(function (b, c) {
            return {
                constructor: function (b) {
                    var d = a.pickIn(b, ["img", "image"]);
                    delete b.image, delete b.img, b.style = {
                        image: d
                    }, this.__opacity = a.pickIn(b, ["opacity"], 0), c.call(this, b)
                },
                eventWarm: function () {
                    b.eventWarm.call(this), this.__crossfadeDone = false
                },
                isComplete: function () {
                    return this.__crossfadeDone
                },
                interrupt: function () {
                    var a = !this.__crossfadeDone;
                    return a && this._stopTransitions(), a
                },
                pump: function () {
                    var a = $(this._target),
                        b = $("#backstage"),
                        c = this._resolveImage(this._style.image),
                        d = this._currentlyActive = a.find(".image.live"),
                        e = this._nextUp = b.find('.image[data-src="' + c + '"]'),
                        f = 1e3 * this._duration;
                    d.transit({
                        opacity: this.__opacity
                    }, f, this._ease), e.addClass("live").removeClass("waiting").css("opacity", 0), a.append(e), e.transit({
                        opacity: 1
                    }, f, this._ease, this.__transitionCallback.bind(this)), b = e = a = d = null
                },
                _stopTransitions: function () {
                    console.log("Ostensibly stopping crossfade animation!"), this.__crossfadeDone = true, $(this._nextUp).stopTransit(true, true), $(this._currentlyActive).stopTransit(true, true).removeClass("live").addClass("dead"), this.__crossfadeDone = true
                },
                __transitionCallback: function () {
                    this.__crossfadeDone || ($(this._currentlyActive).removeClass("live").addClass("dead"), this.__crossfadeDone = true, this._signalComplete())
                }
            }
        });
        return c
    }), define("htmlvn/events/shortcuts/ActorSwapMacro", ["jquery", "htmlvn/lib/utils", "htmlvn/events/drivers/dom/DOMImageEvent", "htmlvn/events/DiscreteEvent", "htmlvn/events/Macro", "htmlvn/events/FadeEvent"], function (a, b, c, d, e, f) {
        "use strict";
        var g = e.inheritWith(function (a, e) {
            return {
                constructor: function (a) {
                    a = a || {};
                    var g = b.getAndDelete(a, "target"),
                        h = b.getAndDelete(a, "newId"),
                        i = b.getAndDelete(a, "image"),
                        j = b.getAndDelete(a, "fadeDuration") || .25,
                        k = b.getAndDelete(a, "text"),
                        l = b.getAndDelete(a, "char") || "",
                        m = [new f({
                            target: g,
                            to: 0,
                            duration: j,
                            auto: true
                        }), new c({
                            target: g,
                            style: {
                                image: i,
                                id: h
                            },
                            auto: true
                        })],
                        n = [new f({
                            target: h,
                            to: 1,
                            duration: j
                        })];
                    k && n.append(new TextEvent({
                        text: k,
                        "char": l
                    })), m.append(new d({
                        events: n
                    })), a.events = m, e.call(this, a)
                }
            }
        });
        return g
    }), define("htmlvn/events/shortcuts/ActorFade", ["jquery", "htmlvn/lib/utils", "htmlvn/events/drivers/dom/DOMImageEvent"], function (a, b, c) {
        "use strict";
        var d = c.inheritWith(function (a, c) {
            return {
                constructor: function (a) {
                    var d = {};
                    b.pickInAndSet(d, "opacity", a, ["opacity"]), delete a.opacity, a.transitions = d, c.call(this, a)
                }
            }
        });
        return d
    }), define("htmlvn/events/shortcuts/BranchMacro", ["jquery", "htmlvn/lib/utils", "htmlvn/events/JumpEvent", "htmlvn/events/ConditionalEvent", "htmlvn/events/Macro"], function (a, b, c, d) {
        "use strict";
        var e = d.inheritWith(function (a, b) {
            return {
                constructor: function (a) {
                    a.events = [new c({
                        path: a.path
                    })], delete a.path, b.call(this, a)
                }
            }
        });
        return e
    }), define("htmlvn/events/shortcuts/ResetShortcut", ["jquery", "htmlvn/lib/utils", "htmlvn/events/drivers/dom/DOMImageEvent"], function (a, b, c) {
        "use strict";
        var d = c.inheritWith(function (a, b) {
            return {
                constructor: function (a) {
                    a = a || {}, a.style = {
                        depth: 0,
                        x: "0%",
                        y: "0%",
                        scaleX: 1,
                        scaleY: 1,
                        opacity: 1,
                        image: ""
                    }, "id" in a && (a.style.id = a.id, delete a.id), b.call(this, a)
                }
            }
        });
        return d
    }), define("htmlvn/events/shortcuts/RenameShortcut", ["jquery", "htmlvn/lib/utils", "htmlvn/events/drivers/dom/DOMImageEvent"], function (a, b, c) {
        "use strict";
        var d = c.inheritWith(function (a, b) {
            return {
                constructor: function (a) {
                    a.style = {
                        id: a.id
                    }, delete a.id, b.call(this, a)
                }
            }
        });
        return d
    }), define("htmlvn/events/shortcuts/DepthShortcut", ["jquery", "htmlvn/lib/utils", "htmlvn/events/drivers/dom/DOMImageEvent"], function (a, b, c) {
        "use strict";
        var d = c.inheritWith(function (a, b) {
            return {
                constructor: function (a) {
                    a.style = {
                        depth: a.depth
                    }, delete a.depth, b.call(this, a)
                }
            }
        });
        return d
    }), define("htmlvn/events/shortcuts/ImageShortcut", ["jquery", "htmlvn/lib/utils", "htmlvn/events/drivers/dom/DOMImageEvent"], function (a, b, c) {
        "use strict";
        var d = c.inheritWith(function (a, b) {
            return {
                constructor: function (a) {
                    a.style = {
                        image: a.image
                    }, delete a.image, b.call(this, a)
                }
            }
        });
        return d
    }), define("htmlvn/events/shortcuts/MoveShortcut", ["jquery", "htmlvn/lib/utils", "htmlvn/events/drivers/dom/DOMImageEvent"], function (a, b, c) {
        "use strict";
        var d = c.inheritWith(function (a, c) {
            return {
                constructor: function (a) {
                    var d = {};
                    b.pickInAndSet(d, "x", a, ["x"]), delete a.x, b.pickInAndSet(d, "y", a, ["y"]), delete a.y, a.transitions = d, c.call(this, a)
                }
            }
        });
        return d
    }), define("htmlvn/events/shortcuts/ScaleShortcut", ["jquery", "htmlvn/lib/utils", "htmlvn/events/drivers/dom/DOMImageEvent"], function (a, b, c) {
        "use strict";
        var d = c.inheritWith(function (a, c) {
            return {
                constructor: function (a) {
                    var d = {};
                    b.pickInAndSet(d, "scaleX", a, ["x"]), delete a.x, b.pickInAndSet(d, "scaleY", a, ["y"]), delete a.y, a.transitions = d, c.call(this, a)
                }
            }
        });
        return d
    }), define("htmlvn/events/shortcuts/FlipShortcut", ["jquery", "htmlvn/lib/utils", "htmlvn/events/drivers/dom/DOMImageEvent"], function (a, b, c) {
        "use strict";
        var d = c.inheritWith(function (b, c) {
            return {
                constructor: function (a) {
                    this.__intendedDuration = a.duration || 0, a.transitions = {
                        scaleX: 1
                    }, c.call(this, a)
                },
                pump: function (c) {
                    var d = a(this._target).css("scaleX"),
                        e = -1 * d,
                        f = {
                            scaleX: e
                        };
                    "scaleX" in this._transitions ? (a(this._target).css("scaleX", d), this._transitions = f) : this._style = f, b.pump.call(this, c)
                }
            }
        });
        return d
    }), define("htmlvn/events/shortcuts/TransformShortcut", ["jquery", "htmlvn/lib/utils", "htmlvn/events/drivers/dom/DOMImageEvent"], function (a, b, c) {
        "use strict";
        var d = c.inheritWith(function (a, c) {
            return {
                constructor: function (a) {
                    var d = {};
                    b.pickInAndSet(d, "x", a, ["x"]), delete a.x, b.pickInAndSet(d, "y", a, ["y"]), delete a.y, b.pickInAndSet(d, "scaleX", a, ["scaleX"]), delete a.scaleX, b.pickInAndSet(d, "scaleY", a, ["scaleY"]), delete a.scaleY, a.transitions = d, c.call(this, a)
                }
            }
        });
        return d
    }), define("htmlvn/events/shortcuts/YesNoChoice", ["jquery", "htmlvn/lib/utils", "htmlvn/events/ChoiceEvent"], function (a, b, c) {
        "use strict";
        var d = c.inheritWith(function (a, b) {
            return {
                __yesText: "@t_ui_yes",
                __noText: "@t_ui_no",
                __yesValue: true,
                __noValue: false,
                constructor: function (a) {
                    "yesText" in a && (this.__yesText = a.yesText), "noText" in a && (this.__noText = a.noText), "yesValue" in a && (this.__yesValue = a.yesValue), "noValue" in a && (this.__noValue = a.noValue), a.choices = [{
                        text: this.__yesText,
                        value: this.__yesValue
                    }, {
                        text: this.__noText,
                        value: this.__noValue
                    }], b.call(this, a)
                },
                _getYesText: function () {
                    return this.__yesText
                },
                _getNoText: function () {
                    return this.__noText
                },
                _getYesValue: function () {
                    return this.__yesValue
                },
                _getNoValue: function () {
                    return this.__noValue
                }
            }
        });
        return d
    }), define("htmlvn/audio/AudioAdapter", ["htmlvn/lib/Class"], function (a) {
        "use strict";
        var b = a.inheritWith(function () {
            return {
                __defaultChannel: "self",
                __layerName: "",
                constructor: function (a, b) {
                    2 === arguments.length || (1 === arguments.length ? "boolean" == typeof a ? (b = a, a = 1) : b = false : 0 === arguments.length && (a = 1, b = false)), this.__volumes = {}, this.__loop = b, this._applyLoop(b), this.setVolume(this.__defaultChannel, 1)
                },
                close: function () {},
                setSource: function (a) {
                    "string" == typeof a ? this._setSrc(a) : this._setAsset(a)
                },
                play: function (a) {
                    a && this.setSource(a)
                },
                pause: function () {
                    throw new Error("no default implementation for AudioAdapter#pause!")
                },
                stop: function () {
                    throw new Error("no default implementation for AudioAdapter#stop!")
                },
                isPlaying: function () {
                    throw new Error("no default implementation for AudioAdapter#isPlaying!")
                },
                getLoop: function () {
                    return this.__loop
                },
                setLoop: function (a) {
                    a != this.__loop && (this.__loop = a, this._applyLoop(a))
                },
                getLayerName: function () {
                    return this.__layerName
                },
                setLayerName: function (a) {
                    this.__layerName = a
                },
                getVolume: function (a) {
                    return a || (a = this.__defaultChannel), this.__volumes[a]
                },
                getFinalVolume: function () {
                    var a = 1;
                    for (var b in this.__volumes) a *= this.__volumes[b];
                    return a
                },
                setVolume: function (a, b) {
                    if (1 === arguments.length) {
                        var c = typeof a;
                        if ("object" === c) return this.__parseVolObj(a), void 0;
                        "number" === c && (b = a, a = this.__defaultChannel)
                    }
                    a || (a = this.__defaultChannel), this.__volumes[a] = b, this.__doVolApply()
                },
                _applyLoop: function () {
                    throw new Error("AudioAdapter#_applyLoop needs a subclass implementation!")
                },
                _applyVolume: function () {
                    throw new Error("AudioAdapter#_applyVolume needs a subclass implementation!")
                },
                _setAsset: function () {},
                _setSrc: function () {},
                __doVolApply: function () {
                    this._applyVolume(this.getFinalVolume())
                },
                __parseVolObj: function (a) {
                    for (var b in a) this.__volumes[b] = a[b];
                    this.__doVolApply()
                }
            }
        });
        return b
    }), define("htmlvn/audio/ElementAdapter", ["jquery", "htmlvn/audio/AudioAdapter"], function (a, b) {
        "use strict";
        var c = b.inheritWith(function (b, c) {
            return {
                __elReady: false,
                constructor: function () {
                    c.apply(this, arguments)
                },
                close: function () {
                    this.pause(), a(this.__el).off().remove(), this.__elReady = false, delete this.__ended, delete this.__canPlay, this.__el = null, b.close.call(this)
                },
                play: function () {
                    if (b.play.apply(this, arguments), this.__playing = true, this.__el) try {
                        this.__el.play()
                    } catch (a) {
                        console.error("Got bad result from this.__el.play: "), console.error(a)
                    }
                },
                pause: function () {
                    if (this.__playing) {
                        if (this.__el) try {
                            this.__el.pause()
                        } catch (a) {
                            console.error("Got bad result from this.__el.pause: "), console.error(a)
                        }
                        this.__playing = false
                    }
                },
                stop: function () {
                    this.__playing && (this.pause(), this.__el.currentTime = 0)
                },
                isPlaying: function () {
                    return this.__playing
                },
                _setAsset: function (a) {
                    var b = a.getLoadedElement();
                    if (!b) throw new Error("Whoops, template element not found for " + a.getPath());
                    var c = b.cloneNode();
                    this._setEl(c)
                },
                _setEl: function (b) {
                    this.__el && this.close(), this.__ended = this.__ended.bind(this), this.__canPlay = this.__canPlay.bind(this), this.__el = b, a(b).on("ended", this.__ended).on("canplaythrough", this.__canPlay), this._applyLoop(this.getLoop()), this._applyVolume(this.getFinalVolume())
                },
                _setSrc: function () {
                    throw new Error("ElementAdapter__playSrc not really implemented yet!")
                },
                _applyLoop: function (a) {
                    this.__el && (this.__el.loop = a)
                },
                _applyVolume: function (a) {
                    this.__el && (this.__el.volume = a)
                },
                __ended: function () {
                    this.__playing = false
                },
                __canPlay: function () {
                    this.__elReady = true
                }
            }
        });
        return c
    }), define("htmlvn/audio/AudioAdapterFactory", ["htmlvn/lib/Class", "htmlvn/audio/AudioAdapter", "htmlvn/audio/ElementAdapter"], function (a, b, c) {
        "use strict";
        var d = {
            getAdapter: function () {
                return new c
            }
        };
        return d
    }), define("htmlvn/audio/AudioLayer", ["jquery", "htmlvn/lib/utils", "htmlvn/lib/Class", "htmlvn/DataStore"], function (a, b, c, d) {
        "use strict";
        var e = c.inheritWith(function () {
            return {
                constructor: function (a) {
                    this.__list = [], this.__name = a, this.__volumes = {}, this.__volumes.layer = 1, this.__volumes.layerUser = d.getVolume(a)
                },
                getVolume: function () {
                    return this.__volumes.layer
                },
                setVolume: function (a) {
                    a != this.__volumes.layer && (this.__volumes.layer = a, this.__applyVolume())
                },
                getUserVolume: function () {
                    return this.__volumes.layerUser
                },
                setUserVolume: function (a) {
                    a != this.__volumes.layerUser && (this.__volumes.layerUser = a, this.__applyVolume())
                },
                getName: function () {
                    return this.__name
                },
                add: function (a) {
                    a.setLayerName(this.__name), this.__list.push(a), this.__applyVolumeToEl(a)
                },
                remove: function (a) {
                    var b = this.__list.indexOf(a),
                        c = 1 != b;
                    return c && this.__list.splice(b, 1), c
                },
                __applyVolume: function () {
                    for (var a = this.__list, b = 0; b < a.length; ++b) this.__applyVolumeToEl(a[b])
                },
                __applyVolumeToEl: function (a) {
                    a.setVolume(this.__volumes)
                }
            }
        });
        return e
    }), define("htmlvn/audio/AudioPool", ["htmlvn/lib/utils", "htmlvn/DataStore", "htmlvn/assets/Asset", "htmlvn/assets/AudioAsset", "htmlvn/assets/AudioCodec", "htmlvn/audio/AudioAdapterFactory", "htmlvn/audio/AudioLayer"], function (a, b, c, d, e, f, g) {
        "use strict";

        function h(a) {
            return a in l || (l[a] = new g(a)), l[a]
        }

        function i() {
            var a = null;
            return a = m.length > 0 ? m.pop() : f.getAdapter()
        }
        var j = {}, k = {}, l = {}, m = [],
            n = {
                registerAudio: function (a, b, c) {
                    if (a in j) {
                        if (c) throw new Error("Cannot add audio into pool with id twice: " + a);
                        this.removeAudio(a)
                    }
                    var d = i(),
                        e = h(b);
                    return e.add(d), k[a] = b, j[a] = d, d
                },
                removeAudio: function (a) {
                    var b = this.getAudioAdapter(a);
                    return b && (h(k[a]).remove(b), delete k[a], delete j[a], b.close()), !! b
                },
                removeAll: function () {
                    var a, b = Object.keys(j);
                    for (a = 0; a < b.length; ++a) this.removeAudio(b[a]);
                    return a
                },
                getAudioAdapter: function (a) {
                    var b = null;
                    return a in j && (b = j[a]), b
                },
                retainPooledAdapter: function (a) {
                    var b = h(a),
                        c = i();
                    return b.add(c), c
                },
                releasePooledAdapter: function (a) {
                    var b = h(a.getLayerName());
                    b.remove(a), a.close()
                },
                getLayerVolume: function (a) {
                    return h(a).getVolume()
                },
                setLayerVolume: function (b, c, d) {
                    var e = h(b);
                    d = a.pick(d, 0), d > 0 || e.setVolume(c)
                },
                getLayerUserVolume: function (a) {
                    return h(a).getUserVolume()
                },
                setLayerUserVolme: function (a, b) {
                    h(a).setUserVolume(b)
                },
                hasLayer: function (a) {
                    return a in l
                }
            };
        return n
    }), define("htmlvn/events/audio/AudioEvent", ["jquery", "htmlvn/lib/utils", "htmlvn/assets/Asset", "htmlvn/assets/AudioAsset", "htmlvn/assets/AudioCodec", "htmlvn/audio/AudioPool", "htmlvn/events/DiscreteEvent"], function (a, b, c, d, e, f, g) {
        "use strict";

        function h(a) {
            var b = null;
            return a instanceof d ? b = a : "string" == typeof a && (b = c.tryResolve(a, false)), b
        }
        var i = g.inheritWith(function (c, d) {
            return {
                _layer: "sfx",
                _ease: "linear",
                _target: null,
                _loop: null,
                _volume: null,
                _sound: null,
                _play: false,
                _stop: false,
                _fadeDuration: 0,
                _animDone: false,
                constructor: function (a) {
                    d.apply(this, arguments), b.pickInAndSet(this, "_layer", a, ["layer", "bus"]), b.pickInAndSet(this, "_target", a, ["audioId", "target"]), b.pickInAndSet(this, "_sound", a, ["audio", "sound", "snd"]), b.pickInAndSet(this, "_volume", a, ["vol", "volume"]), b.pickInAndSet(this, "_ease", a, ["ease"]), b.pickInAndSet(this, "_loop", a, ["loop"]), b.pickInAndSet(this, "_fadeDuration", a, ["fadeDuration", "duration"]), b.pickInAndSet(this, "_play", a, ["play"]), b.pickInAndSet(this, "_stop", a, ["stop"])
                },
                collectAssets: function () {
                    return this._sound ? [this._sound] : []
                },
                eventWarm: function () {
                    c.eventWarm.apply(this, arguments), this._animDone = false
                },
                sceneWarm: function () {
                    if (this._sound) {
                        var a = this._resolveAudio(this._sound);
                        a && (this.__el = a.getLoadedElement().cloneNode())
                    }
                },
                destroy: function () {
                    c.destroy.apply(this, arguments), this.__el && (a(this.__el).off().remove(), this.__el = null)
                },
                interrupt: function () {
                    return this.isComplete() ? false : (console.log("Canceling audio animation!"), this.__interrupting = true, this.__completeAnim(), this.__interrupting = false, true)
                },
                isComplete: function () {
                    return this._fadeDuration <= 0 || this._animDone
                },
                pump: function (a) {
                    var b = this._getAdapter();
                    if (b) {
                        if (this.__el) try {
                            b._setEl(this.__el)
                        } catch (c) {}
                        null !== this._loop && b.setLoop(this._getLoop()), null !== this._volume && (this._fadeDuration > 0 && a ? this._startFade() : (this._animDone = true, b.setVolume(this._volume))), this._play && b.play(), this._stop && b.stop()
                    } else this._animDone = true
                },
                update: function (a) {
                    if (void 0 !== this._fadeTimer)
                        if (this._fadeTimer += a, this._fadeTimer >= this._fadeDuration) this.__completeAnim();
                        else {
                            var b = this._getAdapter(),
                                c = this._fadeTimer / this._fadeDuration,
                                d = this._startingVolume + c * this._volumeDelta;
                            b.setVolume(d)
                        }
                },
                _getLoop: function () {
                    return this._loop
                },
                _getVolume: function () {
                    return this._volume
                },
                _getTarget: function () {
                    return this._target
                },
                _getLayer: function () {
                    return this._layer
                },
                _getAdapter: function () {
                    return this._target ? f.getAudioAdapter(this._target) : null
                },
                _resolveAudio: function (a) {
                    return a = b.pick(a, this._sound), h(a)
                },
                _startFade: function () {
                    var a = this._getAdapter();
                    return a ? (this._fadeTimer = 0, this._startingVolume = a.getVolume(), this._volumeDelta = this._volume - this._startingVolume, void 0) : (this._animDone = true, void 0)
                },
                __completeAnim: function () {
                    var a = this._getAdapter();
                    a.setVolume(this._volume), this._animDone = true, delete this._fadeTimer, this.__interrupting || this._signalComplete()
                }
            }
        }).defineStatic({
            resolveAudio: h
        });
        return i
    }), define("htmlvn/events/audio/AudioCreate", ["htmlvn/lib/utils", "htmlvn/events/audio/AudioEvent", "htmlvn/audio/AudioPool"], function (a, b, c) {
        "use strict";
        var d = b.inheritWith(function (a, b) {
            return {
                constructor: function (a) {
                    "loop" in a || (a.loop = false), b.apply(this, arguments)
                },
                pump: function () {
                    c.registerAudio(this._getTarget(), this._getLayer()), a.pump.apply(this, arguments)
                }
            }
        });
        return d
    }), define("htmlvn/events/audio/AudioDestroy", ["htmlvn/lib/utils", "htmlvn/events/audio/AudioEvent", "htmlvn/audio/AudioPool"], function (a, b, c) {
        "use strict";
        var d = b.inheritWith(function (a, b) {
            return {
                constructor: function () {
                    b.apply(this, arguments)
                },
                collectAssets: function () {
                    return []
                },
                pump: function () {
                    var a = this._getTarget();
                    a && c.removeAudio(a)
                }
            }
        });
        return d
    }), define("htmlvn/events/audio/AudioDestroyAll", ["htmlvn/lib/utils", "htmlvn/events/DiscreteEvent", "htmlvn/audio/AudioPool"], function (a, b, c) {
        "use strict";
        var d = b.inheritWith(function (a, b) {
            return {
                constructor: function () {
                    b.apply(this, arguments)
                },
                pump: function () {
                    c.removeAll()
                }
            }
        });
        return d
    }), define("htmlvn/events/audio/AudioLoopStart", ["jquery", "htmlvn/lib/utils", "htmlvn/events/audio/AudioEvent", "htmlvn/audio/AudioPool"], function (a, b, c) {
        "use strict";
        var d = c.inheritWith(function (b, c) {
            return {
                constructor: function (b) {
                    c.call(this, a.extend({}, b, {
                        loop: true,
                        play: true
                    }))
                }
            }
        });
        return d
    }), define("htmlvn/events/audio/AudioLoopStop", ["jquery", "htmlvn/lib/utils", "htmlvn/events/audio/AudioEvent", "htmlvn/audio/AudioPool"], function (a, b, c) {
        "use strict";
        var d = c.inheritWith(function (b, c) {
            return {
                constructor: function (b) {
                    c.call(this, a.extend({}, b, {
                        stop: true
                    }))
                }
            }
        });
        return d
    }), define("htmlvn/events/audio/AudioOneShot", ["htmlvn/StepMode", "htmlvn/lib/utils", "htmlvn/events/audio/AudioEvent", "htmlvn/audio/AudioPool"], function (a, b, c, d) {
        "use strict";
        var e = c.inheritWith(function (b, c) {
            return {
                __adapter: null,
                __signaled: false,
                constructor: function (a) {
                    delete a.target, delete a.audioId, delete a.fadeDuration, delete a.duration, "loop" in a || (a.loop = false), a.play = true, c.call(this, a)
                },
                eventWarm: function () {
                    b.eventWarm.apply(this, arguments), this.__cleanup()
                },
                update: function () {
                    b.update.apply(this, arguments), !this.__signaled && this.__adapter && (this.__adapter.isPlaying() || (this._signalComplete(), this.__signaled = true))
                },
                finalize: function () {
                    b.finalize.apply(this, arguments), this.__cleanup()
                },
                interrupt: function () {
                    var a = this.__adapter && this.__adapter.isPlaying();
                    return a && (this.__adapter.pause(), this.__signaled = true), a
                },
                pump: function (a) {
                    a && b.pump.apply(this, arguments)
                },
                isComplete: function () {
                    return this.__signaled || !this.__adapter || !this.__adapter.isPlaying()
                },
                shouldSkip: function (b) {
                    return b > a.Normal
                },
                _getAdapter: function () {
                    return this.__adapter || (this.__adapter = d.retainPooledAdapter(this._getLayer())), this.__adapter
                },
                __cleanup: function () {
                    this.__adapter && (d.releasePooledAdapter(this.__adapter), this.__adapter = null), this.__signaled = false
                }
            }
        });
        return e
    }), define("htmlvn/events/drivers/dom/DOMPlayer", ["jquery", "htmlvn/BasePlayer", "htmlvn/menu/MainMenu", "htmlvn/menu/LoadingScreen", "htmlvn/menu/GameScreen", "htmlvn/menu/YesNoPrompt", "htmlvn/events/ConsoleEvent", "htmlvn/events/JumpEvent", "htmlvn/events/ChoiceEvent", "htmlvn/events/DelayEvent", "htmlvn/events/DiscreteEvent", "htmlvn/events/ConditionalEvent", "htmlvn/events/FadeEvent", "htmlvn/events/SceneChangeEvent", "htmlvn/events/Macro", "htmlvn/events/vars/VarDelEvent", "htmlvn/events/vars/VarSetEvent", "htmlvn/events/vars/VarIncEvent", "htmlvn/events/vars/VarEnsure", "htmlvn/events/cond/IfEqual", "htmlvn/events/cond/IfGreater", "htmlvn/events/cond/IfGTE", "htmlvn/events/cond/IfLess", "htmlvn/events/cond/IfLTE", "htmlvn/events/cond/IfTrue", "htmlvn/events/cond/IfFalse", "htmlvn/events/drivers/dom/DOMImageCreate", "htmlvn/events/drivers/dom/DOMImageDestroy", "htmlvn/events/drivers/dom/DOMImageDestroyAll", "htmlvn/events/drivers/dom/DOMImageEvent", "htmlvn/events/drivers/dom/DOMTextEvent", "htmlvn/events/drivers/dom/DOMCrossfadeEvent", "htmlvn/events/shortcuts/ActorSwapMacro", "htmlvn/events/shortcuts/ActorFade", "htmlvn/events/shortcuts/BranchMacro", "htmlvn/events/shortcuts/ResetShortcut", "htmlvn/events/shortcuts/RenameShortcut", "htmlvn/events/shortcuts/DepthShortcut", "htmlvn/events/shortcuts/ImageShortcut", "htmlvn/events/shortcuts/MoveShortcut", "htmlvn/events/shortcuts/ScaleShortcut", "htmlvn/events/shortcuts/FlipShortcut", "htmlvn/events/shortcuts/TransformShortcut", "htmlvn/events/shortcuts/YesNoChoice", "htmlvn/events/audio/AudioEvent", "htmlvn/events/audio/AudioCreate", "htmlvn/events/audio/AudioDestroy", "htmlvn/events/audio/AudioDestroyAll", "htmlvn/events/audio/AudioLoopStart", "htmlvn/events/audio/AudioLoopStop", "htmlvn/events/audio/AudioOneShot", "jquery.transit"], function (a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y) {
        "use strict";
        var Z = {
            DelayEvent: j,
            ParallelEvent: k,
            FadeEvent: m,
            SceneChange: n,
            VarDel: p,
            VarSet: q,
            VarInc: r,
            VarEnsure: s,
            IfEqual: t,
            IfGreater: u,
            IfGTE: v,
            IfLess: w,
            IfLTE: x,
            IfTrue: y,
            IfFalse: z,
            BranchMacro: I,
            JumpEvent: h,
            ConsoleEvent: g,
            ChoiceEvent: i,
            YesNoChoice: R,
            ConditionalEvent: l,
            ActorCreate: A,
            ActorDestroy: B,
            ActorDestroyAll: C,
            ActorEvent: D,
            ActorCrossfade: F,
            ActorFade: H,
            ActorSwap: G,
            ActorReset: J,
            ActorDepth: L,
            ActorFlip: P,
            ActorImage: M,
            ActorMove: N,
            ActorScale: O,
            ActorTransform: Q,
            ActorRename: K,
            AudioEvent: S,
            AudioCreate: T,
            AudioDestroy: U,
            AudioDestroyAll: V,
            AudioLoopStart: W,
            AudioStop: X,
            AudioOneShot: Y,
            TextEvent: E,
            Macro: o
        }, $ = {
                main: c,
                loading: d,
                game: e,
                yesno: f
            }, _ = !! navigator.userAgent.match(/Trident/),
            ab = b.inheritWith(function (b, c) {
                return {
                    constructor: function (b, d, e, f, g) {
                        var h = a.extend({}, $, d),
                            i = a.extend({}, Z, e),
                            j = a.extend({}, f),
                            k = this.__gameWidth = b.getOption("canvasWidth"),
                            l = this.__gameHeight = b.getOption("canvasHeight");
                        this.__xaspect = l / k, this.__yaspect = k / l;
                        var m = this.__resize = this.__resize.bind(this);
                        a(window).resize(m), a(window).ready(m), c.call(this, b, h, i, j, g)
                    },
                    resetStage: function () {
                        b.resetStage.call(this), a("#textArea").html(this.__textAreaInitial), a("#game").html(this.__gameInitial)
                    },
                    _ready: function () {
                        a("html").addClass("domDriver"), _ && (this.__initialPadding = a("#textContent").css("padding-right"), console.log("initial textContent padding:" + this.__initialPadding)), this.__textAreaInitial = a("#textArea").html(), this.__gameInitial = a("#game").html(), b._ready.apply(this, arguments)
                    },
                    _update: function () {
                        b._update.apply(this, arguments), this.__paddingDirty && (a("#textContent").css("padding-right", "45px"), this.__paddingDirty = false)
                    },
                    __resize: function () {
                        var b = a(window).width(),
                            c = a(window).height(),
                            d = b,
                            e = d * this.__xaspect,
                            f = d / this.__gameWidth;
                        e > c && (e = c, d = e * this.__yaspect, f = e / this.__gameHeight), a("#container").css({
                            width: Math.floor(d),
                            height: Math.floor(e)
                        });
                        var g = E.getLastAnimated();
                        if (g) g.scrollIntoView(false);
                        else {
                            var h = a("#textContent").children().last();
                            h.length > 0 && h[0].scrollIntoView(false)
                        }
                        _ && (this.__paddingDirty = true, a("#textContent").css("padding-right", "0"))
                    }
                }
            });
        return ab
    }), define("namcohigh/charlist", [], function () {
        "use strict";

        function a(a) {
            return m[a]
        }

        function b() {
            if (0 === n.length)
                for (var a in m) n.push(m[a]);
            return n
        }

        function c(a, b) {
            return "s_" + l[a] + b
        }

        function d(a) {
            return k[a]
        }

        function e(a) {
            return l[a]
        }

        function f(a) {
            return "pick_count_" + l[a]
        }

        function g(a) {
            return "${slot:" + f(a) + "}"
        }

        function h(a) {
            return j[a]
        }
        var i = ["amazona", "albatross", "antibravo", "bluemax", "davesprite", "donko", "galaga", "hiromi", "jane", "lolo", "meowkie", "mrdriller", "nidia", "richard", "taira", "terezi", "tomari", "valkyrie"],
            j = {
                "Aki Matsuo": "amazona",
                Albatross: "albatros",
                "Anti-Bravoman": "antibravo",
                "Blue Max": "bluemax",
                Davesprite: "davesprite",
                Donko: "donko",
                Galaga: "galaga",
                Hiromi: "hiromi",
                "Kame Crocker": "jane",
                "Jane Crocker": "jane",
                Lolo: "lolo",
                Meowkie: "meowkie",
                "Mr. Driller": "mrdriller",
                Nidia: "nidia",
                "Richard Miller": "richard",
                Taira: "taira",
                "Terezi Pyrope": "terezi",
                Tomari: "tomari",
                Valkyrie: "valk"
            }, k = {
                amazona: "@t_ch_aki",
                albatross: "@t_ch_albatros",
                antibravo: "@t_ch_antibravo",
                bluemax: "@t_ch_max",
                davesprite: "@t_ch_davesprite",
                donko: "@t_ch_donko",
                galaga: "@t_ch_galaga",
                hiromi: "@t_ch_hiromi",
                jane: "@t_ch_jane",
                lolo: "@t_ch_lolo",
                meowkie: "@t_ch_meowkie",
                mrdriller: "@t_ch_mrdriller",
                nidia: "@t_ch_nidia",
                richard: "@t_ch_richard",
                taira: "@t_ch_taira",
                terezi: "@t_ch_terezi",
                tomari: "@t_ch_tomari",
                valkyrie: "@t_ch_valkyrie"
            }, l = {
                amazona: "amazona",
                albatross: "albatros",
                antibravo: "antibravo",
                bluemax: "bluemax",
                davesprite: "davesprite",
                donko: "donko",
                galaga: "galaga",
                hiromi: "hiromi",
                jane: "jane",
                lolo: "lolo",
                meowkie: "meowkie",
                mrdriller: "mrdriller",
                nidia: "nidia",
                richard: "richard",
                taira: "taira",
                terezi: "terezi",
                tomari: "tomari",
                valkyrie: "valk",
                cousin: "cousin"
            }, m = {
                amazona: "@i_aki_akimbo_sil",
                albatross: "@i_albatross_welcome_sil",
                antibravo: "@i_abm_backturned_sil",
                bluemax: "@i_bluemax_stand_sil",
                davesprite: "@i_davesprite_standing_sil",
                donko: "@i_donko_akimbo_sil",
                galaga: "@i_galaga_default_sil",
                hiromi: "@i_hiromi_akimbo_sil",
                jane: "@i_jane_default_sil",
                lolo: "@i_lolo_crossed_sil",
                meowkie: "@i_meowkie_normal_sil",
                mrdriller: "@i_mrdriller_slumped_smug_sil",
                nidia: "@i_nidia_akimbo_sil",
                richard: "@i_miller_akimbo_sil",
                taira: "@i_taira_default_sil",
                terezi: "@i_terezi_default_sil",
                tomari: "@i_tomari_pondering_sil",
                valkyrie: "@i_valkyrie_forjustice_sil"
            }, n = [];
        return {
            getSilhouette: a,
            getAllSilhouettes: b,
            getScene: c,
            getRawScene: e,
            getName: d,
            getActor: e,
            ordered: i,
            getPickVar: f,
            getPickVarToken: g,
            names: k,
            scenes: l,
            fromStoreName: h
        }
    }), define("namcohigh/user/UserError", [], function () {
        function a() {
            Error.apply(this, arguments)
        }
        return a.prototype = new Error, a.prototype.constructor = a, a.prototype.name = "UserError", a
    }), define("namcohigh/user/UserLoggedOutError", ["namcohigh/user/UserError"], function (a) {
        function b() {
            a.apply(this, arguments)
        }
        return b.prototype = new a, b.prototype.constructor = b, b.prototype.name = "UserLoggedOutError", b
    }), define("namcohigh/user/UserStore", ["jquery", "Q", "namcohigh/user/UserError", "namcohigh/user/UserLoggedOutError", "htmlvn/lib/utils", "htmlvn/lib/Class", "htmlvn/DataStore", "namcohigh/charlist"], function (a, b, c, d, e, f, g, h) {
        "use strict";
        var i = "", // formerly http://namcohigh.shiftylook.com/
            j = i + "api/saveGame",
            k = i + "api/loadGame.json", // Neither loadGame nor access contain the proper information, only enough to prevent crashing. saveGame doesn't work at all.
            l = i + "api/access.json",   // ...but the game conveniently duplicates the saves in DOM storage along with online, so we don't care.
            m = null,
            n = null,
            o = false,
            p = null,
            q = "XXXnahmanXXX",
            r = "test@datenighto.com",
            s = null,
            t = {}, u = ["amazona", "albatros", "antibravo", "bluemax", "davesprite", "donko", "galaga", "hiromi", "jane", "lolo", "meowkie", "mrdriller", "nidia", "richard", "taira", "terezi", "tomari", "valk", "cousin"], // defines non-paid characters
            v = true,
            w = "UserStore is not initialized!",
            x = function (b) {
                if (!a.isArray(b)) throw new Error;
                var c = 0;
                for (t = {}, c = 0; c < u.length; ++c) {
                    var d = u[c];
                    t[d] = true
                }
                for (c = 0; c < b.length; ++c) {
                    var e = b[c],
                        f = h.fromStoreName(e);
                    t[f] = true
                }
            }, y = {
                init: function (e) {
                    if (o) throw new Error("Already initialized, dog!");
                    return p || (s = e, p = b(a.ajax({
                        url: k,
                        crossDomain: true,
                        dataType: "json",
                        type: "GET",
                        data: {},
                        xhrFields: {
                            withCredentials: true
                        }
                    })).then(function (a) {
                        if ("error" in a) throw new c(a.error);
                        q = a.uid, r = a.email, x(a.characters), g.init(s, q, false), a.data && g.replaceWithIfNewer(a.data)
                    }, function (a) {
                        var b = void 0;
                        if ("object" == typeof a.responseJSON && "error" in a.responseJSON && (b = a.responseJSON.error), 401 === a.status) throw new d(b);
                        throw new c(b)
                    }).then(function () {
                        o = true
                    }).fin(function () {
                        p = null
                    })), p
                },
                isInitialized: function () {
                    return o
                },
                refreshAccess: function () {
                    return n || (n = b(a.ajax({
                        url: l,
                        crossDomain: true,
                        dataType: "json",
                        type: "GET",
                        data: {},
                        xhrFields: {
                            withCredentials: true
                        }
                    })).then(function (a) {
                        console.log("access response: "), console.log(a), x(a.characters)
                    }).fin(function () {
                        n = null
                    })), n
                },
                hasPermission: function () {
                    return true
                },
                characterUnlocked: function (a) {
                    if (!v) return true;
                    if (!o) throw new c(w);
                    return !v || a in t
                },
                pushSaveData: function () {
                    if (!o) throw new c(w);
                    if (m) return m;
                    var d = g.getRemoteObj(false),
                        e = {
                            user: {
                                email: r,
                                data: d
                            }
                        }, f = JSON.stringify(e);
                    return m = b(a.ajax({
                        url: j,
                        dataType: "json",
                        crossDomain: true,
                        contentType: "application/json; charset=utf-8",
                        type: "POST",
                        data: f,
                        xhrFields: {
                            withCredentials: true
                        }
                    })).then(function (a) {}).fin(function () {
                        m = null
                    })
                }
            };
        return y
    }), define("namcohigh/menu/ErrorScreen", ["jquery", "htmlvn/menu/Screen", "htmlvn/assets/Asset", "htmlvn/audio/AudioPool", "htmlvn/DataStore", "htmlvn/Game", "namcohigh/user/UserStore"], function (a, b) {
        "use strict";
        var c = b.inheritWith(function (a, b) {
            return {
                constructor: function (a) {
                    b.call(this, a, "#errorScreen"), this.__refreshClicked = this.__refreshClicked.bind(this)
                },
                _didPresent: function () {
                    a._didPresent.apply(this, arguments), this.on("refresh", this.__refreshClicked)
                },
                _willDismiss: function () {
                    a._willDismiss.apply(this, arguments), this.off("refresh", this.__refreshClicked)
                },
                __refreshClicked: function () {
                    console.warn("error screen is doing it!!!"), window.location.reload()
                }
            }
        });
        return c
    }), define("namcohigh/menu/UpsellScreen", ["jquery", "htmlvn/menu/Screen", "htmlvn/assets/Asset", "htmlvn/audio/AudioPool", "htmlvn/DataStore", "htmlvn/Game", "namcohigh/charlist", "namcohigh/user/UserStore"], function (a, b, c, d, e, f, g) {
        "use strict";
        var h = b.inheritWith(function (b, d) {
            return {
                constructor: function (a) {
                    d.call(this, a, "#upsellPrompt", ["done"])
                },
                configure: function (b) {
                    var d = this.getRoot(),
                        e = d.find(".silhouette img"),
                        f = c.tryResolve(g.getSilhouette(b)),
                        h = f.getLoadedElement();
                    e.attr("src", a(h).attr("src"))
                },
                _willPresent: function (c, d) {
                    b._willPresent.apply(this, arguments), a("#textArea").animate({
                        opacity: 0
                    }, 1e3 * d)
                },
                _didPresent: function () {
                    b._didPresent.apply(this, arguments)
                },
                _willDismiss: function (c, d) {
                    b._willDismiss.apply(this, arguments), a("#textArea").animate({
                        opacity: 1
                    }, 1e3 * d)
                }
            }
        });
        return h
    }), define("namcohigh/menu/LogoSplashScreen", ["jquery", "Q", "htmlvn/menu/Screen", "htmlvn/assets/Asset", "htmlvn/audio/AudioPool", "htmlvn/DataStore", "htmlvn/Game", "namcohigh/user/UserStore"], function (a, b, c, d, e) {
        "use strict";
        var f = null,
            g = "@a_sfx_pacman",
            h = "@i_titlecard_nbgi",
            i = "@i_titlecard_shiftylook_black",
            j = "@i_titlecard_whatpumpkin",
            k = "@i_titlecard_dn",
            l = [g, h, i, j, k],
            m = 1e3,
            n = c.inheritWith(function (c, g) {
                return {
                    constructor: function (b) {
                        var c = this;
                        g.call(this, b, "#logoSplashScreen", ["done"]), a.each(["__loadDone", "__doNBGI", "__doSL", "__doWP", "__doDN", "__done"], function (a, b) {
                            c[b] = c[b].bind(c)
                        })
                    },
                    _willPresent: function () {
                        c._willPresent.apply(this, arguments), this.getRoot(), this.loadPromise = this.__loadAll().then(this.__loadDone())
                    },
                    _didPresent: function () {
                        c._didPresent.apply(this, arguments)
                    },
                    __loadDone: function () {
                        return this.__ready = true, b().delay(m).then(this.__doNBGI).delay(m).then(this.__doWP).delay(m).then(this.__doSL).delay(m).then(this.__doDN).delay(m).then(this.__done)
                    },
                    __doNBGI: function () {
                        var a = this.getRoot();
                        a.find(".logoSplash").css("display", ""), a.find(".nbgi").css("display", "block")
                    },
                    __doWP: function () {
                        var a = this.getRoot();
                        a.find(".logoSplash").css("display", ""), a.find(".whatpumpkin").css("display", "block")
                    },
                    __doSL: function () {
                        var a = this.getRoot(),
                            b = this.__pacmanAdapter = e.retainPooledAdapter("sfx");
                        b._setEl(f.getLoadedElement()), b.play(), a.find(".logoSplash").css("display", ""), a.find(".shifty").css("display", "block")
                    },
                    __doDN: function () {
                        var a = this.getRoot();
                        a.find(".logoSplash").css("display", ""), a.find(".datenighto").css("display", "block")
                    },
                    __done: function () {
                        e.releasePooledAdapter(this.__pacmanAdapter), this.__pacmanAdapter = null;
                        for (var a = 0; a < l.length; ++a) {
                            var b = l[a],
                                c = d.tryResolve(b);
                            c && c.unload()
                        }
                        this._fireEvent("done", {})
                    },
                    __loadAll: function () {
                        for (var a = [], c = 0; c < l.length; ++c) {
                            var e = l[c],
                                g = d.tryResolve(e);
                            g ? (a.push(g.load()), 0 === c && (f = g)) : console.warn("couldnt resolve: " + e)
                        }
                        return b.all(a)
                    }
                }
            });
        return n
    }), define("namcohigh/audioassets", ["htmlvn/assets/AudioAsset", "htmlvn/assets/AudioCodec", "htmlvn/lib/utils", "assetpaths"], function (a, b, c, d) {
        "use strict";

        function e(b, d, e) {
            var f = c.format("a_{0}_{1}", b, e.toLowerCase());
            return new a(f, d + e, m)
        }

        function f(a) {
            return e("sfx", l, a)
        }

        function g(a) {
            return e("bgm", k, a)
        }
        var h = ["aroundtown", "bosstheme", "credits", "namcotheme", "privatetimes", "romance", "sadtimes", "school", "upbeat", "upbeat_half"],
            i = ["AlbatrossWatchBeep", "CameraShutterSnap", "CircularSAW", "FabricMove1", "FabricMove2", "FingerSnaps", "FireAlarm", "InteriorCrowd", "KISS1", "KISS2", "KingROAR1", "KingROAR2", "KingROAR3", "MotorcycleAWAY", "MotorcycleRACE", "MotorcycleREV", "RushingWATER", "SLAM", "SLAP", "SentaiSignal", "SwordClank1", "SwordClank2", "Transform1", "Transform2", "pacman", "whoosh", "Crash1", "Crash2", "CrashWall", "MetalSlam", "Explosion", "VaultCrash", "drill1", "drill2", "shovel", "westminster", "thunderclap", "TubaSolo", "arenacrowd"],
            j = d.audioRoot + "namcohigh/",
            k = j + "bgm/",
            l = j + "sfx/",
            m = ["m4a", "ogg"],
            n = [],
            o = 0;
        for (o = 0; o < h.length; ++o) n.push(g(h[o]));
        for (o = 0; o < i.length; ++o) n.push(f(i[o]));
        return n
    });
    var __slice = [].slice,
        __indexOf = [].indexOf || function (a) {
            for (var b = 0, c = this.length; c > b; b++)
                if (b in this && this[b] === a) return b;
            return -1
        };
    ! function (a) {
        var b;
        return b = function () {
            function b(b, c) {
                var d, e = this;
                this.input = b, this.defaultOptions = {
                    animate: true,
                    snapMid: false,
                    classPrefix: null,
                    classSuffix: null,
                    theme: null,
                    highlight: false
                }, this.settings = a.extend({}, this.defaultOptions, c), this.settings.theme && (this.settings.classSuffix = "-" + this.settings.theme), this.input.hide(), this.slider = a("<div>").addClass("slider" + (this.settings.classSuffix || "")).css({
                    position: "relative",
                    userSelect: "none",
                    boxSizing: "border-box"
                }).insertBefore(this.input), this.input.attr("id") && this.slider.attr("id", this.input.attr("id") + "-slider"), this.track = this.createDivElement("track").css({
                    width: "100%"
                }), this.settings.highlight && (this.highlightTrack = this.createDivElement("highlight-track").css({
                    width: "0"
                })), this.dragger = this.createDivElement("dragger"), this.slider.css({
                    minHeight: this.dragger.outerHeight(),
                    marginLeft: this.dragger.outerWidth() / 2,
                    marginRight: this.dragger.outerWidth() / 2
                }), this.track.css({
                    marginTop: this.track.outerHeight() / -2
                }), this.settings.highlight && this.highlightTrack.css({
                    marginTop: this.track.outerHeight() / -2
                }), this.dragger.css({
                    marginTop: this.dragger.outerWidth() / -2,
                    marginLeft: this.dragger.outerWidth() / -2
                }), this.track.mousedown(function (a) {
                    return e.trackEvent(a)
                }), this.settings.highlight && this.highlightTrack.mousedown(function (a) {
                    return e.trackEvent(a)
                }), this.dragger.mousedown(function (a) {
                    return 1 === a.which ? (e.dragging = true, e.dragger.addClass("dragging"), e.domDrag(a.pageX, a.pageY), false) : void 0
                }), a("body").mousemove(function (b) {
                    return e.dragging ? (e.domDrag(b.pageX, b.pageY), a("body").css({
                        cursor: "pointer"
                    })) : void 0
                }).mouseup(function () {
                    return e.dragging ? (e.dragging = false, e.dragger.removeClass("dragging"), a("body").css({
                        cursor: "auto"
                    })) : void 0
                }), this.pagePos = 0, "" === this.input.val() ? (this.value = this.getRange().min, this.input.val(this.value)) : this.value = this.nearestValidValue(this.input.val()), this.setSliderPositionFromValue(this.value), d = this.valueToRatio(this.value), this.input.trigger("slider:ready", {
                    value: this.value,
                    ratio: d,
                    position: d * this.slider.outerWidth(),
                    el: this.slider
                })
            }
            return b.prototype.createDivElement = function (b) {
                var c;
                return c = a("<div>").addClass(b).css({
                    position: "absolute",
                    top: "50%",
                    userSelect: "none",
                    cursor: "pointer"
                }).appendTo(this.slider)
            }, b.prototype.setRatio = function (a) {
                var b;
                return a = Math.min(1, a), a = Math.max(0, a), b = this.ratioToValue(a), this.setSliderPositionFromValue(b), this.valueChanged(b, a, "setRatio")
            }, b.prototype.setValue = function (a) {
                var b;
                return a = this.nearestValidValue(a), b = this.valueToRatio(a), this.setSliderPositionFromValue(a), this.valueChanged(a, b, "setValue")
            }, b.prototype.trackEvent = function (a) {
                return 1 === a.which ? (this.domDrag(a.pageX, a.pageY, true), this.dragging = true, false) : void 0
            }, b.prototype.domDrag = function (a, b, c) {
                var d, e, f;
                return null == c && (c = false), d = a - this.slider.offset().left, d = Math.min(this.slider.outerWidth(), d), d = Math.max(0, d), this.pagePos !== d ? (this.pagePos = d, e = d / this.slider.outerWidth(), f = this.ratioToValue(e), this.valueChanged(f, e, "domDrag"), this.settings.snap ? this.setSliderPositionFromValue(f, c) : this.setSliderPosition(d, c)) : void 0
            }, b.prototype.setSliderPosition = function (a, b) {
                if (null == b && (b = false), b && this.settings.animate) {
                    if (this.dragger.animate({
                        left: a
                    }, 200), this.settings.highlight) return this.highlightTrack.animate({
                        width: a
                    }, 200)
                } else if (this.dragger.css({
                    left: a
                }), this.settings.highlight) return this.highlightTrack.css({
                    width: a
                })
            }, b.prototype.setSliderPositionFromValue = function (a, b) {
                var c;
                return null == b && (b = false), c = this.valueToRatio(a), this.setSliderPosition(c * this.slider.outerWidth(), b)
            }, b.prototype.getRange = function () {
                return this.settings.allowedValues ? {
                    min: Math.min.apply(Math, this.settings.allowedValues),
                    max: Math.max.apply(Math, this.settings.allowedValues)
                } : this.settings.range ? {
                    min: parseFloat(this.settings.range[0]),
                    max: parseFloat(this.settings.range[1])
                } : {
                    min: 0,
                    max: 1
                }
            }, b.prototype.nearestValidValue = function (b) {
                var c, d, e, f;
                return e = this.getRange(), b = Math.min(e.max, b), b = Math.max(e.min, b), this.settings.allowedValues ? (c = null, a.each(this.settings.allowedValues, function () {
                    return null === c || Math.abs(this - b) < Math.abs(c - b) ? c = this : void 0
                }), c) : this.settings.step ? (d = (e.max - e.min) / this.settings.step, f = Math.floor((b - e.min) / this.settings.step), (b - e.min) % this.settings.step > this.settings.step / 2 && d > f && (f += 1), f * this.settings.step + e.min) : b
            }, b.prototype.valueToRatio = function (a) {
                var b, c, d, e, f, g, h, i;
                if (this.settings.equalSteps) {
                    for (i = this.settings.allowedValues, e = g = 0, h = i.length; h > g; e = ++g) b = i[e], ("undefined" == typeof c || null === c || Math.abs(b - a) < Math.abs(c - a)) && (c = b, d = e);
                    return this.settings.snapMid ? (d + .5) / this.settings.allowedValues.length : d / (this.settings.allowedValues.length - 1)
                }
                return f = this.getRange(), (a - f.min) / (f.max - f.min)
            }, b.prototype.ratioToValue = function (a) {
                var b, c, d, e, f;
                return this.settings.equalSteps ? (f = this.settings.allowedValues.length, e = Math.round(a * f - .5), b = Math.min(e, this.settings.allowedValues.length - 1), this.settings.allowedValues[b]) : (c = this.getRange(), d = a * (c.max - c.min) + c.min, this.nearestValidValue(d))
            }, b.prototype.valueChanged = function (b, c, d) {
                var e;
                if (b.toString() !== this.value.toString()) return this.value = b, e = {
                    value: b,
                    ratio: c,
                    position: c * this.slider.outerWidth(),
                    trigger: d,
                    el: this.slider
                }, this.input.val(b).trigger(a.Event("change", e)).trigger("slider:changed", e)
            }, b
        }(), a.extend(a.fn, {
            simpleSlider: function () {
                var c, d, e;
                return e = arguments[0], c = 2 <= arguments.length ? __slice.call(arguments, 1) : [], d = ["setRatio", "setValue"], a(this).each(function () {
                    var f, g;
                    return e && __indexOf.call(d, e) >= 0 ? (f = a(this).data("slider-object"), f[e].apply(f, c)) : (g = e, a(this).data("slider-object", new b(a(this), g)))
                })
            }
        }), a(function () {
            return a("[data-slider]").each(function () {
                var b, c, d, e;
                return b = a(this), d = {}, c = b.data("slider-values"), c && (d.allowedValues = function () {
                    var a, b, d, f;
                    for (d = c.split(","), f = [], a = 0, b = d.length; b > a; a++) e = d[a], f.push(parseFloat(e));
                    return f
                }()), b.data("slider-range") && (d.range = b.data("slider-range").split(",")), b.data("slider-step") && (d.step = b.data("slider-step")), d.snap = b.data("slider-snap"), d.equalSteps = b.data("slider-equal-steps"), b.data("slider-theme") && (d.theme = b.data("slider-theme")), b.attr("data-slider-highlight") && (d.highlight = b.data("slider-highlight")), null != b.data("slider-animate") && (d.animate = b.data("slider-animate")), b.simpleSlider(d)
            })
        })
    }(this.jQuery || this.Zepto, this), define("jquery-simple-slider", ["jquery"], function () {}), define("namcohigh/menu/NHMainMenu", ["jquery", "htmlvn/menu/Screen", "htmlvn/assets/Asset", "htmlvn/audio/AudioPool", "htmlvn/DataStore", "htmlvn/Game", "namcohigh/audioassets", "jquery-simple-slider"], function (a, b, c, d) {
        "use strict";
        var e = 90,
            f = b.inheritWith(function (b, f) {
                return {
                    constructor: function (a) {
                        f.call(this, a, "#mainMenu");
                        var b = this;
                        ["__showStore", "__closeStore", "__creditsDone", "__showCredits", "__dismissCredits", "__showMainOptions", "__hideMainOptions", "__titleAssetLoaded", "__presentLicenses"].map(function (a) {
                            b[a] = b[a].bind(b)
                        })
                    },
                    configure: function (b) {
                        b ? a("#mainMenu .button[data-action=continue]").css({
                            display: ""
                        }) : a("#mainMenu .button[data-action=continue]").css({
                            display: "none"
                        })
                    },
                    _willPresent: function () {
                        this.__hideMainOptions(), b._willPresent.apply(this, arguments)
                    },
                    _didPresent: function () {
                        this.on("credits", this.__showCredits), this.on("licenses", this.__presentLicenses), a("#mainMenu .button[data-privAction=options]").on("click", this.__showMainOptions), a("#mainMenu .button[data-privAction=store]").on("click", this.__showStore), b._didPresent.apply(this, arguments);
                        var d = c.getAsset("a_bgm_namcotheme");
                        d ? d.load().then(this.__titleAssetLoaded) : console.warn("Couldn't resolve audio asset a_bgm_namcotheme???")
                    },
                    _willDismiss: function () {
                        b._willDismiss.apply(this, arguments), d.removeAudio("mainMenu"), a("#mainMenu .button[data-privAction=options]").off("click", this.__showMainOptions), a("#mainMenu .button[data-privAction=store]").off("click", this.__showStore), this.off("credits", this.__showCredits), this.off("licenses", this.__presentLicenses)
                    },
                    _didDismiss: function () {
                        b._didDismiss.apply(this, arguments), this.__hideMainOptions()
                    },
                    __showMainOptions: function () {
                        var b = this.getPlayer(),
                            c = b._getMenu("options");
                        c.on("escape", this.__hideMainOptions), c.present(), a("#mainMenu .mainButtons").css({
                            visibility: "hidden"
                        }), a("#mainMenu .licenseButton").css({
                            display: "none"
                        })
                    },
                    __hideMainOptions: function () {
                        var b = this.getPlayer(),
                            c = b._getMenu("options");
                        c.off("escape", this.__hideMainOptions), c.dismiss(), a("#mainMenu .mainButtons").css({
                            visibility: "visible"
                        }), a("#mainMenu .licenseButton").css({
                            display: ""
                        })
                    },
                    __titleAssetLoaded: function (a) {
                        var b = c.getAsset("a_bgm_namcotheme");
                        if (b && this.isPresented() && !this.isDismissing()) {
                            var e = d.registerAudio("mainMenu", "bgm");
                            e.setLoop(true), e.setSource(a), e.play()
                        }
                    },
                    __showStore: function () {
                        var a = this.getPlayer(),
                            b = a._getMenu("store");
                        b.on("close", this.__closeStore), b.present()
                    },
                    __closeStore: function () {
                        var a = this.getPlayer(),
                            b = a._getMenu("store");
                        b.off("close", this.__closeStore), b.dismiss()
                    },
                    __showCredits: function () {
                        var a = this.__getCredits();
                        a.configure(e), a.on("break", this.__dismissCredits), a.on("done", this.__creditsDone), a.present({
                            opacity: 1
                        }, 0, {
                            opacity: 1
                        })
                    },
                    __dismissCredits: function () {
                        var a = this.__getCredits();
                        a.isDismissing() || a.dismiss()
                    },
                    __creditsDone: function () {
                        var a = this.__getCredits();
                        a.isPresented() && a.dismiss(), a.off("break", this.__dismissCredits), a.off("done", this.__creditsDone)
                    },
                    __getCredits: function () {
                        return this.getPlayer()._getMenu("credits")
                    },
                    __presentLicenses: function () {
                        this.getPlayer()._getMenu("license").present()
                    }
                }
            });
        return f
    }), define("htmlvn/menu/ChoiceScreen", ["jquery", "htmlvn/menu/Screen", "htmlvn/events/drivers/dom/DOMTextEvent"], function (a, b, c) {
        "use strict";
        var d = b.inheritWith(function (b, d) {
            return {
                __ev: null,
                constructor: function (a, b, c) {
                    b = b || "#choicePrompt", c ? c.push("choice") : c = ["choice"], d.call(this, a, b, c)
                },
                configure: function (a, b) {
                    this.__boundClick = this._handleClick.bind(this), this.__ev = a;
                    for (var d = this.getRoot(), e = d.find(".prompt"), f = 0; f < e.length; ++f) {
                        var g = e.eq(f);
                        if (f < b.length) {
                            var h = b[f],
                                i = c.resolveText(h.text);
                            g.attr("data-value", h.value), this._showChoice(g, f, h, i)
                        } else this._hideChoice(g, f)
                    }
                    d.attr("data-count", b.length)
                },
                _getEvent: function () {
                    return this.__ev
                },
                _didPresent: function () {
                    b._didPresent.apply(this, arguments), this.getRoot().find(".prompt").on("click", this.__boundClick)
                },
                _willDismiss: function () {
                    b._willDismiss.apply(this, arguments), this.getRoot().find(".prompt").off("click", this.__boundClick)
                },
                _showChoice: function (a, b, c, d) {
                    a.css("display", "").text(d)
                },
                _hideChoice: function (a) {
                    a.css("display", "none")
                },
                _handleClick: function (b) {
                    var c = a(b.currentTarget).attr("data-value");
                    this._fireEvent("choice", {
                        value: c
                    })
                }
            }
        });
        return d
    }), define("namcohigh/menu/NHExplorePrompt", ["jquery", "htmlvn/menu/Screen", "htmlvn/menu/ChoiceScreen", "htmlvn/events/drivers/dom/DOMTextEvent", "namcohigh/charlist", "namcohigh/user/UserStore"], function (a, b, c, d, e) {
        "use strict";
        var f = c.inheritWith(function (b, c) {
            return {
                constructor: function (a) {
                    c.call(this, a, "#exploreChoices")
                },
                configure: function (a, c, d) {
                    this.__clearTextBox = d, b.configure.apply(this, arguments)
                },
                eligibleForOverlay: function () {
                    return true
                },
                _willPresent: function (c, d) {
                    this.__clearTextBox && a("#textArea").transit({
                        opacity: 0
                    }, {
                        duration: 1e3 * d
                    }), b._willPresent.apply(this, arguments)
                },
                _didPresent: function () {
                    b._didPresent.apply(this, arguments)
                },
                _willDismiss: function (c, d) {
                    this.__clearTextBox && a("#textArea").transit({
                        opacity: 1
                    }, {
                        duration: 1e3 * d
                    }), b._willDismiss.apply(this, arguments)
                },
                _didDismiss: function () {
                    b._didDismiss.apply(this, arguments)
                },
                _showChoice: function (a, b, c, d) {
                    a.attr("data-character", e.ordered[b]).css("display", "").find(".buttonContent").text(d)
                },
                _handleClick: function (b) {
                    var c = a(b.currentTarget).attr("data-value"),
                        d = a(b.currentTarget).attr("data-character");
                    this._fireEvent("choice", {
                        value: c,
                        "char": d
                    })
                }
            }
        });
        return f
    }), define("namcohigh/menu/NHOptions", ["jquery", "htmlvn/menu/Screen", "htmlvn/DataStore", "htmlvn/audio/AudioPool", "htmlvn/BasePlayer", "jquery-simple-slider"], function (a, b, c, d) {
        "use strict";
        var e = b.inheritWith(function (b, e) {
            return {
                constructor: function (b) {
                    e.call(this, b, "#optionsMenu"), a(document).ready(this._ready.bind(this)), this.__valueChanged = this.__valueChanged.bind(this), this.__windowResized = this.__windowResized.bind(this), this.__handleKeyDown = this.__handleKeyDown.bind(this), this.__handleKeyUp = this.__handleKeyUp.bind(this), this.__openStore = this.__openStore.bind(this), this.__closeStore = this.__closeStore.bind(this)
                },
                _ready: function () {
                    console.log("NHOptions#ready!");
                    var b = this.getRoot();
                    b.find("input.vol").each(function (b, d) {
                        var e = a(d),
                            f = e.attr("data-bus"),
                            g = c.getVolume(f);
                        e.attr("value", g).val(g)
                    }).simpleSlider().on("changed slider:changed", this.__valueChanged)
                },
                _willPresent: function (c, d) {
                    b._willPresent.apply(this, arguments), this.__updateVolume(), a(window).on("resize", this.__windowResized), a("#mainMenu").hasClass("shown") ? this.getRoot().addClass("main") : (this.getRoot().addClass("game"), a("#overlayBacking").css({
                        opacity: 0,
                        display: "block"
                    }).transit({
                        opacity: .6
                    }, 1e3 * d))
                },
                _didPresent: function () {
                    b._didPresent.apply(this, arguments), this.__updateVolume(), a(window).on("keydown", this.__handleKeyDown), a(window).on("keyup", this.__handleKeyUp), this.on("store", this.__openStore)
                },
                _willDismiss: function (c, d) {
                    b._willDismiss.apply(this, arguments), a(window).off("keydown", this.__handleKeyDown), a(window).off("keyup", this.__handleKeyUp), this.off("store", this.__openStore), this.getRoot().hasClass("game") && a("#overlayBacking").transit({
                        opacity: 0
                    }, 1e3 * d)
                },
                _didDismiss: function () {
                    b._didDismiss.apply(this, arguments), a(window).off("resize", this.__windowResized), this.getRoot().removeClass("main game"), a("#overlayBacking").css({
                        display: "none"
                    })
                },
                __handleKeyDown: function () {},
                __handleKeyUp: function () {},
                __updateVolume: function () {
                    var b = this.getRoot();
                    b.find("input.vol").each(function (b, d) {
                        var e = a(d),
                            f = e.attr("data-bus"),
                            g = c.getVolume(f);
                        e.attr("value", g).val(g).simpleSlider("setValue", g)
                    })
                },
                __valueChanged: function (b) {
                    var e = a(b.target),
                        f = e.attr("data-bus"),
                        g = e.val();
                    c.setVolume(f, g), d.setLayerUserVolme(f, g), c.saveGameData()
                },
                __windowResized: function () {
                    this.__updateVolume()
                },
                __openStore: function () {
                    var a = this.__getStore();
                    a.on("close", this.__closeStore), a.present()
                },
                __closeStore: function () {
                    var a = this.__getStore();
                    a.dismiss(), a.off("close", this.__closeStore)
                },
                __getStore: function () {
                    return this.getPlayer()._getMenu("store")
                }
            }
        });
        return e
    }), define("namcohigh/menu/NewGamePrompt", ["jquery", "htmlvn/menu/Screen", "htmlvn/menu/YesNoPrompt"], function (a, b, c) {
        "use strict";
        var d = c.inheritWith(function (a, b) {
            return {
                constructor: function (a) {
                    b.call(this, a, "#yesNoPrompt")
                },
                _willPresent: function () {
                    this.configure("@t_ui_newgame"), a._willPresent.apply(this, arguments)
                }
            }
        });
        return d
    }), define("namcohigh/menu/SimpleToast", ["jquery", "htmlvn/menu/Screen", "htmlvn/assets/Asset"], function (a, b) {
        "use strict";
        var c = b.inheritWith(function (a, b) {
            return {
                constructor: function (a) {
                    b.call(this, a, "#simpleToast")
                },
                configure: function (a) {
                    var b = this.getRoot();
                    this._setElText(b.find(".showThis"), a)
                }
            }
        });
        return c
    }), define("namcohigh/menu/NamePrompt", ["jquery", "htmlvn/lib/utils", "htmlvn/menu/Screen", "htmlvn/assets/Asset", "htmlvn/DataStore", "htmlvn/events/drivers/dom/DOMTextEvent"], function (a, b, c, d, e, f) {
        "use strict";
        var g = "zoosmell pooplord",
            h = c.inheritWith(function (a, b) {
                return {
                    constructor: function (a) {
                        b.call(this, a, "#namePrompt", ["done"]), this.__yesClicked = this.__yesClicked.bind(this), this.__noClicked = this.__noClicked.bind(this), this.__trySubmit = this.__trySubmit.bind(this)
                    },
                    getValue: function () {
                        return this.__getInput().val()
                    },
                    _didPresent: function () {
                        this.on("submit", this.__trySubmit), a._didPresent.apply(this, arguments), this.__getInput().val(f.resolveText("@t_ui_cousinDefault")).focus()
                    },
                    _willDismiss: function () {
                        this.off("submit", this.__trySubmit), a._willDismiss.apply(this, arguments)
                    },
                    _didDismiss: function () {
                        var b = this.getRoot();
                        b.css("display", ""), b.find(".nameError").removeClass("live"), a._didDismiss.apply(this, arguments)
                    },
                    __validateName: function () {
                        var a = this.getValue().trim();
                        return a.toLowerCase() == g ? null : a.length >= 2 && a.length <= 18
                    },
                    __getInput: function () {
                        return this.getRoot().find("input")
                    },
                    __trySubmit: function () {
                        var a = this.getRoot();
                        a.find(".error").removeClass("live");
                        var b = this.__validateName();
                        if (b === true) {
                            var c = this.getValue();
                            e.set("playerName", c, "slot");
                            var d = this.getPlayer(),
                                f = d._getMenu("yesno");
                            f.configure("@t_ui_nameCheck"), f.on("yes", this.__yesClicked), f.on("no", this.__noClicked), f.present(), a.css("display", "none")
                        } else null === b ? a.find(".tryAgain").addClass("live") : b === false && a.find(".nameError").addClass("live")
                    },
                    __yesClicked: function () {
                        var a = this;
                        this.__clearYesNo();
                        var b = this.getPlayer(),
                            c = b._getMenu("toast");
                        c.configure("@t_ui_welcomeStudent"), c.present(), setTimeout(function () {
                            c.dismiss({
                                opacity: 0
                            }, .5).then(function () {
                                a._fireEvent("done", {})
                            })
                        }, 2e3)
                    },
                    __noClicked: function () {
                        this.__clearYesNo(), this.__getInput().val(f.resolveText("@t_ui_cousinDefault")), this.getRoot().css("display", "")
                    },
                    __clearYesNo: function () {
                        var a = this.getPlayer(),
                            b = a._getMenu("yesno");
                        b.off("yes", this.__yesClicked), b.off("no", this.__noClicked), b.dismiss()
                    }
                }
            });
        return h
    }), define("namcohigh/menu/UserSyncMenu", ["jquery", "htmlvn/menu/Screen", "htmlvn/assets/Asset", "htmlvn/audio/AudioPool", "htmlvn/DataStore", "htmlvn/Game", "namcohigh/user/UserStore"], function (a, b) {
        "use strict";
        var c = b.inheritWith(function (a, b) {
            return {
                constructor: function (a) {
                    b.call(this, a, "#syncingMenu")
                }
            }
        });
        return c
    }), define("namcohigh/menu/CreditsScreen", ["Q", "jquery", "htmlvn/menu/Screen", "htmlvn/assets/Asset", "htmlvn/audio/AudioPool", "htmlvn/DataStore", "htmlvn/Game", "namcohigh/user/UserStore", "jquery.transit"], function (a, b, c) {
        "use strict";
        var d = function () {
            return b("#creditRoll")
        }, e = 164,
            f = c.inheritWith(function (a, c) {
                return {
                    __runTime: e,
                    __running: false,
                    constructor: function (a) {
                        c.call(this, a, "#creditsScreen", ["done", "break"]), this.__handleKeyDown = this.__handleKeyDown.bind(this), this.__handleTap = this.__handleTap.bind(this)
                    },
                    eligibleForOverlay: function () {
                        return false
                    },
                    _willPresent: function () {
                        a._willPresent.apply(this, arguments), d().css("y", "0%")
                    },
                    _didPresent: function () {
                        var c = this.getRoot();
                        a._didPresent.apply(this, arguments), c.on("touchend", this.__handleTap), c.on("click", this.__handleTap), b(window).on("keydown", this.__handleKeyDown), this.run()
                    },
                    _willDismiss: function () {
                        var c = this.getRoot();
                        a._willDismiss.apply(this, arguments), b(window).off("keydown", this.__handleKeyDown), c.off("touchend", this.__handleTap), c.off("click", this.__handleTap)
                    },
                    _didDismiss: function () {
                        if (a._didDismiss.apply(this, arguments), this.__running) {
                            var b = d();
                            b.stopTransit(true, true), this.__running = false, this._fireEvent("done")
                        }
                    },
                    isRunning: function () {
                        return this.__running
                    },
                    configure: function (a) {
                        this.__runTime = a || e
                    },
                    run: function () {
                        if (!this.__running) {
                            var a = this,
                                b = d(),
                                c = function () {
                                    a.__running && a.__isProcessingInput() && (a.__running = false, a._fireEvent("done"))
                                };
                            b.transit({
                                y: "-100%"
                            }, 1e3 * this.__runTime, "linear", c), this.__running = true
                        }
                    },
                    __handleKeyDown: function (a) {
                        this.__isProcessingInput() && 13 === a.which && this._fireEvent("break", {})
                    },
                    __handleTap: function () {
                        this.__isProcessingInput() && this._fireEvent("break", {})
                    },
                    __isProcessingInput: function () {
                        return this.isPresented() && this.hasFocus() && !this.isDismissing()
                    }
                }
            });
        return f
    }), define("htmlvn/menu/IFrameScreen", ["jquery", "htmlvn/menu/Screen"], function (a, b) {
        "use strict";
        var c = b.inheritWith(function (b, c) {
            return {
                constructor: function (b, d, e, f) {
                    this.__url = e, a.isArray(f) ? f.push("load") : f = ["load"], c.call(this, b, d, f);
                    var d = this.getRoot(),
                        g = this.__iframe = d.find("iframe");
                    g.on("load", this._iframeLoaded.bind(this))
                },
                _willPresent: function () {
                    b._willPresent.apply(this, arguments);
                    var a = this.__iframe;
                    a.attr("src", "").attr("src", this.__url)
                },
                _didPresent: function () {
                    b._didPresent.apply(this, arguments)
                },
                _willDismiss: function () {
                    b._willDismiss.apply(this, arguments)
                },
                _didDismiss: function () {
                    b._didDismiss.apply(this, arguments)
                },
                _getIFrame: function () {
                    return this.__iframe
                },
                _iframeLoaded: function () {
                    var a = this.__iframe;
                    console.log("iframe finished loading " + a.attr("src")), this._fireEvent("load", {
                        url: this.__url
                    })
                }
            }
        });
        return c
    }), define("namcohigh/menu/NHStoreScreen", ["jquery", "htmlvn/menu/IFrameScreen"], function (a, b) {
        "use strict";
        var c = "http://namcohigh.shiftylook.com",
            d = b.inheritWith(function (a, b) {
                return {
                    constructor: function (a, d) {
                        d = d || "#storeMenu", b.call(this, a, d, c)
                    },
                    _iframeLoaded: function () {
                        a._iframeLoaded.apply(this, arguments);
                        var b = this._getIFrame();
                        console.log("iframe finished loading " + b.attr("src"))
                    }
                }
            });
        return d
    }), define("namcohigh/menu/LicenseScreen", ["jquery", "htmlvn/menu/IFrameScreen"], function (a, b) {
        "use strict";
        var c = "licenses.html",
            d = b.inheritWith(function (a, b) {
                return {
                    constructor: function (a, d) {
                        d = d || "#licenseScreen", b.call(this, a, d, c);
                        var e = this;
                        this.on("close", function () {
                            e.dismiss()
                        })
                    }
                }
            });
        return d
    }), define("namcohigh/macros/SettingChange", ["htmlvn/lib/utils", "htmlvn/events/DiscreteEvent", "htmlvn/events/ConditionalEvent", "htmlvn/events/FadeEvent", "htmlvn/events/drivers/dom/DOMImageEvent", "htmlvn/events/drivers/dom/DOMTextEvent", "htmlvn/events/Macro"], function (a, b, c, d, e, f, g) {
        "use strict";
        var h = g.inheritWith(function (c, g) {
            return {
                constructor: function (c) {
                    var h = a.getAndDelete,
                        i = h(c, "curtainActor") || "curtain",
                        j = h(c, "curtainFadeTime") || 0,
                        k = h(c, "bgActor") || "bg",
                        l = h(c, "bgImage"),
                        m = c.events || [];
                    m.push(new e({
                        target: k,
                        style: {
                            image: l
                        }
                    })), m.push(new f({
                        "char": "",
                        text: ""
                    })), c.events = [new d({
                        auto: true,
                        target: i,
                        duration: j,
                        to: 1
                    }), new b({
                        auto: true,
                        events: m
                    }), new d({
                        auto: true,
                        target: i,
                        duration: j,
                        to: 0
                    })], c.auto = true, g.call(this, c)
                }
            }
        });
        return h
    }), define("namcohigh/macros/SilhouetteMacro", ["htmlvn/events/DiscreteEvent", "htmlvn/events/ConditionalEvent", "htmlvn/events/FadeEvent", "htmlvn/events/DelayEvent", "htmlvn/events/drivers/dom/DOMImageEvent", "htmlvn/events/drivers/dom/DOMTextEvent", "htmlvn/events/shortcuts/FlipShortcut", "htmlvn/events/shortcuts/TransformShortcut", "htmlvn/events/Macro", "htmlvn/lib/utils"], function (a, b, c, d, e, f, g, h, i, j) {
        "use strict";
        var k = i.inheritWith(function (b, g) {
            return {
                constructor: function (b) {
                    var i = j.getAndDelete,
                        k = i(b, "silActor"),
                        l = i(b, "silImage"),
                        m = i(b, "realActor"),
                        n = i(b, "realImage"),
                        o = i(b, "cousinActor"),
                        p = i(b, "cousinImage"),
                        q = i(b, "lastActor"),
                        r = i(b, "firstText"),
                        s = i(b, "secondText"),
                        t = i(b, "appendSecond") || false;
                    i(b, "cousinText");
                    var u = i(b, "actorName");
                    i(b, "cousinName") || "@t_ch_cousin";
                    var v = i(b, "fadeTime") || .5,
                        w = i(b, "moveTime") || .15,
                        x = i(b, "waitTime") || .5,
                        y = i(b, "cousinX"),
                        z = i(b, "cousinScaleX") || 1,
                        A = i(b, "actorScaleX") || 1,
                        B = i(b, "actorScaleY") || 1,
                        C = i(b, "actorY") || "0%",
                        D = new e({
                            target: m,
                            style: {
                                image: n,
                                scaleX: A,
                                scaleY: B,
                                y: C
                            },
                            transitions: {
                                opacity: 1
                            },
                            duration: v
                        }),
                        E = new e({
                            target: k,
                            transitions: {
                                opacity: 0
                            },
                            duration: v
                        }),
                        F = [new e({
                            target: k,
                            style: {
                                image: l,
                                scaleX: A,
                                scaleY: B,
                                y: C
                            },
                            transitions: {
                                opacity: 1
                            },
                            duration: v
                        }), new f({
                            txt: r,
                            actor: u
                        })];
                    "string" == typeof q && F.push(new c({
                        target: q,
                        to: 0,
                        duration: .25
                    })), "string" == typeof y && F.push(new d({
                        delay: .55,
                        events: [new h({
                            target: o,
                            scaleX: z
                        }), new h({
                            target: o,
                            x: y,
                            duration: w
                        })]
                    })), "string" == typeof p && F.push(new e({
                        target: o,
                        style: {
                            image: p
                        }
                    }));
                    var G = [];
                    s ? (G.push(D), G.push(new f({
                        txt: s,
                        actor: u,
                        append: t
                    }))) : F.push(new d({
                        events: [D],
                        delay: x,
                        auto: true
                    })), b.events = [new a({
                        events: F,
                        auto: !s
                    }), new a({
                        events: G,
                        auto: true
                    }), new a({
                        events: [E]
                    })], g.call(this, b)
                }
            }
        });
        return k
    }), define("namcohigh/macros/BattleMacro", [
    "jquery", // a
    "htmlvn/lib/utils", // b
    "htmlvn/events/Macro", // c
    "htmlvn/events/DiscreteEvent", // d
    "htmlvn/events/drivers/dom/DOMImageEvent", // e
    "htmlvn/events/drivers/dom/DOMTextEvent", //f
    "htmlvn/events/DelayEvent", // g
    "htmlvn/events/audio/AudioEvent" // h,
    "htmlvn/events/audio/AudioOneShot", // i
    "htmlvn/events/audio/AudioCreate", // j
    "htmlvn/events/audio/AudioDestroy" // k
    ], function (a, b, c, d, e, f, g, h, i, j, k) {
        "use strict";
        var l = "@a_sfx_thunderclap",
            m = "thunderclap",
            n = function (a, b) { // a = "white_swatch", b = "valkyrie"
                return new d({
                    auto: true,
                    allowInterrupt: false,
                    events: [new e({ // DOMImageEvent // DOMImageEvent
                        target: a, // swatch
                        duration: .4,
                        animation: "flash"
                    }), new e({ // DOMImageEvent
                        target: b, // valk
                        duration: .75,
                        transitions: {
                            opacity: 1
                        }
                    })]
                })
            }, o = function (a, b) {
                return new e({ // DOMImageEvent
                    allowInterrupt: false,
                    ease: "ease",
                    duration: 1,
                    target: a, // valkyrie
                    transitions: {
                        x: b // 20%
                    }
                })
            }, p = c.inheritWith(function (a, b) {
                return {
                    constructor: function (a) {
                        "auto" in a || (a.auto = true);
                        var c = a.partnerActor,
                            i = a.whiteSwatchActor || "white_swatch",
                            p = a.robotArmyActor || "robotarmy",
                            q = a.curtainActor || "curtain",
                            r = a.cousinActor || "cousin",
                            s = a.bgActor || "bg",
                            t = a.whiteHoldTime || 2,
                            u = a.whiteFadeOutTime || 2,
                            v = a.whiteFadeOutTime || 2,
                            w = a.bgZoomTime || .75,
                            x = a.bgZoomEase || "ease-out",
                            y = a.robotArmyStartingX || "0%",
                            z = a.robotArmyDstX || "-40%",
                            A = a.robotArmyHoldTime || .75,
                            B = a.robotArmyMoveTime || 1,
                            C = a.bgmFadeTime || "bgm",
                            D = [new d({ // DiscreteEvent
                                auto: true,
                                allowInterrupt: false,
                                events: [new e({ // DOMImageEvent
                                    target: s,
                                    style: {
                                        x: "0%",
                                        y: "15%",
                                        scaleX: "2",
                                        scaleY: "2"
                                    }
                                }), new e({ // DOMImageEven
                                    target: p,
                                    style: {
                                        x: y
                                    }
                                })]
                            }), new g({ // DelayEvent 
                                auto: true,
                                allowInterrupt: false,
                                delay: .5,
                                events: [new j({ // AudioCreate
                                    audioId: m,
                                    sound: l,
                                    layer: "sfx",
                                    loop: false,
                                    play: true
                                }), new e({ // DOMImageEvent
                                    target: i,
                                    duration: .4,
                                    animation: "flash"
                                }), new g({ // DelayEvent
                                    delay: .5,
                                    events: [new e({ // DOMImageEvent
                                        target: i,
                                        duration: .4,
                                        animation: "flash"
                                    })]
                                })]
                            }), new g({ // DelayEvent
                                auto: true,
                                allowInterrupt: false,
                                delay: v,
                                events: [new e({ // DOMImageEvent
                                    target: s,
                                    duration: w,
                                    ease: x,
                                    transitions: {
                                        x: "0%",
                                        y: "0%",
                                        scaleX: "1",
                                        scaleY: "1"
                                    }
                                })]
                            }), new e({ // DOMImageEvent
                                target: p,
                                allowInterrupt: false,
                                duration: .75,
                                transitions: {
                                    opacity: 1
                                },
                                auto: true
                            }), new g({ // DelayEvent
                                auto: true,
                                allowInterrupt: false,
                                delay: A,
                                events: [new e({ // DOMImageEvent
                                    target: p,
                                    allowInterrupt: false,
                                    duration: B,
                                    transitions: {
                                        x: z
                                    },
                                    auto: true
                                })]
                            })],
                            E = [o(p, "-20%"), o(r, "27.5%")];
                        c && (D.push(n(i, c)), E.push(o(c, "20%"))), D.push(n(i, r)), D.push(new d({
                            allowInterrupt: false,
                            auto: true,
                            events: E
                        })), D.push(new e({
                            allowInterrupt: false,
                            target: i,
                            duration: .5,
                            auto: true,
                            transitions: {
                                opacity: 1
                            }
                        }));
                        var F = a.events || [];
                        if (F.length > 0) {
                            var G = new d({
                                allowInterrupt: false,
                                auto: true,
                                events: F
                            });
                            D.push(G)
                        }
                        D.push(new g({
                            allowInterrupt: false,
                            auto: true,
                            delay: t,
                            events: [new k({
                                target: m
                            }), new f({
                                "char": "",
                                text: ""
                            }), new e({
                                target: q,
                                style: {
                                    opacity: 1
                                }
                            }), new e({
                                target: i,
                                duration: u,
                                transitions: {
                                    opacity: 0
                                }
                            }), new h({
                                target: C,
                                volume: 0,
                                fadeDuration: u
                            })]
                        })), a.events = D, b.call(this, a)
                    }
                }
            });
        return p
    }), define("namcohigh/macros/ExplorationChoice", ["jquery", "htmlvn/lib/utils", "namcohigh/charlist", "htmlvn/events/ChoiceEvent", "htmlvn/events/ConsoleEvent", "htmlvn/DataStore", "htmlvn/BasePlayer", "namcohigh/user/UserStore"], function (a, b, c, d, e, f, g) {
        "use strict";
        g.getInstance;
        var h = d.inheritWith(function (a, b) {
            return {
                constructor: function (a) {
                    this.__scene = a.scene, a.name;
                    for (var d = a.passText || "@t_ui_done", e = a.passVal || "cousin", f = [], g = c.ordered, h = 0; h < g.length; ++h) {
                        var i = g[h];
                        f.push({
                            text: c.getName(i),
                            value: i
                        })
                    }
                    d && f.push({
                        text: d,
                        value: e
                    }), a.choices = f, a.menuName = "explore", b.call(this, a)
                },
                _configureMenu: function () {
                    var a = this.__choices,
                        b = this.__getSceneVar(),
                        c = this._getMenu();
                    if (!f.hasKey(b, "scene")) {
                        var d = a.slice(0, a.length - 1);
                        this.__choices = d, f.set(b, true, "scene")
                    }
                    c.on("choice", this.__boundChoice), c.configure(this, this.__choices, true), this.__choices = a
                },
                _presentScreen: function () {
                    return this._getMenu().present({
                        opacity: 1
                    }, .5, {
                        opacity: 0
                    })
                },
                _dismissScreen: function () {
                    return this._getMenu().dismiss({
                        opacity: 0
                    }, .5)
                },
                __getSceneVar: function () {
                    return "seen_choice_" + this.__scene
                }
            }
        });
        return h
    }), define("namcohigh/macros/ExplorationBranch", ["jquery", "htmlvn/lib/utils", "namcohigh/charlist", "htmlvn/DataStore", "htmlvn/Comparisons", "htmlvn/events/shortcuts/BranchMacro", "htmlvn/events/Macro", "htmlvn/events/DiscreteEvent"], function (a, b, c, d, e, f, g) {
        "use strict";
        var h = g.inheritWith(function (a, b) {
            return {
                constructor: function (a) {
                    var d = a.character || a.char;
                    this.__sceneName = a.scene;
                    var g = [];
                    g.push(new f({
                        comparison: e.EQ(this._getFullVar(), d),
                        path: c.getRawScene(d)
                    })), a.events = g, !("auto" in a) && (a.auto = true), b.call(this, a)
                },
                _getVarName: function () {
                    return "explore" + this.__sceneName
                },
                _getFullVar: function () {
                    return "${scene:explore" + this.__sceneName + "}"
                }
            }
        });
        return h
    }), define("namcohigh/macros/ExplorationMacro", ["jquery", "htmlvn/lib/utils", "namcohigh/charlist", "htmlvn/DataStore", "htmlvn/Comparisons", "htmlvn/events/ConsoleEvent", "htmlvn/events/Macro", "namcohigh/macros/ExplorationChoice", "namcohigh/macros/ExplorationBranch"], function (a, b, c, d, e, f, g, h, i) {
        "use strict";
        var j = g.inheritWith(function (a, b) {
            return {
                constructor: function (a) {
                    for (var d = this.__sceneName = a.sceneName.replace(".", "_"), e = this.__doLockout = a.lockout || false, g = [new h({
                            scene: d,
                            lockout: e,
                            passText: a.passText,
                            passVal: a.passVal,
                            varName: this._getVarName(),
                            storeName: a.storeName || "scene"
                        })], j = c.ordered, k = 0; k < j.length; ++k) {
                        var l = j[k];
                        g.push(new i({
                            "char": l,
                            scene: d
                        }))
                    }
                    g.push(new i({
                        "char": "cousin",
                        scene: d
                    })), g.push(new f({
                        severity: "error",
                        value: "FAILED TO BRANCH; DYING!!!"
                    })), a.events = g, b.call(this, a)
                },
                _getVarName: function () {
                    return "explore" + this.__sceneName
                },
                _getFullVar: function () {
                    return "${scene:explore" + this.__sceneName + "}"
                }
            }
        });
        return j
    }), define("namcohigh/macros/NHSceneChange", ["jquery", "htmlvn/lib/utils", "htmlvn/events/Macro", "htmlvn/events/SceneChangeEvent", "htmlvn/events/FadeEvent", "htmlvn/events/drivers/dom/DOMImageDestroyAll", "htmlvn/events/audio/AudioDestroyAll", "htmlvn/events/DiscreteEvent", "htmlvn/events/audio/AudioEvent"], function (a, b, c, d, e, f, g, h, i) {
        "use strict";
        var j = c.inheritWith(function (a, c) {
            return {
                constructor: function (a) {
                    var j = b.pickIn,
                        k = j(a, ["curtainActor"], "curtain"),
                        l = j(a, ["bgmId"], "bgm"),
                        m = j(a, ["scene", "sceneId", "s"]),
                        n = j(a, ["duration"], 1),
                        o = j(a, ["destroyAudio"], true),
                        p = j(a, ["musicFadeTarget"], 0);
                    a.events = [new h({
                        auto: true,
                        events: [new e({
                            target: k,
                            to: 1,
                            duration: n
                        }), new i({
                            target: l,
                            volume: p,
                            duration: n
                        })]
                    }), new f({
                        auto: true
                    })], o && a.events.push(new g({
                        auto: true
                    })), a.events.push(new d({
                        scene: m
                    })), c.call(this, a)
                }
            }
        });
        return j
    }), define("namcohigh/events/GameOverEvent", ["jquery", "htmlvn/lib/utils", "htmlvn/BasePlayer", "htmlvn/events/DiscreteEvent"], function (a, b, c, d) {
        var e = d.inheritWith(function (a, b) {
            return {
                constructor: function (a) {
                    b.call(this, a)
                },
                pump: function () {
                    var a = c.getInstance();
                    a.gameOver()
                },
                shouldSkip: function () {
                    return false
                },
                isComplete: function () {
                    return false
                }
            }
        });
        return e
    }), define("namcohigh/credits/CreditsEvent", ["jquery", "htmlvn/lib/utils", "htmlvn/StepMode", "htmlvn/BasePlayer", "htmlvn/events/MenuEvent", "htmlvn/events/Event", "htmlvn/events/Macro", "htmlvn/events/DiscreteEvent", "htmlvn/events/drivers/dom/DOMTextEvent", "htmlvn/DataStore", "htmlvn/assets/Asset"], function (a, b, c, d, e, f, g, h) {
        var i = e.inheritWith(function (a, b) {
            return {
                __done: false,
                constructor: function (a) {
                    a.character, "auto" in a || (a.auto = true), this.__time = a.time || 164, a.menuName = "credits", b.call(this, a)
                },
                eventWarm: function () {
                    this._getMenu(), this.__done = false, this.__interrupted = false, this.__boundDone = this.__menuDone.bind(this), this.__boundBreak = this.__menuBreak.bind(this), a.eventWarm.apply(this, arguments)
                },
                shouldSkip: function () {
                    return h.prototype.shouldSkip.apply(this, arguments)
                },
                finalize: function () {
                    var b = this._getMenu();
                    b.off("done", this.__boundDone), b.off("break", this.__boundBreak), this.__boundDone = null, this.__boundBreak = null, a.finalize.apply(this, arguments)
                },
                interrupt: function () {
                    var a = false,
                        b = this._getMenu();
                    return b.isRunning() && !this.__interrupted && (a = this.__interrupted = true, this.__menuDone()), a
                },
                pump: function () {
                    var b = a.pump.apply(this, arguments);
                    return this.__done = b, b
                },
                isComplete: function () {
                    return this.__done
                },
                _configureMenu: function (a) {
                    a.on("done", this.__boundDone), a.on("break", this.__boundBreak), a.configure(this.__time)
                },
                __menuDone: function () {
                    function a() {
                        b.off("done", this.__boundDone), b.off("break", this.__boundBreak), c.__done = true, c._signalComplete()
                    }
                    var b = this._getMenu(),
                        c = this,
                        d = this._dismissScreen();
                    d ? d.then(a) : (console.warn("Didn't get a promise from _dismissScreen; completing immediately!!"), a())
                },
                __menuBreak: function () {
                    var a = this._getMenu();
                    this.canInterrupt() && !a.isDismissing() && this._dismissScreen()
                },
                _presentScreen: function () {
                    return this._getMenu().present({
                        opacity: 1
                    }, .5, {
                        opacity: 0
                    })
                },
                _dismissScreen: function () {
                    return this._getMenu().dismiss({
                        opacity: 0
                    }, .5)
                }
            }
        });
        return i
    }), define("namcohigh/macros/BadEndMacro", ["jquery", "htmlvn/lib/utils", "htmlvn/events/Macro", "htmlvn/events/cond/IfLTE", "htmlvn/events/DiscreteEvent", "htmlvn/events/drivers/dom/DOMImageEvent", "htmlvn/events/drivers/dom/DOMImageCreate", "htmlvn/events/DelayEvent", "namcohigh/events/GameOverEvent", "namcohigh/credits/CreditsEvent", "htmlvn/events/audio/AudioEvent"], function (a, b, c, d, e, f, g, h, i, j, k) {
        "use strict";
        var l = "@a_bgm_namcotheme",
            m = "@i_event_badend",
            n = "@i_event_badend_gameover",
            o = "badEnd",
            p = "badEndText",
            q = b.getAndDelete,
            r = d.inheritWith(function (a, b) {
                return {
                    constructor: function (a) {
                        var c = a.time || 130;
                        a.lvalue = q(a, "varName"), a.rvalue = 1, "auto" in a || (a.auto = true), a.curtainActor || "curtain", a.events = [new e({
                            auto: true,
                            allowInterrupt: false,
                            events: [new g({
                                actorId: o,
                                styles: {
                                    depth: 18,
                                    image: m,
                                    opacity: 0
                                }
                            }), new g({
                                actorId: p,
                                styles: {
                                    depth: 19,
                                    image: n,
                                    opacity: 0
                                }
                            })]
                        }), new f({
                            target: o,
                            transitions: {
                                opacity: 1
                            },
                            duration: 1,
                            auto: true,
                            allowInterrupt: false
                        }), new f({
                            target: p,
                            transitions: {
                                opacity: 1
                            },
                            duration: 1,
                            auto: true,
                            allowInterrupt: false
                        }), new f({
                            target: "badEnd",
                            styles: {
                                opacity: 0
                            },
                            auto: true,
                            allowInterrupt: false
                        }), new h({
                            allowInterrupt: false,
                            delay: 4,
                            auto: true,
                            events: [new f({
                                target: p,
                                transitions: {
                                    opacity: 0
                                },
                                duration: 1
                            })]
                        }), new k({
                            target: "bgm",
                            volume: 1,
                            sound: l,
                            auto: true,
                            loop: true,
                            play: true
                        }), new j({ // AudioCreate
                            time: c,
                            auto: true,
                            allowInterrupt: true
                        }), new k({
                            target: "bgm",
                            volume: 0,
                            fadeDuration: .5,
                            auto: true
                        }), new i], b.call(this, a)
                    }
                }
            });
        return r
    }), define("namcohigh/macros/HardSwap", ["jquery", 
    "htmlvn/lib/utils", // b
    "htmlvn/events/drivers/dom/DOMImageEvent", // c 
    "htmlvn/events/DiscreteEvent", // d
    "htmlvn/events/Macro", // e
    "htmlvn/events/FadeEvent" // f
    ], function (a, b, c, d, e, f) {
        "use strict";
        var g = e.inheritWith(function (a, e) {
            return {
                constructor: function (a) {
                    a = a || {};
                    var g = b.getAndDelete,
                        h = g(a, "lastActor"),
                        i = g(a, "nextActor"),
                        j = g(a, "image"),
                        k = g(a, "fadeDuration") || .335,
                        l = g(a, "text"),
                        m = g(a, "char") || "",
                        n = [new f({
                            target: h,
                            to: 0,
                            duration: k,
                            auto: true
                        })],
                        o = {
                            target: i,
                            transitions: {
                                opacity: 1
                            },
                            duration: k
                        };
                    j && (o.style = {
                        image: j
                    });
                    var p = [new c(o)];
                    l && p.push(new TextEvent({
                        text: l,
                        "char": m
                    })), n.push(new d({
                        events: p
                    })), a.events = n, e.call(this, a)
                }
            }
        });
        return g
    }), define("namcohigh/macros/NormalEndMacro", 
    ["jquery", 
    "htmlvn/lib/utils",  // b
    "htmlvn/events/Macro",  // c
    "htmlvn/events/ConditionalEvent", // d
    "htmlvn/events/DiscreteEvent", // e
    "htmlvn/events/drivers/dom/DOMImageEvent",  // f
    "htmlvn/events/drivers/dom/DOMImageCreate",  //  g
    "htmlvn/events/DelayEvent", // h
    "namcohigh/events/GameOverEvent", // i 
    "namcohigh/credits/CreditsEvent", // j
    "htmlvn/events/audio/AudioEvent", // k
    "htmlvn/events/drivers/dom/DOMTextEvent" // l
    ], function (a, b, c, d, e, f, g, h, i, j, k, l) {
        "use strict";
        var m = "@a_bgm_credits",
            n = d.inheritWith(function (a, b) {
                return {
                    constructor: function (a) {
                        "comparison" in a || (a.comparison = "true"), "auto" in a || (a.auto = true);
                        var c = a.curtainActor || "curtain",
                            d = a.cousinActor || "cousin",
                            g = a.partnerActor,
                            h = a.pacmanActor || "pacman";
                        a.digdugActor || "digdug";
                        var i = a.firstLine || "@t_com00.00",
                            n = a.secondLine || "@t_com01.00",
                            o = a.cousinX || "-15%",
                            p = a.partnerX || "-35%",
                            q = a.curtainFadeOutTime || .5,
                            r = a.curtainFadeInTime || .5,
                            s = a.cousinImage || "@i_cousin_energetic_grin",
                            t = a.partnerImage,
                            u = a.runCredits || false,
                            v = a.events = [new e({
                                auto: true,
                                allowInterrupt: false,
                                events: [new f({
                                    target: d,
                                    style: {
                                        x: o,
                                        image: s,
                                        depth: 3
                                    }
                                }), new f({
                                    target: g,
                                    style: {
                                        x: p,
                                        image: t,
                                        depth: 2
                                    }
                                }), new f({
                                    target: h,
                                    style: {
                                        x: "30%",
                                        opacity: 1,
                                        depth: 2
                                    }
                                }), new l({
                                    "char": "@t_ch_pacman",
                                    text: i
                                })]
                            }), new f({
                                target: c,
                                transitions: {
                                    opacity: 0
                                },
                                duration: q
                            }), new l({
                                "char": "@t_ch_cousin",
                                text: n
                            }), new f({
                                target: c,
                                transitions: {
                                    opacity: 1
                                },
                                duration: r,
                                auto: true
                            }), new l({
                                "char": "",
                                text: "",
                                auto: true
                            })];
                        u && (v.push(new k({
                            target: "bgm",
                            volume: 1,
                            sound: m,
                            auto: true,
                            loop: false,
                            play: true
                        })), v.push(new j({
                            allowInterrupt: false
                        }))), b.call(this, a)
                    }
                }
            });
        return n
    }), define("namcohigh/macros/SuperSecretMacro", ["jquery", "htmlvn/lib/utils", "namcohigh/charlist", "htmlvn/events/ConditionalEvent", "namcohigh/macros/NHSceneChange", "htmlvn/DataStore"], function (a, b, c, d, e, f) {
        "use strict";
        var g = function () {
            var a = true,
                b = c.scenes;
            for (var d in b) {
                var e = "got_trueend_" + b[d];
                a = a && f.get(e, "game")
            }
            return a
        }, h = d.inheritWith(function (a, b) {
                return {
                    constructor: function (a) {
                        a.comparison = g, a.events = [new e({
                            duration: 0,
                            scene: "s_supersecret"
                        })], b.call(this, a)
                    }
                }
            });
        return h
    }), define("namcohigh/events/NHYesNoChoice", ["htmlvn/events/shortcuts/YesNoChoice"], function (a) {
        "use strict";
        var b = a.inheritWith(function (a, b) {
            return {
                constructor: function (a) {
                    "menuName" in a || (a.menuName = "explore"), b.call(this, a)
                },
                _presentScreen: function () {
                    return this._getMenu().present({
                        opacity: 1
                    }, .5, {
                        opacity: 0
                    })
                },
                _dismissScreen: function () {
                    return this._getMenu().dismiss({
                        opacity: 0
                    }, .5)
                }
            }
        });
        return b
    }), define("namcohigh/events/LockoutChoice", ["jquery", "htmlvn/lib/utils", "namcohigh/charlist", "namcohigh/events/NHYesNoChoice", "htmlvn/DataStore", "htmlvn/BasePlayer", "namcohigh/user/UserStore"], function (a, b, c, d, e, f, g) {
        "use strict";
        var h = f.getInstance,
            i = "upsell",
            j = "store",
            k = d.inheritWith(function (a, b) {
                return {
                    constructor: function (a) {
                        this.__character = a.character, b.call(this, a), this.__defaultMenu = this._getMenuName()
                    },
                    eventWarm: function () {
                        var b = this;
                        a.eventWarm.call(b), b.__boundReturn = b.__returnClicked.bind(b), b.__boundStore = b.__storeClicked.bind(b), b.__boundDismiss = b.__storeDismissed.bind(b)
                    },
                    finalize: function () {
                        var b = this,
                            c = h(),
                            d = c._getMenu(i),
                            e = c._getMenu(j);
                        d.off("return", b.__boundReturn), d.off("store", b.__boundStore), e.off("close", b.__boundDismiss), a.finalize.call(b), b.__boundReturn = null, b.__boundStore = null, b.__boundDismiss = null
                    },
                    pump: function (b) {
                        var c = this.__character,
                            d = false;
                        return b ? g.characterUnlocked(c) ? d = a.pump.call(this, b) : this.__firstLockout() : d = this.__done = true, d
                    },
                    __firstLockout: function () {
                        var a = this,
                            b = this.__character;
                        h().doRefreshAccess().then(function () {
                            g.characterUnlocked(b) ? a.pump(true) : a.__showLockout(b)
                        })
                    },
                    __showLockout: function () {
                        var a = this;
                        this.__character;
                        var b = h(),
                            c = a._getMenu(),
                            d = b._getMenu(i);
                        d.on("return", this.__boundReturn), d.on("store", this.__boundStore), c.dismiss(), d.present()
                    },
                    __returnClicked: function () {
                        var a = h(),
                            b = a._getMenu(i);
                        b.dismiss(), this.__retreat()
                    },
                    __storeClicked: function () {
                        var a = h(),
                            b = a._getMenu(i),
                            c = a._getMenu(j);
                        c.present(), c.on("close", this.__boundDismiss), b.dismiss()
                    },
                    __storeDismissed: function () {
                        var a = h(),
                            b = this.__character,
                            c = a._getMenu(j);
                        c.dismiss();
                        var d = this;
                        d._getMenu(), h().doRefreshAccess().then(function () {
                            g.characterUnlocked(b) ? d.pump(true) : d.__retreat()
                        })
                    },
                    __retreat: function () {
                        this._menuChoice({
                            text: this._getNoText(),
                            value: this._getNoValue()
                        })
                    }
                }
            });
        return k
    }), define("namcohigh/NHPlayer", ["jquery", "Q", "assetpaths", "htmlvn/lib/utils", "htmlvn/DataStore", "htmlvn/Game", "htmlvn/BasePlayer", "htmlvn/StepMode", "htmlvn/assets/Asset", "htmlvn/assets/Scene", "htmlvn/events/Event", "htmlvn/events/DiscreteEvent", "htmlvn/events/drivers/dom/DOMPlayer", "htmlvn/events/drivers/dom/DOMTextEvent", "htmlvn/audio/AudioPool", "namcohigh/charlist", "namcohigh/user/UserStore", "namcohigh/user/UserError", "namcohigh/user/UserLoggedOutError", "namcohigh/menu/ErrorScreen", "namcohigh/menu/UpsellScreen", "namcohigh/menu/LogoSplashScreen", "namcohigh/menu/NHMainMenu", "namcohigh/menu/NHExplorePrompt", "namcohigh/menu/NHOptions", "namcohigh/menu/NewGamePrompt", "namcohigh/menu/SimpleToast", "namcohigh/menu/NamePrompt", "namcohigh/menu/UserSyncMenu", "namcohigh/menu/CreditsScreen", "namcohigh/menu/NHStoreScreen", "namcohigh/menu/LicenseScreen", "namcohigh/macros/SettingChange", "namcohigh/macros/SilhouetteMacro", "namcohigh/macros/BattleMacro", "namcohigh/macros/ExplorationMacro", "namcohigh/macros/NHSceneChange", "namcohigh/macros/BadEndMacro", "namcohigh/macros/HardSwap", "namcohigh/macros/NormalEndMacro", "namcohigh/macros/SuperSecretMacro", "namcohigh/events/GameOverEvent", "namcohigh/events/NHYesNoChoice", "namcohigh/events/LockoutChoice", "namcohigh/credits/CreditsEvent"], function (a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S) {
        "use strict";
        var T = {
            SettingChange: G,
            SilhouetteMacro: H,
            ExplorationMacro: J,
            NHSceneChange: K,
            HardSwap: M,
            CreditsEvent: S,
            BattleMacro: I,
            BadEndMacro: L,
            YesNoChoice: Q,
            LockoutChoice: R,
            GameOver: P,
            NormalEndMacro: N,
            SuperSecretMacro: O
        }, U = {
                main: w,
                explore: x,
                options: y,
                error: t,
                upsell: u,
                newgame: z,
                toast: A,
                name: B,
                usersync: C,
                credits: D,
                store: E,
                splash: v,
                license: F
            }, V = false,
            W = V && false,
            X = "auto",
            Y = true,
            Z = 750,
            $ = 120,
            _ = 5,
            ab = function (a) {
                var b = a.toLowerCase();
                return b
            }, bb = /i/gi,
            cb = /e/gi,
            db = /a/gi,
            eb = function (a) {
                var b = a.toUpperCase();
                return b = b.replace(bb, "1"), b = b.replace(cb, "3"), b = b.replace(db, "4")
            }, fb = m.fastClass(function (g, m) {
                this.constructor = function (b, c, d) {
                    m.call(this, b, a.extend({}, c, U), a.extend({}, d, T), {}, false), this.__syncFailCount = 0, this.__syncTimer = 0, k.addChangeListener(this.__activeEvChanged.bind(this)), n.registerTransformer("davesprite", ab), n.registerTransformer("terezi", eb)
                }, this.gameOver = function () {
                    e.deleteSave(X), e.newGame(), e.saveGameData(), this.mainMenu(false)
                }, this.mainMenu = function (a) {
                    void 0 === a && (a = true);
                    var b = this,
                        c = b._getMenu("game"),
                        d = b._getMenu("main");
                    c.isPresented() && (a && b.saveGame(), this.__doDataPush(), b.changeScene(null), c.dismiss()), this.resetStage(), o.removeAll(), d.isPresented() || this.__presentMainMenu()
                }, this.saveGame = function () {
                    return g.saveGame.call(this, X)
                }, this.raiseError = function (a) {
                    console.error(a.stack), this._getMenu("error").present()
                }, this.changeScene = function (a, c) {
                    function d() {
                        var a = e._getMenu("loading"),
                            b = e._getMenu("game");
                        a.isPresented() || a.present({
                            opacity: 1
                        }, .5, {
                            opacity: 0
                        }), b.isPresented() && b.dismiss({
                            opacity: 0
                        }, .5)
                    }
                    var e = this,
                        f = e.getScene();
                    if (!g.changeScene.call(e, a, c, false)) return false;
                    e.__syncTimer = 0;
                    var i = e.getScene(),
                        j = e._getMenu("explore");
                    j.dismiss();
                    return i ? (f && (k.setActiveEvent(null), e.saveGame(), e.__doDataPush()), b().then(function () {
                        var a = e.getScene(),
                            c = null;
                        return a.isLoaded() || (c = a.load(), d()), c || b(a)
                    }).then(function () {
                        i.retainAssets(), V && e.__updateEvList(i), f && f.unload()
                    }).then(function () {
                        var a = e._getMenu("loading"),
                            c = null;
                        return i.isPreloaded() || (i.preload(false), c = a.startBlockingPreload(i), d()), c || b(e)
                    }).then(function () {
                        var a = e.__evTarget,
                            b = false,
                            c = !! a;
                        e.__evTarget = null, e.__beenHere = true;
                        var d = .5;
                        b && (d = 0);
                        var f = e._getMenu("loading"),
                            g = e._getMenu("game");
                        g.isPresented() || g.present({
                            opacity: 1
                        }, d, {
                            opacity: 0
                        });
                        var i = !c;
                        c && (i = e.__fastForwardToEvent(a)), i && e.stepScene(h.Normal), f.isPresented() && f.dismiss({
                            opacity: 0
                        }, d), e.__syncTimer = $
                    }).fail(function (a) {
                        e.raiseError(a)
                    }), true) : (f.unload(), void 0)
                }, this.doRefreshAccess = function () {
                    var a = this,
                        b = a._getMenu("usersync");
                    b.present();
                    var c = q.refreshAccess().then(function () {
                        b.dismiss()
                    }, function (b) {
                        a.raiseError(b)
                    });
                    return c
                }, this._update = function (a) {
                    g._update.call(this, a);
                    var b = this,
                        c = b.getScene(),
                        d = b._getMenu("game");
                    !b.__savePromise && c && c.isPreloaded() && d.isPresented() && (b.__syncTimer += a, b.__syncTimer > $ && (b.__doDataPush(), b.__syncTimer = 0))
                }, this.__doDataPush = function () {
                    self.__savePromise || (self.__savePromise = q.pushSaveData().then(function () {
                        self.__syncFailCount = 0
                    }, function (a) {
                        self.__syncFailCount += 1, self.__syncFailCount > _ && self.raiseError(a)
                    }).fin(function () {
                        self.__savePromise = null
                    }))
                }, this._ready = function () {
                    V ? W || a(".css-treeview").remove() : a(".debugStuff").remove();
                    var b = i.getAsset("a_bgm_namcotheme");
                    b.load();
                    var c = false;
                    Y && !c ? this.__doDataSync() : (e.init(this.getGame()), this.__splashesDone()), g._ready.apply(this, arguments)
                }, this.__redirectToLogin = function () {
                    window.location.href = c.loginUrl
                }, this.__userIsLoggedOut = function () {
                    this.__redirectToLogin()
                }, this.__doDataSync = function () {
                    var a = this,
                        b = this._getMenu("usersync"),
                        c = this._getMenu("toast");
                    b.present(), q.init(this.getGame()).then(function () {
                        b.dismiss(), c.configure("@t_ui_done_bang"), c.present({
                            opacity: 1
                        }, 0, {
                            opacity: 0
                        })
                    }, function (b) {
                        b instanceof s ? a.__userIsLoggedOut() : a.raiseError(b)
                    }).delay(Z).then(function () {
                        c.dismiss(), a.__dataSyncDone()
                    }).done()
                }, this.__dataSyncDone = function () {
                    var a = this._getMenu("splash");
                    a.on("done", this.__splashesDone.bind(this)), a.present()
                }, this.__splashesDone = function () {
                    var a = this._getMenu("splash"),
                        b = false,
                        c = this._getMenu("main");
                    V && (this.__createSceneList(), this.__readyDataInspector()), a.off("done"), a.dismiss(), c.on("newGame", this._newGameClicked.bind(this)), c.on("continue", this._continueClicked.bind(this)), b ? this.__continue() : this.__presentMainMenu()
                }, this._play = function () {
                    g.play.apply(this, arguments)
                }, this._continueClicked = function () {
                    var a = this;
                    a._getMenu("main").dismiss({
                        opacity: 0
                    }, 1).then(function () {
                        a.__continue()
                    })
                }, this._newGameClicked = function () {
                    var a = this;
                    if (e.hasSave(X)) {
                        var b = this._getMenu("newgame");
                        b.on("yes", function () {
                            b.off(), b.dismiss(), a.__doNewGame()
                        }), b.on("no", function () {
                            b.off(), b.dismiss()
                        }), b.present()
                    } else this.__doNewGame()
                }, this._unloadScene = function () {
                    g._unloadScene.apply(this, arguments)
                }, this.__continue = function () {
                    if (!e.hasSave(X)) return console.warn("refusing to load a game that doesnt exist!!"), void 0;
                    var a = e.getSaveMeta(X),
                        b = a.scene,
                        c = a.evPath;
                    e.load(X), this.__evTarget = c, this.changeScene(b, false)
                }, this.__doNewGame = function () {
                    e.newGame();
                    var a = i.tryResolve(f.getDefaultScene());
                    a.preload(false);
                    var b = this;
                    b._getMenu("main").dismiss({
                        opacity: 0
                    }, 1).then(function () {
                        var a = b._getMenu("name");
                        a.on("done", b.__namePromptDone.bind(b)), a.present()
                    })
                }, this.__namePromptDone = function () {
                    var a = this._getMenu("name");
                    a.off("done"), a.dismiss(), this.changeScene(f.getDefaultScene())
                }, this.__presentMainMenu = function () {
                    var a = this._getMenu("main");
                    a.configure(this.__canContinue()), a.present({
                        opacity: 1
                    }, 1, {
                        opacity: 0
                    })
                }, this.__canContinue = function () {
                    return e.hasSave(X)
                }, this.__activeEvChanged = function (b) {
                    var c = this;
                    if (c._isFastforwarding() || c.saveGame(), V && b) {
                        var d = b.getEventPath(),
                            e = a("#eventTree"),
                            f = e.find(".active").removeClass("active").end().find('li[data-path="' + d + '"]').addClass("active"),
                            g = function (b) {
                                var c = b.offset(),
                                    d = c.top,
                                    e = a(window).height();
                                return d > e ? false : true
                            };
                        this._isFastforwarding() || !e.hasClass("shown") || g(f) || f[0].scrollIntoView(false)
                    }
                }, V && (this.__evReplay = function () {
                    this.debugJump(k.getActiveEvent().getEventPath())
                }, this.__evNext = function () {
                    this.stepScene(h.Normal)
                }, this.__evBack = function () {
                    for (var a = k.getActiveEvent().getEventPath(), b = d.getGameState(a).lastEvPath, c = d.getGameState(b); c && c.lastEvIsAuto;) c = d.getGameState(c.lastEvPath);
                    c && c.lastEvPath && this.debugJump(c.lastEvPath)
                }, this.__toggleDataInspector = function () {
                    if (0 === a("input:focus").length) {
                        var b = a("#dataStoreInspector");
                        b.hasClass("shown") ? (b.find(".handle").html("&laquo;"), b.removeClass("shown")) : (this.__doDataInspectorSync(), b.find(".handle").html("&raquo;"), b.addClass("shown"))
                    }
                }, this.__clearTrueEnds = function () {
                    var a = p.scenes;
                    for (var b in a) {
                        var c = "got_trueend_" + a[b];
                        e.set(c, false, "game")
                    }
                }, this.__getTrueEnds = function () {
                    var a = p.scenes;
                    for (var b in a) {
                        var c = "got_trueend_" + a[b];
                        e.set(c, true, "game")
                    }
                }, this.__readyDataInspector = function () {
                    var b = this,
                        c = a("#dataStoreInspector");
                    c.find(".handle").on("click", b.__toggleDataInspector.bind(b)).end().find("button[name=push]").on("click", function () {
                        q.pushSaveData()
                    }).end().find("button[name=refresh]").on("click", function () {
                        b.__doDataInspectorSync()
                    }).end().find("button[name=refreshUser]").on("click", function () {
                        q.refreshAccess()
                    }).end().find("button[name=save]").on("click", function () {
                        b.saveGame()
                    }).end().find("button[name=clear]").on("click", function () {
                        e.clearAll()
                    }).end().find("button[name=clearScene]").on("click", function () {
                        e.clearSceneData(), b.saveGame()
                    }).end().find("button[name=pickCount0]").on("click", function () {
                        b.__setPickCount(0)
                    }).end().find("button[name=pickCount1]").on("click", function () {
                        b.__setPickCount(1)
                    }).end().find("button[name=pickCount2]").on("click", function () {
                        b.__setPickCount(2)
                    }).end().find("button[name=pickCount3]").on("click", function () {
                        b.__setPickCount(3)
                    }).end().find("button[name=pickEvent1]").on("click", function () {
                        b.__setPickDay(1, true)
                    }).end().find("button[name=pickEvent3]").on("click", function () {
                        b.__setPickDay(3, true)
                    }).end().find("button[name=pickEvent5]").on("click", function () {
                        b.__setPickDay(5, true)
                    }).end().find("button[name=clearEvent1]").on("click", function () {
                        b.__setPickDay(1, false)
                    }).end().find("button[name=clearEvent3]").on("click", function () {
                        b.__setPickDay(3, false)
                    }).end().find("button[name=clearEvent5]").on("click", function () {
                        b.__setPickDay(5, false)
                    }).end().find("button[name=ensure]").on("click", function () {
                        b.getScene().ensurePaths()
                    }).end().find("button[name=gotTrue]").on("click", function () {
                        b.__getTrueEnds()
                    }).end().find("button[name=clearTrue]").on("click", function () {
                        b.__clearTrueEnds()
                    }).end(), a(window).on("keyup", function (a) {
                        68 === a.keyCode && b.__toggleDataInspector()
                    }), W && (e.addChangeListener(function () {
                        b.__doDataInspectorSync()
                    }), b.__doDataInspectorSync())
                }, this.__setPickCount = function (a) {
                    for (var b in p.scenes) e.set("pick_count_" + p.scenes[b], a, "slot")
                }, this.__setPickDay = function (a, b) {
                    for (var c in p.scenes) e.set("picked_" + p.scenes[c] + "_day" + a, b, "slot")
                }, this.__doDataInspectorSync = function () {
                    if (W && !this._isFastforwarding() && a("#dataStoreInspector").hasClass("shown")) {
                        var b = e._getDebugRawObj();
                        for (var c in b) {
                            var f = b[c],
                                g = a(d.format(".varList.data-store-{0}", c));
                            if (g.length > 0) {
                                g.find("input").off("blur").end().find("li").remove();
                                for (var h in f)
                                    if ("timestamp" != h) {
                                        var i = a(d.format('<li data-var-name="{0}">{0}: <input type="text" data-var-store="{2}" data-var-name="{0}" value="{1}"></li>', h, f[h], c)),
                                            j = i.find("input");
                                        j.blur(function () {
                                            var b = a(this).attr("data-var-store"),
                                                c = a(this).attr("data-var-name"),
                                                f = a(this).val(),
                                                g = d.coerceType(f);
                                            e.set(c, g, b)
                                        }), g.append(i)
                                    }
                            }
                        }
                    }
                }, this.__toggleEvList = function () {
                    if (0 === a("input:focus").length) {
                        var b = a("#eventTree");
                        b.hasClass("shown") ? (b.find(".handle").html("&raquo;"), b.removeClass("shown")) : (b.find(".handle").html("&laquo;"), b.addClass("shown"))
                    }
                }, this.__createSceneList = function () {
                    var b = this,
                        c = a("#eventTree");
                    c.find(".handle").on("click", this.__toggleEvList.bind(this)).end().find("button[name=replay]").on("click", this.__evReplay.bind(this)).end().find("button[name=fwd]").on("click", this.__evNext.bind(this)).end().find("button[name=back]").on("click", this.__evBack.bind(this)), a(window).on("keyup", function (a) {
                        37 === a.keyCode ? b.__evBack() : 39 === a.keyCode ? b.__evNext() : 82 === a.keyCode ? b.__evReplay() : 69 === a.keyCode && b.__toggleEvList()
                    }), a("#game").on("wheel mousewheel", function (a) {
                        a.originalEvent.deltaY && (a.originalEvent.deltaY > 0 ? b.__evNext() : b.__evBack())
                    });
                    var d = i.getAssetsOfType(j),
                        e = a("#eventTree select.sceneList");
                    e.append(a('<option value=""></option>'));
                    for (var f = 0; f < d.length; ++f) {
                        var g = d[f],
                            h = g.getAssetId();
                        e.append(a("<option></option>").attr("value", h.replace(".", "-")).text(h))
                    }
                    e.on("change", function () {
                        var c = a(this).find("option:selected").attr("value");
                        c = c.replace("-", "."), c && c.length > 0 && (!b.getScene() || c != b.getScene().getAssetId()) && (b.resetStage(), b.changeScene(c)), a(this).blur()
                    })
                }, this.__updateEvList = function (b) {
                    var c = b.getRootMacro(),
                        d = a("<ul></ul>");
                    a("#eventTree").find("li").off("click").end().children("ul").remove().end().append(d), this.__buildEvTree(c, d)
                }, this.__buildEvTree = function (b, c) {
                    var d = a("<li>" + b.getEventName() + "</li>");
                    if (c.append(d), b instanceof l) {
                        var e = null;
                        b instanceof n ? e = b : b.hasChildren() && b.eachChild(function (a) {
                            a instanceof n && (e = a)
                        }), e && d.text(d.text() + " (" + e.__textId + ")"), d.attr("data-path", b.getEventPath()).on("click", function (b) {
                            var c = a(b.target).attr("data-path");
                            c && c.length > 0 && this.debugJump(c)
                        }.bind(this))
                    } else
                        for (var f = 0; f < b.getChildCount(); ++f) {
                            var g = b.getChildAtIndex(f),
                                h = a("<li></li>"),
                                i = a("<ul></ul>");
                            h.append(i), this.__buildEvTree(g, i), c.append(h)
                        }
                })
            });
        return fb
    }), define("namcohigh/scenes", ["htmlvn/assets/Scene", "namcohigh/charlist", "assetpaths"], function (a, b, c) {
        for (var d = function (b) {
            var d = "s_" + b;
            return new a(d, {
                xmlUrl: c.getSceneXMLUrl(d)
            })
        }, e = [d("intro"), d("day0"), d("day0.5"), d("day2"), d("day2.5"), d("day4"), d("day4.5"), d("day5.5"), d("cousin6"), d("supersecret")], f = ["1", "3", "5", "6"], g = b.ordered, h = 0; h < g.length; ++h)
            for (var i = 0; i < f.length; ++i) e.push(d(b.getActor(g[h]) + f[i]));
        return e
    }), define("htmlvn/assets/ImageType", [], function () {
        "use strict";
        return {
            Character: "character",
            Background: "background",
            Event: "event"
        }
    }), define("namcohigh/imageassets", ["htmlvn/assets/ImageAsset", "htmlvn/assets/ImageType", "assetpaths"], function (a, b, c) {
        "use strict";

        function d(b, c, d) {
            var f = {
                mdpi: c
            };
            return d && (f.hdpi = c.replace(e, "$1@2.$2")), new a(b, f)
        }
        var e = /(.*?)\.(je?pg|png)$/i,
            f = c.imageRoot + "namcohigh/",
            g = f + "battlepose/",
            h = f + "portrait/",
            i = f + "bg/",
            j = f + "event/",
            k = "i_bg_",
            l = "i_abm_",
            m = l + "backturned_",
            n = l + "default_",
            o = l + "shadowknows_",
            p = "i_albatross_",
            q = p + "fistinhand_",
            r = p + "notebook_",
            s = p + "toocool_",
            t = p + "watch_",
            u = p + "welcome_",
            v = "i_aki_",
            w = v + "akimbo_",
            x = v + "default_",
            y = v + "justice_",
            z = v + "notebook_",
            A = v + "tuba_",
            B = "i_amazona_",
            C = B + "akimbo_",
            D = B + "default_",
            E = "i_battlepose_",
            F = "i_bluemax_",
            G = "i_cousin_",
            H = "i_davesprite_",
            I = "i_donko_",
            J = "i_event_",
            K = "i_jane_",
            L = "i_hiromi_",
            M = "i_lolo_",
            N = "i_meowkie_",
            O = "i_miller_",
            P = "i_mrdriller_",
            Q = "i_nidia_",
            R = "i_taira_",
            S = "i_terezi_",
            T = "i_tomari_",
            U = "i_valkyrie_",
            V = [d(k + "cafe", i + "cafe.jpg", true), d(k + "classroom_a", i + "classroom-a.jpg", true), d(k + "classroom_b", i + "classroom-b.jpg", true), d(k + "cliff_day", i + "cliff-day.jpg", true), d(k + "cliff_night", i + "cliff-night.jpg", true), d(k + "cliff_night_fireflies", i + "cliff_night_fireflies.jpg", true), d(k + "dayride", i + "dayride.jpg", true), d(k + "evil_namco_high", i + "evil_namco_high.jpg", true), d(k + "galaga_house", i + "galaga-house.jpg", true), d(k + "hallway_a", i + "hallway-a.jpg", true), d(k + "hallway_b", i + "hallway-b.jpg", true), d(k + "library", i + "library.jpg", true), d(k + "nightrace", i + "nightrace.jpg", true), d(k + "quad_bleachers", i + "quad_bleachers.jpg", true), d(k + "quad_tents", i + "quad_tents.jpg", true), d(k + "rooftop", i + "rooftop.jpg", true), d(k + "rooftop_sunset", i + "rooftop_sunset.jpg", true), d(k + "school_front", i + "school_front.jpg", true), d(k + "shopclass", i + "shopclass.jpg", true), d(k + "stage_cardboard", i + "stage-cardboard.jpg", true), d(k + "stage", i + "stage.jpg", true), d(k + "vault", i + "vault.jpg", true), d(k + "vault_open", i + "vault_open.jpg", true), d(k + "vault_closed", i + "vault_closed.jpg", true), d(E + "albatross", g + "albatross.png", true), d(E + "albatross_glitch", g + "albatross_glitch.png", true), d(E + "albatross_multi", g + "albatross_multi.png", true), d(E + "amazona", g + "amazona.png", true), d(E + "antibravo", g + "antibravo.png", true), d(E + "bluemax", g + "bluemax.png", true), d(E + "cousin_evil", g + "cousin_evil.png", true), d(E + "cousin_normal", g + "cousin_normal.png", true), d(E + "davesprite", g + "davesprite.png", true), d(E + "donko", g + "donko.png", true), d(E + "galaga", g + "galaga.png", true), d(E + "hiromi", g + "hiromi.png", true), d(E + "hiromi_notoby", g + "hiromi_notoby.png", true), d(E + "jane", g + "jane.png", true), d(E + "jane_regular", g + "jane_regular.png", true), d(E + "lolo", g + "lolo.png", true), d(E + "meowkie", g + "meowkie.png", true), d(E + "miller", g + "miller.png", true), d(E + "mrdriller", g + "mrdriller.png", true), d(E + "mrdriller_nodrill", g + "mrdriller_nodrill.png", true), d(E + "nidia", g + "nidia.png", true), d(E + "robotarmy", g + "robotarmy.png", true), d(E + "taira", g + "taira.png", true), d(E + "terezi", g + "terezi.png", true), d(E + "tomari", g + "tomari.png", true), d(E + "valkyrie", g + "valkyrie.png", true), d(J + "albatross_ending", j + "albatross_ending.jpg", true), d(J + "amazona_ending", j + "amazona_ending.jpg", true), d(J + "antibravo_ending", j + "antibravo_ending.jpg", true), d(J + "badend", j + "badend.jpg", true), d(J + "badend_gameover", j + "badend_gameover.jpg", true), d(J + "bluemax_ending", j + "bluemax_ending.jpg", true), d(J + "cousin_badend", j + "cousin_badend.jpg", true), d(J + "davesprite_ending", j + "davesprite_ending.jpg", true), d(J + "davesprite_scene1", j + "davesprite_scene1.jpg", true), d(J + "donko_ending", j + "donko_ending.jpg", true), d(J + "donko_scene3", j + "donko_scene3.jpg", true), d(J + "hiromi_ending", j + "hiromi_ending.jpg", true), d(J + "hiromi_scene3", j + "hiromi_scene3.png", true), d(J + "jane_ending", j + "jane_ending.jpg", true), d(J + "lolo_ending", j + "lolo_ending.jpg", true), d(J + "lolo_yearbook", j + "lolo_yearbook.png", true), d(J + "meowkie_ending", j + "meowkie_ending.jpg", true), d(J + "miller_ending", j + "miller_ending.jpg", true), d(J + "mrdriller_ending", j + "mrdriller_ending.jpg", true), d(J + "nidia_ending", j + "nidia_ending.jpg", true), d(J + "taira_ending", j + "taira_ending.jpg", true), d(J + "terezi_ending", j + "terezi_ending.jpg", true), d(J + "terezi_scene3", j + "terezi_scene3.jpg", true), d(J + "tomari_ending", j + "tomari_ending.jpg", true), d(J + "valkyrie_ending", j + "valkyrie_ending.jpg", true), d(m + "sil", h + "abm/backturned_sil.png", false), d(m + "broody", h + "abm/backturned_broody.png", true), d(m + "grin", h + "abm/backturned_grin.png", true), d(m + "grin_blush", h + "abm/backturned_grin_blush.png", true), d(m + "sad", h + "abm/backturned_sad.png", true), d(m + "surprised", h + "abm/backturned_surprised.png", true), d(m + "surprised_blush", h + "abm/backturned_surprised_blush.png", true), d(n + "sil", h + "abm/default_sil.png", false), d(n + "broody", h + "abm/default_broody.png", true), d(n + "grin", h + "abm/default_grin.png", true), d(n + "grin_blush", h + "abm/default_grin_blush.png", true), d(n + "sad", h + "abm/default_sad.png", true), d(n + "surprised", h + "abm/default_surprised.png", true), d(n + "surprised_blush", h + "abm/default_surprised_blush.png", true), d(o + "sil", h + "abm/shadowknows_sil.png", false), d(o + "broody", h + "abm/shadowknows_broody.png", true), d(o + "grin", h + "abm/shadowknows_grin.png", true), d(o + "grin_blush", h + "abm/shadowknows_grin_blush.png", true), d(o + "sad", h + "abm/shadowknows_sad.png", true), d(o + "surprised", h + "abm/shadowknows_surprised.png", true), d(o + "surprised_blush", h + "abm/shadowknows_surprised_blush.png", true), d(q + "distraught", h + "albatross/fistinhand_distraught.png", true), d(q + "inquisitive", h + "albatross/fistinhand_inquisitive.png", true), d(q + "smirk", h + "albatross/fistinhand_smirk.png", true), d(q + "smirk_wink", h + "albatross/fistinhand_smirk_wink.png", true), d(q + "smug", h + "albatross/fistinhand_smug.png", true), d(q + "staredown", h + "albatross/fistinhand_staredown.png", true), d(r + "distraught", h + "albatross/notebook_distraught.png", true), d(r + "inquisitive", h + "albatross/notebook_inquisitive.png", true), d(r + "smirk", h + "albatross/notebook_smirk.png", true), d(r + "smirk_wink", h + "albatross/notebook_smirk_wink.png", true), d(r + "smug", h + "albatross/notebook_smug.png", true), d(r + "staredown", h + "albatross/notebook_staredown.png", true), d(s + "distraught", h + "albatross/toocool_distraught.png", true), d(s + "inquisitive", h + "albatross/toocool_inquisitive.png", true), d(s + "smirk", h + "albatross/toocool_smirk.png", true), d(s + "smirk_wink", h + "albatross/toocool_smirk_wink.png", true), d(s + "smug", h + "albatross/toocool_smug.png", true), d(s + "staredown", h + "albatross/toocool_staredown.png", true), d(t + "distraught", h + "albatross/watch_distraught.png", true), d(t + "inquisitive", h + "albatross/watch_inquisitive.png", true), d(t + "smirk", h + "albatross/watch_smirk.png", true), d(t + "smirk_wink", h + "albatross/watch_smirk_wink.png", true), d(t + "smug", h + "albatross/watch_smug.png", true), d(t + "staredown", h + "albatross/watch_staredown.png", true), d(u + "distraught", h + "albatross/welcome_distraught.png", true), d(u + "inquisitive", h + "albatross/welcome_inquisitive.png", true), d(u + "smirk", h + "albatross/welcome_smirk.png", true), d(u + "sil", h + "albatross/welcome_sil.png", false), d(u + "smirk_wink", h + "albatross/welcome_smirk_wink.png", true), d(u + "smug", h + "albatross/welcome_smug.png", true), d(u + "staredown", h + "albatross/welcome_staredown.png", true), d(w + "sil", h + "aki/akimbo_sil.png", false), d(w + "distracted", h + "aki/akimbo_distracted.png", true), d(w + "embarrassed", h + "aki/akimbo_embarrassed.png", true), d(w + "focus", h + "aki/akimbo_focus.png", true), d(w + "laughter", h + "aki/akimbo_laughter.png", true), d(w + "laughter_nervous", h + "aki/akimbo_laughter_nervous.png", true), d(w + "shocked", h + "aki/akimbo_shocked.png", true), d(w + "smile", h + "aki/akimbo_smile.png", true), d(x + "distracted", h + "aki/default_distracted.png", true), d(x + "focus", h + "aki/default_focus.png", true), d(x + "laughter", h + "aki/default_laughter.png", true), d(x + "nervouslaughter", h + "aki/default_nervouslaughter.png", true), d(x + "shocked", h + "aki/default_shocked.png", true), d(x + "shocked_blush", h + "aki/default_shocked_blush.png", true), d(x + "smile", h + "aki/default_smile.png", true), d(y + "focus", h + "aki/justice_focus.png", true), d(y + "laughter", h + "aki/justice_laughter.png", true), d(y + "laughter_nervous", h + "aki/justice_laughter_nervous.png", true), d(y + "overwhelmed", h + "aki/justice_overwhelmed.png", true), d(y + "shocked", h + "aki/justice_shocked.png", true), d(y + "shocked_embarassed", h + "aki/justice_shocked_embarassed.png", true), d(y + "smile", h + "aki/justice_smile.png", true), d(z + "focus", h + "aki/notebook_focus.png", true), d(z + "laughter", h + "aki/notebook_laughter.png", true), d(z + "laughter_nervous", h + "aki/notebook_laughter_nervous.png", true), d(z + "overwhelmed", h + "aki/notebook_overwhelmed.png", true), d(z + "shocked", h + "aki/notebook_shocked.png", true), d(z + "shocked_embarrassed", h + "aki/notebook_shocked_embarrassed.png", true), d(z + "smile", h + "aki/notebook_smile.png", true), d(A + "focus", h + "aki/tuba_focus.png", true), d(A + "laughter", h + "aki/tuba_laughter.png", true), d(A + "laughter_nervous", h + "aki/tuba_laughter_nervous.png", true), d(A + "overwhelmed", h + "aki/tuba_overwhelmed.png", true), d(A + "shocked", h + "aki/tuba_shocked.png", true), d(A + "shocked_embarrased", h + "aki/tuba_shocked_embarrased.png", true), d(A + "smile", h + "aki/tuba_smile.png", true), d(C + "distracted", h + "amazona/akimbo_distracted.png", true), d(C + "embarassed", h + "amazona/akimbo_embarassed.png", true), d(C + "focus", h + "amazona/akimbo_focus.png", true), d(C + "laugh", h + "amazona/akimbo_laugh.png", true), d(C + "laughter_nervous", h + "amazona/akimbo_laughter_nervous.png", true), d(C + "shocked", h + "amazona/akimbo_shocked.png", true), d(C + "smile", h + "amazona/akimbo_smile.png", true), d(D + "distracted", h + "amazona/default_distracted.png", true), d(D + "sil", h + "amazona/default_sil.png", false), d(D + "focus", h + "amazona/default_focus.png", true), d(D + "laughter", h + "amazona/default_laughter.png", true), d(D + "nervouslaugh", h + "amazona/default_nervouslaugh.png", true), d(D + "shocked", h + "amazona/default_shocked.png", true), d(D + "shocked_blush", h + "amazona/default_shocked_blush.png", true), d(D + "smile", h + "amazona/default_smile.png", true), d(F + "cower_sil", h + "bluemax/cower_sil.png", false), d(F + "cower_flustered", h + "bluemax/cower_flustered.png", true), d(F + "cower_serious", h + "bluemax/cower_serious.png", true), d(F + "cower_shock", h + "bluemax/cower_shock.png", true), d(F + "cower_smile", h + "bluemax/cower_smile.png", true), d(F + "cower_worried", h + "bluemax/cower_worried.png", true), d(F + "shock_flustered", h + "bluemax/shock_flustered.png", true), d(F + "shock_serious", h + "bluemax/shock_serious.png", true), d(F + "shock_shocked", h + "bluemax/shock_shocked.png", true), d(F + "shock_smile", h + "bluemax/shock_smile.png", true), d(F + "shock_worried", h + "bluemax/shock_worried.png", true), d(F + "stand_flustered", h + "bluemax/stand_flustered.png", true), d(F + "stand_serious", h + "bluemax/stand_serious.png", true), d(F + "stand_sil", h + "bluemax/stand_sil.png", false), d(F + "stand_shock", h + "bluemax/stand_shock.png", true), d(F + "stand_smile", h + "bluemax/stand_smile.png", true), d(F + "stand_worried", h + "bluemax/stand_worried.png", true), d(F + "stop_flustered", h + "bluemax/stop_flustered.png", true), d(F + "stop_serious", h + "bluemax/stop_serious.png", true), d(F + "stop_shocked", h + "bluemax/stop_shocked.png", true), d(F + "stop_smile", h + "bluemax/stop_smile.png", true), d(F + "stop_worried", h + "bluemax/stop_worried.png", true), d("i_connie_neutral", h + "connie/connie.png", true), d(G + "default_angry", h + "cousin/default_angry.png", true), d(G + "default_angry_blush", h + "cousin/default_angry_blush.png", true), d(G + "default_angry_scarf", h + "cousin/default_angry_scarf.png", true), d(G + "default_angry_scarf_blush", h + "cousin/default_angry_scarf_blush.png", true), d(G + "default_grin", h + "cousin/default_grin.png", true), d(G + "default_grin_blush", h + "cousin/default_grin_blush.png", true), d(G + "default_grin_scarf", h + "cousin/default_grin_scarf.png", true), d(G + "default_grin_scarf_blush", h + "cousin/default_grin_scarf_blush.png", true), d(G + "default_laugh", h + "cousin/default_laugh.png", true), d(G + "default_laugh_blush", h + "cousin/default_laugh_blush.png", true), d(G + "default_laugh_scarf", h + "cousin/default_laugh_scarf.png", true), d(G + "default_laugh_scarf_blush", h + "cousin/default_laugh_scarf_blush.png", true), d(G + "default_mortified", h + "cousin/default_mortified.png", true), d(G + "default_mortified_blush", h + "cousin/default_mortified_blush.png", true), d(G + "default_mortified_scarf", h + "cousin/default_mortified_scarf.png", true), d(G + "default_mortified_scarf_blush", h + "cousin/default_mortified_scarf_blush.png", true), d(G + "default_neutral", h + "cousin/default_neutral.png", true), d(G + "default_neutral_blush", h + "cousin/default_neutral_blush.png", true), d(G + "default_neutral_scarf", h + "cousin/default_neutral_scarf.png", true), d(G + "default_neutral_scarf_blush", h + "cousin/default_neutral_scarf_blush.png", true), d(G + "default_sad", h + "cousin/default_sad.png", true), d(G + "default_sad_blush", h + "cousin/default_sad_blush.png", true), d(G + "default_sad_scarf", h + "cousin/default_sad_scarf.png", true), d(G + "default_sad_scarf_blush", h + "cousin/default_sad_scarf_blush.png", true), d(G + "default_surprise_scarf", h + "cousin/default_surprise_scarf.png", true), d(G + "default_surprise_scarf_blush", h + "cousin/default_surprise_scarf_blush.png", true), d(G + "default_surprised", h + "cousin/default_surprised.png", true), d(G + "default_surprised_blush", h + "cousin/default_surprised_blush.png", true), d(G + "energetic_angry", h + "cousin/energetic_angry.png", true), d(G + "energetic_angry_blush", h + "cousin/energetic_angry_blush.png", true), d(G + "energetic_angry_scarf", h + "cousin/energetic_angry_scarf.png", true), d(G + "energetic_angry_scarf_blush", h + "cousin/energetic_angry_scarf_blush.png", true), d(G + "energetic_grin", h + "cousin/energetic_grin.png", true), d(G + "energetic_grin_blush", h + "cousin/energetic_grin_blush.png", true), d(G + "energetic_grin_scarf", h + "cousin/energetic_grin_scarf.png", true), d(G + "energetic_grin_scarf_blush", h + "cousin/energetic_grin_scarf_blush.png", true), d(G + "energetic_laugh", h + "cousin/energetic_laugh.png", true), d(G + "energetic_laugh_blush", h + "cousin/energetic_laugh_blush.png", true), d(G + "energetic_laugh_scarf", h + "cousin/energetic_laugh_scarf.png", true), d(G + "energetic_laugh_scarf_blush", h + "cousin/energetic_laugh_scarf_blush.png", true), d(G + "energetic_mortified", h + "cousin/energetic_mortified.png", true), d(G + "energetic_mortified_blush", h + "cousin/energetic_mortified_blush.png", true), d(G + "energetic_mortified_scarf", h + "cousin/energetic_mortified_scarf.png", true), d(G + "energetic_mortified_scarf_blush", h + "cousin/energetic_mortified_scarf_blush.png", true), d(G + "energetic_neutral", h + "cousin/energetic_neutral.png", true), d(G + "energetic_neutral_blush", h + "cousin/energetic_neutral_blush.png", true), d(G + "energetic_neutral_scarf", h + "cousin/energetic_neutral_scarf.png", true), d(G + "energetic_neutral_scarf_blush", h + "cousin/energetic_neutral_scarf_blush.png", true), d(G + "energetic_sad", h + "cousin/energetic_sad.png", true), d(G + "energetic_sad_blush", h + "cousin/energetic_sad_blush.png", true), d(G + "energetic_sad_scarf", h + "cousin/energetic_sad_scarf.png", true), d(G + "energetic_sad_scarf_blush", h + "cousin/energetic_sad_scarf_blush.png", true), d(G + "energetic_surprise", h + "cousin/energetic_surprise.png", true), d(G + "energetic_surprise_blush", h + "cousin/energetic_surprise_blush.png", true), d(G + "energetic_surprise_scarf", h + "cousin/energetic_surprise_scarf.png", true), d(G + "energetic_surprise_scarf_blush", h + "cousin/energetic_surprise_scarf_blush.png", true), d(G + "exhausted_angry", h + "cousin/exhausted_angry.png", true), d(G + "exhausted_angry_blush", h + "cousin/exhausted_angry_blush.png", true), d(G + "exhausted_angry_scarf", h + "cousin/exhausted_angry_scarf.png", true), d(G + "exhausted_angry_scarf_blush", h + "cousin/exhausted_angry_scarf_blush.png", true), d(G + "exhausted_grin", h + "cousin/exhausted_grin.png", true), d(G + "exhausted_grin_blush", h + "cousin/exhausted_grin_blush.png", true), d(G + "exhausted_grin_scarf", h + "cousin/exhausted_grin_scarf.png", true), d(G + "exhausted_grin_scarf_blush", h + "cousin/exhausted_grin_scarf_blush.png", true), d(G + "exhausted_laugh", h + "cousin/exhausted_laugh.png", true), d(G + "exhausted_laugh_blush", h + "cousin/exhausted_laugh_blush.png", true), d(G + "exhausted_laugh_scarf", h + "cousin/exhausted_laugh_scarf.png", true), d(G + "exhausted_laugh_scarf_blush", h + "cousin/exhausted_laugh_scarf_blush.png", true), d(G + "exhausted_mortified", h + "cousin/exhausted_mortified.png", true), d(G + "exhausted_mortified_blush", h + "cousin/exhausted_mortified_blush.png", true), d(G + "exhausted_mortified_scarf", h + "cousin/exhausted_mortified_scarf.png", true), d(G + "exhausted_mortified_scarf_blush", h + "cousin/exhausted_mortified_scarf_blush.png", true), d(G + "exhausted_neutral", h + "cousin/exhausted_neutral.png", true), d(G + "exhausted_neutral_blush", h + "cousin/exhausted_neutral_blush.png", true), d(G + "exhausted_neutral_scarf", h + "cousin/exhausted_neutral_scarf.png", true), d(G + "exhausted_neutral_scarf_blush", h + "cousin/exhausted_neutral_scarf_blush.png", true), d(G + "exhausted_sad", h + "cousin/exhausted_sad.png", true), d(G + "exhausted_sad_blush", h + "cousin/exhausted_sad_blush.png", true), d(G + "exhausted_sad_scarf", h + "cousin/exhausted_sad_scarf.png", true), d(G + "exhausted_sad_scarf_blush", h + "cousin/exhausted_sad_scarf_blush.png", true), d(G + "exhausted_surprised", h + "cousin/exhausted_surprised.png", true), d(G + "exhausted_surprised_blush", h + "cousin/exhausted_surprised_blush.png", true), d(G + "exhausted_surprised_scarf", h + "cousin/exhausted_surprised_scarf.png", true), d(G + "exhausted_surprised_scarf_blush", h + "cousin/exhausted_surprised_scarf_blush.png", true), d(H + "defeated_disinterest", h + "davesprite/defeated_disinterest.png", true), d(H + "defeated_eyebrow", h + "davesprite/defeated_eyebrow.png", true), d(H + "defeated_grin", h + "davesprite/defeated_grin.png", true), d(H + "defeated_sad", h + "davesprite/defeated_sad.png", true), d(H + "defeated_smile", h + "davesprite/defeated_smile.png", true), d(H + "defeated_smile_blush", h + "davesprite/defeated_smile_blush.png", true), d(H + "glitched", h + "davesprite/glitched.png", true), d(H + "shrug_disinterest", h + "davesprite/shrug_disinterest.png", true), d(H + "shrug_eyebrow", h + "davesprite/shrug_eyebrow.png", true), d(H + "shrug_grin", h + "davesprite/shrug_grin.png", true), d(H + "shrug_sad", h + "davesprite/shrug_sad.png", true), d(H + "shrug_smile", h + "davesprite/shrug_smile.png", true), d(H + "shrug_smile_blush", h + "davesprite/shrug_smile_blush.png", true), d(H + "standing_sil", h + "davesprite/standing_sil.png", false), d(H + "standing_disinterest", h + "davesprite/standing_disinterest.png", true), d(H + "standing_eyebrow", h + "davesprite/standing_eyebrow.png", true), d(H + "standing_grin", h + "davesprite/standing_grin.png", true), d(H + "standing_sad", h + "davesprite/standing_sad.png", true), d(H + "standing_smile", h + "davesprite/standing_smile.png", true), d(H + "standing_smile_blush", h + "davesprite/standing_smile_blush.png", true), d("i_digdug_left", h + "digdug/left.png", false), d("i_digdug_right", h + "digdug/right.png", false), d(I + "akimbo_sil", h + "don/akimbo_sil.png", false), d(I + "akimbo_crying", h + "don/akimbo_crying.png", true), d(I + "akimbo_crying_comic", h + "don/akimbo_crying_comic.png", true), d(I + "akimbo_grin", h + "don/akimbo_grin.png", true), d(I + "akimbo_grin_blush", h + "don/akimbo_grin_blush.png", true), d(I + "akimbo_meloncholic", h + "don/akimbo_meloncholic.png", true), d(I + "akimbo_meloncholic_blush", h + "don/akimbo_meloncholic_blush.png", true), d(I + "akimbo_wink", h + "don/akimbo_wink.png", true), d(I + "akimbo_wink_blush", h + "don/akimbo_wink_blush.png", true), d(I + "default_crying", h + "don/default_crying.png", true), d(I + "default_crying_comic", h + "don/default_crying_comic.png", true), d(I + "default_grin", h + "don/default_grin.png", true), d(I + "default_grin_blush", h + "don/default_grin_blush.png", true), d(I + "default_meloncholic", h + "don/default_meloncholic.png", true), d(I + "default_meloncholic_blush", h + "don/default_meloncholic_blush.png", true), d(I + "default_wink", h + "don/default_wink.png", true), d(I + "default_wink_blush", h + "don/default_wink_blush.png", true), d(I + "phone_crying", h + "don/phone_crying.png", true), d(I + "phone_crying_comic", h + "don/phone_crying_comic.png", true), d(I + "phone_grin", h + "don/phone_grin.png", true), d(I + "phone_grin_blush", h + "don/phone_grin_blush.png", true), d(I + "phone_meloncholic", h + "don/phone_meloncholic.png", true), d(I + "phone_meloncholic_blush", h + "don/phone_meloncholic_blush.png", true), d(I + "phone_wink", h + "don/phone_wink.png", true), d(I + "phone_wink_blush", h + "don/phone_wink_blush.png", true), d(I + "ygg_crying", h + "don/ygg_crying.png", true), d(I + "ygg_crying_comic", h + "don/ygg_crying_comic.png", true), d(I + "ygg_grin", h + "don/ygg_grin.png", true), d(I + "ygg_grin_blush", h + "don/ygg_grin_blush.png", true), d(I + "ygg_meloncholic", h + "don/ygg_meloncholic.png", true), d(I + "ygg_meloncholic_blush", h + "don/ygg_meloncholic_blush.png", true), d(I + "ygg_wink", h + "don/ygg_wink.png", true), d(I + "ygg_wink_blush", h + "don/ygg_wink_blush.png", true), d("i_galaga_blush", h + "galaga/blush.png", true), d("i_galaga_default", h + "galaga/default.png", true), d("i_galaga_default_sil", h + "galaga/default_sil.png", false), d("i_galaga_script", h + "galaga/script.png", true), d("i_galaga_wig", h + "galaga/wig.png", true), d(L + "akimbo_sil", h + "hiromi/akimbo_sil.png", false), d(L + "akimbo_serious", h + "hiromi/akimbo_serious.png", true), d(L + "akimbo_serious_blush", h + "hiromi/akimbo_serious_blush.png", true), d(L + "akimbo_smile", h + "hiromi/akimbo_smile.png", true), d(L + "akimbo_smile_blush", h + "hiromi/akimbo_smile_blush.png", true), d(L + "crossed_sil", h + "hiromi/crossed_sil.png", false), d(L + "crossed_serious", h + "hiromi/crossed_serious.png", true), d(L + "crossed_smile", h + "hiromi/crossed_smile.png", true), d(L + "crossed_smile_blush", h + "hiromi/crossed_smile_blush.png", true), d(L + "crossed_straight_blush", h + "hiromi/crossed_straight_blush.png", true), d(L + "stand_sil", h + "hiromi/stand_sil.png", false), d(L + "stand_serious", h + "hiromi/stand_serious.png", true), d(L + "stand_smile", h + "hiromi/stand_smile.png", true), d(L + "stand_smile_blush", h + "hiromi/stand_smile_blush.png", true), d(L + "stand_straight_blush", h + "hiromi/stand_straight_blush.png", true), d(L + "tool_serious", h + "hiromi/tool_serious.png", true), d(L + "tool_smile", h + "hiromi/tool_smile.png", true), d(L + "tool_smile_blush", h + "hiromi/tool_smile_blush.png", true), d(L + "tool_straight_blush", h + "hiromi/tool_straight_blush.png", true), d(K + "armscrossed_embarrassed", h + "jane/armscrossed_embarrassed.png", true), d(K + "armscrossed_embarrassed_blush", h + "jane/armscrossed_embarrassed_blush.png", true), d(K + "armscrossed_frustrated", h + "jane/armscrossed_frustrated.png", true), d(K + "armscrossed_frustrated_blush", h + "jane/armscrossed_frustrated_blush.png", true), d(K + "armscrossed_grin", h + "jane/armscrossed_grin.png", true), d(K + "armscrossed_grin_blush", h + "jane/armscrossed_grin_blush.png", true), d(K + "armscrossed_grin_mustache", h + "jane/armscrossed_grin_mustache.png", true), d(K + "armscrossed_laugh", h + "jane/armscrossed_laugh.png", true), d(K + "armscrossed_laugh_blush", h + "jane/armscrossed_laugh_blush.png", true), d(K + "armscrossed_laugh_mustache", h + "jane/armscrossed_laugh_mustache.png", true), d(K + "armscrossed_smile", h + "jane/armscrossed_smile.png", true), d(K + "armscrossed_smile_blush", h + "jane/armscrossed_smile_blush.png", true), d(K + "default_embarrassed", h + "jane/default_embarrassed.png", true), d(K + "default_embarrassed_blush", h + "jane/default_embarrassed_blush.png", true), d(K + "default_frustrated", h + "jane/default_frustrated.png", true), d(K + "default_frustrated_blush", h + "jane/default_frustrated_blush.png", true), d(K + "default_sil", h + "jane/default_sil.png", false), d(K + "default_grin", h + "jane/default_grin.png", true), d(K + "default_grin_blush", h + "jane/default_grin_blush.png", true), d(K + "default_grin_mustache", h + "jane/default_grin_mustache.png", true), d(K + "default_laugh", h + "jane/default_laugh.png", true), d(K + "default_laugh_blush", h + "jane/default_laugh_blush.png", true), d(K + "default_laugh_mustache", h + "jane/default_laugh_mustache.png", true), d(K + "default_smile", h + "jane/default_smile.png", true), d(K + "default_smile_blush", h + "jane/default_smile_blush.png", true), d(K + "godtier_embarrassed", h + "jane/godtier_embarrassed.png", true), d(K + "godtier_embarrassed_blush", h + "jane/godtier_embarrassed_blush.png", true), d(K + "godtier_frustrated", h + "jane/godtier_frustrated.png", true), d(K + "godtier_frustrated_blush", h + "jane/godtier_frustrated_blush.png", true), d(K + "godtier_grin", h + "jane/godtier_grin.png", true), d(K + "godtier_grin_blush", h + "jane/godtier_grin_blush.png", true), d(K + "godtier_grin_mustache", h + "jane/godtier_grin_mustache.png", true), d(K + "godtier_laugh", h + "jane/godtier_laugh.png", true), d(K + "godtier_laugh_blush", h + "jane/godtier_laugh_blush.png", true), d(K + "godtier_laugh_mustache", h + "jane/godtier_laugh_mustache.png", true), d(K + "godtier_smile", h + "jane/godtier_smile.png", true), d(K + "godtier_smile_blush", h + "jane/godtier_smile_blush.png", true), d(K + "handonhip_embarrassed", h + "jane/handonhip_embarrassed.png", true), d(K + "handonhip_embarrassed_blush", h + "jane/handonhip_embarrassed_blush.png", true), d(K + "handonhip_frustrated", h + "jane/handonhip_frustrated.png", true), d(K + "handonhip_frustrated_blush", h + "jane/handonhip_frustrated_blush.png", true), d(K + "handonhip_grin", h + "jane/handonhip_grin.png", true), d(K + "handonhip_grin_blush", h + "jane/handonhip_grin_blush.png", true), d(K + "handonhip_grin_mustache", h + "jane/handonhip_grin_mustache.png", true), d(K + "handonhip_laugh", h + "jane/handonhip_laugh.png", true), d(K + "handonhip_laugh_blush", h + "jane/handonhip_laugh_blush.png", true), d(K + "handonhip_laugh_mustache", h + "jane/handonhip_laugh_mustache.png", true), d(K + "handonhip_smile", h + "jane/handonhip_smile.png", true), d(K + "handonhip_smile_blush", h + "jane/handonhip_smile_blush.png", true), d(K + "notebook_embarrassed", h + "jane/notebook_embarrassed.png", true), d(K + "notebook_embarrassed_blush", h + "jane/notebook_embarrassed_blush.png", true), d(K + "notebook_frustrated", h + "jane/notebook_frustrated.png", true), d(K + "notebook_frustrated_blush", h + "jane/notebook_frustrated_blush.png", true), d(K + "notebook_grin", h + "jane/notebook_grin.png", true), d(K + "notebook_grin_blush", h + "jane/notebook_grin_blush.png", true), d(K + "notebook_grin_mustache", h + "jane/notebook_grin_mustache.png", true), d(K + "notebook_laugh", h + "jane/notebook_laugh.png", true), d(K + "notebook_laugh_blush", h + "jane/notebook_laugh_blush.png", true), d(K + "notebook_laugh_mustache", h + "jane/notebook_laugh_mustache.png", true), d(K + "notebook_smile", h + "jane/notebook_smile.png", true), d(K + "notebook_smile_blush", h + "jane/notebook_smile_blush.png", true), d(K + "spoon_embarrassed", h + "jane/spoon_embarrassed.png", true), d(K + "spoon_embarrassed_blush", h + "jane/spoon_embarrassed_blush.png", true), d(K + "spoon_frustrated", h + "jane/spoon_frustrated.png", true), d(K + "spoon_frustrated_blush", h + "jane/spoon_frustrated_blush.png", true), d(K + "spoon_grin", h + "jane/spoon_grin.png", true), d(K + "spoon_grin_blush", h + "jane/spoon_grin_blush.png", true), d(K + "spoon_grin_mustache", h + "jane/spoon_grin_mustache.png", true), d(K + "spoon_laugh", h + "jane/spoon_laugh.png", true), d(K + "spoon_laugh_blush", h + "jane/spoon_laugh_blush.png", true), d(K + "spoon_laugh_mustache", h + "jane/spoon_laugh_mustache.png", true), d(K + "spoon_smile", h + "jane/spoon_smile.png", true), d(K + "spoon_smile_blush", h + "jane/spoon_smile_blush.png", true), d("i_king_confident", h + "king/confident.png", true), d("i_king_screaming", h + "king/screaming.png", true), d(M + "crossed_sil", h + "lolo/crossed_sil.png", false), d(M + "crossed_cry", h + "lolo/crossed_cry.png", true), d(M + "crossed_cry_blush", h + "lolo/crossed_cry_blush.png", true), d(M + "crossed_frustrated", h + "lolo/crossed_frustrated.png", true), d(M + "crossed_frustrated_blush", h + "lolo/crossed_frustrated_blush.png", true), d(M + "crossed_grin", h + "lolo/crossed_grin.png", true), d(M + "crossed_grin_blush", h + "lolo/crossed_grin_blush.png", true), d(M + "crossed_melancholy", h + "lolo/crossed_melancholy.png", true), d(M + "crossed_melancholy_blush", h + "lolo/crossed_melancholy_blush.png", true), d(M + "crossed_raisedbrow", h + "lolo/crossed_raisedbrow.png", true), d(M + "crossed_raisedbrow_blush", h + "lolo/crossed_raisedbrow_blush.png", true), d(M + "crossed_realsmile", h + "lolo/crossed_realsmile.png", true), d(M + "crossed_realsmile_blush", h + "lolo/crossed_realsmile_blush.png", true), d(M + "default_sil", h + "lolo/default_sil.png", false), d(M + "default_cry", h + "lolo/default_cry.png", true), d(M + "default_cry_blush", h + "lolo/default_cry_blush.png", true), d(M + "default_frustrated", h + "lolo/default_frustrated.png", true), d(M + "default_frustrated_blush", h + "lolo/default_frustrated_blush.png", true), d(M + "default_grin", h + "lolo/default_grin.png", true), d(M + "default_grin_blush", h + "lolo/default_grin_blush.png", true), d(M + "default_melancholy", h + "lolo/default_melancholy.png", true), d(M + "default_melancholy_blush", h + "lolo/default_melancholy_blush.png", true), d(M + "default_raisedbrow", h + "lolo/default_raisedbrow.png", true), d(M + "default_raisedbrow_blush", h + "lolo/default_raisedbrow_blush.png", true), d(M + "default_realsmile", h + "lolo/default_realsmile.png", true), d(M + "default_realsmile_blush", h + "lolo/default_realsmile_blush.png", true), d(M + "shrug_sil", h + "lolo/shrug_sil.png", false), d(M + "shrug_cry", h + "lolo/shrug_cry.png", true), d(M + "shrug_cry_blush", h + "lolo/shrug_cry_blush.png", true), d(M + "shrug_frustrated", h + "lolo/shrug_frustrated.png", true), d(M + "shrug_frustrated_blush", h + "lolo/shrug_frustrated_blush.png", true), d(M + "shrug_grin", h + "lolo/shrug_grin.png", true), d(M + "shrug_grin_blush", h + "lolo/shrug_grin_blush.png", true), d(M + "shrug_melancholy", h + "lolo/shrug_melancholy.png", true), d(M + "shrug_melancholy_blush", h + "lolo/shrug_melancholy_blush.png", true), d(M + "shrug_raisedbrow", h + "lolo/shrug_raisedbrow.png", true), d(M + "shrug_raisedbrow_blush", h + "lolo/shrug_raisedbrow_blush.png", true), d(M + "shrug_realsmile", h + "lolo/shrug_realsmile.png", true), d(M + "shrug_realsmile_blush", h + "lolo/shrug_realsmile_blush.png", true), d(M + "slumped_cry", h + "lolo/slumped_cry.png", true), d(M + "slumped_cry_blush", h + "lolo/slumped_cry_blush.png", true), d(M + "slumped_frustrated", h + "lolo/slumped_frustrated.png", true), d(M + "slumped_frustrated_blush", h + "lolo/slumped_frustrated_blush.png", true), d(M + "slumped_grin", h + "lolo/slumped_grin.png", true), d(M + "slumped_grin_blush", h + "lolo/slumped_grin_blush.png", true), d(M + "slumped_melancholy", h + "lolo/slumped_melancholy.png", true), d(M + "slumped_melancholy_blush", h + "lolo/slumped_melancholy_blush.png", true), d(M + "slumped_raisedbrow", h + "lolo/slumped_raisedbrow.png", true), d(M + "slumped_raisedbrow_blush", h + "lolo/slumped_raisedbrow_blush.png", true), d(M + "slumped_realsmile", h + "lolo/slumped_realsmile.png", true), d(M + "slumped_realsmile_blush", h + "lolo/slumped_realsmile_blush.png", true), d("i_mc_normal", h + "mc/normal.png", true), d("i_mc_ref", h + "mc/ref.png", true), d(N + "akimbo_sil", h + "meowkie/akimbo_sil.png", false), d(N + "akimbo_alert", h + "meowkie/akimbo_alert.png", true), d(N + "akimbo_alert_badge", h + "meowkie/akimbo_alert_badge.png", true), d(N + "akimbo_forcedsmile", h + "meowkie/akimbo_forcedsmile.png", true), d(N + "akimbo_forcedsmile_badge", h + "meowkie/akimbo_forcedsmile_badge.png", true), d(N + "akimbo_frown", h + "meowkie/akimbo_frown.png", true), d(N + "akimbo_frown_badge", h + "meowkie/akimbo_frown_badge.png", true), d(N + "akimbo_grin", h + "meowkie/akimbo_grin.png", true), d(N + "akimbo_grin_badge", h + "meowkie/akimbo_grin_badge.png", true), d(N + "akimbo_normal", h + "meowkie/akimbo_normal.png", true), d(N + "akimbo_normal_badge", h + "meowkie/akimbo_normal_badge.png", true), d(N + "normal_sil", h + "meowkie/normal_sil.png", false), d(N + "normal_alert", h + "meowkie/normal_alert.png", true), d(N + "normal_alert_badge", h + "meowkie/normal_alert_badge.png", true), d(N + "normal_forcedsmile", h + "meowkie/normal_forcedsmile.png", true), d(N + "normal_forcedsmile_badge", h + "meowkie/normal_forcedsmile_badge.png", true), d(N + "normal_frown", h + "meowkie/normal_frown.png", true), d(N + "normal_frown_badge", h + "meowkie/normal_frown_badge.png", true), d(N + "normal_happy", h + "meowkie/normal_happy.png", true), d(N + "normal_happy_badge", h + "meowkie/normal_happy_badge.png", true), d(N + "normal_normal", h + "meowkie/normal_normal.png", true), d(N + "normal_normal_badge", h + "meowkie/normal_normal_badge.png", true), d(N + "slouch_alert", h + "meowkie/slouch_alert.png", true), d(N + "slouch_alert_badge", h + "meowkie/slouch_alert_badge.png", true), d(N + "slouch_forcedsmile", h + "meowkie/slouch_forcedsmile.png", true), d(N + "slouch_forcedsmile_badge", h + "meowkie/slouch_forcedsmile_badge.png", true), d(N + "slouch_frown", h + "meowkie/slouch_frown.png", true), d(N + "slouch_frown_badge", h + "meowkie/slouch_frown_badge.png", true), d(N + "slouch_happy", h + "meowkie/slouch_happy.png", true), d(N + "slouch_happy_badge", h + "meowkie/slouch_happy_badge.png", true), d(N + "slouch_normal", h + "meowkie/slouch_normal.png", true), d(N + "slouch_normal_badge", h + "meowkie/slouch_normal_badge.png", true), d(O + "akimbo_sil", h + "miller/akimbo_sil.png", false), d(O + "akimbo_contemplative", h + "miller/akimbo_contemplative.png", true), d(O + "akimbo_halfgrin", h + "miller/akimbo_halfgrin.png", true), d(O + "akimbo_laugh", h + "miller/akimbo_laugh.png", true), d(O + "akimbo_serious", h + "miller/akimbo_serious.png", true), d(O + "akimbo_shocked", h + "miller/akimbo_shocked.png", true), d(O + "aliens_sil", h + "miller/aliens_sil.png", false), d(O + "aliens_contemplative", h + "miller/aliens_contemplative.png", true), d(O + "aliens_halfgrin", h + "miller/aliens_halfgrin.png", true), d(O + "aliens_laugh", h + "miller/aliens_laugh.png", true), d(O + "aliens_serious", h + "miller/aliens_serious.png", true), d(O + "aliens_shocked", h + "miller/aliens_shocked.png", true), d(O + "notebook_contemplative", h + "miller/notebook_contemplative.png", true), d(O + "notebook_halfgrin", h + "miller/notebook_halfgrin.png", true), d(O + "notebook_laugh", h + "miller/notebook_laugh.png", true), d(O + "notebook_serious", h + "miller/notebook_serious.png", true), d(O + "notebook_shocked", h + "miller/notebook_shocked.png", true), d(O + "pondering_sil", h + "miller/pondering_sil.png", false), d(O + "pondering_contemplative", h + "miller/pondering_contemplative.png", true), d(O + "pondering_halfgrin", h + "miller/pondering_halfgrin.png", true), d(O + "pondering_laugh", h + "miller/pondering_laugh.png", true), d(O + "pondering_serious", h + "miller/pondering_serious.png", true), d(O + "pondering_shocked", h + "miller/pondering_shocked.png", true), d(O + "standing_sil", h + "miller/standing_sil.png", false), d(O + "standing_contemplative", h + "miller/standing_contemplative.png", true), d(O + "standing_halfgrin", h + "miller/standing_halfgrin.png", true), d(O + "standing_laugh", h + "miller/standing_laugh.png", true), d(O + "standing_serious", h + "miller/standing_serious.png", true), d(O + "standing_shocked", h + "miller/standing_shocked.png", true), d(P + "drillup_confused", h + "mrdriller/drillup_confused.png", true), d(P + "drillup_crying", h + "mrdriller/drillup_crying.png", true), d(P + "drillup_excited", h + "mrdriller/drillup_excited.png", true), d(P + "drillup_happy", h + "mrdriller/drillup_happy.png", true), d(P + "drillup_sad", h + "mrdriller/drillup_sad.png", true), d(P + "drillup_shock", h + "mrdriller/drillup_shock.png", true), d(P + "drillup_smug", h + "mrdriller/drillup_smug.png", true), d(P + "handsup_confused", h + "mrdriller/handsup_confused.png", true), d(P + "handsup_cry", h + "mrdriller/handsup_cry.png", true), d(P + "handsup_excited", h + "mrdriller/handsup_excited.png", true), d(P + "handsup_happy", h + "mrdriller/handsup_happy.png", true), d(P + "handsup_sad", h + "mrdriller/handsup_sad.png", true), d(P + "handsup_shock", h + "mrdriller/handsup_shock.png", true), d(P + "handsup_smug", h + "mrdriller/handsup_smug.png", true), d(P + "slumped_confused", h + "mrdriller/slumped_confused.png", true), d(P + "slumped_cry", h + "mrdriller/slumped_cry.png", true), d(P + "slumped_excited", h + "mrdriller/slumped_excited.png", true), d(P + "slumped_happy", h + "mrdriller/slumped_happy.png", true), d(P + "slumped_sad", h + "mrdriller/slumped_sad.png", true), d(P + "slumped_shock", h + "mrdriller/slumped_shock.png", true), d(P + "slumped_smug", h + "mrdriller/slumped_smug.png", true), d(P + "slumped_smug_sil", h + "mrdriller/slumped_smug_sil.png", false), d(P + "standing_confused", h + "mrdriller/standing_confused.png", true), d(P + "standing_cry", h + "mrdriller/standing_cry.png", true), d(P + "standing_excited", h + "mrdriller/standing_excited.png", true), d(P + "standing_happy", h + "mrdriller/standing_happy.png", true), d(P + "standing_sad", h + "mrdriller/standing_sad.png", true), d(P + "standing_shock", h + "mrdriller/standing_shock.png", true), d(P + "standing_smug", h + "mrdriller/standing_smug.png", true), d(P + "standing_smug_sil", h + "mrdriller/standing_smug_sil.png", false), d(Q + "akimbo_sil", h + "nidia/akimbo_sil.png", false), d(Q + "akimbo_angry", h + "nidia/akimbo_angry.png", true), d(Q + "akimbo_angry_blush", h + "nidia/akimbo_angry_blush.png", true), d(Q + "akimbo_happy", h + "nidia/akimbo_happy.png", true), d(Q + "akimbo_happy_blush", h + "nidia/akimbo_happy_blush.png", true), d(Q + "akimbo_surprised", h + "nidia/akimbo_surprised.png", true), d(Q + "akimbo_surprised_blush", h + "nidia/akimbo_surprised_blush.png", true), d(Q + "akimbo_worried", h + "nidia/akimbo_worried.png", true), d(Q + "akimbo_worried_blush", h + "nidia/akimbo_worried_blush.png", true), d(Q + "clasped_sil", h + "nidia/clasped_silpng", false), d(Q + "clasped_angry", h + "nidia/clasped_angry.png", true), d(Q + "clasped_angry_blush", h + "nidia/clasped_angry_blush.png", true), d(Q + "clasped_happy", h + "nidia/clasped_happy.png", true), d(Q + "clasped_happy_blush", h + "nidia/clasped_happy_blush.png", true), d(Q + "clasped_surprised", h + "nidia/clasped_surprised.png", true), d(Q + "clasped_surprised_blush", h + "nidia/clasped_surprised_blush.png", true), d(Q + "clasped_worried", h + "nidia/clasped_worried.png", true), d(Q + "clasped_worried_blush", h + "nidia/clasped_worried_blush.png", true), d(Q + "notepad_angry", h + "nidia/notepad_angry.png", true), d(Q + "notepad_angry_blush", h + "nidia/notepad_angry_blush.png", true), d(Q + "notepad_happy", h + "nidia/notepad_happy.png", true), d(Q + "notepad_happy_blush", h + "nidia/notepad_happy_blush.png", true), d(Q + "notepad_surprised", h + "nidia/notepad_surprised.png", true), d(Q + "notepad_surprised_blush", h + "nidia/notepad_surprised_blush.png", true), d(Q + "notepad_worried", h + "nidia/notepad_worried.png", true), d(Q + "notepad_worried_blush", h + "nidia/notepad_worried_blush.png", true), d(Q + "resolute_angry", h + "nidia/resolute_angry.png", true), d(Q + "resolute_angry_blush", h + "nidia/resolute_angry_blush.png", true), d(Q + "resolute_happy", h + "nidia/resolute_happy.png", true), d(Q + "resolute_happy_blush", h + "nidia/resolute_happy_blush.png", true), d(Q + "resolute_surprised", h + "nidia/resolute_surprised.png", true), d(Q + "resolute_surprised_blush", h + "nidia/resolute_surprised_blush.png", true), d(Q + "resolute_worried", h + "nidia/resolute_worried.png", true), d(Q + "resolute_worried_blush", h + "nidia/resolute_worried_blush.png", true), d("i_pacman_left", h + "pacman/left.png", false), d("i_pacman_right", h + "pacman/right.png", false), d("i_prop_parents", h + "prop/parents.png", true), d("i_prop_picnic", h + "prop/picnic.png", true), d("i_prop_hiromi_bike", h + "prop/hiromi_bike.png", true), d("i_prop_sword_good", h + "prop/sword_good.png", true), d("i_prop_sword_wood", h + "prop/sword_wood.png", true), d(R + "akimbo_sil", h + "taira/akimbo_sil.png", false), d(R + "akimbo_angry", h + "taira/akimbo_angry.png", true), d(R + "akimbo_confused", h + "taira/akimbo_confused.png", true), d(R + "akimbo_confused_blush", h + "taira/akimbo_confused_blush.png", true), d(R + "akimbo_happy", h + "taira/akimbo_happy.png", true), d(R + "akimbo_happy_blush", h + "taira/akimbo_happy_blush.png", true), d(R + "akimbo_pleading", h + "taira/akimbo_pleading.png", true), d(R + "akimbo_pleading_cry", h + "taira/akimbo_pleading_cry.png", true), d(R + "akimbo_revenge", h + "taira/akimbo_revenge.png", true), d(R + "akimbo_serious", h + "taira/akimbo_serious.png", true), d(R + "akimbo_serious_blush", h + "taira/akimbo_serious_blush.png", true), d(R + "akimbo_serious_cry", h + "taira/akimbo_serious_cry.png", true), d(R + "default_sil", h + "taira/default_sil.png", false), d(R + "default_angry", h + "taira/default_angry.png", true), d(R + "default_confused", h + "taira/default_confused.png", true), d(R + "default_confused_blush", h + "taira/default_confused_blush.png", true), d(R + "default_happy", h + "taira/default_happy.png", true), d(R + "default_happy_blush", h + "taira/default_happy_blush.png", true), d(R + "default_pleading", h + "taira/default_pleading.png", true), d(R + "default_pleading_cry", h + "taira/default_pleading_cry.png", true), d(R + "default_revenge", h + "taira/default_revenge.png", true), d(R + "default_serious", h + "taira/default_serious.png", true), d(R + "default_serious_blush", h + "taira/default_serious_blush.png", true), d(R + "default_serious_cry", h + "taira/default_serious_cry.png", true), d(R + "revenge_angry", h + "taira/revenge_angry.png", true), d(R + "revenge_confused", h + "taira/revenge_confused.png", true), d(R + "revenge_confused_blush", h + "taira/revenge_confused_blush.png", true), d(R + "revenge_happy", h + "taira/revenge_happy.png", true), d(R + "revenge_happy_blush", h + "taira/revenge_happy_blush.png", true), d(R + "revenge_pleading", h + "taira/revenge_pleading.png", true), d(R + "revenge_pleading_cry", h + "taira/revenge_pleading_cry.png", true), d(R + "revenge_revenge", h + "taira/revenge_revenge.png", true), d(R + "revenge_serious", h + "taira/revenge_serious.png", true), d(R + "revenge_serious_blush", h + "taira/revenge_serious_blush.png", true), d(R + "revenge_serious_cry", h + "taira/revenge_serious_cry.png", true), d(R + "steveholt_sil", h + "taira/steveholt_sil.png", false), d(R + "steveholt_angry", h + "taira/steveholt_angry.png", true), d(R + "steveholt_confused", h + "taira/steveholt_confused.png", true), d(R + "steveholt_confused_blush", h + "taira/steveholt_confused_blush.png", true), d(R + "steveholt_happy", h + "taira/steveholt_happy.png", true), d(R + "steveholt_happy_blush", h + "taira/steveholt_happy_blush.png", true), d(R + "steveholt_pleading", h + "taira/steveholt_pleading.png", true), d(R + "steveholt_pleading_cry", h + "taira/steveholt_pleading_cry.png", true), d(R + "steveholt_revenge", h + "taira/steveholt_revenge.png", true), d(R + "steveholt_serious", h + "taira/steveholt_serious.png", true), d(R + "steveholt_serious_blush", h + "taira/steveholt_serious_blush.png", true), d(R + "steveholt_serious_cry", h + "taira/steveholt_serious_cry.png", true), d(S + "default_sil", h + "terezi/default_sil.png", false), d(S + "default_grin", h + "terezi/default_grin.png", true), d(S + "default_huh", h + "terezi/default_huh.png", true), d(S + "default_laugh", h + "terezi/default_laugh.png", true), d(S + "default_pout", h + "terezi/default_pout.png", true), d(S + "default_resigned", h + "terezi/default_resigned.png", true), d(S + "lean_grin", h + "terezi/lean_grin.png", true), d(S + "lean_huh", h + "terezi/lean_huh.png", true), d(S + "lean_laugh", h + "terezi/lean_laugh.png", true), d(S + "lean_pout", h + "terezi/lean_pout.png", true), d(S + "lean_resigned", h + "terezi/lean_resigned.png", true), d(S + "rope_grin", h + "terezi/rope_grin.png", true), d(S + "rope_huh", h + "terezi/rope_huh.png", true), d(S + "rope_laugh", h + "terezi/rope_laugh.png", true), d(S + "rope_pout", h + "terezi/rope_pout.png", true), d(S + "rope_resigned", h + "terezi/rope_resigned.png", true), d("i_tobi_stand_cheering", h + "tobi/stand_cheering.png", true), d("i_tobi_stand_grin", h + "tobi/stand_grin.png", true), d("i_tobi_stand_sweetsmile", h + "tobi/stand_sweetsmile.png", true), d(T + "alive_frustrated", h + "tomari/alive_frustrated.png", true), d(T + "alive_mortified", h + "tomari/alive_mortified.png", true), d(T + "alive_smile", h + "tomari/alive_smile.png", true), d(T + "alive_smile_glass", h + "tomari/alive_smile_glass.png", true), d(T + "alive_thinking", h + "tomari/alive_thinking.png", true), d(T + "alive_thinking_glass", h + "tomari/alive_thinking_glass.png", true), d(T + "alive_thoughtful", h + "tomari/alive_thoughtful.png", true), d(T + "defeated_frustrated", h + "tomari/defeated_frustrated.png", true), d(T + "defeated_mortified", h + "tomari/defeated_mortified.png", true), d(T + "defeated_smile", h + "tomari/defeated_smile.png", true), d(T + "defeated_smile_glass", h + "tomari/defeated_smile_glass.png", true), d(T + "defeated_thinking", h + "tomari/defeated_thinking.png", true), d(T + "defeated_thinking_glass", h + "tomari/defeated_thinking_glass.png", true), d(T + "defeated_thoughtful", h + "tomari/defeated_thoughtful.png", true), d(T + "notebook_mortified", h + "tomari/notebook_mortified.png", true), d(T + "notebook_smile", h + "tomari/notebook_smile.png", true), d(T + "notebook_smile_glass", h + "tomari/notebook_smile_glass.png", true), d(T + "notebook_thinking", h + "tomari/notebook_thinking.png", true), d(T + "notebook_thinking_glass", h + "tomari/notebook_thinking_glass.png", true), d(T + "notebook_thoughtful", h + "tomari/notebook_thoughtful.png", true), d(T + "pondering_sil", h + "tomari/pondering_sil.png", false), d(T + "pondering_frustrated", h + "tomari/pondering_frustrated.png", true), d(T + "pondering_mortified", h + "tomari/pondering_mortified.png", true), d(T + "pondering_smile", h + "tomari/pondering_smile.png", true), d(T + "pondering_smile_glass", h + "tomari/pondering_smile_glass.png", true), d(T + "pondering_thinking", h + "tomari/pondering_thinking.png", true), d(T + "pondering_thinking_glass", h + "tomari/pondering_thinking_glass.png", true), d(T + "pondering_thoughtful", h + "tomari/pondering_thoughtful.png", true), d(T + "standing_sil", h + "tomari/standing_sil.png", false), d(T + "standing_frustrated", h + "tomari/standing_frustrated.png", true), d(T + "standing_mortified", h + "tomari/standing_mortified.png", true), d(T + "standing_smile", h + "tomari/standing_smile.png", true), d(T + "standing_smile_glass", h + "tomari/standing_smile_glass.png", true), d(T + "standing_thinking", h + "tomari/standing_thinking.png", true), d(T + "standing_thinking_glass", h + "tomari/standing_thinking_glass.png", true), d(T + "standing_thoughtful", h + "tomari/standing_thoughtful.png", true), d("i_trio_ballers", h + "trio/ballers.png", true), d("i_trio_evil", h + "trio/evil.png", true), d("i_trio_preps", h + "trio/preps.png", true), d(U + "akimbo_sil", h + "valkyria/akimbo_sil.png", false), d(U + "akimbo_bored", h + "valkyria/akimbo_bored.png", true), d(U + "akimbo_grin", h + "valkyria/akimbo_grin.png", true), d(U + "akimbo_grinblush", h + "valkyria/akimbo_grinblush.png", true), d(U + "akimbo_melancholy", h + "valkyria/akimbo_melancholy.png", true), d(U + "akimbo_thoughtful", h + "valkyria/akimbo_thoughtful.png", true), d(U + "akimbo_wink", h + "valkyria/akimbo_wink.png", true), d(U + "armscrossed_bored", h + "valkyria/armscrossed_bored.png", true), d(U + "armscrossed_grin", h + "valkyria/armscrossed_grin.png", true), d(U + "armscrossed_grinblush", h + "valkyria/armscrossed_grinblush.png", true), d(U + "armscrossed_melancholy", h + "valkyria/armscrossed_melancholy.png", true), d(U + "armscrossed_thoughtful", h + "valkyria/armscrossed_thoughtful.png", true), d(U + "armscrossed_wink", h + "valkyria/armscrossed_wink.png", true), d(U + "default_bored", h + "valkyria/default_bored.png", true), d(U + "default_grin", h + "valkyria/default_grin.png", true), d(U + "default_grinblush", h + "valkyria/default_grinblush.png", true), d(U + "default_melancholy", h + "valkyria/default_melancholy.png", true), d(U + "default_thoughtful", h + "valkyria/default_thoughtful.png", true), d(U + "default_wink", h + "valkyria/default_wink.png", true), d(U + "forjustice_sil", h + "valkyria/forjustice_sil.png", false), d(U + "forjustice_bored", h + "valkyria/forjustice_bored.png", true), d(U + "forjustice_grin", h + "valkyria/forjustice_grin.png", true), d(U + "forjustice_grinblush", h + "valkyria/forjustice_grinblush.png", true), d(U + "forjustice_melancholy", h + "valkyria/forjustice_melancholy.png", true), d(U + "forjustice_thoughtful", h + "valkyria/forjustice_thoughtful.png", true), d(U + "forjustice_wink", h + "valkyria/forjustice_wink.png", true), d("i_sw_black", c.imageRoot + "htmlvn/swatch_black.png", false), d("i_sw_white", c.imageRoot + "htmlvn/swatch_white.png", false), d("i_titlecard_dn", f + "credits/TitleCard_DateNighto.png", false), d("i_titlecard_nbgi", f + "credits/TitleCard_NBGI_half.png", false), d("i_titlecard_shiftylook_black", f + "credits/TitleCard_ShiftyLook.png", false), d("i_titlecard_whatpumpkin", f + "credits/TitleCard_WhatPumpkin.png", false)];
        return V
    }), define("namcohigh/text_en", ["htmlvn/assets/TextAsset"], function (a) {
        function b(b, c, d) {
            var e = {
                en: c
            };
            return d && (e.jp = d), new a(b, e)
        }
        var c = [b("t_ch_cousin", "${slot:playerName}"), b("t_ch_aki", "Aki"), b("t_ch_albatros", "Al. B. Tross"), b("t_ch_albatross", "Albatross"), b("t_ch_antibravo", "Anti-Bravoman"), b("t_ch_davesprite", "Davesprite"), b("t_ch_donko", "Donko"), b("t_ch_galaga", "Galaga"), b("t_ch_hiromi", "Hiromi"), b("t_ch_jane", "Jane"), b("t_ch_lolo", "Lolo"), b("t_ch_max", "Blue Max"), b("t_ch_meowkie", "Meowkie"), b("t_ch_mrdriller", "Mr. Driller"), b("t_ch_nidia", "Nidia"), b("t_ch_richard", "Richard Miller"), b("t_ch_taira", "Taira"), b("t_ch_terezi", "Terezi"), b("t_ch_toby", "Toby"), b("t_ch_tomari", "Tomari"), b("t_ch_valkyrie", "Valkyrie"), b("t_ch_condor", "Condor"), b("t_ch_condorconnie", "Condor I Mean Connie"), b("t_ch_codenameconnie", "Codename Connie"), b("t_ch_conniequestion", "Connie (...?)"), b("t_ch_connie", "Connie"), b("t_ch_pacman", "Pac-Man"), b("t_ch_bullies", "bullies"), b("t_ch_digdug", "Dig Dug"), b("t_ch_pictures", "pictures"), b("t_ch_dirtomari", "Director Tomari"), b("t_ch_tomaribang", "Tomari!"), b("t_ch_parents", "parents"), b("t_ch_thunder", "thunder"), b("t_ch_rain", "rain"), b("t_ch_door", "door"), b("t_ch_miller", "Miller"), b("t_ch_amazona", "Amazona"), b("t_ch_king", "King"), b("t_ch_tairanokagekiyo", "Taira no Kagekiyo"), b("t_ch_student", "Student"), b("t_ch_student1", "Student 1"), b("t_ch_student2", "Student 2"), b("t_ch_student3", "Student 3"), b("t_ch_eating", "eating"), b("t_ch_cousinmeowkie", "Cousin and Meowkie"), b("t_ch_akiquestion", "Aki???"), b("t_ch_nidiacousins", "Nidia & Cousin"), b("t_ch_oven", "Oven"), b("t_ch_coolguy", "A Cool Guy From Last Year"), b("t_ch_robotprint", "Amazing Robot Blueprint"), b("t_ch_shadowfigure", "Shadowy Figure"), b("t_ch_darklord", "xx-d4rkl0rd99-xx"), b("t_ch_unknown", "???"), b("t_ch_questionmarks", "???"), b("t_ch_mc", "M.C."), b("t_ch_waiter", "Waiter"), b("t_ch_tarp", "Mysterious Tarp"), b("t_ch_donkoandaki", "Donko and Aki"), b("t_ch_referee", "Referee"), b("t_ch_cashier", "Cashier"), b("t_ch_shadow1", "Shadow 1"), b("t_ch_shadow2", "Shadow 2"), b("t_ch_shadow3", "Shadow 3"), b("t_ch_announcer", "Announcer"), b("t_ch_narrator", "Narrator"), b("t_ui_mainMenu", "Main Menu"), b("t_ui_returnToGame", "Return to Game"), b("t_ui_sound_vol", "Sound Volume"), b("t_ui_music_vol", "Music Volume"), b("t_ui_language", "Language"), b("t_ui_newGame", "New Game"), b("t_ui_continue", "Continue"), b("t_ui_store", "Store"), b("t_ui_options", "Options"), b("t_ui_credits", "Credits"), b("t_ui_done", "Done"), b("t_ui_done_bang", "Done!"), b("t_ui_dontjoin", "Don't Join a Club"), b("t_ui_areyousureclub", "Are you sure you don’t want to join a club?"), b("t_ui_notsureclub", "Wait, I wanted to look around some more…"), b("t_ui_sureclub", "Yeah, I’m not interested in any of these."), b("t_ui_waitfordetention", "Wait for Detention to End."), b("t_ui_areyousuretalk", "Are you sure you don’t want to talk to anyone else?"), b("t_ui_notsuretalk", "Wait, I wanted to talk to someone else…"), b("t_ui_suretalk1", "Yeah, I just want detention to be over with."), b("t_ui_suretalk2", "Yeah, please just let this day be over."), b("t_ui_suretalk3", "Yeah, I just want out of here."), b("t_ui_bymyself1", "BY MYSELF."), b("t_ui_bymyself2", "I HAVE TO DO THIS ON MY OWN."), b("t_ui_yes", "Yes"), b("t_ui_no", "No"), b("t_ui_rusMain", "Return to Main Menu? All progress will be saved."), b("t_ui_r2mainMenu", "Return to main menu"), b("t_ui_ruSure", "Are you sure?"), b("t_ui_cancel", "Cancel"), b("t_ui_nextday", "The next day ..."), b("t_ui_syncing", "Syncing user data"), b("t_ui_oops", "Oops!"), b("t_ui_errorLong", "We're sorry, but it looks like an error has occured. Please refresh your browser and try again."), b("t_ui_refresh", "Refresh"), b("t_ui_notUnlocked", "You have not unlocked this character."), b("t_ui_unlockNow", "Unlock Now"), b("t_ui_newgame", "Are you sure you want to start a new game?"), b("t_ui_nameCheck", "You are enrolling as ${slot:playerName}. Is that correct?"), b("t_ui_welcomeStudent", "Welcome to Namco High, ${slot:playerName}!"), b("t_ui_cousinDefault", "Cousin"), b("t_ui_nameError", "Your name must be between 2 and 18 letters long"), b("t_ui_tryAgainSmartbutt", "Try again, smartbutt"), b("t_com00.00", "Thank you students for saving me! I thought I was a goner!"), b("t_com01.00", "Thank, YOU, Pac-Man. We were only able to do it, because we were true to ourselves!")];
        return c
    }), define("namcohigh", ["htmlvn/Game", "htmlvn/assets/Scene", "htmlvn/lib/utils", "namcohigh/NHPlayer", "namcohigh/scenes", "namcohigh/imageassets", "namcohigh/audioassets", "namcohigh/text_en"], function (a, b, c, d) {
        "use strict";
        var e = null,
            f = false,
            g = new a({
                identifier: "com.datenighto.game.namcohigh",
                defaultScene: "s_intro",
                startingEvPath: e,
                skipMenu: f
            });
        return new d(g)
    }), require.config({
        paths: {
            "jquery.transit": "vendor/jquery.transit",
            "jquery.scrollintoview": "vendor/jquery.scrollintoview",
            "jquery-simple-slider": "../bower_components/jquery-simple-slider/js/simple-slider",
            "es5-shim": "../bower_components/es5-shim/es5-shim",
            "es5-sham": "../bower_components/es5-shim/es5-sham",
            "store-js": "../bower_components/store.js/store",
            jquery: "../bower_components/jquery/jquery",
            Q: "../bower_components/q/q",
            stacktrace: "vendor/stacktrace",
            FastClass: "vendor/FastClass",
            domReady: "vendor/domReady"
        },
        shim: {
            "jquery.transit": {
                deps: ["jquery"]
            },
            "jquery.scrollintoview": {
                deps: ["jquery"]
            },
            "jquery-simple-slider": {
                deps: ["jquery"]
            },
            FastClass: {
                exports: "Function.define"
            }
        }
    }),
    function (a) {
        var b = function () {};
        a.console || (a.console = {
            log: b,
            warn: b,
            error: b
        })
    }(window), require(["namcohigh", "jquery"], function (a, b) {
        "use strict";
        b(window).ready(function () {})
    }), define("app", function () {})
}();