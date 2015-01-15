/* skel.js v2.2.0 | (c) n33 | getskel.com | MIT licensed */
var skel = function() {
    var e = "breakpoints",
        t = "config",
        n = "iterate",
        r = "elements",
        i = "stateId",
        s = "stateElements",
        o = "getElementsByClassName",
        u = !1,
        a = "getElementsByTagName",
        f = "length",
        l = null,
        c = "gridZoomMax",
        h = "getCachedElement",
        p = "viewport",
        d = " 0 -1px ",
        v = "cacheNewElement",
        m = "config_breakpoint",
        g = !0,
        y = "createElement",
        b = "gutters",
        w = "vars",
        E = "insertBefore",
        S = "newInline",
        x = "}",
        T = "parentNode",
        N = "cache",
        C = "locations",
        k = "substring",
        L = "orientationChange",
        A = "deviceType",
        O = "className",
        M = "gridZoomMap",
        _ = "object",
        D = " 0 0 ",
        P = "match",
        H = "isArray",
        B = "+*,",
        j = "replace",
        F = "grid",
        I = "head",
        q = "newElement",
        R = "indexOf",
        U = "canUseProperty_element",
        z = "_skel_isReversed",
        W = "push",
        X = "extend",
        V = "matchesMedia",
        $ = "containers",
        J = "onorientationchange",
        K = "lock",
        Q = "DOMReady",
        G = "defaults",
        Y = "addEventListener",
        Z = "getComputedStyle",
        et = "^head",
        tt = "{display:none!important}",
        nt = "registerLocation",
        rt = "parseMeasurement",
        it = "documentElement",
        st = "IEVersion",
        ot = "placeholder",
        ut = "events",
        at = "charAt",
        ft = "attachElements",
        lt = "isActive",
        ct = "attachElement",
        ht = "isStatic",
        pt = "plugins",
        dt = "text/css",
        vt = "DOMContentLoaded",
        mt = "states",
        gt = "_skel_attach",
        yt = "initial-scale=1",
        bt = "device-width",
        wt = "trigger",
        Et = "removeEventListener",
        St = "attached",
        xt = "normalize",
        Tt = "applyRowTransforms",
        Nt = "collapse",
        Ct = "(min-width: ",
        kt = "previousSibling",
        Lt = "change",
        At = "location",
        Ot = "resize",
        Mt = "media",
        _t = "html",
        Dt = "forceDefaultState",
        Pt = "_skel_placeholder",
        Ht = "style",
        Bt = "firstChild",
        jt = "split",
        Ft = "querySelectorAll",
        It = "max-height",
        qt = "min-height",
        Rt = "zoom",
        Ut = "min-width",
        zt = "innerHTML",
        Wt = "prototype",
        Xt = "max-width",
        Vt = "hasOwnProperty",
        $t = "domready",
        Jt = "nextSibling",
        Kt = "height=",
        Qt = "android",
        Gt = "priority",
        Yt = "onresize",
        Zt = ".\\3$1 ",
        en = "href",
        tn = "readyState",
        nn = {
            breakpoints: [],
            breakpointList: [],
            cache: {
                elements: {},
                states: {},
                stateElements: {}
            },
            config: {
                breakpoints: {
                    "*": {
                        href: u,
                        media: ""
                    }
                },
                containers: 1140,
                defaultState: l,
                events: {},
                grid: {
                    zoom: 1,
                    collapse: u,
                    gutters: [40, 0]
                },
                lock: {
                    path: u,
                    permanent: g
                },
                plugins: {},
                pollOnce: u,
                preload: u,
                reset: xt,
                RTL: u,
                viewport: {
                    width: bt,
                    height: "",
                    scalable: g
                }
            },
            css: {
                bm: "*,*:before,*:after{-moz-box-sizing:border-box;-webkit-box-sizing:border-box;box-sizing:border-box}",
                n: "html{font-family:sans-serif;-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%}body{margin:0}article,aside,details,figcaption,figure,footer,header,hgroup,main,menu,nav,section,summary{display:block}audio,canvas,progress,video{display:inline-block;vertical-align:baseline}audio:not([controls]){display:none;height:0}[hidden],template{display:none}a{background-color:transparent}a:active,a:hover{outline:0}abbr[title]{border-bottom:1px dotted}b,strong{font-weight:700}dfn{font-style:italic}h1{font-size:2em;margin:.67em 0}mark{background:#ff0;color:#000}small{font-size:80%}sub,sup{font-size:75%;line-height:0;position:relative;vertical-align:baseline}sup{top:-.5em}sub{bottom:-.25em}img{border:0}svg:not(:root){overflow:hidden}figure{margin:1em 40px}hr{-moz-box-sizing:content-box;box-sizing:content-box;height:0}pre{overflow:auto}code,kbd,pre,samp{font-family:monospace,monospace;font-size:1em}button,input,optgroup,select,textarea{color:inherit;font:inherit;margin:0}button{overflow:visible}button,select{text-transform:none}button,html input[type=button],input[type=reset],input[type=submit]{-webkit-appearance:button;cursor:pointer}button[disabled],html input[disabled]{cursor:default}button::-moz-focus-inner,input::-moz-focus-inner{border:0;padding:0}input{line-height:normal}input[type=checkbox],input[type=radio]{box-sizing:border-box;padding:0}input[type=number]::-webkit-inner-spin-button,input[type=number]::-webkit-outer-spin-button{height:auto}input[type=search]{-webkit-appearance:textfield;-moz-box-sizing:content-box;-webkit-box-sizing:content-box;box-sizing:content-box}input[type=search]::-webkit-search-cancel-button,input[type=search]::-webkit-search-decoration{-webkit-appearance:none}fieldset{border:1px solid silver;margin:0 2px;padding:.35em .625em .75em}legend{border:0;padding:0}textarea{overflow:auto}optgroup{font-weight:700}table{border-collapse:collapse;border-spacing:0}td,th{padding:0}",
                r: "html,body,div,span,applet,object,iframe,h1,h2,h3,h4,h5,h6,p,blockquote,pre,a,abbr,acronym,address,big,cite,code,del,dfn,em,img,ins,kbd,q,s,samp,small,strike,strong,sub,sup,tt,var,b,u,i,center,dl,dt,dd,ol,ul,li,fieldset,form,label,legend,table,caption,tbody,tfoot,thead,tr,th,td,article,aside,canvas,details,embed,figure,figcaption,footer,header,hgroup,menu,nav,output,ruby,section,summary,time,mark,audio,video{margin:0;padding:0;border:0;font-size:100%;font:inherit;vertical-align:baseline}article,aside,details,figcaption,figure,footer,header,hgroup,menu,nav,section{display:block}body{line-height:1}ol,ul{list-style:none}blockquote,q{quotes:none}blockquote:before,blockquote:after,q:before,q:after{content:'';content:none}table{border-collapse:collapse;border-spacing:0}body{-webkit-text-size-adjust:none}",
                gc: function(e) {
                    return ".\\31 2u" + e + ",.\\31 2u\\24" + e + "{width:100%;clear:none;margin-left:0}" + ".\\31 1u" + e + ",.\\31 1u\\24" + e + "{width:91.6666666667%;clear:none;margin-left:0}" + ".\\31 0u" + e + ",.\\31 0u\\24" + e + "{width:83.3333333333%;clear:none;margin-left:0}" + ".\\39 u" + e + ",.\\39 u\\24" + e + "{width:75%;clear:none;margin-left:0}" + ".\\38 u" + e + ",.\\38 u\\24" + e + "{width:66.6666666667%;clear:none;margin-left:0}" + ".\\37 u" + e + ",.\\37 u\\24" + e + "{width:58.3333333333%;clear:none;margin-left:0}" + ".\\36 u" + e + ",.\\36 u\\24" + e + "{width:50%;clear:none;margin-left:0}" + ".\\35 u" + e + ",.\\35 u\\24" + e + "{width:41.6666666667%;clear:none;margin-left:0}" + ".\\34 u" + e + ",.\\34 u\\24" + e + "{width:33.3333333333%;clear:none;margin-left:0}" + ".\\33 u" + e + ",.\\33 u\\24" + e + "{width:25%;clear:none;margin-left:0}" + ".\\32 u" + e + ",.\\32 u\\24" + e + "{width:16.6666666667%;clear:none;margin-left:0}" + ".\\31 u" + e + ",.\\31 u\\24" + e + "{width:8.3333333333%;clear:none;margin-left:0}" + ".\\31 2u\\24" + e + B + ".\\31 1u\\24" + e + B + ".\\31 0u\\24" + e + B + ".\\39 u\\24" + e + B + ".\\38 u\\24" + e + B + ".\\37 u\\24" + e + B + ".\\36 u\\24" + e + B + ".\\35 u\\24" + e + B + ".\\34 u\\24" + e + B + ".\\33 u\\24" + e + B + ".\\32 u\\24" + e + B + ".\\31 u\\24" + e + "+*{" + "clear:left;" + x + ".\\-11u" + e + "{margin-left:91.6666666667%}" + ".\\-10u" + e + "{margin-left:83.3333333333%}" + ".\\-9u" + e + "{margin-left:75%}" + ".\\-8u" + e + "{margin-left:66.6666666667%}" + ".\\-7u" + e + "{margin-left:58.3333333333%}" + ".\\-6u" + e + "{margin-left:50%}" + ".\\-5u" + e + "{margin-left:41.6666666667%}" + ".\\-4u" + e + "{margin-left:33.3333333333%}" + ".\\-3u" + e + "{margin-left:25%}" + ".\\-2u" + e + "{margin-left:16.6666666667%}" + ".\\-1u" + e + "{margin-left:8.3333333333%}"
                }
            },
            defaults: {
                breakpoint: {
                    config: l,
                    elements: l,
                    test: l
                },
                config_breakpoint: {
                    containers: "100%",
                    grid: {},
                    href: u,
                    media: "",
                    viewport: {}
                }
            },
            events: [],
            forceDefaultState: u,
            gridZoomMap: {
                k: {},
                v: {}
            },
            gridZoomMax: 1,
            isInit: u,
            isStatic: u,
            locations: {
                body: l,
                head: l,
                html: l
            },
            lcn: "_skel_lock",
            me: l,
            plugins: {},
            sd: "/",
            stateId: "",
            vars: {},
            DOMReady: l,
            getElementsByClassName: l,
            indexOf: l,
            isArray: l,
            iterate: l,
            matchesMedia: l,
            canUseProperty_element: l,
            canUseProperty: function(e) {
                nn[U] || (nn[U] = document[y]("div"));
                var t = nn[U][Ht],
                    n = e[at](0).toUpperCase() + e.slice(1);
                return e in t || "Moz" + n in t || "Webkit" + n in t || "O" + n in t || "ms" + n in t
            },
            extend: function(e, t) {
                var r;
                nn[n](t, function(n) {
                    nn[H](t[n]) ? (nn[H](e[n]) || (e[n] = []), nn[X](e[n], t[n])) : typeof t[n] == _ ? (typeof e[n] != _ && (e[n] = {}), nn[X](e[n], t[n])) : e[n] = t[n]
                })
            },
            getArray: function(e) {
                return nn[H](e) ? e : [e]
            },
            parseMeasurement: function(e) {
                var t, n;
                if (typeof e != "string") t = [e, "px"];
                else if (e == "fluid") t = [100, "%"];
                else {
                    var n;
                    n = e[P](/([0-9\.]+)([^\s]*)/), n[f] < 3 || !n[2] ? t = [parseFloat(e), "px"] : t = [parseFloat(n[1]), n[2]]
                }
                return t
            },
            canUse: function(t) {
                return nn[e][t] && nn[e][t].test()
            },
            hasActive: function(e) {
                var t = u;
                return nn[n](e, function(n) {
                    t = t || nn[lt](e[n])
                }), t
            },
            isActive: function(e) {
                return nn[R](nn[i], nn.sd + e) !== -1
            },
            isLocked: function() {
                return !!nn[w][K] && nn[H](nn[w][K])
            },
            lock: function(e, n) {
                nn[w][K] = [e, n], document.cookie = nn.lcn + "=" + nn[w][K].join("_") + (nn[t][K].path ? ";path=" + nn[t][K].path : "") + (nn[t][K].permanent ? ";expires=Tue, 19 Jan 2038 03:14:07 GMT" : ""), window[At].reload()
            },
            unlock: function() {
                nn[w][K] = l, document.cookie = nn.lcn + "=" + (nn[t][K].path ? ";path=" + nn[t][K].path : "") + ";expires=Thu, 01 Jan 1970 01:02:03 GMT", window[At].reload()
            },
            useActive: function(e) {
                if (typeof e !== _) return e;
                var t = l;
                return nn[n](e, function(n) {
                    if (t !== l) return;
                    nn[lt](n) && (t = e[n])
                }), t
            },
            wasActive: function(e) {
                return nn[R](nn[w].lastStateId, nn.sd + e) !== -1
            },
            applyRowTransforms: function(e) {
                nn[t].RTL && (nn.unreverseRows(), e[t][F][Nt] && nn.reverseRows());
                var r = "_skel_important",
                    i = [],
                    s, a;
                for (s = 1; s <= nn[c]; s++) a = nn[o]("important(" + nn[M].k[s] + ")"), nn[n](a, function(e) {
                    i[W](a[e])
                });
                a = nn[o]("important(collapse)"), nn[n](a, function(e) {
                    i[W](a[e])
                }), nn[n](i, function(n) {
                    if (n === f) return;
                    var s = i[n],
                        o = s[T],
                        a, l = u,
                        c, h;
                    if (!o) return;
                    if (!s[Vt](r) || s[r] === u) {
                        e[t][F][Nt] && s[O][P](/important\(collapse\)/) ? l = "c" : s[O][P](/important\((.+)\)/) && (h = parseInt(nn[M].v[RegExp.$1])) <= e[t][F][Rt] && (l = "z");
                        if (!l) return;
                        c = nn[t].RTL ? Jt : kt, a = s[c];
                        while (a && a.nodeName == "#text") a = a[c];
                        if (!a) return;
                        o[E](s, nn[t].RTL && l == "z" ? o.lastChild : o[Bt]), s[r] = {
                            placeholder: a,
                            mode: l,
                            zoom: h
                        }
                    } else {
                        a = s[r][ot], l = s[r].mode;
                        if (l == "c" && e[t][F][Nt] || l == "z" && s[r][Rt] <= e[t][F][Rt]) return;
                        o[E](s, nn[t].RTL && l == "z" ? a[kt] : a[Jt]), s[r] = u
                    }
                })
            },
            reverseRows: function() {
                var e = nn[o]("row");
                nn[n](e, function(t) {
                    if (t === f) return;
                    var n = e[t];
                    if (n[z]) return;
                    var r = n.children,
                        i;
                    for (i = 1; i < r[f]; i++) n[E](r[i], r[0]);
                    n[z] = g
                })
            },
            unreverseRows: function() {
                var e = nn[o]("row");
                nn[n](e, function(t) {
                    if (t === f) return;
                    var n = e[t];
                    if (!n[z]) return;
                    var r = n.children,
                        i;
                    for (i = 1; i < r[f]; i++) n[E](r[i], r[0]);
                    n[z] = u
                })
            },
            bind: function(e, t) {
                return nn.on(e, t)
            },
            on: function(e, t) {
                nn[ut][e] || (nn[ut][e] = []), nn[ut][e][W](t), nn.isInit && (e == Lt ? t() : e[at](0) == "+" && nn[lt](e[k](1)) && t())
            },
            change: function(e) {
                nn.on(Lt, e)
            },
            trigger: function(e) {
                if (!nn[ut][e] || nn[ut][e][f] == 0) return;
                var t;
                nn[n](nn[ut][e], function(t) {
                    nn[ut][e][t]()
                })
            },
            registerLocation: function(e, t) {
                e == I ? t[gt] = function(e, t) {
                    t ? this[E](e, this[Bt]) : this === nn.me[T] ? this[E](e, nn.me) : this.appendChild(e)
                } : t[gt] = function(e, t) {
                    t ? this[E](e, this[Bt]) : this.appendChild(e)
                }, nn[C][e] = t
            },
            addCachedElementToBreakpoint: function(t, n) {
                nn[e][t] && nn[e][t][r][W](n)
            },
            addCachedElementToState: function(e, t) {
                nn[N][s][e] ? nn[N][s][e][W](t) : nn[N][s][e] = [t]
            },
            attachElement: function(e) {
                var t, n = e[At],
                    r = u;
                return e[St] ? g : (n[0] == "^" && (n = n[k](1), r = g), n in nn[C] ? (t = nn[C][n], t[gt](e[_], r), e[St] = g, e.onAttach && e.onAttach(), g) : u)
            },
            attachElements: function(e) {
                var t = [],
                    r = [],
                    i, s, o;
                nn[n](e, function(n) {
                    t[e[n][Gt]] || (t[e[n][Gt]] = []), t[e[n][Gt]][W](e[n])
                }), nn[n](t, function(e) {
                    if (t[e][f] == 0) return;
                    nn[n](t[e], function(n) {
                        nn[ct](t[e][n]) || r[W](t[e][n])
                    })
                }), r[f] > 0 && nn[Q](function() {
                    nn[n](r, function(e) {
                        nn[ct](r[e])
                    })
                })
            },
            cacheElement: function(e) {
                return nn[N][r][e.id] = e, e
            },
            cacheNewElement: function(e, t, n, r) {
                var i;
                return t[T] && t[T].removeChild(t), i = nn[q](e, t, n, r), nn.cacheElement(i)
            },
            detachAllElements: function(e) {
                var t, i, s = {};
                nn[n](e, function(t) {
                    s[e[t].id] = g
                }), nn[n](nn[N][r], function(e) {
                    if (e in s) return;
                    nn.detachElement(e)
                })
            },
            detachElement: function(e) {
                var t = nn[N][r][e],
                    n;
                if (!t[St]) return;
                n = t[_];
                if (!n[T] || n[T] && !n[T].tagName) return;
                n[T].removeChild(n), t[St] = u, t.onDetach && t.onDetach()
            },
            getCachedElement: function(e) {
                return nn[N][r][e] ? nn[N][r][e] : l
            },
            newElement: function(e, t, n, r) {
                return {
                    id: e,
                    object: t,
                    location: n,
                    priority: r,
                    attached: u
                }
            },
            removeCachedElementFromBreakpoint: function(t, i) {
                return nn[n](nn[e][t][r], function(n) {
                    nn[e][t][r][n].id == i && delete nn[e][t][r][n]
                }), g
            },
            removeCachedElementFromState: function(e, t) {
                return nn[n](nn[N][s][e], function(n) {
                    nn[N][s][e][n].id == t && delete nn[N][s][e][n]
                }), g
            },
            uncacheElement: function(e) {
                return e in nn[N][r] ? (delete nn[N][r][e], g) : u
            },
            changeState: function(o) {
                var a, l, c, y, E, T, C, L, A;
                nn[w].lastStateId = nn[i], nn[i] = o;
                if (!nn[N][mt][nn[i]]) {
                    nn[N][mt][nn[i]] = {
                        config: {},
                        elements: [],
                        values: {}
                    }, c = nn[N][mt][nn[i]], nn[i] === nn.sd ? a = [] : a = nn[i][k](1)[jt](nn.sd), nn[X](c[t], nn[G][m]), nn[n](a, function(n) {
                        nn[X](c[t], nn[e][a[n]][t])
                    }), C = "mV" + nn[i], c[t][p].content ? L = c[t][p].content : nn.isLocked() ? (y = [], y[W]("user-scalable=yes"), nn[w][K][0] && y[W]("width=" + nn[w][K][0]), nn[w][K][1] && y[W](Kt + nn[w][K][1]), L = y.join(","), window.setTimeout(function() {
                        nn.poll()
                    }, 0)) : (y = [], y[W]("user-scalable=" + (c[t][p].scalable ? "yes" : "no")), c[t][p].width && y[W]("width=" + c[t][p].width), c[t][p].height && y[W](Kt + c[t][p].height), c[t][p].width == bt && y[W](yt), L = y.join(",")), (E = nn[h](C)) || (E = nn[v](C, nn.newMeta(p, L), et, 4)), c[r][W](E);
                    var O, _, P = u;
                    y = nn[rt](c[t][$]), O = y[0], _ = y[1], c.values[$] = O + _, C = "iC" + c.values[$], _.substr(-1) == "!" && (P = g, _ = _.substr(0, _[f] - 1)), (E = nn[h](C)) || (E = nn[v](C, nn[S](".container{margin-left:auto;margin-right:auto;width:" + O * 1 + _ + (P ? "!important;max-width:none!important;min-width:0!important" + x : x + ".container.\\31 25\\25{width:100%;max-width:" + O * 1.25 + _ + ";min-width:" + O + _ + x + ".container.\\37 5\\25{width:" + O * .75 + _ + x + ".container.\\35 0\\25{width:" + O * .5 + _ + x + ".container.\\32 5\\25{width:" + O * .25 + _ + x)), I, 3)), c[r][W](E), C = "iGG" + c[t][F][b][0] + "_" + c[t][F][b][1];
                    if (!(E = nn[h](C))) {
                        var H, B;
                        y = nn[rt](c[t][F][b][0]), H = y[0], B = y[1];
                        var q, U;
                        y = nn[rt](c[t][F][b][1]), q = y[0], U = y[1], E = nn[v]("iGG" + c[t][F][b][0] + "_" + c[t][F][b][1], nn[S](".row>*{padding:" + q * 1 + U + D + H * 1 + B + x + ".row{margin:" + q * -1 + U + d + H * -1 + B + x + ".row.uniform>*{padding:" + H * 1 + B + D + H * 1 + B + x + ".row.uniform{margin:" + H * -1 + B + d + H * -1 + B + x + ".row.\\32 00\\25>*{padding:" + q * 2 + U + D + H * 2 + B + x + ".row.\\32 00\\25{margin:" + q * -2 + U + d + H * -2 + B + x + ".row.uniform.\\32 00\\25>*{padding:" + H * 2 + B + D + H * 2 + B + x + ".row.uniform.\\32 00\\25{margin:" + H * -2 + B + d + H * -2 + B + x + ".row.\\31 50\\25>*{padding:" + q * 1.5 + U + D + H * 1.5 + B + x + ".row.\\31 50\\25{margin:" + q * -1.5 + U + d + H * -1.5 + B + x + ".row.uniform.\\31 50\\25>*{padding:" + H * 1.5 + B + D + H * 1.5 + B + x + ".row.uniform.\\31 50\\25{margin:" + H * -1.5 + B + d + H * -1.5 + B + x + ".row.\\35 0\\25>*{padding:" + q * .5 + U + D + H * .5 + B + x + ".row.\\35 0\\25{margin:" + q * -0.5 + U + d + H * -0.5 + B + x + ".row.uniform.\\35 0\\25>*{padding:" + H * .5 + B + D + H * .5 + B + x + ".row.uniform.\\35 0\\25{margin:" + H * -0.5 + B + d + H * -0.5 + B + x + ".row.\\32 5\\25>*{padding:" + q * .25 + U + D + H * .25 + B + x + ".row.\\32 5\\25{margin:" + q * -0.25 + U + d + H * -0.25 + B + x + ".row.uniform.\\32 5\\25>*{padding:" + H * .25 + B + D + H * .25 + B + x + ".row.uniform.\\32 5\\25{margin:" + H * -0.25 + B + d + H * -0.25 + B + x + ".row.\\30 \\25>*{padding:0}" + ".row.\\30 \\25{margin:0 0 -1px 0}"), I, 3)
                    }
                    c[r][W](E);
                    if (c[t][F][Rt] > 1) {
                        C = "igZ" + c[t][F][Rt];
                        if (!(E = nn[h](C))) {
                            L = "";
                            for (T = 2; T <= c[t][F][Rt]; T++) L += nn.css.gc("\\28 " + nn[M].k[T] + "\\29");
                            E = nn[v](C, nn[S](L), I, 3)
                        }
                        c[r][W](E)
                    }
                    c[t][F][Nt] && (C = "igC" + c[t][$], (E = nn[h](C)) || (E = nn[v](C, nn[S](".row:not(.no-collapse)>*{width:100%!important;margin-left:0!important" + x), I, 3)), c[r][W](E));
                    if (!nn[ht]) {
                        C = "iCd" + nn[i];
                        if (!(E = nn[h](C))) {
                            L = [], A = [], nn[n](nn[e], function(e) {
                                nn[R](a, e) !== -1 ? L[W](".not-" + e) : A[W](".only-" + e)
                            });
                            var z = (L[f] > 0 ? L.join(",") + tt : "") + (A[f] > 0 ? A.join(",") + tt : "");
                            E = nn[v](C, nn[S](z[j](/\.([0-9])/, Zt)), I, 3), c[r][W](E)
                        }
                    }
                    nn[n](a, function(i) {
                        nn[e][a[i]][t][en] && (C = "ss" + a[i], (E = nn[h](C)) || (E = nn[v](C, nn.newStyleSheet(nn[e][a[i]][t][en]), I, 5)), c[r][W](E)), nn[e][a[i]][r][f] > 0 && nn[n](nn[e][a[i]][r], function(t) {
                            c[r][W](nn[e][a[i]][r][t])
                        })
                    }), nn[N][s][nn[i]] && (nn[n](nn[N][s][nn[i]], function(e) {
                        c[r][W](nn[N][s][nn[i]][e])
                    }), nn[N][s][nn[i]] = [])
                } else c = nn[N][mt][nn[i]];
                nn.detachAllElements(c[r]), nn[ft](c[r]), nn[Q](function() {
                    nn[Tt](c)
                }), nn[w].state = nn[N][mt][nn[i]], nn[w][i] = nn[i], nn[wt](Lt), nn[n](nn[e], function(e) {
                    nn[lt](e) ? nn.wasActive(e) || nn[wt]("+" + e) : nn.wasActive(e) && nn[wt]("-" + e)
                })
            },
            getStateId: function() {
                if (nn[Dt] && nn[t].defaultState) return nn[t].defaultState;
                var r = "";
                return nn[n](nn[e], function(t) {
                    nn[e][t].test() && (r += nn.sd + t)
                }), r
            },
            poll: function() {
                var e = "";
                e = nn.getStateId(), e === "" && (e = nn.sd), e !== nn[i] && (nn[ht] ? nn.changeState(e) : (nn[C][_t][O] = nn[C][_t][O][j](nn[i][k](1)[j](new RegExp(nn.sd, "g"), " "), ""), nn.changeState(e), nn[C][_t][O] = nn[C][_t][O] + " " + nn[i][k](1)[j](new RegExp(nn.sd, "g"), " "), nn[C][_t][O][at](0) == " " && (nn[C][_t][O] = nn[C][_t][O][k](1))))
            },
            updateState: function() {
                var t, o, u, a, l = [];
                if (nn[i] == nn.sd) return;
                t = nn[i][k](1)[jt](nn.sd), nn[n](t, function(s) {
                    o = nn[e][t[s]];
                    if (o[r][f] == 0) return;
                    nn[n](o[r], function(e) {
                        nn[N][mt][nn[i]][r][W](o[r][e]), l[W](o[r][e])
                    })
                }), nn[N][s][nn[i]] && (nn[n](nn[N][s][nn[i]], function(e) {
                    nn[N][mt][nn[i]][r][W](nn[N][s][nn[i]][e]), l[W](nn[N][s][nn[i]][e])
                }), nn[N][s][nn[i]] = []), l[f] > 0 && nn[ft](l)
            },
            newDiv: function(e) {
                var t = document[y]("div");
                return t[zt] = e, t
            },
            newInline: function(e) {
                var t;
                return t = document[y](Ht), t.type = dt, t[zt] = e, t
            },
            newMeta: function(e, t) {
                var n = document[y]("meta");
                return n.name = e, n.content = t, n
            },
            newStyleSheet: function(e) {
                var t = document[y]("link");
                var stat = "static/happenings/baseline/"
                return t.rel = "stylesheet", t.type = dt, t[en] = stat + e, t
                // return t.rel = "stylesheet", t.type = dt, t[en] = e, t 
                // the original
            },
            initPlugin: function(e, n) {
                typeof n == _ && nn[X](e[t], n), e.init && e.init()
            },
            registerPlugin: function(e, t) {
                if (!t) return u;
                nn[pt][e] = t, t._ = this, t.register && t.register()
            },
            init: function(e, r) {
                nn.initConfig(e), nn.initElements(), nn.initEvents(), nn.poll(), r && typeof r == _ && (nn[t][pt] = r), nn[n](nn[pt], function(e) {
                    nn.initPlugin(nn[pt][e], e in nn[t][pt] ? nn[t][pt][e] : l)
                }), nn.isInit = g
            },
            initAPI: function() {
                var e, t, r = navigator.userAgent;
                nn[w][st] = 99, e = "other", r[P](/Firefox/) ? e = "firefox" : r[P](/Chrome/) ? e = "chrome" : r[P](/Safari/) && !r[P](/Chrome/) ? e = "safari" : r[P](/(OPR|Opera)/) ? e = "opera" : r[P](/MSIE ([0-9]+)/) ? (e = "ie", nn[w][st] = RegExp.$1) : r[P](/Trident\/.+rv:([0-9]+)/) && (e = "ie", nn[w][st] = RegExp.$1), nn[w].browser = e, nn[w][A] = "other", t = {
                    ios: "(iPad|iPhone|iPod)",
                    android: "Android",
                    mac: "Macintosh",
                    wp: "Windows Phone",
                    windows: "Windows NT"
                }, nn[n](t, function(e) {
                    r[P](new RegExp(t[e], "g")) && (nn[w][A] = e)
                });
                switch (nn[w][A]) {
                    case "ios":
                        r[P](/([0-9_]+) like Mac OS X/), e = parseFloat(RegExp.$1[j]("_", ".")[j]("_", ""));
                        break;
                    case Qt:
                        r[P](/Android ([0-9\.]+)/), e = parseFloat(RegExp.$1);
                        break;
                    case "mac":
                        r[P](/Mac OS X ([0-9_]+)/), e = parseFloat(RegExp.$1[j]("_", ".")[j]("_", ""));
                        break;
                    case "wp":
                        r[P](/IEMobile\/([0-9\.]+)/), e = parseFloat(RegExp.$1);
                        break;
                    case "windows":
                        r[P](/Windows NT ([0-9\.]+)/), e = parseFloat(RegExp.$1);
                        break;
                    default:
                        e = 99
                }
                nn[w].deviceVersion = e, nn[w].isTouch = nn[w][A] == "wp" ? navigator.msMaxTouchPoints > 0 : "ontouchstart" in window, nn[w].isMobile = nn[w][A] == "wp" || nn[w][A] == Qt || nn[w][A] == "ios", e = document.cookie[jt](";"), nn[n](e, function(t) {
                    var n = e[t][jt]("=");
                    if (n[0][j](/^\s+|\s+$/g, "") == nn.lcn && n[1][f] > 0) {
                        nn[w][K] = n[1][jt]("_");
                        return
                    }
                })
            },
            initConfig: function(i) {
                var s = [],
                    o = [],
                    l;
                if (!i || !(e in i)) nn[ht] = g, nn[t][p].width = "", nn[t][p].height = "", nn[t][p].scalable = g;
                typeof i == _ && (i[e] && (nn[t][e] = {}), nn[X](nn[t], i)), F in nn[t] && b in nn[t][F] && !nn[H](nn[t][F][b]) && (nn[t][F][b] = [nn[t][F][b], nn[t][F][b]]), nn[X](nn[G][m][F], nn[t][F]), nn[c] = Math.max(nn[c], nn[t][F][Rt]), nn[X](nn[G][m][p], nn[t][p]), nn[G][m][$] = nn[t][$], nn[n](nn[t][e], function(n) {
                    var i, s = {},
                        u, a;
                    nn[X](s, nn[t][e][n]), en in s || (s[en] = nn[G][m][en]), Mt in s || (s[Mt] = nn[G][m][Mt]), "range" in s && (u = s.range, u == "*" ? a = "" : u[at](0) == "-" ? a = "(max-width: " + parseInt(u[k](1)) + "px)" : u[at](u[f] - 1) == "-" ? a = Ct + parseInt(u[k](0, u[f] - 1)) + "px)" : nn[R](u, "-") != -1 && (u = u[jt]("-"), a = Ct + parseInt(u[0]) + "px) and (max-width: " + parseInt(u[1]) + "px)"), s[Mt] = a), F in s && (b in s[F] && !nn[H](s[F][b]) && (s[F][b] = [s[F][b], s[F][b]]), Rt in s[F] && (nn[c] = Math.max(nn[c], s[F][Rt]))), nn[t][e][n] = s, i = {}, nn[X](i, nn[G].breakpoint), i[t] = nn[t][e][n], i.test = function() {
                        return nn[V](s[Mt])
                    }, i[r] = [], nn[t].preload && i[t][en] && o[W](i[t][en]), nn[e][n] = i, nn.breakpointList[W](n)
                });
                if (nn[c] > 1 || nn[ht])
                    for (l = 2; l <= nn[c]; l++) nn[M].k[l] = nn[M].v[l] = l;
                else nn[n](nn[t][e], function(n) {
                    var r = nn[t][e][n];
                    nn[c] ++, F in r || (r[F] = {}), r[F][Rt] = nn[c], nn[M].k[nn[c]] = n, nn[M].v[n] = nn[c]
                });
                nn[n](nn[t][ut], function(e) {
                    nn.on(e, nn[t][ut][e])
                }), o[f] > 0 && window[At].protocol != "file:" && nn[Q](function() {
                    var e, t = document[a](I)[0],
                        r = new XMLHttpRequest;
                    nn[n](o, function(e) {
                        r.open("GET", o[e], u), r.send("")
                    })
                })
            },
            initElements: function() {
                var e = [];
                e[W](nn[q]("mV", nn.newMeta(p, yt), et, 1));
                switch (nn[t].reset) {
                    case "full":
                        e[W](nn[q]("iR", nn[S](nn.css.r), et, 2));
                        break;
                    case xt:
                        e[W](nn[q]("iN", nn[S](nn.css.n), et, 2))
                }
                e[W](nn[q]("iBM", nn[S](nn.css.bm), et, 1)), e[W](nn[q]("iG", nn[S]('.row{border-bottom:solid 1px transparent}.row>*{float:left}.row:after,.row:before{content:"";display:block;clear:both;height:0}.row.uniform>*>:first-child{margin-top:0}.row.uniform>*>:last-child{margin-bottom:0}' + nn.css.gc("")), I, 3)), nn[ft](e)
            },
            initEvents: function() {
                var e;
                !nn[t].pollOnce && !nn[ht] && (nn.on(Ot, function() {
                    nn.poll()
                }), nn.on(L, function() {
                    nn.poll()
                })), nn[w][A] == "ios" && nn[Q](function() {
                    nn.on(L, function() {
                        var e = document[a]("input");
                        nn[n](e, function(t) {
                            e[t][Pt] = e[t][ot], e[t][ot] = ""
                        }), window.setTimeout(function() {
                            nn[n](e, function(t) {
                                e[t][ot] = e[t][Pt]
                            })
                        }, 100)
                    })
                }), window[Yt] && nn.on(Ot, window[Yt]), window[Yt] = function() {
                    nn[wt](Ot)
                }, window[J] && nn.on(L, window[J]), window[J] = function() {
                    nn[wt](L)
                }
            },
            initUtilityMethods: function() {
                document[Y] ? ! function(e, t) {
                    nn[Q] = t()
                }($t, function() {
                    function e(e) {
                        s = 1;
                        while (e = t.shift()) e()
                    }
                    var t = [],
                        n, r = document,
                        i = vt,
                        s = /^loaded|^c/.test(r[tn]);
                    return r[Y](i, n = function() {
                            r[Et](i, n), e()
                        }),
                        function(e) {
                            s ? e() : t[W](e)
                        }
                }) : ! function(e, t) {
                    nn[Q] = t()
                }($t, function(e) {
                    function t(e) {
                        p = 1;
                        while (e = n.shift()) e()
                    }
                    var n = [],
                        r, i = !1,
                        s = document,
                        o = s[it],
                        u = o.doScroll,
                        a = vt,
                        f = Y,
                        l = "onreadystatechange",
                        c = tn,
                        h = u ? /^loaded|^c/ : /^loaded|c/,
                        p = h.test(s[c]);
                    return s[f] && s[f](a, r = function() {
                        s[Et](a, r, i), t()
                    }, i), u && s.attachEvent(l, r = function() {
                        /^c/.test(s[c]) && (s.detachEvent(l, r), t())
                    }), e = u ? function(t) {
                        self != top ? p ? t() : n[W](t) : function() {
                            try {
                                o.doScroll("left")
                            } catch (n) {
                                return setTimeout(function() {
                                    e(t)
                                }, 50)
                            }
                            t()
                        }()
                    } : function(e) {
                        p ? e() : n[W](e)
                    }
                }), document[o] ? nn[o] = function(e) {
                    return document[o](e)
                } : nn[o] = function(e) {
                    var t = document;
                    return t[Ft] ? t[Ft](("." + e[j](" ", " ."))[j](/\.([0-9])/, Zt)) : []
                }, Array[Wt][R] ? nn[R] = function(e, t) {
                    return e[R](t)
                } : nn[R] = function(e, t) {
                    if (typeof e == "string") return e[R](t);
                    var n, r = t ? t : 0,
                        i;
                    if (!this) throw new TypeError;
                    i = this[f];
                    if (i === 0 || r >= i) return -1;
                    r < 0 && (r = i - Math.abs(r));
                    for (n = r; n < i; n++)
                        if (this[n] === e) return n;
                    return -1
                }, Array[H] ? nn[H] = function(e) {
                    return Array[H](e)
                } : nn[H] = function(e) {
                    return Object[Wt].toString.call(e) === "[object Array]"
                }, Object.keys ? nn[n] = function(e, t) {
                    if (!e) return [];
                    var n, r = Object.keys(e);
                    for (n = 0; r[n]; n++) t(r[n])
                } : nn[n] = function(e, t) {
                    if (!e) return [];
                    var n;
                    for (n in e) Object[Wt][Vt].call(e, n) && t(n)
                }, window.matchMedia ? nn[V] = function(e) {
                    return e == "" ? g : window.matchMedia(e).matches
                } : window.styleMedia || window[Mt] ? nn[V] = function(e) {
                    if (e == "") return g;
                    var t = window.styleMedia || window[Mt];
                    return t.matchMedium(e || "all")
                } : window[Z] ? nn[V] = function(e) {
                    if (e == "") return g;
                    var t = document[y](Ht),
                        n = document[a]("script")[0],
                        r = l;
                    t.type = dt, t.id = "matchmediajs-test", n[T][E](t, n), r = Z in window && window[Z](t, l) || t.currentStyle;
                    var i = "@media " + e + "{ #matchmediajs-test { width: 1px; } }";
                    return t.styleSheet ? t.styleSheet.cssText = i : t.textContent = i, r.width === "1px"
                } : (nn[Dt] = g, nn[V] = function(e) {
                    if (e == "") return g;
                    var t, n, r, i, s = {
                            "min-width": l,
                            "max-width": l
                        },
                        o = u;
                    n = e[jt](/\s+and\s+/);
                    for (i in n) t = n[i], t[at](0) == "(" && (t = t[k](1, t[f] - 1), r = t[jt](/:\s+/), r[f] == 2 && (s[r[0][j](/^\s+|\s+$/g, "")] = parseInt(r[1]), o = g));
                    if (!o) return u;
                    var a = document[it].clientWidth,
                        c = document[it].clientHeight;
                    return s[Ut] !== l && a < s[Ut] || s[Xt] !== l && a > s[Xt] || s[qt] !== l && c < s[qt] || s[It] !== l && c > s[It] ? u : g
                })
            },
            preInit: function() {
                var e = document[a]("script");
                nn.me = e[e[f] - 1], nn.initUtilityMethods(), nn.initAPI(), nn[nt](_t, document[a](_t)[0]), nn[nt](I, document[a](I)[0]), nn[Q](function() {
                    nn[nt]("body", document[a]("body")[0])
                }), nn[w].browser == "ie" && nn[w][st] >= 10 && nn[ct](nn[q]("msie-viewport-fix", nn[S]("@-ms-viewport{width:device-width}"), et, 1))
            }
        };
    return nn.preInit(), nn[w][st] < 9 && (nn[Tt] = function(e) {}, nn[S] = function(e) {
        var t;
        return t = document[y]("span"), t[zt] = '&nbsp;<style type="text/css">' + e + "</style>", t
    }), nn
}();
(function(e, t) {
    typeof define == "function" && define.amd ? define([], t) : typeof exports == "object" ? module.exports = t() : e.skel = t()
})(this, function() {
    return skel
});