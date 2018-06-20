(function(){var l,aa="function"==typeof Object.create?Object.create:function(a){function b(){}
b.prototype=a;return new b},ba;
if("function"==typeof Object.setPrototypeOf)ba=Object.setPrototypeOf;else{var ca;a:{var da={wa:!0},ea={};try{ea.__proto__=da;ca=ea.wa;break a}catch(a){}ca=!1}ba=ca?function(a,b){a.__proto__=b;if(a.__proto__!==b)throw new TypeError(a+" is not extensible");return a}:null}var fa=ba;
function n(a,b){a.prototype=aa(b.prototype);a.prototype.constructor=a;if(fa)fa(a,b);else for(var c in b)if("prototype"!=c)if(Object.defineProperties){var d=Object.getOwnPropertyDescriptor(b,c);d&&Object.defineProperty(a,c,d)}else a[c]=b[c];a.u=b.prototype}
var ha="function"==typeof Object.defineProperties?Object.defineProperty:function(a,b,c){a!=Array.prototype&&a!=Object.prototype&&(a[b]=c.value)},ia="undefined"!=typeof window&&window===this?this:"undefined"!=typeof global&&null!=global?global:this;
function ja(a){if(a){for(var b=ia,c=["Reflect","construct"],d=0;d<c.length-1;d++){var e=c[d];e in b||(b[e]={});b=b[e]}c=c[c.length-1];d=b[c];a=a(d);a!=d&&null!=a&&ha(b,c,{configurable:!0,writable:!0,value:a})}}
var ka=function(){function a(){function a(){}
Reflect.construct(a,[],function(){});
return new a instanceof a}
if("undefined"!=typeof Reflect&&Reflect.construct){if(a())return Reflect.construct;var b=Reflect.construct;return function(a,d,e){a=b(a,d);e&&Reflect.setPrototypeOf(a,e.prototype);return a}}return function(a,b,e){void 0===e&&(e=a);
e=aa(e.prototype||Object.prototype);return Function.prototype.apply.call(a,e,b)||e}}();
ja(function(){return ka});
var p=this;function q(a){return void 0!==a}
function r(a){return"string"==typeof a}
function la(a){return"number"==typeof a}
function t(a,b,c){a=a.split(".");c=c||p;a[0]in c||!c.execScript||c.execScript("var "+a[0]);for(var d;a.length&&(d=a.shift());)!a.length&&q(b)?c[d]=b:c[d]&&c[d]!==Object.prototype[d]?c=c[d]:c=c[d]={}}
function v(a,b){for(var c=a.split("."),d=b||p,e=0;e<c.length;e++)if(d=d[c[e]],null==d)return null;return d}
function ma(){}
function na(a){a.ga=void 0;a.getInstance=function(){return a.ga?a.ga:a.ga=new a}}
function oa(a){var b=typeof a;if("object"==b)if(a){if(a instanceof Array)return"array";if(a instanceof Object)return b;var c=Object.prototype.toString.call(a);if("[object Window]"==c)return"object";if("[object Array]"==c||"number"==typeof a.length&&"undefined"!=typeof a.splice&&"undefined"!=typeof a.propertyIsEnumerable&&!a.propertyIsEnumerable("splice"))return"array";if("[object Function]"==c||"undefined"!=typeof a.call&&"undefined"!=typeof a.propertyIsEnumerable&&!a.propertyIsEnumerable("call"))return"function"}else return"null";
else if("function"==b&&"undefined"==typeof a.call)return"object";return b}
function w(a){return"array"==oa(a)}
function pa(a){var b=oa(a);return"array"==b||"object"==b&&"number"==typeof a.length}
function qa(a){return"function"==oa(a)}
function ra(a){var b=typeof a;return"object"==b&&null!=a||"function"==b}
var sa="closure_uid_"+(1E9*Math.random()>>>0),ta=0;function ua(a,b,c){return a.call.apply(a.bind,arguments)}
function va(a,b,c){if(!a)throw Error();if(2<arguments.length){var d=Array.prototype.slice.call(arguments,2);return function(){var c=Array.prototype.slice.call(arguments);Array.prototype.unshift.apply(c,d);return a.apply(b,c)}}return function(){return a.apply(b,arguments)}}
function x(a,b,c){Function.prototype.bind&&-1!=Function.prototype.bind.toString().indexOf("native code")?x=ua:x=va;return x.apply(null,arguments)}
function y(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var b=c.slice();b.push.apply(b,arguments);return a.apply(this,b)}}
var z=Date.now||function(){return+new Date};
function A(a,b){function c(){}
c.prototype=b.prototype;a.u=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.ab=function(a,c,f){for(var d=Array(arguments.length-2),e=2;e<arguments.length;e++)d[e-2]=arguments[e];return b.prototype[c].apply(a,d)}}
;function B(a){if(Error.captureStackTrace)Error.captureStackTrace(this,B);else{var b=Error().stack;b&&(this.stack=b)}a&&(this.message=String(a))}
A(B,Error);B.prototype.name="CustomError";var wa=Array.prototype.indexOf?function(a,b){return Array.prototype.indexOf.call(a,b,void 0)}:function(a,b){if(r(a))return r(b)&&1==b.length?a.indexOf(b,0):-1;
for(var c=0;c<a.length;c++)if(c in a&&a[c]===b)return c;return-1},C=Array.prototype.forEach?function(a,b,c){Array.prototype.forEach.call(a,b,c)}:function(a,b,c){for(var d=a.length,e=r(a)?a.split(""):a,f=0;f<d;f++)f in e&&b.call(c,e[f],f,a)},xa=Array.prototype.filter?function(a,b){return Array.prototype.filter.call(a,b,void 0)}:function(a,b){for(var c=a.length,d=[],e=0,f=r(a)?a.split(""):a,g=0;g<c;g++)if(g in f){var h=f[g];
b.call(void 0,h,g,a)&&(d[e++]=h)}return d},ya=Array.prototype.map?function(a,b){return Array.prototype.map.call(a,b,void 0)}:function(a,b){for(var c=a.length,d=Array(c),e=r(a)?a.split(""):a,f=0;f<c;f++)f in e&&(d[f]=b.call(void 0,e[f],f,a));
return d};
function za(a,b){a:{var c=a.length;for(var d=r(a)?a.split(""):a,e=0;e<c;e++)if(e in d&&b.call(void 0,d[e],e,a)){c=e;break a}c=-1}return 0>c?null:r(a)?a.charAt(c):a[c]}
function Aa(a,b){var c=wa(a,b);0<=c&&Array.prototype.splice.call(a,c,1)}
function Ba(a){var b=a.length;if(0<b){for(var c=Array(b),d=0;d<b;d++)c[d]=a[d];return c}return[]}
function Ea(a,b){for(var c=1;c<arguments.length;c++){var d=arguments[c];if(pa(d)){var e=a.length||0,f=d.length||0;a.length=e+f;for(var g=0;g<f;g++)a[e+g]=d[g]}else a.push(d)}}
;var Fa=String.prototype.trim?function(a){return a.trim()}:function(a){return/^[\s\xa0]*([\s\S]*?)[\s\xa0]*$/.exec(a)[1]};
function Ga(a){if(!Ha.test(a))return a;-1!=a.indexOf("&")&&(a=a.replace(Ia,"&amp;"));-1!=a.indexOf("<")&&(a=a.replace(Ja,"&lt;"));-1!=a.indexOf(">")&&(a=a.replace(Ka,"&gt;"));-1!=a.indexOf('"')&&(a=a.replace(La,"&quot;"));-1!=a.indexOf("'")&&(a=a.replace(Ma,"&#39;"));-1!=a.indexOf("\x00")&&(a=a.replace(Na,"&#0;"));return a}
var Ia=/&/g,Ja=/</g,Ka=/>/g,La=/"/g,Ma=/'/g,Na=/\x00/g,Ha=/[\x00&<>"']/;function Oa(a){for(var b=0,c=0;c<a.length;++c)b=31*b+a.charCodeAt(c)>>>0;return b}
;var Ra;a:{var Sa=p.navigator;if(Sa){var Ta=Sa.userAgent;if(Ta){Ra=Ta;break a}}Ra=""}function D(a){return-1!=Ra.indexOf(a)}
;function Ua(a,b){for(var c in a)b.call(void 0,a[c],c,a)}
function Va(a,b){var c=pa(b),d=c?b:arguments;for(c=c?0:1;c<d.length;c++){if(null==a)return;a=a[d[c]]}return a}
function Wa(a){var b=Xa,c;for(c in b)if(a.call(void 0,b[c],c,b))return c}
function Ya(a){for(var b in a)return!1;return!0}
function Za(a,b){if(null!==a&&b in a)throw Error('The object already contains the key "'+b+'"');a[b]=!0}
function $a(a){var b={},c;for(c in a)b[c]=a[c];return b}
var ab="constructor hasOwnProperty isPrototypeOf propertyIsEnumerable toLocaleString toString valueOf".split(" ");function bb(a,b){for(var c,d,e=1;e<arguments.length;e++){d=arguments[e];for(c in d)a[c]=d[c];for(var f=0;f<ab.length;f++)c=ab[f],Object.prototype.hasOwnProperty.call(d,c)&&(a[c]=d[c])}}
;var cb=D("Opera"),db=D("Trident")||D("MSIE"),eb=D("Edge"),fb=D("Gecko")&&!(-1!=Ra.toLowerCase().indexOf("webkit")&&!D("Edge"))&&!(D("Trident")||D("MSIE"))&&!D("Edge"),gb=-1!=Ra.toLowerCase().indexOf("webkit")&&!D("Edge");function hb(){var a=p.document;return a?a.documentMode:void 0}
var ib;a:{var jb="",kb=function(){var a=Ra;if(fb)return/rv:([^\);]+)(\)|;)/.exec(a);if(eb)return/Edge\/([\d\.]+)/.exec(a);if(db)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a);if(gb)return/WebKit\/(\S+)/.exec(a);if(cb)return/(?:Version)[ \/]?(\S+)/.exec(a)}();
kb&&(jb=kb?kb[1]:"");if(db){var lb=hb();if(null!=lb&&lb>parseFloat(jb)){ib=String(lb);break a}}ib=jb}var mb=ib,nb;var ob=p.document;nb=ob&&db?hb()||("CSS1Compat"==ob.compatMode?parseInt(mb,10):5):void 0;var pb=!db||9<=Number(nb);function qb(){this.b="";this.g=rb}
qb.prototype.K=!0;qb.prototype.H=function(){return this.b};
qb.prototype.fa=!0;qb.prototype.aa=function(){return 1};
function sb(a){return a instanceof qb&&a.constructor===qb&&a.g===rb?a.b:"type_error:TrustedResourceUrl"}
var rb={};function E(){this.b="";this.g=tb}
E.prototype.K=!0;E.prototype.H=function(){return this.b};
E.prototype.fa=!0;E.prototype.aa=function(){return 1};
function ub(a){return a instanceof E&&a.constructor===E&&a.g===tb?a.b:"type_error:SafeUrl"}
var vb=/^(?:(?:https?|mailto|ftp):|[^:/?#]*(?:[/?#]|$))/i;function wb(a){if(a instanceof E)return a;a=a.K?a.H():String(a);vb.test(a)||(a="about:invalid#zClosurez");return xb(a)}
var tb={};function xb(a){var b=new E;b.b=a;return b}
xb("about:blank");function yb(){this.ea="";this.va=zb;this.b=null}
yb.prototype.fa=!0;yb.prototype.aa=function(){return this.b};
yb.prototype.K=!0;yb.prototype.H=function(){return this.ea};
var zb={};function Ab(a,b){var c=new yb;c.ea=a;c.b=b;return c}
Ab("<!DOCTYPE html>",0);Ab("",0);Ab("<br>",0);function Bb(a,b){var c=b instanceof E?b:wb(b);a.href=ub(c)}
function Cb(a,b,c){a.rel=c;a.href=-1!=c.toLowerCase().indexOf("stylesheet")?sb(b):b instanceof qb?sb(b):b instanceof E?ub(b):wb(b).H()}
function Db(a,b){a.src=sb(b)}
;function Eb(a,b){this.x=q(a)?a:0;this.y=q(b)?b:0}
Eb.prototype.equals=function(a){return a instanceof Eb&&(this==a?!0:this&&a?this.x==a.x&&this.y==a.y:!1)};
Eb.prototype.ceil=function(){this.x=Math.ceil(this.x);this.y=Math.ceil(this.y);return this};
Eb.prototype.floor=function(){this.x=Math.floor(this.x);this.y=Math.floor(this.y);return this};
Eb.prototype.round=function(){this.x=Math.round(this.x);this.y=Math.round(this.y);return this};function Fb(a,b){this.width=a;this.height=b}
l=Fb.prototype;l.aspectRatio=function(){return this.width/this.height};
l.isEmpty=function(){return!(this.width*this.height)};
l.ceil=function(){this.width=Math.ceil(this.width);this.height=Math.ceil(this.height);return this};
l.floor=function(){this.width=Math.floor(this.width);this.height=Math.floor(this.height);return this};
l.round=function(){this.width=Math.round(this.width);this.height=Math.round(this.height);return this};function Gb(a){var b=document;return r(a)?b.getElementById(a):a}
function Hb(a,b){Ua(b,function(b,d){b&&b.K&&(b=b.H());"style"==d?a.style.cssText=b:"class"==d?a.className=b:"for"==d?a.htmlFor=b:Ib.hasOwnProperty(d)?a.setAttribute(Ib[d],b):0==d.lastIndexOf("aria-",0)||0==d.lastIndexOf("data-",0)?a.setAttribute(d,b):a[d]=b})}
var Ib={cellpadding:"cellPadding",cellspacing:"cellSpacing",colspan:"colSpan",frameborder:"frameBorder",height:"height",maxlength:"maxLength",nonce:"nonce",role:"role",rowspan:"rowSpan",type:"type",usemap:"useMap",valign:"vAlign",width:"width"};
function Jb(a,b,c){var d=arguments,e=document,f=String(d[0]),g=d[1];if(!pb&&g&&(g.name||g.type)){f=["<",f];g.name&&f.push(' name="',Ga(g.name),'"');if(g.type){f.push(' type="',Ga(g.type),'"');var h={};bb(h,g);delete h.type;g=h}f.push(">");f=f.join("")}f=e.createElement(f);g&&(r(g)?f.className=g:w(g)?f.className=g.join(" "):Hb(f,g));2<d.length&&Kb(e,f,d);return f}
function Kb(a,b,c){function d(c){c&&b.appendChild(r(c)?a.createTextNode(c):c)}
for(var e=2;e<c.length;e++){var f=c[e];if(!pa(f)||ra(f)&&0<f.nodeType)d(f);else{a:{if(f&&"number"==typeof f.length){if(ra(f)){var g="function"==typeof f.item||"string"==typeof f.item;break a}if(qa(f)){g="function"==typeof f.item;break a}}g=!1}C(g?Ba(f):f,d)}}}
function Lb(a,b){for(var c=0;a;){if(b(a))return a;a=a.parentNode;c++}return null}
;function Mb(a){Nb();var b=new qb;b.b=a;return b}
var Nb=ma;var Ob=/^[\w+/_-]+[=]{0,2}$/;function Pb(){var a=p.document.querySelector("script[nonce]");if(a&&(a=a.nonce||a.getAttribute("nonce"))&&Ob.test(a))return a}
;var Qb=document,F=window;function Rb(a){"number"==typeof a&&(a=Math.round(a)+"px");return a}
;var Sb=(new Date).getTime();function Tb(a){if(!a)return"";a=a.split("#")[0].split("?")[0];a=a.toLowerCase();0==a.indexOf("//")&&(a=window.location.protocol+a);/^[\w\-]*:\/\//.test(a)||(a=window.location.href);var b=a.substring(a.indexOf("://")+3),c=b.indexOf("/");-1!=c&&(b=b.substring(0,c));a=a.substring(0,a.indexOf("://"));if("http"!==a&&"https"!==a&&"chrome-extension"!==a&&"file"!==a&&"android-app"!==a&&"chrome-search"!==a)throw Error("Invalid URI scheme in origin");c="";var d=b.indexOf(":");if(-1!=d){var e=b.substring(d+
1);b=b.substring(0,d);if("http"===a&&"80"!==e||"https"===a&&"443"!==e)c=":"+e}return a+"://"+b+c}
;function Ub(){function a(){e[0]=1732584193;e[1]=4023233417;e[2]=2562383102;e[3]=271733878;e[4]=3285377520;u=m=0}
function b(a){for(var b=g,c=0;64>c;c+=4)b[c/4]=a[c]<<24|a[c+1]<<16|a[c+2]<<8|a[c+3];for(c=16;80>c;c++)a=b[c-3]^b[c-8]^b[c-14]^b[c-16],b[c]=(a<<1|a>>>31)&4294967295;a=e[0];var d=e[1],f=e[2],h=e[3],k=e[4];for(c=0;80>c;c++){if(40>c)if(20>c){var m=h^d&(f^h);var u=1518500249}else m=d^f^h,u=1859775393;else 60>c?(m=d&f|h&(d|f),u=2400959708):(m=d^f^h,u=3395469782);m=((a<<5|a>>>27)&4294967295)+m+k+u+b[c]&4294967295;k=h;h=f;f=(d<<30|d>>>2)&4294967295;d=a;a=m}e[0]=e[0]+a&4294967295;e[1]=e[1]+d&4294967295;e[2]=
e[2]+f&4294967295;e[3]=e[3]+h&4294967295;e[4]=e[4]+k&4294967295}
function c(a,c){if("string"===typeof a){a=unescape(encodeURIComponent(a));for(var d=[],e=0,g=a.length;e<g;++e)d.push(a.charCodeAt(e));a=d}c||(c=a.length);d=0;if(0==m)for(;d+64<c;)b(a.slice(d,d+64)),d+=64,u+=64;for(;d<c;)if(f[m++]=a[d++],u++,64==m)for(m=0,b(f);d+64<c;)b(a.slice(d,d+64)),d+=64,u+=64}
function d(){var a=[],d=8*u;56>m?c(h,56-m):c(h,64-(m-56));for(var g=63;56<=g;g--)f[g]=d&255,d>>>=8;b(f);for(g=d=0;5>g;g++)for(var k=24;0<=k;k-=8)a[d++]=e[g]>>k&255;return a}
for(var e=[],f=[],g=[],h=[128],k=1;64>k;++k)h[k]=0;var m,u;a();return{reset:a,update:c,digest:d,ya:function(){for(var a=d(),b="",c=0;c<a.length;c++)b+="0123456789ABCDEF".charAt(Math.floor(a[c]/16))+"0123456789ABCDEF".charAt(a[c]%16);return b}}}
;function Vb(a,b,c){var d=[],e=[];if(1==(w(c)?2:1))return e=[b,a],C(d,function(a){e.push(a)}),Wb(e.join(" "));
var f=[],g=[];C(c,function(a){g.push(a.key);f.push(a.value)});
c=Math.floor((new Date).getTime()/1E3);e=0==f.length?[c,b,a]:[f.join(":"),c,b,a];C(d,function(a){e.push(a)});
a=Wb(e.join(" "));a=[c,a];0==g.length||a.push(g.join(""));return a.join("_")}
function Wb(a){var b=Ub();b.update(a);return b.ya().toLowerCase()}
;function Xb(a){this.b=a||{cookie:""}}
l=Xb.prototype;l.isEnabled=function(){return navigator.cookieEnabled};
l.set=function(a,b,c,d,e,f){if(/[;=\s]/.test(a))throw Error('Invalid cookie name "'+a+'"');if(/[;\r\n]/.test(b))throw Error('Invalid cookie value "'+b+'"');q(c)||(c=-1);e=e?";domain="+e:"";d=d?";path="+d:"";f=f?";secure":"";c=0>c?"":0==c?";expires="+(new Date(1970,1,1)).toUTCString():";expires="+(new Date(z()+1E3*c)).toUTCString();this.b.cookie=a+"="+b+e+d+c+f};
l.get=function(a,b){for(var c=a+"=",d=(this.b.cookie||"").split(";"),e=0,f;e<d.length;e++){f=Fa(d[e]);if(0==f.lastIndexOf(c,0))return f.substr(c.length);if(f==a)return""}return b};
l.remove=function(a,b,c){var d=q(this.get(a));this.set(a,"",0,b,c);return d};
l.isEmpty=function(){return!this.b.cookie};
l.clear=function(){for(var a=(this.b.cookie||"").split(";"),b=[],c=[],d,e,f=0;f<a.length;f++)e=Fa(a[f]),d=e.indexOf("="),-1==d?(b.push(""),c.push(e)):(b.push(e.substring(0,d)),c.push(e.substring(d+1)));for(a=b.length-1;0<=a;a--)this.remove(b[a])};
var Yb=new Xb("undefined"==typeof document?null:document);Yb.g=3950;function Zb(){var a=[],b=Tb(String(p.location.href)),c=p.__OVERRIDE_SID;null==c&&(c=(new Xb(document)).get("SID"));if(c&&(b=(c=0==b.indexOf("https:")||0==b.indexOf("chrome-extension:"))?p.__SAPISID:p.__APISID,null==b&&(b=(new Xb(document)).get(c?"SAPISID":"APISID")),b)){c=c?"SAPISIDHASH":"APISIDHASH";var d=String(p.location.href);return d&&b&&c?[c,Vb(Tb(d),b,a||null)].join(" "):null}return null}
;function $b(a,b){this.f=a;this.h=b;this.g=0;this.b=null}
$b.prototype.get=function(){if(0<this.g){this.g--;var a=this.b;this.b=a.next;a.next=null}else a=this.f();return a};
function ac(a,b){a.h(b);100>a.g&&(a.g++,b.next=a.b,a.b=b)}
;function bc(a){p.setTimeout(function(){throw a;},0)}
var cc;
function dc(){var a=p.MessageChannel;"undefined"===typeof a&&"undefined"!==typeof window&&window.postMessage&&window.addEventListener&&!D("Presto")&&(a=function(){var a=document.createElement("IFRAME");a.style.display="none";a.src="";document.documentElement.appendChild(a);var b=a.contentWindow;a=b.document;a.open();a.write("");a.close();var c="callImmediate"+Math.random(),d="file:"==b.location.protocol?"*":b.location.protocol+"//"+b.location.host;a=x(function(a){if(("*"==d||a.origin==d)&&a.data==
c)this.port1.onmessage()},this);
b.addEventListener("message",a,!1);this.port1={};this.port2={postMessage:function(){b.postMessage(c,d)}}});
if("undefined"!==typeof a&&!D("Trident")&&!D("MSIE")){var b=new a,c={},d=c;b.port1.onmessage=function(){if(q(c.next)){c=c.next;var a=c.ma;c.ma=null;a()}};
return function(a){d.next={ma:a};d=d.next;b.port2.postMessage(0)}}return"undefined"!==typeof document&&"onreadystatechange"in document.createElement("SCRIPT")?function(a){var b=document.createElement("SCRIPT");
b.onreadystatechange=function(){b.onreadystatechange=null;b.parentNode.removeChild(b);b=null;a();a=null};
document.documentElement.appendChild(b)}:function(a){p.setTimeout(a,0)}}
;function ec(){this.g=this.b=null}
var gc=new $b(function(){return new fc},function(a){a.reset()});
ec.prototype.add=function(a,b){var c=gc.get();c.set(a,b);this.g?this.g.next=c:this.b=c;this.g=c};
ec.prototype.remove=function(){var a=null;this.b&&(a=this.b,this.b=this.b.next,this.b||(this.g=null),a.next=null);return a};
function fc(){this.next=this.scope=this.b=null}
fc.prototype.set=function(a,b){this.b=a;this.scope=b;this.next=null};
fc.prototype.reset=function(){this.next=this.scope=this.b=null};function hc(a,b){ic||jc();kc||(ic(),kc=!0);lc.add(a,b)}
var ic;function jc(){if(-1!=String(p.Promise).indexOf("[native code]")){var a=p.Promise.resolve(void 0);ic=function(){a.then(mc)}}else ic=function(){var a=mc;
!qa(p.setImmediate)||p.Window&&p.Window.prototype&&!D("Edge")&&p.Window.prototype.setImmediate==p.setImmediate?(cc||(cc=dc()),cc(a)):p.setImmediate(a)}}
var kc=!1,lc=new ec;function mc(){for(var a;a=lc.remove();){try{a.b.call(a.scope)}catch(b){bc(b)}ac(gc,a)}kc=!1}
;function G(){this.g=this.g;this.B=this.B}
G.prototype.g=!1;G.prototype.dispose=function(){this.g||(this.g=!0,this.l())};
function nc(a,b){a.g?q(void 0)?b.call(void 0):b():(a.B||(a.B=[]),a.B.push(q(void 0)?x(b,void 0):b))}
G.prototype.l=function(){if(this.B)for(;this.B.length;)this.B.shift()()};
function oc(a){a&&"function"==typeof a.dispose&&a.dispose()}
function pc(a){for(var b=0,c=arguments.length;b<c;++b){var d=arguments[b];pa(d)?pc.apply(null,d):oc(d)}}
;function qc(a){if(a.classList)return a.classList;a=a.className;return r(a)&&a.match(/\S+/g)||[]}
function rc(a,b){if(a.classList)var c=a.classList.contains(b);else c=qc(a),c=0<=wa(c,b);return c}
function sc(){var a=document.body;a.classList?a.classList.remove("inverted-hdpi"):rc(a,"inverted-hdpi")&&(a.className=xa(qc(a),function(a){return"inverted-hdpi"!=a}).join(" "))}
;var tc="StopIteration"in p?p.StopIteration:{message:"StopIteration",stack:""};function uc(){}
uc.prototype.next=function(){throw tc;};
uc.prototype.U=function(){return this};
function vc(a){if(a instanceof uc)return a;if("function"==typeof a.U)return a.U(!1);if(pa(a)){var b=0,c=new uc;c.next=function(){for(;;){if(b>=a.length)throw tc;if(b in a)return a[b++];b++}};
return c}throw Error("Not implemented");}
function wc(a,b){if(pa(a))try{C(a,b,void 0)}catch(c){if(c!==tc)throw c;}else{a=vc(a);try{for(;;)b.call(void 0,a.next(),void 0,a)}catch(c){if(c!==tc)throw c;}}}
function xc(a){if(pa(a))return Ba(a);a=vc(a);var b=[];wc(a,function(a){b.push(a)});
return b}
;(function(){if(!p.addEventListener||!Object.defineProperty)return!1;var a=!1,b=Object.defineProperty({},"passive",{get:function(){a=!0}});
p.addEventListener("test",ma,b);p.removeEventListener("test",ma,b);return a})();function yc(a){var b=[];zc(new Ac,a,b);return b.join("")}
function Ac(){}
function zc(a,b,c){if(null==b)c.push("null");else{if("object"==typeof b){if(w(b)){var d=b;b=d.length;c.push("[");for(var e="",f=0;f<b;f++)c.push(e),zc(a,d[f],c),e=",";c.push("]");return}if(b instanceof String||b instanceof Number||b instanceof Boolean)b=b.valueOf();else{c.push("{");e="";for(d in b)Object.prototype.hasOwnProperty.call(b,d)&&(f=b[d],"function"!=typeof f&&(c.push(e),Bc(d,c),c.push(":"),zc(a,f,c),e=","));c.push("}");return}}switch(typeof b){case "string":Bc(b,c);break;case "number":c.push(isFinite(b)&&
!isNaN(b)?String(b):"null");break;case "boolean":c.push(String(b));break;case "function":c.push("null");break;default:throw Error("Unknown type: "+typeof b);}}}
var Cc={'"':'\\"',"\\":"\\\\","/":"\\/","\b":"\\b","\f":"\\f","\n":"\\n","\r":"\\r","\t":"\\t","\x0B":"\\u000b"},Dc=/\uffff/.test("\uffff")?/[\\"\x00-\x1f\x7f-\uffff]/g:/[\\"\x00-\x1f\x7f-\xff]/g;function Bc(a,b){b.push('"',a.replace(Dc,function(a){var b=Cc[a];b||(b="\\u"+(a.charCodeAt(0)|65536).toString(16).substr(1),Cc[a]=b);return b}),'"')}
;function Ec(a){a.prototype.then=a.prototype.then;a.prototype.$goog_Thenable=!0}
function Fc(a){if(!a)return!1;try{return!!a.$goog_Thenable}catch(b){return!1}}
;function H(a,b){this.b=0;this.m=void 0;this.h=this.g=this.f=null;this.i=this.j=!1;if(a!=ma)try{var c=this;a.call(b,function(a){Gc(c,2,a)},function(a){Gc(c,3,a)})}catch(d){Gc(this,3,d)}}
function Hc(){this.next=this.context=this.g=this.h=this.b=null;this.f=!1}
Hc.prototype.reset=function(){this.context=this.g=this.h=this.b=null;this.f=!1};
var Ic=new $b(function(){return new Hc},function(a){a.reset()});
function Jc(a,b,c){var d=Ic.get();d.h=a;d.g=b;d.context=c;return d}
function Kc(a){return new H(function(b,c){c(a)})}
function Lc(a,b,c){Mc(a,b,c,null)||hc(y(b,a))}
function Nc(a){return new H(function(b,c){a.length||b(void 0);for(var d=0,e;d<a.length;d++)e=a[d],Lc(e,b,c)})}
function Oc(a){return new H(function(b){var c=a.length,d=[];if(c)for(var e=function(a,e,f){c--;d[a]=e?{Z:!0,value:f}:{Z:!1,reason:f};0==c&&b(d)},f=0,g;f<a.length;f++)g=a[f],Lc(g,y(e,f,!0),y(e,f,!1));
else b(d)})}
H.prototype.then=function(a,b,c){return Pc(this,qa(a)?a:null,qa(b)?b:null,c)};
Ec(H);function Qc(a,b){var c=Jc(b,b,void 0);c.f=!0;Rc(a,c);return a}
function Sc(a,b){return Pc(a,null,b,void 0)}
H.prototype.cancel=function(a){0==this.b&&hc(function(){var b=new Tc(a);Uc(this,b)},this)};
function Uc(a,b){if(0==a.b)if(a.f){var c=a.f;if(c.g){for(var d=0,e=null,f=null,g=c.g;g&&(g.f||(d++,g.b==a&&(e=g),!(e&&1<d)));g=g.next)e||(f=g);e&&(0==c.b&&1==d?Uc(c,b):(f?(d=f,d.next==c.h&&(c.h=d),d.next=d.next.next):Vc(c),Wc(c,e,3,b)))}a.f=null}else Gc(a,3,b)}
function Rc(a,b){a.g||2!=a.b&&3!=a.b||Xc(a);a.h?a.h.next=b:a.g=b;a.h=b}
function Pc(a,b,c,d){var e=Jc(null,null,null);e.b=new H(function(a,g){e.h=b?function(c){try{var e=b.call(d,c);a(e)}catch(m){g(m)}}:a;
e.g=c?function(b){try{var e=c.call(d,b);!q(e)&&b instanceof Tc?g(b):a(e)}catch(m){g(m)}}:g});
e.b.f=a;Rc(a,e);return e.b}
H.prototype.o=function(a){this.b=0;Gc(this,2,a)};
H.prototype.w=function(a){this.b=0;Gc(this,3,a)};
function Gc(a,b,c){0==a.b&&(a===c&&(b=3,c=new TypeError("Promise cannot resolve to itself")),a.b=1,Mc(c,a.o,a.w,a)||(a.m=c,a.b=b,a.f=null,Xc(a),3!=b||c instanceof Tc||Yc(a,c)))}
function Mc(a,b,c,d){if(a instanceof H)return Rc(a,Jc(b||ma,c||null,d)),!0;if(Fc(a))return a.then(b,c,d),!0;if(ra(a))try{var e=a.then;if(qa(e))return Zc(a,e,b,c,d),!0}catch(f){return c.call(d,f),!0}return!1}
function Zc(a,b,c,d,e){function f(a){h||(h=!0,d.call(e,a))}
function g(a){h||(h=!0,c.call(e,a))}
var h=!1;try{b.call(a,g,f)}catch(k){f(k)}}
function Xc(a){a.j||(a.j=!0,hc(a.B,a))}
function Vc(a){var b=null;a.g&&(b=a.g,a.g=b.next,b.next=null);a.g||(a.h=null);return b}
H.prototype.B=function(){for(var a;a=Vc(this);)Wc(this,a,this.b,this.m);this.j=!1};
function Wc(a,b,c,d){if(3==c&&b.g&&!b.f)for(;a&&a.i;a=a.f)a.i=!1;if(b.b)b.b.f=null,$c(b,c,d);else try{b.f?b.h.call(b.context):$c(b,c,d)}catch(e){ad.call(null,e)}ac(Ic,b)}
function $c(a,b,c){2==b?a.h.call(a.context,c):a.g&&a.g.call(a.context,c)}
function Yc(a,b){a.i=!0;hc(function(){a.i&&ad.call(null,b)})}
var ad=bc;function Tc(a){B.call(this,a)}
A(Tc,B);Tc.prototype.name="cancel";function I(a){G.call(this);this.j=1;this.h=[];this.i=0;this.b=[];this.f={};this.m=!!a}
A(I,G);l=I.prototype;l.subscribe=function(a,b,c){var d=this.f[a];d||(d=this.f[a]=[]);var e=this.j;this.b[e]=a;this.b[e+1]=b;this.b[e+2]=c;this.j=e+3;d.push(e);return e};
function bd(a,b,c,d){if(b=a.f[b]){var e=a.b;(b=za(b,function(a){return e[a+1]==c&&e[a+2]==d}))&&a.I(b)}}
l.I=function(a){var b=this.b[a];if(b){var c=this.f[b];0!=this.i?(this.h.push(a),this.b[a+1]=ma):(c&&Aa(c,a),delete this.b[a],delete this.b[a+1],delete this.b[a+2])}return!!b};
l.J=function(a,b){var c=this.f[a];if(c){for(var d=Array(arguments.length-1),e=1,f=arguments.length;e<f;e++)d[e-1]=arguments[e];if(this.m)for(e=0;e<c.length;e++){var g=c[e];cd(this.b[g+1],this.b[g+2],d)}else{this.i++;try{for(e=0,f=c.length;e<f;e++)g=c[e],this.b[g+1].apply(this.b[g+2],d)}finally{if(this.i--,0<this.h.length&&0==this.i)for(;c=this.h.pop();)this.I(c)}}return 0!=e}return!1};
function cd(a,b,c){hc(function(){a.apply(b,c)})}
l.clear=function(a){if(a){var b=this.f[a];b&&(C(b,this.I,this),delete this.f[a])}else this.b.length=0,this.f={}};
l.l=function(){I.u.l.call(this);this.clear();this.h.length=0};function dd(a){this.b=a}
dd.prototype.set=function(a,b){q(b)?this.b.set(a,yc(b)):this.b.remove(a)};
dd.prototype.get=function(a){try{var b=this.b.get(a)}catch(c){return}if(null!==b)try{return JSON.parse(b)}catch(c){throw"Storage: Invalid value was encountered";}};
dd.prototype.remove=function(a){this.b.remove(a)};function ed(a){this.b=a}
A(ed,dd);function fd(a){this.data=a}
function gd(a){return!q(a)||a instanceof fd?a:new fd(a)}
ed.prototype.set=function(a,b){ed.u.set.call(this,a,gd(b))};
ed.prototype.g=function(a){a=ed.u.get.call(this,a);if(!q(a)||a instanceof Object)return a;throw"Storage: Invalid value was encountered";};
ed.prototype.get=function(a){if(a=this.g(a)){if(a=a.data,!q(a))throw"Storage: Invalid value was encountered";}else a=void 0;return a};function hd(a){this.b=a}
A(hd,ed);hd.prototype.set=function(a,b,c){if(b=gd(b)){if(c){if(c<z()){hd.prototype.remove.call(this,a);return}b.expiration=c}b.creation=z()}hd.u.set.call(this,a,b)};
hd.prototype.g=function(a){var b=hd.u.g.call(this,a);if(b){var c=b.creation,d=b.expiration;if(d&&d<z()||c&&c>z())hd.prototype.remove.call(this,a);else return b}};function id(a){this.b=a}
A(id,hd);function jd(){}
;function kd(){}
A(kd,jd);kd.prototype.clear=function(){var a=xc(this.U(!0)),b=this;C(a,function(a){b.remove(a)})};function ld(a){this.b=a}
A(ld,kd);l=ld.prototype;l.isAvailable=function(){if(!this.b)return!1;try{return this.b.setItem("__sak","1"),this.b.removeItem("__sak"),!0}catch(a){return!1}};
l.set=function(a,b){try{this.b.setItem(a,b)}catch(c){if(0==this.b.length)throw"Storage mechanism: Storage disabled";throw"Storage mechanism: Quota exceeded";}};
l.get=function(a){a=this.b.getItem(a);if(!r(a)&&null!==a)throw"Storage mechanism: Invalid value was encountered";return a};
l.remove=function(a){this.b.removeItem(a)};
l.U=function(a){var b=0,c=this.b,d=new uc;d.next=function(){if(b>=c.length)throw tc;var d=c.key(b++);if(a)return d;d=c.getItem(d);if(!r(d))throw"Storage mechanism: Invalid value was encountered";return d};
return d};
l.clear=function(){this.b.clear()};
l.key=function(a){return this.b.key(a)};function md(){var a=null;try{a=window.localStorage||null}catch(b){}this.b=a}
A(md,ld);function nd(){var a=null;try{a=window.sessionStorage||null}catch(b){}this.b=a}
A(nd,ld);function od(a){if(!qa(a))if(a&&"function"==typeof a.handleEvent)a=x(a.handleEvent,a);else throw Error("Invalid listener argument");return 2147483647<Number(5E3)?-1:p.setTimeout(a,5E3)}
function pd(){var a=null;return Sc(new H(function(b,c){a=od(function(){b(void 0)});
-1==a&&c(Error("Failed to schedule timer."))}),function(b){p.clearTimeout(a);
throw b;})}
;var qd=/^(?:([^:/?#.]+):)?(?:\/\/(?:([^/?#]*)@)?([^/#?]*?)(?::([0-9]+))?(?=[/#?]|$))?([^?#]+)?(?:\?([^#]*))?(?:#([\s\S]*))?$/;function J(a){return a.match(qd)}
function rd(a){return a?decodeURI(a):a}
function sd(a,b,c){if(w(b))for(var d=0;d<b.length;d++)sd(a,String(b[d]),c);else null!=b&&c.push(a+(""===b?"":"="+encodeURIComponent(String(b))))}
function td(a){var b=[],c;for(c in a)sd(c,a[c],b);return b.join("&")}
function ud(a,b){var c=td(b);if(c){var d=a.indexOf("#");0>d&&(d=a.length);var e=a.indexOf("?");if(0>e||e>d){e=d;var f=""}else f=a.substring(e+1,d);d=[a.substr(0,e),f,a.substr(d)];e=d[1];d[1]=c?e?e+"&"+c:c:e;c=d[0]+(d[1]?"?"+d[1]:"")+d[2]}else c=a;return c}
;var vd=!1,wd="";function xd(a){a=a.match(/[\d]+/g);if(!a)return"";a.length=3;return a.join(".")}
(function(){if(navigator.plugins&&navigator.plugins.length){var a=navigator.plugins["Shockwave Flash"];if(a&&(vd=!0,a.description)){wd=xd(a.description);return}if(navigator.plugins["Shockwave Flash 2.0"]){vd=!0;wd="2.0.0.11";return}}if(navigator.mimeTypes&&navigator.mimeTypes.length&&(a=navigator.mimeTypes["application/x-shockwave-flash"],vd=!(!a||!a.enabledPlugin))){wd=xd(a.enabledPlugin.description);return}try{var b=new ActiveXObject("ShockwaveFlash.ShockwaveFlash.7");vd=!0;wd=xd(b.GetVariable("$version"));
return}catch(c){}try{b=new ActiveXObject("ShockwaveFlash.ShockwaveFlash.6");vd=!0;wd="6.0.21";return}catch(c){}try{b=new ActiveXObject("ShockwaveFlash.ShockwaveFlash"),vd=!0,wd=xd(b.GetVariable("$version"))}catch(c){}})();
var zd=vd,Ad=wd;function Bd(a,b,c){var d="script";d=void 0===d?"":d;var e=a.createElement("link");Cb(e,b,"preload");d&&(e.as=d);c&&(e.nonce=c);if(a=a.getElementsByTagName("head")[0])try{a.appendChild(e)}catch(f){}}
;var Cd=/^\.google\.(com?\.)?[a-z]{2,3}$/,Dd=/\.(cn|com\.bi|do|sl)$/;function Ed(a){return Cd.test(a)&&!Dd.test(a)}
var Fd=p;function Gd(a){a="https://"+("adservice"+a+"/adsid/integrator.js");var b=["domain="+encodeURIComponent(p.location.hostname)];K[3]>=z()&&b.push("adsid="+encodeURIComponent(K[1]));return a+"?"+b.join("&")}
var K,L;function Hd(){Fd=p;K=Fd.googleToken=Fd.googleToken||{};var a=z();K[1]&&K[3]>a&&0<K[2]||(K[1]="",K[2]=-1,K[3]=-1,K[4]="",K[6]="");L=Fd.googleIMState=Fd.googleIMState||{};Ed(L[1])||(L[1]=".google.com");w(L[5])||(L[5]=[]);"boolean"==typeof L[6]||(L[6]=!1);w(L[7])||(L[7]=[]);la(L[8])||(L[8]=0)}
function Id(){Hd();return K[1]}
var M={da:function(){return 0<L[8]},
Na:function(){L[8]++},
Oa:function(){0<L[8]&&L[8]--},
Pa:function(){L[8]=0},
shouldRetry:function(){return!1},
na:function(){return L[5]},
la:function(a){try{a()}catch(b){p.setTimeout(function(){throw b;},0)}},
ja:function(){if(!M.da()){var a=p.document,b=function(b){b=Gd(b);a:{try{var c=Pb();break a}catch(h){}c=void 0}var d=c;Bd(a,b,d);c=a.createElement("script");c.type="text/javascript";d&&(c.nonce=d);c.onerror=function(){return p.processGoogleToken({},2)};
b=Mb(b);Db(c,b);try{(a.head||a.body||a.documentElement).appendChild(c),M.Na()}catch(h){}},c=L[1];
b(c);".google.com"!=c&&b(".google.com");b={};var d=(b.newToken="FBT",b);p.setTimeout(function(){return p.processGoogleToken(d,1)},1E3)}}};
function Jd(a){Hd();var b=Fd.googleToken[5]||0;a&&(0!=b||K[3]>=z()?M.la(a):(M.na().push(a),M.ja()));K[3]>=z()&&K[2]>=z()||M.ja()}
function Kd(a){p.processGoogleToken=p.processGoogleToken||function(a,c){var b=a,e=c;b=void 0===b?{}:b;e=void 0===e?0:e;var f=b.newToken||"",g="NT"==f,h=parseInt(b.freshLifetimeSecs||"",10),k=parseInt(b.validLifetimeSecs||"",10);g&&!k&&(k=3600);var m=b["1p_jar"]||"";b=b.pucrd||"";Hd();1==e?M.Pa():M.Oa();if(!f&&M.shouldRetry())Ed(".google.com")&&(L[1]=".google.com"),M.ja();else{var u=Fd.googleToken=Fd.googleToken||{},Z=0==e&&f&&r(f)&&!g&&la(h)&&0<h&&la(k)&&0<k&&r(m);g=g&&!M.da()&&(!(K[3]>=z())||"NT"==
K[1]);var Ca=!(K[3]>=z())&&0!=e;if(Z||g||Ca)g=z(),h=g+1E3*h,k=g+1E3*k,1E-5>Math.random()&&(g="https://pagead2.googlesyndication.com/pagead/gen_204?id=imerr&err="+e,p.google_image_requests||(p.google_image_requests=[]),Ca=p.document.createElement("img"),Ca.src=g,p.google_image_requests.push(Ca)),u[5]=e,u[1]=f,u[2]=h,u[3]=k,u[4]=m,u[6]=b,Hd();if(Z||!M.da()){e=M.na();for(f=0;f<e.length;f++)M.la(e[f]);e.length=0}}};
Jd(a)}
;function Ld(a,b){if(1<b.length)a[b[0]]=b[1];else{var c=b[0],d;for(d in c)a[d]=c[d]}}
var N=window.performance&&window.performance.timing&&window.performance.now?function(){return window.performance.timing.navigationStart+window.performance.now()}:function(){return(new Date).getTime()};var Md=window.yt&&window.yt.config_||window.ytcfg&&window.ytcfg.data_||{};t("yt.config_",Md,void 0);function O(a){Ld(Md,arguments)}
function P(a,b){return a in Md?Md[a]:b}
function Nd(a){return P(a,void 0)}
function Od(){return P("PLAYER_CONFIG",{})}
;function Pd(a){return a&&window.yterr?function(){try{return a.apply(this,arguments)}catch(b){Q(b)}}:a}
function Q(a,b,c,d,e){var f=v("yt.logging.errors.log");f?f(a,b,c,d,e):(f=P("ERRORS",[]),f.push([a,b,c,d,e]),O("ERRORS",f))}
;function R(a){return P("EXPERIMENT_FLAGS",{})[a]}
;function Qd(a){a&&(a.dataset?a.dataset[Rd("loaded")]="true":a.setAttribute("data-loaded","true"))}
function Sd(a,b){return a?a.dataset?a.dataset[Rd(b)]:a.getAttribute("data-"+b):null}
var Td={};function Rd(a){return Td[a]||(Td[a]=String(a).replace(/\-([a-z])/g,function(a,c){return c.toUpperCase()}))}
;function T(a,b){qa(a)&&(a=Pd(a));return window.setTimeout(a,b)}
function Ud(a){window.clearTimeout(a)}
;var Vd=v("ytPubsubPubsubInstance")||new I;I.prototype.subscribe=I.prototype.subscribe;I.prototype.unsubscribeByKey=I.prototype.I;I.prototype.publish=I.prototype.J;I.prototype.clear=I.prototype.clear;t("ytPubsubPubsubInstance",Vd,void 0);var Wd=v("ytPubsubPubsubSubscribedKeys")||{};t("ytPubsubPubsubSubscribedKeys",Wd,void 0);var Xd=v("ytPubsubPubsubTopicToKeys")||{};t("ytPubsubPubsubTopicToKeys",Xd,void 0);var Yd=v("ytPubsubPubsubIsSynchronous")||{};t("ytPubsubPubsubIsSynchronous",Yd,void 0);
function Zd(a,b){var c=$d();if(c){var d=c.subscribe(a,function(){var c=arguments;var f=function(){Wd[d]&&b.apply(window,c)};
try{Yd[a]?f():T(f,0)}catch(g){Q(g)}},void 0);
Wd[d]=!0;Xd[a]||(Xd[a]=[]);Xd[a].push(d);return d}return 0}
function ae(a){var b=$d();b&&(la(a)?a=[a]:r(a)&&(a=[parseInt(a,10)]),C(a,function(a){b.unsubscribeByKey(a);delete Wd[a]}))}
function be(a,b){var c=$d();c&&c.publish.apply(c,arguments)}
function ce(a){var b=$d();if(b)if(b.clear(a),a)de(a);else for(var c in Xd)de(c)}
function $d(){return v("ytPubsubPubsubInstance")}
function de(a){Xd[a]&&(a=Xd[a],C(a,function(a){Wd[a]&&delete Wd[a]}),a.length=0)}
;var ee=/\.vflset|-vfl[a-zA-Z0-9_+=-]+/,fe=/-[a-zA-Z]{2,3}_[a-zA-Z]{2,3}(?=(\/|$))/;function ge(a,b){if(window.spf){var c="";if(a){var d=a.indexOf("jsbin/"),e=a.lastIndexOf(".js"),f=d+6;-1<d&&-1<e&&e>f&&(c=a.substring(f,e),c=c.replace(ee,""),c=c.replace(fe,""),c=c.replace("debug-",""),c=c.replace("tracing-",""))}spf.script.load(a,c,b)}else he(a,b)}
function he(a,b){var c=ie(a),d=document.getElementById(c),e=d&&Sd(d,"loaded"),f=d&&!e;if(e)b&&b();else{if(b){e=Zd(c,b);var g=""+(b[sa]||(b[sa]=++ta));je[g]=e}f||(d=ke(a,c,function(){Sd(d,"loaded")||(Qd(d),be(c),T(y(ce,c),0))}))}}
function ke(a,b,c){var d=document.createElement("SCRIPT");d.id=b;d.onload=function(){c&&setTimeout(c,0)};
d.onreadystatechange=function(){switch(d.readyState){case "loaded":case "complete":d.onload()}};
Db(d,Mb(a));a=document.getElementsByTagName("head")[0]||document.body;a.insertBefore(d,a.firstChild);return d}
function le(a){a=ie(a);var b=document.getElementById(a);b&&(ce(a),b.parentNode.removeChild(b))}
function me(a,b){if(a&&b){var c=""+(b[sa]||(b[sa]=++ta));(c=je[c])&&ae(c)}}
function ie(a){var b=document.createElement("a");Bb(b,a);a=b.href.replace(/^[a-zA-Z]+:\/\//,"//");return"js-"+Oa(a)}
var je={};var ne=null;function oe(){var a=P("BG_I",null),b=P("BG_IU",null),c=P("BG_P",void 0);b?ge(b,function(){window.botguard?pe(c):(le(b),Q(Error("Unable to load Botguard from "+b),"WARNING"))}):a&&(eval(a),window.botguard?pe(c):Q(Error("Unable to load Botguard from JS"),"WARNING"))}
function pe(a){ne=new window.botguard.bg(a);R("botguard_periodic_refresh")&&N()}
function qe(){return null!=ne}
function re(){return ne?ne.invoke():null}
;z();var se=q(XMLHttpRequest)?function(){return new XMLHttpRequest}:q(ActiveXObject)?function(){return new ActiveXObject("Microsoft.XMLHTTP")}:null;
function te(){if(!se)return null;var a=se();return"open"in a?a:null}
function ue(a){switch(a&&"status"in a?a.status:-1){case 200:case 201:case 202:case 203:case 204:case 205:case 206:case 304:return!0;default:return!1}}
;function ve(a){"?"==a.charAt(0)&&(a=a.substr(1));a=a.split("&");for(var b={},c=0,d=a.length;c<d;c++){var e=a[c].split("=");if(1==e.length&&e[0]||2==e.length){var f=decodeURIComponent((e[0]||"").replace(/\+/g," "));e=decodeURIComponent((e[1]||"").replace(/\+/g," "));f in b?w(b[f])?Ea(b[f],e):b[f]=[b[f],e]:b[f]=e}}return b}
;var we={"X-Goog-Visitor-Id":"SANDBOXED_VISITOR_ID","X-YouTube-Client-Name":"INNERTUBE_CONTEXT_CLIENT_NAME","X-YouTube-Client-Version":"INNERTUBE_CONTEXT_CLIENT_VERSION","X-Youtube-Identity-Token":"ID_TOKEN","X-YouTube-Page-CL":"PAGE_CL","X-YouTube-Page-Label":"PAGE_BUILD_LABEL","X-YouTube-Variants-Checksum":"VARIANTS_CHECKSUM"},xe=!1;
function ye(a,b){b=void 0===b?{}:b;if(!c)var c=window.location.href;var d=J(a)[1]||null,e=rd(J(a)[3]||null);d&&e?(d=c,c=J(a),d=J(d),c=c[3]==d[3]&&c[1]==d[1]&&c[4]==d[4]):c=e?rd(J(c)[3]||null)==e&&(Number(J(c)[4]||null)||null)==(Number(J(a)[4]||null)||null):!0;for(var f in we){if((e=d=P(we[f]))&&!(e=c)){e=f;var g=P("CORS_HEADER_WHITELIST")||{},h=rd(J(a)[3]||null);e=h?(g=g[h])?0<=wa(g,e):!1:!0}e&&(b[f]=d)}return b}
function ze(a,b){if(window.fetch&&"XML"!=b.format){var c={method:b.method||"GET",credentials:"same-origin"};b.headers&&(c.headers=b.headers);a=Ae(a,b);var d=Be(a,b);d&&(c.body=d);b.withCredentials&&(c.credentials="include");var e=!1,f;fetch(a,c).then(function(a){if(!e){e=!0;f&&Ud(f);var c=a.ok,d=function(d){d=d||{};var e=b.context||p;c?b.C&&b.C.call(e,d,a):b.onError&&b.onError.call(e,d,a);b.ia&&b.ia.call(e,d,a)};
"JSON"==(b.format||"JSON")&&(c||400<=a.status&&500>a.status)?a.json().then(d,function(){d(null)}):d(null)}});
b.oa&&0<b.timeout&&(f=T(function(){e||(e=!0,Ud(f),b.oa.call(b.context||p))},b.timeout))}else Ce(a,b)}
function Ce(a,b){var c=b.format||"JSON";a=Ae(a,b);var d=Be(a,b),e=!1,f,g=De(a,function(a){if(!e){e=!0;f&&Ud(f);var d=ue(a),g=null;if(d||400<=a.status&&500>a.status)g=Ee(c,a,b.cb);if(d)a:if(a&&204==a.status)d=!0;else{switch(c){case "XML":d=0==parseInt(g&&g.return_code,10);break a;case "RAW":d=!0;break a}d=!!g}g=g||{};var h=b.context||p;d?b.C&&b.C.call(h,a,g):b.onError&&b.onError.call(h,a,g);b.ia&&b.ia.call(h,a,g)}},b.method,d,b.headers,b.responseType,b.withCredentials);
b.L&&0<b.timeout&&(f=T(function(){e||(e=!0,g.abort(),Ud(f),b.L.call(b.context||p,g))},b.timeout))}
function Ae(a,b){b.Da&&(a=document.location.protocol+"//"+document.location.hostname+(document.location.port?":"+document.location.port:"")+a);var c=P("XSRF_FIELD_NAME",void 0),d=b.Za;if(d){d[c]&&delete d[c];d=d||{};var e=a.split("#",2);c=e[0];e=1<e.length?"#"+e[1]:"";var f=c.split("?",2);c=f[0];f=ve(f[1]||"");for(var g in d)f[g]=d[g];a=ud(c,f)+e}return a}
function Be(a,b){var c=P("XSRF_FIELD_NAME",void 0),d=P("XSRF_TOKEN",void 0),e=b.postBody||"",f=b.A,g=Nd("XSRF_FIELD_NAME"),h;b.headers&&(h=b.headers["Content-Type"]);b.eb||rd(J(a)[3]||null)&&!b.withCredentials&&rd(J(a)[3]||null)!=document.location.hostname||"POST"!=b.method||h&&"application/x-www-form-urlencoded"!=h||b.A&&b.A[g]||(f||(f={}),f[c]=d);f&&r(e)&&(e=ve(e),bb(e,f),e=b.pa&&"JSON"==b.pa?JSON.stringify(e):td(e));f=e||f&&!Ya(f);!xe&&f&&"POST"!=b.method&&(xe=!0,Q(Error("AJAX request with postData should use POST")));
return e}
function Ee(a,b,c){var d=null;switch(a){case "JSON":a=b.responseText;b=b.getResponseHeader("Content-Type")||"";a&&0<=b.indexOf("json")&&(d=JSON.parse(a));break;case "XML":if(b=(b=b.responseXML)?Fe(b):null)d={},C(b.getElementsByTagName("*"),function(a){d[a.tagName]=Ge(a)})}c&&He(d);
return d}
function He(a){if(ra(a))for(var b in a){var c;(c="html_content"==b)||(c=b.length-5,c=0<=c&&b.indexOf("_html",c)==c);if(c){c=b;var d=Ab(a[b],null);a[c]=d}else He(a[b])}}
function Fe(a){return a?(a=("responseXML"in a?a.responseXML:a).getElementsByTagName("root"))&&0<a.length?a[0]:null:null}
function Ge(a){var b="";C(a.childNodes,function(a){b+=a.nodeValue});
return b}
function Ie(a,b){b.method="POST";b.A||(b.A={});Ce(a,b)}
function De(a,b,c,d,e,f,g){function h(){4==(k&&"readyState"in k?k.readyState:0)&&b&&Pd(b)(k)}
c=void 0===c?"GET":c;d=void 0===d?"":d;var k=te();if(!k)return null;"onloadend"in k?k.addEventListener("loadend",h,!1):k.onreadystatechange=h;k.open(c,a,!0);f&&(k.responseType=f);g&&(k.withCredentials=!0);c="POST"==c;if(e=ye(a,e))for(var m in e)k.setRequestHeader(m,e[m]),"content-type"==m.toLowerCase()&&(c=!1);c&&k.setRequestHeader("Content-Type","application/x-www-form-urlencoded");k.send(d);return k}
;var Je={},Ke=0;
function Le(a,b,c,d,e){e=void 0===e?"":e;a&&(c&&(c=Ra,c=!(c&&0<=c.toLowerCase().indexOf("cobalt"))),c?a&&(a instanceof E||(a=a.K?a.H():String(a),vb.test(a)||(a="about:invalid#zClosurez"),a=xb(a)),b=ub(a),"about:invalid#zClosurez"===b?a="":(b instanceof yb?a=b:(a=null,b.fa&&(a=b.aa()),b=Ga(b.K?b.H():String(b)),a=Ab(b,a)),a=encodeURIComponent(String(yc(a instanceof yb&&a.constructor===yb&&a.va===zb?a.ea:"type_error:SafeHtml")))),/^[\s\xa0]*$/.test(a)||(a=Jb("IFRAME",{src:'javascript:"<body><img src=\\""+'+a+
'+"\\"></body>"',style:"display:none"}),(9==a.nodeType?a:a.ownerDocument||a.document).body.appendChild(a))):e?De(a,b,"POST",e,d):P("USE_NET_AJAX_FOR_PING_TRANSPORT",!1)||d?De(a,b,"GET","",d):Me(a,b))}
function Me(a,b){var c=new Image,d=""+Ke++;Je[d]=c;c.onload=c.onerror=function(){b&&Je[d]&&b();delete Je[d]};
c.src=a}
;var Ne={},Oe=0;
function Pe(a,b,c,d,e,f){f=f||{};f.name=c||P("INNERTUBE_CONTEXT_CLIENT_NAME",1);f.version=d||P("INNERTUBE_CONTEXT_CLIENT_VERSION",void 0);b=void 0===b?"ERROR":b;e=void 0===e?!1:e;e=window&&window.yterr||(void 0===e?!1:e)||!1;if(a&&e&&!(5<=Oe)){e=a.stacktrace;c=a.columnNumber;d=v("window.location.href");if(r(a))a={message:a,name:"Unknown error",lineNumber:"Not available",fileName:d,stack:"Not available"};else{var g=!1;try{var h=a.lineNumber||a.line||"Not available"}catch(Z){h="Not available",g=!0}try{var k=
a.fileName||a.filename||a.sourceURL||p.$googDebugFname||d}catch(Z){k="Not available",g=!0}a=!g&&a.lineNumber&&a.fileName&&a.stack&&a.message&&a.name?a:{message:a.message||"Not available",name:a.name||"UnknownError",lineNumber:h,fileName:k,stack:a.stack||"Not available"}}e=e||a.stack;h=a.lineNumber.toString();isNaN(h)||isNaN(c)||(h=h+":"+c);if(!(Ne[a.message]||0<=e.indexOf("/YouTubeCenter.js")||0<=e.indexOf("/mytube.js"))){k=e;h={Za:{a:"logerror",t:"jserror",type:a.name,msg:a.message.substr(0,1E3),
line:h,level:void 0===b?"ERROR":b,"client.name":f.name},A:{url:P("PAGE_NAME",window.location.href),file:a.fileName},method:"POST"};f.version&&(h["client.version"]=f.version);k&&(h.A.stack=k);for(var m in f)h.A["client."+m]=f[m];if(m=P("LATEST_ECATCHER_SERVICE_TRACKING_PARAMS",void 0))for(var u in m)h.A[u]=m[u];Ce("/error_204",h);Ne[a.message]=!0;Oe++}}}
;var Qe=window.yt&&window.yt.msgs_||window.ytcfg&&window.ytcfg.msgs||{};t("yt.msgs_",Qe,void 0);function Re(a){Ld(Qe,arguments)}
;function Se(){}
function Te(a,b){return Ue(a,1,b)}
;function Ve(){}
n(Ve,Se);function Ue(a,b,c){isNaN(c)&&(c=void 0);var d=v("yt.scheduler.instance.addJob");return d?d(a,b,c):void 0===c?(a(),NaN):T(a,c||0)}
function We(a){if(!isNaN(a)){var b=v("yt.scheduler.instance.cancelJob");b?b(a):Ud(a)}}
Ve.prototype.start=function(){var a=v("yt.scheduler.instance.start");a&&a()};
Ve.prototype.pause=function(){var a=v("yt.scheduler.instance.pause");a&&a()};
na(Ve);Ve.getInstance();var Xe=[],Ye=!1;function Ze(){if("1"!=Va(Od(),"args","privembed")||!R("do_not_set_cookies_for_ads_on_youtube_nocookie")){var a=function(){Ye=!0;"google_ad_status"in window?O("DCLKSTAT",1):O("DCLKSTAT",2)};
ge("//static.doubleclick.net/instream/ad_status.js",a);Xe.push(Te(function(){Ye||"google_ad_status"in window||(me("//static.doubleclick.net/instream/ad_status.js",a),O("DCLKSTAT",3))},5E3))}}
function $e(){return parseInt(P("DCLKSTAT",0),10)}
;var af=0;t("ytDomDomGetNextId",v("ytDomDomGetNextId")||function(){return++af},void 0);var bf={stopImmediatePropagation:1,stopPropagation:1,preventMouseEvent:1,preventManipulation:1,preventDefault:1,layerX:1,layerY:1,screenX:1,screenY:1,scale:1,rotation:1,webkitMovementX:1,webkitMovementY:1};
function cf(a){this.type="";this.state=this.source=this.data=this.currentTarget=this.relatedTarget=this.target=null;this.charCode=this.keyCode=0;this.shiftKey=this.ctrlKey=this.altKey=!1;this.clientY=this.clientX=0;this.changedTouches=this.touches=null;if(a=a||window.event){this.event=a;for(var b in a)b in bf||(this[b]=a[b]);(b=a.target||a.srcElement)&&3==b.nodeType&&(b=b.parentNode);this.target=b;if(b=a.relatedTarget)try{b=b.nodeName?b:null}catch(c){b=null}else"mouseover"==this.type?b=a.fromElement:
"mouseout"==this.type&&(b=a.toElement);this.relatedTarget=b;this.clientX=void 0!=a.clientX?a.clientX:a.pageX;this.clientY=void 0!=a.clientY?a.clientY:a.pageY;this.keyCode=a.keyCode?a.keyCode:a.which;this.charCode=a.charCode||("keypress"==this.type?this.keyCode:0);this.altKey=a.altKey;this.ctrlKey=a.ctrlKey;this.shiftKey=a.shiftKey;this.b=a.pageX;this.g=a.pageY}}
function df(a){if(document.body&&document.documentElement){var b=document.body.scrollTop+document.documentElement.scrollTop;a.b=a.clientX+(document.body.scrollLeft+document.documentElement.scrollLeft);a.g=a.clientY+b}}
cf.prototype.preventDefault=function(){this.event&&(this.event.returnValue=!1,this.event.preventDefault&&this.event.preventDefault())};
cf.prototype.stopPropagation=function(){this.event&&(this.event.cancelBubble=!0,this.event.stopPropagation&&this.event.stopPropagation())};
cf.prototype.stopImmediatePropagation=function(){this.event&&(this.event.cancelBubble=!0,this.event.stopImmediatePropagation&&this.event.stopImmediatePropagation())};var Xa=v("ytEventsEventsListeners")||{};t("ytEventsEventsListeners",Xa,void 0);var ef=v("ytEventsEventsCounter")||{count:0};t("ytEventsEventsCounter",ef,void 0);function ff(a,b,c,d){d=void 0===d?!1:d;a.addEventListener&&("mouseenter"!=b||"onmouseenter"in document?"mouseleave"!=b||"onmouseenter"in document?"mousewheel"==b&&"MozBoxSizing"in document.documentElement.style&&(b="MozMousePixelScroll"):b="mouseout":b="mouseover");return Wa(function(e){return!!e.length&&e[0]==a&&e[1]==b&&e[2]==c&&e[4]==!!d})}
function U(a,b,c){var d=void 0===d?!1:d;if(!a||!a.addEventListener&&!a.attachEvent)return"";var e=ff(a,b,c,d);if(e)return e;e=++ef.count+"";var f=!("mouseenter"!=b&&"mouseleave"!=b||!a.addEventListener||"onmouseenter"in document);var g=f?function(d){d=new cf(d);if(!Lb(d.relatedTarget,function(b){return b==a}))return d.currentTarget=a,d.type=b,c.call(a,d)}:function(b){b=new cf(b);
b.currentTarget=a;return c.call(a,b)};
g=Pd(g);a.addEventListener?("mouseenter"==b&&f?b="mouseover":"mouseleave"==b&&f?b="mouseout":"mousewheel"==b&&"MozBoxSizing"in document.documentElement.style&&(b="MozMousePixelScroll"),a.addEventListener(b,g,d)):a.attachEvent("on"+b,g);Xa[e]=[a,b,c,g,d];return e}
function gf(a){a&&("string"==typeof a&&(a=[a]),C(a,function(a){if(a in Xa){var b=Xa[a],d=b[0],e=b[1],f=b[3];b=b[4];d.removeEventListener?d.removeEventListener(e,f,b):d.detachEvent&&d.detachEvent("on"+e,f);delete Xa[a]}}))}
;function hf(a){this.o=a;this.b=null;this.i=0;this.m=null;this.j=0;this.f=[];for(a=0;4>a;a++)this.f.push(0);this.h=0;this.D=U(window,"mousemove",x(this.F,this));a=x(this.w,this);qa(a)&&(a=Pd(a));this.G=window.setInterval(a,25)}
A(hf,G);hf.prototype.F=function(a){q(a.b)||df(a);var b=a.b;q(a.g)||df(a);this.b=new Eb(b,a.g)};
hf.prototype.w=function(){if(this.b){var a=N();if(0!=this.i){var b=this.m,c=this.b,d=b.x-c.x;b=b.y-c.y;d=Math.sqrt(d*d+b*b)/(a-this.i);this.f[this.h]=.5<Math.abs((d-this.j)/this.j)?1:0;for(c=b=0;4>c;c++)b+=this.f[c]||0;3<=b&&this.o();this.j=d}this.i=a;this.m=this.b;this.h=(this.h+1)%4}};
hf.prototype.l=function(){window.clearInterval(this.G);gf(this.D)};var jf={};
function kf(a){if(null==v("_lact",window)){var b=parseInt(P("LACT"),10);b=isFinite(b)?z()-Math.max(b,0):-1;t("_lact",b,window);t("_fact",b,window);-1==b&&V();U(document,"keydown",V);U(document,"keyup",V);U(document,"mousedown",V);U(document,"mouseup",V);R("lact_local_listeners")||a?(U(window,"resize",function(){lf("resize",200)}),U(window,"scroll",function(){lf("scroll",200)}),new hf(function(){lf("mouse",100)}),U(document,"touchstart",V),U(document,"touchend",V)):(Zd("page-mouse",V),Zd("page-scroll",V),
Zd("page-resize",V))}}
function lf(a,b){jf[a]||(jf[a]=!0,Te(function(){V();jf[a]=!1},b))}
function V(){null==v("_lact",window)&&kf();var a=z();t("_lact",a,window);-1==v("_fact",window)&&t("_fact",a,window);(a=v("ytglobal.ytUtilActivityCallback_"))&&a()}
function mf(){var a=v("_lact",window);return null==a?-1:Math.max(z()-a,0)}
;function nf(a,b,c,d,e){this.f=a;this.i=b;this.h=c;this.g=d;this.b=e}
function of(a){var b={};void 0!==a.f?b.trackingParams=a.f:(b.veType=a.i,null!=a.h&&(b.veCounter=a.h),null!=a.g&&(b.elementIndex=a.g));void 0!==a.b&&(b.dataElement=of(a.b));return b}
var pf=1;var qf={log_event:"events",log_interaction:"interactions"},rf=Object.create(null);rf.log_event="GENERIC_EVENT_LOGGING";rf.log_interaction="INTERACTION_LOGGING";var sf={},tf={},uf=0,W=v("ytLoggingTransportLogPayloadsQueue_")||{};t("ytLoggingTransportLogPayloadsQueue_",W,void 0);var vf=v("ytLoggingTransportTokensToCttTargetIds_")||{};t("ytLoggingTransportTokensToCttTargetIds_",vf,void 0);var wf=v("ytLoggingTransportDispatchedStats_")||{};t("ytLoggingTransportDispatchedStats_",wf,void 0);
t("ytytLoggingTransportCapturedTime_",v("ytLoggingTransportCapturedTime_")||{},void 0);function xf(a,b){tf[a.endpoint]=b;if(a.W){var c=a.W;var d={};c.videoId?d.videoId=c.videoId:c.playlistId&&(d.playlistId=c.playlistId);vf[a.W.token]=d;c=yf(a.endpoint,a.W.token)}else c=yf(a.endpoint);c.push(a.payload);c.length>=(Number(R("web_logging_max_batch")||0)||20)?zf():Af()}
function zf(){Ud(uf);if(!Ya(W)){for(var a in W){var b=sf[a];if(!b){var c=tf[a];if(!c)continue;b=new c;sf[a]=b}c=void 0;var d=a,e=b,f=qf[d],g=wf[d]||{};wf[d]=g;b=Math.round(N());for(c in W[d]){var h=e.b;h={client:{hl:h.Ga,gl:h.Fa,clientName:h.Ea,clientVersion:h.innertubeContextClientVersion}};P("DELEGATED_SESSION_ID")&&(h.user={onBehalfOfUser:P("DELEGATED_SESSION_ID")});h={context:h};h[f]=yf(d,c);g.dispatchedEventCount=g.dispatchedEventCount||0;g.dispatchedEventCount+=h[f].length;h.requestTimeMs=b;
var k=vf[c];if(k)a:{var m=h,u=c;if(k.videoId)var Z="VIDEO";else if(k.playlistId)Z="PLAYLIST";else break a;m.credentialTransferTokenTargetId=k;m.context=m.context||{};m.context.user=m.context.user||{};m.context.user.credentialTransferTokens=[{token:u,scope:Z}]}delete vf[c];Bf(e,d,h)}c=g;d=b;c.previousDispatchMs&&(b=d-c.previousDispatchMs,e=c.diffCount||0,c.averageTimeBetweenDispatchesMs=e?(c.averageTimeBetweenDispatchesMs*e+b)/(e+1):b,c.diffCount=e+1);c.previousDispatchMs=d;delete W[a]}Ya(W)||Af()}}
function Af(){Ud(uf);uf=T(zf,P("LOGGING_BATCH_TIMEOUT",1E4))}
function yf(a,b){b=void 0===b?"":b;W[a]=W[a]||{};W[a][b]=W[a][b]||[];return W[a][b]}
;function Cf(a,b,c,d){var e=Df,f={};f.eventTimeMs=Math.round(c||N());f[a]=b;f.context={lastActivityMs:String(c?-1:mf())};xf({endpoint:"log_event",payload:f,W:d},e)}
;function Ef(a,b,c){c.context&&c.context.capabilities&&(c=c.context.capabilities,c.snapshot||c.golden)&&(a="vix");return"/youtubei/"+a+"/"+b}
;function Df(a){this.b=a||{innertubeApiKey:Nd("INNERTUBE_API_KEY"),innertubeApiVersion:Nd("INNERTUBE_API_VERSION"),Ea:P("INNERTUBE_CONTEXT_CLIENT_NAME","WEB"),innertubeContextClientVersion:Nd("INNERTUBE_CONTEXT_CLIENT_VERSION"),Ga:Nd("INNERTUBE_CONTEXT_HL"),Fa:Nd("INNERTUBE_CONTEXT_GL"),Ha:Nd("INNERTUBE_HOST_OVERRIDE")||""}}
function Bf(a,b,c){var d={};!P("VISITOR_DATA")&&.01>Math.random()&&Q(Error("Missing VISITOR_DATA when sending innertube request."),"WARNING");var e={headers:{"Content-Type":"application/json","X-Goog-Visitor-Id":P("VISITOR_DATA","")},method:"POST",A:c,pa:"JSON",L:function(){d.L()},
oa:d.L,C:function(a,b){d.C&&d.C(b)},
gb:function(a){d.C&&d.C(a)},
onError:function(a,b){if(d.onError)d.onError(b)},
fb:function(a){if(d.onError)d.onError(a)},
timeout:d.timeout,withCredentials:!0},f=Zb();f&&(e.headers.Authorization=f,e.headers["X-Goog-AuthUser"]=P("SESSION_INDEX",0));var g="",h=a.b.Ha;h&&(g=h);f&&!g&&(e.headers["x-origin"]=window.location.origin);a=""+g+Ef(a.b.innertubeApiVersion,b,c)+"?alt=json&key="+a.b.innertubeApiKey;try{R("use_fetch_for_op_xhr")?ze(a,e):Ie(a,e)}catch(k){if("InvalidAccessError"==k)Q(Error("An extension is blocking network request."),"WARNING");else throw k;}}
;var Ff=z().toString();
function Gf(){a:{if(window.crypto&&window.crypto.getRandomValues)try{var a=Array(16),b=new Uint8Array(16);window.crypto.getRandomValues(b);for(var c=0;c<a.length;c++)a[c]=b[c];var d=a;break a}catch(e){}d=Array(16);for(a=0;16>a;a++){b=z();for(c=0;c<b%23;c++)d[a]=Math.random();d[a]=Math.floor(256*Math.random())}if(Ff)for(a=1,b=0;b<Ff.length;b++)d[a%16]=d[a%16]^d[(a-1)%16]/4^Ff.charCodeAt(b),a++}a=[];for(b=0;b<d.length;b++)a.push("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_".charAt(d[b]&63));
return a.join("")}
;var Hf=Gf();function If(){if(!Jf&&!Kf||!window.JSON)return null;try{var a=Jf.get("yt-player-two-stage-token")}catch(b){}if(!r(a))try{a=Kf.get("yt-player-two-stage-token")}catch(b){}if(!r(a))return null;try{a=JSON.parse(a,void 0)}catch(b){}return a}
var Kf,Lf=new md;Kf=Lf.isAvailable()?new id(Lf):null;var Jf,Mf=new nd;Jf=Mf.isAvailable()?new id(Mf):null;function Nf(){var a=P("ROOT_VE_TYPE",void 0);return a?new nf(void 0,a,void 0):null}
function Of(){var a=P("client-screen-nonce")||P("EVENT_ID");return a?a:null}
;function Pf(a,b,c){Yb.set(""+a,b,c,"/","youtube.com",!1)}
;function Qf(a){if(a){a=a.itct||a.ved;var b=v("yt.logging.screen.storeParentElement");a&&b&&b(new nf(a))}}
;function Rf(a,b,c){b=void 0===b?{}:b;c=void 0===c?!1:c;var d=P("EVENT_ID");d&&(b.ei||(b.ei=d));if(b){d=a;var e=P("VALID_SESSION_TEMPDATA_DOMAINS",[]),f=rd(J(window.location.href)[3]||null);f&&e.push(f);f=rd(J(d)[3]||null);if(0<=wa(e,f)||!f&&0==d.lastIndexOf("/",0))if(R("autoescape_tempdata_url")&&(e=document.createElement("a"),Bb(e,d),d=e.href),d){f=J(d);d=f[5];e=f[6];f=f[7];var g="";d&&(g+=d);e&&(g+="?"+e);f&&(g+="#"+f);d=g;e=d.indexOf("#");if(d=0>e?d:d.substr(0,e)){if(b.itct||b.ved)b.csn=b.csn||
Of();if(h){var h=parseInt(h,10);isFinite(h)&&0<h&&(d="ST-"+Oa(d).toString(36),e=b?td(b):"",Pf(d,e,h||5),Qf(b))}else h="ST-"+Oa(d).toString(36),d=b?td(b):"",Pf(h,d,5),Qf(b)}}}if(c)return!1;if((window.ytspf||{}).enabled)spf.navigate(a);else{var k=void 0===k?{}:k;var m=void 0===m?"":m;var u=void 0===u?window:u;c=u.location;a=ud(a,k)+m;a=a instanceof E?a:wb(a);c.href=ub(a)}return!0}
;t("yt.abuse.botguardInitialized",v("yt.abuse.botguardInitialized")||qe,void 0);t("yt.abuse.invokeBotguard",v("yt.abuse.invokeBotguard")||re,void 0);t("yt.abuse.dclkstatus.checkDclkStatus",v("yt.abuse.dclkstatus.checkDclkStatus")||$e,void 0);t("yt.player.exports.navigate",v("yt.player.exports.navigate")||Rf,void 0);t("yt.util.activity.init",v("yt.util.activity.init")||kf,void 0);t("yt.util.activity.getTimeSinceActive",v("yt.util.activity.getTimeSinceActive")||mf,void 0);
t("yt.util.activity.setTimestamp",v("yt.util.activity.setTimestamp")||V,void 0);function Sf(a,b,c){Tf({attachChild:{csn:a,parentVisualElement:of(b),visualElements:[of(c)]}})}
function Tf(a){var b=Df;a.eventTimeMs=Math.round(N());a.lactMs=mf();xf({endpoint:"log_interaction",payload:a},b)}
;function Uf(a){a=a||{};this.url=a.url||"";this.args=a.args||$a(Vf);this.assets=a.assets||{};this.attrs=a.attrs||$a(Wf);this.params=a.params||$a(Xf);this.minVersion=a.min_version||"8.0.0";this.fallback=a.fallback||null;this.fallbackMessage=a.fallbackMessage||null;this.html5=!!a.html5;this.disable=a.disable||{};this.loaded=!!a.loaded;this.messages=a.messages||{}}
var Vf={enablejsapi:1},Wf={},Xf={allowscriptaccess:"always",allowfullscreen:"true",bgcolor:"#000000"};function Yf(a){var b=new Uf,c;for(c in a)if(a.hasOwnProperty(c)){var d=a[c];b[c]="object"==oa(d)?$a(d):d}return b}
;function Zf(){G.call(this);this.b=[]}
n(Zf,G);Zf.prototype.l=function(){for(;this.b.length;){var a=this.b.pop();a.target.removeEventListener(a.name,a.bb)}G.prototype.l.call(this)};var $f=/cssbin\/(?:debug-)?([a-zA-Z0-9_-]+?)(?:-2x|-web|-rtl|-vfl|.css)/;function ag(a){a=a||"";if(window.spf){var b=a.match($f);spf.style.load(a,b?b[1]:"",void 0)}else bg(a)}
function bg(a){var b=cg(a),c=document.getElementById(b),d=c&&Sd(c,"loaded");d||c&&!d||(c=dg(a,b,function(){Sd(c,"loaded")||(Qd(c),be(b),T(y(ce,b),0))}))}
function dg(a,b,c){var d=document.createElement("link");d.id=b;d.onload=function(){c&&setTimeout(c,0)};
a=Mb(a);Cb(d,a,"stylesheet");(document.getElementsByTagName("head")[0]||document.body).appendChild(d);return d}
function cg(a){var b=document.createElement("A");a=xb(a);Bb(b,a);b=b.href.replace(/^[a-zA-Z]+:\/\//,"//");return"css-"+Oa(b)}
;var eg=v("ytLoggingLatencyUsageStats_")||{};t("ytLoggingLatencyUsageStats_",eg,void 0);var fg=0;function gg(a){eg[a]=eg[a]||{count:0};var b=eg[a];b.count++;b.time=N();fg||(fg=Ue(hg,0,5E3));return 10<b.count?(11==b.count&&Pe(Error("CSI data exceeded logging limit with key: "+a),0==a.indexOf("info")?"WARNING":"ERROR"),!0):!1}
function hg(){var a=N(),b;for(b in eg)6E4<a-eg[b].time&&delete eg[b];fg=0}
;function ig(a,b){this.version=a;this.args=b}
;function jg(a){this.topic=a}
jg.prototype.toString=function(){return this.topic};var kg=v("ytPubsub2Pubsub2Instance")||new I;I.prototype.subscribe=I.prototype.subscribe;I.prototype.unsubscribeByKey=I.prototype.I;I.prototype.publish=I.prototype.J;I.prototype.clear=I.prototype.clear;t("ytPubsub2Pubsub2Instance",kg,void 0);t("ytPubsub2Pubsub2SubscribedKeys",v("ytPubsub2Pubsub2SubscribedKeys")||{},void 0);t("ytPubsub2Pubsub2TopicToKeys",v("ytPubsub2Pubsub2TopicToKeys")||{},void 0);t("ytPubsub2Pubsub2IsAsync",v("ytPubsub2Pubsub2IsAsync")||{},void 0);
t("ytPubsub2Pubsub2SkipSubKey",null,void 0);function lg(a,b){var c=v("ytPubsub2Pubsub2Instance");c&&c.publish.call(c,a.toString(),a,b)}
;var X=window.performance||window.mozPerformance||window.msPerformance||window.webkitPerformance||{};function mg(){var a=P("TIMING_TICK_EXPIRATION");a||(a={},O("TIMING_TICK_EXPIRATION",a));return a}
function ng(){var a=mg(),b;for(b in a)We(a[b]);O("TIMING_TICK_EXPIRATION",{})}
;function og(a,b){ig.call(this,1,arguments)}
n(og,ig);function pg(a,b){ig.call(this,1,arguments)}
n(pg,ig);var qg=new jg("aft-recorded"),rg=new jg("timing-sent");var sg={vc:!0},tg={ad_allowed:"adTypesAllowed",ad_at:"adType",ad_cpn:"adClientPlaybackNonce",ad_docid:"adVideoId",yt_ad_an:"adNetworks",p:"httpProtocol",t:"transportProtocol",cpn:"clientPlaybackNonce",csn:"clientScreenNonce",docid:"videoId",is_nav:"isNavigation",yt_lt:"loadType",yt_ad:"isMonetized",nr:"webInfo.navigationReason",ncnp:"webInfo.nonPreloadedNodeCount",paused:"playerInfo.isPausedOnLoad",fmt:"playerInfo.itag",yt_pl:"watchInfo.isPlaylist",yt_ad_pr:"prerollAllowed",yt_red:"isRedSubscriber",
st:"serverTimeMs",vph:"viewportHeight",vpw:"viewportWidth",yt_vis:"isVisible"},wg="ap c cver ei srt yt_fss yt_li plid vpil vpni vpst yt_eil vpni2 vpil2 icrc icrt pa GetBrowse_rid GetPlayer_rid GetSearch_rid GetWatchNext_rid cmt pc prerender psc rc start yt_abt yt_fn yt_fs yt_pft yt_pre yt_pt yt_pvis yt_ref yt_sts".split(" "),xg="isNavigation isMonetized playerInfo.isPausedOnLoad prerollAllowed isRedSubscriber isVisible watchInfo.isPlaylist".split(" "),yg=!1;
function zg(a){if("_"!=a[0]){var b=a;X.mark&&(0==b.lastIndexOf("mark_",0)||(b="mark_"+b),X.mark(b))}b=Ag();var c=N();b[a]&&(b["_"+a]=b["_"+a]||[b[a]],b["_"+a].push(c));b[a]=c;b=mg();if(c=b[a])We(c),b[a]=0;Bg()["tick_"+a]=void 0;N();R("csi_on_gel")?(b=Cg(),"_start"==a?gg("baseline_"+b)||Cf("latencyActionBaselined",{clientActionNonce:b},void 0,void 0):gg("tick_"+a+"_"+b)||Cf("latencyActionTicked",{tickName:a,clientActionNonce:b},void 0,void 0),a=!0):a=!1;if(a=!a)a=!v("yt.timing.pingSent_");if(a&&(b=
Nd("TIMING_ACTION"),a=Ag(),v("ytglobal.timingready_")&&b&&a._start&&(b=Dg()))){R("tighter_critical_section")&&!yg&&(lg(qg,new og(Math.round(b-a._start),void 0)),yg=!0);b=!0;c=P("TIMING_WAIT",[]);if(c.length)for(var d=0,e=c.length;d<e;++d)if(!(c[d]in a)){b=!1;break}b&&Eg()}}
function Fg(){var a=Gg().info.yt_lt="hot_bg";Bg().info_yt_lt=a;if(R("csi_on_gel"))if("yt_lt"in tg){var b={},c=tg.yt_lt;0<=wa(xg,c)&&(a=!!a);c=c.split(".");for(var d=b,e=0;e<c.length-1;e++)d[c[e]]=d[c[e]]||{},d=d[c[e]];b[c[c.length-1]]=a;a=Cg();c=Object.keys(b).join("");gg("info_"+c+"_"+a)||(b.clientActionNonce=a,Cf("latencyActionInfo",b,void 0,void 0))}else 0<=wa(wg,"yt_lt")||Q(Error("Unknown label yt_lt logged with GEL CSI."))}
function Dg(){var a=Ag();if(a.aft)return a.aft;for(var b=P("TIMING_AFT_KEYS",["ol"]),c=b.length,d=0;d<c;d++){var e=a[b[d]];if(e)return e}return NaN}
function Eg(){ng();if(!R("csi_on_gel")){var a=Ag(),b=Gg().info,c=a._start,d;for(d in a)if(0==d.lastIndexOf("_",0)&&w(a[d])){var e=d.slice(1);if(e in sg){var f=ya(a[d],function(a){return Math.round(a-c)});
b["all_"+e]=f.join()}delete a[d]}e=!!b.ap;if(f=v("ytglobal.timingReportbuilder_")){if(f=f(a,b,void 0))Hg(f,e),Ig(),Jg(),Kg(!1,void 0),P("TIMING_ACTION")&&O("PREVIOUS_ACTION",P("TIMING_ACTION")),O("TIMING_ACTION","")}else{var g=P("CSI_SERVICE_NAME","youtube");f={v:2,s:g,action:P("TIMING_ACTION",void 0)};var h=b.srt;void 0!==a.srt&&delete b.srt;if(b.h5jse){var k=window.location.protocol+v("ytplayer.config.assets.js");(k=X.getEntriesByName?X.getEntriesByName(k)[0]:null)?b.h5jse=Math.round(b.h5jse-k.responseEnd):
delete b.h5jse}a.aft=Dg();Lg()&&"youtube"==g&&(Fg(),g=a.vc,k=a.pbs,delete a.aft,b.aft=Math.round(k-g));for(var m in b)"_"!=m.charAt(0)&&(f[m]=b[m]);a.ps=N();b={};m=[];for(d in a)"_"!=d.charAt(0)&&(g=Math.round(a[d]-c),b[d]=g,m.push(d+"."+g));f.rt=m.join(",");(a=v("ytdebug.logTiming"))&&a(f,b);Hg(f,e,void 0);lg(rg,new pg(b.aft+(h||0),void 0))}}}
var Jg=x(X.clearResourceTimings||X.webkitClearResourceTimings||X.mozClearResourceTimings||X.msClearResourceTimings||X.oClearResourceTimings||ma,X);
function Hg(a,b,c){if(R("debug_csi_data")){var d=v("yt.timing.csiData");d||(d=[],t("yt.timing.csiData",d,void 0));d.push({page:location.href,time:new Date,args:a})}d="";for(var e in a)d+="&"+e+"="+a[e];a="/csi_204?"+d.substring(1);if(window.navigator&&window.navigator.sendBeacon&&b){var f=void 0===f?"":f;try{window.navigator&&window.navigator.sendBeacon&&window.navigator.sendBeacon(a,f)||Le(a,void 0,void 0,void 0,f)}catch(g){Le(a,void 0,void 0,void 0,f)}}else Le(a);Kg(!0,c)}
function Cg(){var a=Gg().nonce;a||(a=Gf(),Gg().nonce=a);return a}
function Ag(){return Gg().tick}
function Bg(){var a=Gg();"gel"in a||(a.gel={});return a.gel}
function Gg(){return v("ytcsi.data_")||Ig()}
function Ig(){var a={tick:{},info:{}};t("ytcsi.data_",a,void 0);return a}
function Kg(a,b){t("yt.timing."+(b||"")+"pingSent_",a,void 0)}
function Lg(){var a=Ag(),b=a.pbr,c=a.vc;a=a.pbs;return b&&c&&a&&b<c&&c<a&&1==Gg().info.yt_pvis}
;function Mg(a,b){G.call(this);this.m=this.S=a;this.G=b;this.o=!1;this.f={};this.P=this.F=null;this.w=new I;nc(this,y(oc,this.w));this.i={};this.N=this.R=this.h=this.Y=this.b=null;this.M=!1;this.j=this.D=null;this.T={};this.ta=["onReady"];this.X=null;this.ka=NaN;this.O={};Ng(this);this.V("WATCH_LATER_VIDEO_ADDED",this.Ja.bind(this));this.V("WATCH_LATER_VIDEO_REMOVED",this.Ka.bind(this));this.V("onAdAnnounce",this.xa.bind(this));this.ua=new Zf(this);nc(this,y(oc,this.ua))}
n(Mg,G);l=Mg.prototype;
l.ha=function(a){if(!this.g){a instanceof Uf||(a=new Uf(a));this.Y=a;this.b=Yf(a);this.h=this.b.attrs.id||this.h;"video-player"==this.h&&(this.h=this.G,this.b.attrs.id=this.G);this.m.id==this.h&&(this.h+="-player",this.b.attrs.id=this.h);this.b.args.enablejsapi="1";this.b.args.playerapiid=this.G;this.R||(this.R=Og(this,this.b.args.jsapicallback||"onYouTubePlayerReady"));this.b.args.jsapicallback=null;if(a=this.b.attrs.width)this.m.style.width=Rb(Number(a)||a);if(a=this.b.attrs.height)this.m.style.height=Rb(Number(a)||
a);Pg(this);this.o&&Qg(this)}};
l.Aa=function(){return this.Y};
function Qg(a){a.b.loaded||(a.b.loaded=!0,"0"!=a.b.args.autoplay?a.f.loadVideoByPlayerVars(a.b.args):a.f.cueVideoByPlayerVars(a.b.args))}
function Rg(a){var b=!0,c=Sg(a);c&&a.b&&(a=a.b,b=Sd(c,"version")==a.assets.js);return b&&!!v("yt.player.Application.create")}
function Pg(a){if(!a.g&&!a.M){var b=Rg(a);if(b&&"html5"==(Sg(a)?"html5":null))a.N="html5",a.o||Tg(a);else if(Ug(a),a.N="html5",b&&a.j)a.S.appendChild(a.j),Tg(a);else{a.b.loaded=!0;var c=!1;a.D=function(){c=!0;var b=Yf(a.b);v("yt.player.Application.create")(a.S,b);Tg(a)};
a.M=!0;b?a.D():(ge(a.b.assets.js,a.D),ag(a.b.assets.css),Vg(a)&&!c&&t("yt.player.Application.create",null,void 0))}}}
function Sg(a){var b=Gb(a.h);!b&&a.m&&a.m.querySelector&&(b=a.m.querySelector("#"+a.h));return b}
function Tg(a){if(!a.g){var b=Sg(a),c=!1;b&&b.getApiInterface&&b.getApiInterface()&&(c=!0);c?(a.M=!1,b.isNotServable&&b.isNotServable(a.b.args.video_id)||Wg(a)):a.ka=T(function(){Tg(a)},50)}}
function Wg(a){Ng(a);a.o=!0;var b=Sg(a);b.addEventListener&&(a.F=Xg(a,b,"addEventListener"));b.removeEventListener&&(a.P=Xg(a,b,"removeEventListener"));var c=b.getApiInterface();c=c.concat(b.getInternalApiInterface());for(var d=0;d<c.length;d++){var e=c[d];a.f[e]||(a.f[e]=Xg(a,b,e))}for(var f in a.i)a.F(f,a.i[f]);Qg(a);a.R&&a.R(a.f);a.w.J("onReady",a.f)}
function Xg(a,b,c){var d=b[c];return function(){try{return a.X=null,d.apply(b,arguments)}catch(e){"sendAbandonmentPing"!=c&&(e.message+=" ("+c+")",a.X=e,Q(e,"WARNING",void 0,void 0,void 0))}}}
function Ng(a){a.o=!1;if(a.P)for(var b in a.i)a.P(b,a.i[b]);for(var c in a.O)Ud(parseInt(c,10));a.O={};a.F=null;a.P=null;for(var d in a.f)a.f[d]=null;a.f.addEventListener=a.V.bind(a);a.f.removeEventListener=a.Qa.bind(a);a.f.destroy=a.dispose.bind(a);a.f.getLastError=a.Ba.bind(a);a.f.getPlayerType=a.Ca.bind(a);a.f.getCurrentVideoConfig=a.Aa.bind(a);a.f.loadNewVideoConfig=a.ha.bind(a);a.f.isReady=a.Ia.bind(a)}
l.Ia=function(){return this.o};
l.V=function(a,b){var c=this,d=Og(this,b);if(d){if(!(0<=wa(this.ta,a)||this.i[a])){var e=Yg(this,a);this.F&&this.F(a,e)}this.w.subscribe(a,d);"onReady"==a&&this.o&&T(function(){d(c.f)},0)}};
l.Qa=function(a,b){if(!this.g){var c=Og(this,b);c&&bd(this.w,a,c)}};
function Og(a,b){var c=b;if("string"==typeof b){if(a.T[b])return a.T[b];c=function(){var a=v(b);a&&a.apply(p,arguments)};
a.T[b]=c}return c?c:null}
function Yg(a,b){var c="ytPlayer"+b+a.G;a.i[b]=c;p[c]=function(c){var d=a.b&&a.b.args&&a.b.args.fflags;if(d&&0>d.indexOf("use_html5_player_event_timeout=true"))a.w.J(b,c);else{var f=T(function(){if(!a.g){a.w.J(b,c);var d=a.O,e=String(f);e in d&&delete d[e]}},0);
Za(a.O,String(f))}};
return c}
l.xa=function(a){be("a11y-announce",a)};
l.Ja=function(a){be("WATCH_LATER_VIDEO_ADDED",a)};
l.Ka=function(a){be("WATCH_LATER_VIDEO_REMOVED",a)};
l.Ca=function(){return this.N||(Sg(this)?"html5":null)};
l.Ba=function(){return this.X};
function Ug(a){zg("dcp");a.cancel();Ng(a);a.N=null;a.b&&(a.b.loaded=!1);var b=Sg(a);b&&(Rg(a)||!Vg(a)?a.j=b:(b&&b.destroy&&b.destroy(),a.j=null));for(a=a.S;b=a.firstChild;)a.removeChild(b)}
l.cancel=function(){this.D&&me(this.b.assets.js,this.D);Ud(this.ka);this.M=!1};
l.l=function(){Ug(this);if(this.j&&this.b&&this.j.destroy)try{this.j.destroy()}catch(b){Q(Error("Error destroying player: "+b))}this.T=null;for(var a in this.i)p[this.i[a]]=null;this.Y=this.b=this.f=null;delete this.S;delete this.m;G.prototype.l.call(this)};
function Vg(a){return a.b&&a.b.args&&a.b.args.fflags?-1!=a.b.args.fflags.indexOf("player_destroy_old_version=true"):!1}
;var Zg={},$g="player_uid_"+(1E9*Math.random()>>>0);function ah(a){var b="player";b=r(b)?Gb(b):b;var c=$g+"_"+(b[sa]||(b[sa]=++ta)),d=Zg[c];if(d)return d.ha(a),d.f;d=new Mg(b,c);Zg[c]=d;be("player-added",d.f);nc(d,y(bh,d));T(function(){d.ha(a)},0);
return d.f}
function bh(a){delete Zg[a.G]}
;function ch(a){return(0==a.search("cue")||0==a.search("load"))&&"loadModule"!=a}
function dh(a,b,c){r(a)&&(a={mediaContentUrl:a,startSeconds:b,suggestedQuality:c});b=/\/([ve]|embed)\/([^#?]+)/.exec(a.mediaContentUrl);a.videoId=b&&b[2]?b[2]:null;return eh(a)}
function eh(a,b,c){if(ra(a)){b="endSeconds startSeconds mediaContentUrl suggestedQuality videoId two_stage_token".split(" ");c={};for(var d=0;d<b.length;d++){var e=b[d];a[e]&&(c[e]=a[e])}return c}return{videoId:a,startSeconds:b,suggestedQuality:c}}
function fh(a,b,c,d){if(ra(a)&&!w(a)){b="playlist list listType index startSeconds suggestedQuality".split(" ");c={};for(d=0;d<b.length;d++){var e=b[d];a[e]&&(c[e]=a[e])}return c}b={index:b,startSeconds:c,suggestedQuality:d};r(a)&&16==a.length?b.list="PL"+a:b.playlist=a;return b}
function gh(a){var b=a.video_id||a.videoId;if(r(b)){var c=If()||{},d=If()||{};q(void 0)?d[b]=void 0:delete d[b];var e=z()+3E5,f=Kf;if(f&&window.JSON){r(d)||(d=JSON.stringify(d,void 0));try{f.set("yt-player-two-stage-token",d,e)}catch(g){f.remove("yt-player-two-stage-token")}}(b=c[b])&&(a.two_stage_token=b)}}
;function hh(a){G.call(this);this.b=a;this.b.subscribe("command",this.qa,this);this.f={};this.i=!1}
A(hh,G);l=hh.prototype;l.start=function(){this.i||this.g||(this.i=!0,ih(this.b,"RECEIVING"))};
l.qa=function(a,b,c){if(this.i&&!this.g){var d=b||{};switch(a){case "addEventListener":r(d.event)&&(a=d.event,a in this.f||(c=x(this.Sa,this,a),this.f[a]=c,this.addEventListener(a,c)));break;case "removeEventListener":r(d.event)&&jh(this,d.event);break;default:this.h.isReady()&&this.h[a]&&(b=kh(a,b||{}),c=this.h.handleExternalCall(a,b,c||null),(c=lh(a,c))&&this.i&&!this.g&&ih(this.b,a,c))}}};
l.Sa=function(a,b){this.i&&!this.g&&ih(this.b,a,this.ba(a,b))};
l.ba=function(a,b){if(null!=b)return{value:b}};
function jh(a,b){b in a.f&&(a.removeEventListener(b,a.f[b]),delete a.f[b])}
l.l=function(){var a=this.b;a.g||bd(a.b,"command",this.qa,this);this.b=null;for(var b in this.f)jh(this,b);hh.u.l.call(this)};function mh(a,b){hh.call(this,b);this.h=a;this.start()}
A(mh,hh);mh.prototype.addEventListener=function(a,b){this.h.addEventListener(a,b)};
mh.prototype.removeEventListener=function(a,b){this.h.removeEventListener(a,b)};
function kh(a,b){switch(a){case "loadVideoById":return b=eh(b),gh(b),[b];case "cueVideoById":return b=eh(b),gh(b),[b];case "loadVideoByPlayerVars":return gh(b),[b];case "cueVideoByPlayerVars":return gh(b),[b];case "loadPlaylist":return b=fh(b),gh(b),[b];case "cuePlaylist":return b=fh(b),gh(b),[b];case "seekTo":return[b.seconds,b.allowSeekAhead];case "playVideoAt":return[b.index];case "setVolume":return[b.volume];case "setPlaybackQuality":return[b.suggestedQuality];case "setPlaybackRate":return[b.suggestedRate];
case "setLoop":return[b.loopPlaylists];case "setShuffle":return[b.shufflePlaylist];case "getOptions":return[b.module];case "getOption":return[b.module,b.option];case "setOption":return[b.module,b.option,b.value];case "handleGlobalKeyDown":return[b.keyCode,b.shiftKey]}return[]}
function lh(a,b){switch(a){case "isMuted":return{muted:b};case "getVolume":return{volume:b};case "getPlaybackRate":return{playbackRate:b};case "getAvailablePlaybackRates":return{availablePlaybackRates:b};case "getVideoLoadedFraction":return{videoLoadedFraction:b};case "getPlayerState":return{playerState:b};case "getCurrentTime":return{currentTime:b};case "getPlaybackQuality":return{playbackQuality:b};case "getAvailableQualityLevels":return{availableQualityLevels:b};case "getDuration":return{duration:b};
case "getVideoUrl":return{videoUrl:b};case "getVideoEmbedCode":return{videoEmbedCode:b};case "getPlaylist":return{playlist:b};case "getPlaylistIndex":return{playlistIndex:b};case "getOptions":return{options:b};case "getOption":return{option:b}}}
mh.prototype.ba=function(a,b){switch(a){case "onReady":return;case "onStateChange":return{playerState:b};case "onPlaybackQualityChange":return{playbackQuality:b};case "onPlaybackRateChange":return{playbackRate:b};case "onError":return{errorCode:b}}return mh.u.ba.call(this,a,b)};
mh.prototype.l=function(){mh.u.l.call(this);delete this.h};function nh(a,b,c,d){G.call(this);this.f=b||null;this.o="*";this.h=c||null;this.sessionId=null;this.channel=d||null;this.D=!!a;this.m=x(this.w,this);window.addEventListener("message",this.m)}
n(nh,G);nh.prototype.w=function(a){if(!("*"!=this.h&&a.origin!=this.h||this.f&&a.source!=this.f)&&r(a.data)){try{var b=JSON.parse(a.data)}catch(c){return}if(!(null==b||this.D&&(this.sessionId&&this.sessionId!=b.id||this.channel&&this.channel!=b.channel))&&b)switch(b.event){case "listening":"null"!=a.origin&&(this.h=this.o=a.origin);this.f=a.source;this.sessionId=b.id;this.b&&(this.b(),this.b=null);break;case "command":this.i&&(!this.j||0<=wa(this.j,b.func))&&this.i(b.func,b.args,a.origin)}}};
nh.prototype.sendMessage=function(a,b){var c=b||this.f;if(c){this.sessionId&&(a.id=this.sessionId);this.channel&&(a.channel=this.channel);try{var d=yc(a);c.postMessage(d,this.o)}catch(e){Q(e,"WARNING")}}};
nh.prototype.l=function(){window.removeEventListener("message",this.m);G.prototype.l.call(this)};function oh(a,b,c){nh.call(this,a,b,c||P("POST_MESSAGE_ORIGIN",void 0)||window.document.location.protocol+"//"+window.document.location.hostname,"widget");this.j=this.b=this.i=null}
n(oh,nh);function ph(){var a=this.g=new oh(!!P("WIDGET_ID_ENFORCE")),b=x(this.Ma,this);a.i=b;a.j=null;this.g.channel="widget";if(a=P("WIDGET_ID"))this.g.sessionId=a;this.h=[];this.j=!1;this.i={}}
l=ph.prototype;l.Ma=function(a,b,c){"addEventListener"==a&&b?(a=b[0],this.i[a]||"onReady"==a||(this.addEventListener(a,qh(this,a)),this.i[a]=!0)):this.sa(a,b,c)};
l.sa=function(){};
function qh(a,b){return x(function(a){this.sendMessage(b,a)},a)}
l.addEventListener=function(){};
l.za=function(){this.j=!0;this.sendMessage("initialDelivery",this.ca());this.sendMessage("onReady");C(this.h,this.ra,this);this.h=[]};
l.ca=function(){return null};
function rh(a,b){a.sendMessage("infoDelivery",b)}
l.ra=function(a){this.j?this.g.sendMessage(a):this.h.push(a)};
l.sendMessage=function(a,b){this.ra({event:a,info:void 0==b?null:b})};
l.dispose=function(){this.g=null};function sh(a){ph.call(this);this.b=a;this.f=[];this.addEventListener("onReady",x(this.La,this));this.addEventListener("onVideoProgress",x(this.Wa,this));this.addEventListener("onVolumeChange",x(this.Xa,this));this.addEventListener("onApiChange",x(this.Ra,this));this.addEventListener("onPlaybackQualityChange",x(this.Ta,this));this.addEventListener("onPlaybackRateChange",x(this.Ua,this));this.addEventListener("onStateChange",x(this.Va,this));this.addEventListener("onWebglSettingsChanged",x(this.Ya,
this))}
A(sh,ph);l=sh.prototype;l.sa=function(a,b,c){if(this.b[a]){b=b||[];if(0<b.length&&ch(a)){var d=b;if(ra(d[0])&&!w(d[0]))d=d[0];else{var e={};switch(a){case "loadVideoById":case "cueVideoById":e=eh.apply(window,d);break;case "loadVideoByUrl":case "cueVideoByUrl":e=dh.apply(window,d);break;case "loadPlaylist":case "cuePlaylist":e=fh.apply(window,d)}d=e}gh(d);b.length=1;b[0]=d}this.b.handleExternalCall(a,b,c);ch(a)&&rh(this,this.ca())}};
l.La=function(){var a=x(this.za,this);this.g.b=a};
l.addEventListener=function(a,b){this.f.push({eventType:a,listener:b});this.b.addEventListener(a,b)};
l.ca=function(){if(!this.b)return null;var a=this.b.getApiInterface();Aa(a,"getVideoData");for(var b={apiInterface:a},c=0,d=a.length;c<d;c++){var e=a[c],f=e;if(0==f.search("get")||0==f.search("is")){f=e;var g=0;0==f.search("get")?g=3:0==f.search("is")&&(g=2);f=f.charAt(g).toLowerCase()+f.substr(g+1);try{var h=this.b[e]();b[f]=h}catch(k){}}}b.videoData=this.b.getVideoData();b.currentTimeLastUpdated_=z()/1E3;return b};
l.Va=function(a){a={playerState:a,currentTime:this.b.getCurrentTime(),duration:this.b.getDuration(),videoData:this.b.getVideoData(),videoStartBytes:0,videoBytesTotal:this.b.getVideoBytesTotal(),videoLoadedFraction:this.b.getVideoLoadedFraction(),playbackQuality:this.b.getPlaybackQuality(),availableQualityLevels:this.b.getAvailableQualityLevels(),videoUrl:this.b.getVideoUrl(),playlist:this.b.getPlaylist(),playlistIndex:this.b.getPlaylistIndex(),currentTimeLastUpdated_:z()/1E3,playbackRate:this.b.getPlaybackRate(),
mediaReferenceTime:this.b.getMediaReferenceTime()};this.b.getProgressState&&(a.progressState=this.b.getProgressState());this.b.getStoryboardFormat&&(a.storyboardFormat=this.b.getStoryboardFormat());rh(this,a)};
l.Ta=function(a){rh(this,{playbackQuality:a})};
l.Ua=function(a){rh(this,{playbackRate:a})};
l.Ra=function(){for(var a=this.b.getOptions(),b={namespaces:a},c=0,d=a.length;c<d;c++){var e=a[c],f=this.b.getOptions(e);b[e]={options:f};for(var g=0,h=f.length;g<h;g++){var k=f[g],m=this.b.getOption(e,k);b[e][k]=m}}this.sendMessage("apiInfoDelivery",b)};
l.Xa=function(){rh(this,{muted:this.b.isMuted(),volume:this.b.getVolume()})};
l.Wa=function(a){a={currentTime:a,videoBytesLoaded:this.b.getVideoBytesLoaded(),videoLoadedFraction:this.b.getVideoLoadedFraction(),currentTimeLastUpdated_:z()/1E3,playbackRate:this.b.getPlaybackRate(),mediaReferenceTime:this.b.getMediaReferenceTime()};this.b.getProgressState&&(a.progressState=this.b.getProgressState());rh(this,a)};
l.Ya=function(){if(this.b.getSphericalConfig){var a={sphericalConfig:this.b.getSphericalConfig()};rh(this,a)}};
l.dispose=function(){sh.u.dispose.call(this);for(var a=0;a<this.f.length;a++){var b=this.f[a];this.b.removeEventListener(b.eventType,b.listener)}this.f=[]};function th(){G.call(this);this.b=new I;nc(this,y(oc,this.b))}
A(th,G);th.prototype.subscribe=function(a,b,c){return this.g?0:this.b.subscribe(a,b,c)};
th.prototype.I=function(a){return this.g?!1:this.b.I(a)};
th.prototype.j=function(a,b){this.g||this.b.J.apply(this.b,arguments)};function uh(a,b,c){th.call(this);this.f=a;this.h=b;this.i=c}
A(uh,th);function ih(a,b,c){if(!a.g){var d=a.f;d.g||a.h!=d.b||(a={id:a.i,command:b},c&&(a.data=c),d.b.postMessage(yc(a),d.h))}}
uh.prototype.l=function(){this.h=this.f=null;uh.u.l.call(this)};function vh(a,b,c){G.call(this);this.b=a;this.h=c;this.i=U(window,"message",x(this.j,this));this.f=new uh(this,a,b);nc(this,y(oc,this.f))}
A(vh,G);vh.prototype.j=function(a){var b;if(b=!this.g)if(b=a.origin==this.h)a:{b=this.b;do{b:{var c=a.source;do{if(c==b){c=!0;break b}if(c==c.parent)break;c=c.parent}while(null!=c);c=!1}if(c){b=!0;break a}b=b.opener}while(null!=b);b=!1}if(b&&(b=a.data,r(b))){try{b=JSON.parse(b)}catch(d){return}b.command&&(c=this.f,c.g||c.j("command",b.command,b.data,a.origin))}};
vh.prototype.l=function(){gf(this.i);this.b=null;vh.u.l.call(this)};function wh(){var a=xh()?"//googleads.g.doubleclick.net/pagead/id?exp=nomnom":"//googleads.g.doubleclick.net/pagead/id",b=$a(yh);return new H(function(c,d){b.C=function(a){ue(a)?c(a):d(new zh("Request failed, status="+a.status,"net.badstatus",a))};
b.onError=function(a){d(new zh("Unknown request error","net.unknown",a))};
b.L=function(a){d(new zh("Request timed out","net.timeout",a))};
Ce(a,b)})}
function zh(a,b){B.call(this,a+", errorCode="+b);this.errorCode=b;this.name="PromiseAjaxError"}
n(zh,B);function Ah(a){this.f=void 0===a?null:a;this.g=0;this.b=null}
Ah.prototype.then=function(a,b,c){return this.f?this.f.then(a,b,c):1===this.g&&a?(a=a.call(c,this.b),Fc(a)?a:Bh(a)):2===this.g&&b?(a=b.call(c,this.b),Fc(a)?a:Ch(a)):this};
Ah.prototype.getValue=function(){return this.b};
Ec(Ah);function Ch(a){var b=new Ah;a=void 0===a?null:a;b.g=2;b.b=void 0===a?null:a;return b}
function Bh(a){var b=new Ah;a=void 0===a?null:a;b.g=1;b.b=void 0===a?null:a;return b}
;function Dh(a){B.call(this,a.message||a.description||a.name);this.isMissing=a instanceof Eh;this.isTimeout=a instanceof zh&&"net.timeout"==a.errorCode;this.isCanceled=a instanceof Tc}
n(Dh,B);Dh.prototype.name="BiscottiError";function Eh(){B.call(this,"Biscotti ID is missing from server")}
n(Eh,B);Eh.prototype.name="BiscottiMissingError";var yh={format:"RAW",method:"GET",timeout:5E3,withCredentials:!0},Fh=null;function Gh(){if("1"===Va(Od(),"args","privembed"))return Kc(Error("Biscotti ID is not available in private embed mode"));Fh||(Fh=Sc(wh().then(Hh),function(a){return Ih(2,a)}));
return Fh}
function xh(){var a;(a=!!Va(window,"settings","experiments","flags","html5_serverside_pagead_id_sets_cookie"))||(a=!!P("EXP_HTML5_SERVERSIDE_PAGEAD_ID_SETS_COOKIE",!1));return a||!!R("html5_serverside_pagead_id_sets_cookie")}
function Hh(a){a=a.responseText;if(0!=a.lastIndexOf(")]}'",0))throw new Eh;a=JSON.parse(a.substr(4));if(1<(a.type||1))throw new Eh;a=a.id;Jh(a);Fh=Bh(a);Kh(18E5,2);return a}
function Ih(a,b){var c=new Dh(b);Jh("");Fh=Ch(c);0<a&&Kh(12E4,a-1);throw c;}
function Kh(a,b){T(function(){Sc(wh().then(Hh,function(a){return Ih(b,a)}),ma)},a)}
function Jh(a){t("yt.ads.biscotti.lastId_",a,void 0)}
function Lh(){try{var a=v("yt.ads.biscotti.getId_");return a?a():Gh()}catch(b){return Kc(b)}}
;function Mh(a){B.apply(this,arguments)}
n(Mh,B);Mh.prototype.name="MutsuError";function Nh(){var a=new Mh("ID is missing"),b=new Mh("Timeout"),c=null,d=!1;Kd(function(){c=Id();d=!0});
if(d)return c?Bh(c):Ch(a);var e=new H(function(b,c){Kd(function(){var d=Id();d?b(d):c(a)})}),f=pd().then(function(){return Kc(b)});
return Qc(Nc([e,f]),function(){return f.cancel()})}
;function Oh(a){if("1"!==Va(Od(),"args","privembed")){a&&!v("yt.ads.biscotti.getId_")&&t("yt.ads.biscotti.getId_",Gh,void 0);try{var b=Lh();if(R("enable_mutsu")){v("yt.ads.mutsu.getId_")||t("yt.ads.mutsu.getId_",Nh,void 0);try{var c=v("yt.ads.mutsu.getId_")()}catch(d){c=Kc(d)}}else c=Kc(new Mh("unimplemented"));Oc([b,c]).then(function(a){var b=a[0];a=a[1];if(b.Z||a.Z){b=b.value;a=a.value;var c={};c.dt=Sb;c.flash=Ad||"0";a:{try{var d=window.top.location.href}catch(Qa){d=2;break a}d=null!=d?d==window.document.location.href?
0:1:2}d=(c.frm=d,c);d.u_tz=-(new Date).getTimezoneOffset();var h=void 0===h?F:h;try{var k=h.history.length}catch(Qa){k=0}d.u_his=k;d.u_java=!!F.navigator&&"unknown"!==typeof F.navigator.javaEnabled&&!!F.navigator.javaEnabled&&F.navigator.javaEnabled();F.screen&&(d.u_h=F.screen.height,d.u_w=F.screen.width,d.u_ah=F.screen.availHeight,d.u_aw=F.screen.availWidth,d.u_cd=F.screen.colorDepth);F.navigator&&F.navigator.plugins&&(d.u_nplug=F.navigator.plugins.length);F.navigator&&F.navigator.mimeTypes&&(d.u_nmime=
F.navigator.mimeTypes.length);d.ca_type=zd?"flash":"image";if(R("enable_server_side_search_pyv")||R("enable_server_side_mweb_search_pyv")){k=window;try{var m=k.screenX;var u=k.screenY}catch(Qa){}try{var Z=k.outerWidth;var Ca=k.outerHeight}catch(Qa){}try{var ug=k.innerWidth;var vg=k.innerHeight}catch(Qa){}m=[k.screenLeft,k.screenTop,m,u,k.screen?k.screen.availWidth:void 0,k.screen?k.screen.availTop:void 0,Z,Ca,ug,vg];u=window.top;try{var S=(u||window).document,Pa="CSS1Compat"==S.compatMode?S.documentElement:
S.body;var Da=(new Fb(Pa.clientWidth,Pa.clientHeight)).round()}catch(Qa){Da=new Fb(-12245933,-12245933)}S={};Pa=0;p.SVGElement&&p.document.createElementNS&&(Pa|=1);S.bc=Pa;S.bih=Da.height;S.biw=Da.width;S.brdim=m.join();Da=(S.vis={visible:1,hidden:2,prerender:3,preview:4,unloaded:5}[Qb.visibilityState||Qb.webkitVisibilityState||Qb.mozVisibilityState||""]||0,S.wgl=!!F.WebGLRenderingContext,S);for(var yd in Da)d[yd]=Da[yd]}void 0!==b&&(d.bid=b);void 0!==a&&(d.mutsuid=a);d.bsq=Ph++;Ie("//www.youtube.com/ad_data_204",
{Da:!1,A:d})}});
T(Oh,18E5)}catch(d){Q(d)}}}
var Ph=0;var Y=v("ytglobal.prefsUserPrefsPrefs_")||{};t("ytglobal.prefsUserPrefsPrefs_",Y,void 0);function Qh(){this.b=P("ALT_PREF_COOKIE_NAME","PREF");var a;if(a=Yb.get(""+this.b,void 0)){a=decodeURIComponent(a).split("&");for(var b=0;b<a.length;b++){var c=a[b].split("="),d=c[0];(c=c[1])&&(Y[d]=c.toString())}}}
l=Qh.prototype;l.get=function(a,b){Rh(a);Sh(a);var c=void 0!==Y[a]?Y[a].toString():null;return null!=c?c:b?b:""};
l.set=function(a,b){Rh(a);Sh(a);if(null==b)throw Error("ExpectedNotNull");Y[a]=b.toString()};
l.remove=function(a){Rh(a);Sh(a);delete Y[a]};
l.save=function(){var a=this.b,b=[],c;for(c in Y)b.push(c+"="+encodeURIComponent(String(Y[c])));Pf(a,b.join("&"),63072E3)};
l.clear=function(){for(var a in Y)delete Y[a]};
function Sh(a){if(/^f([1-9][0-9]*)$/.test(a))throw Error("ExpectedRegexMatch: "+a);}
function Rh(a){if(!/^\w+$/.test(a))throw Error("ExpectedRegexMismatch: "+a);}
function Th(a){a=void 0!==Y[a]?Y[a].toString():null;return null!=a&&/^[A-Fa-f0-9]+$/.test(a)?parseInt(a,16):null}
na(Qh);var Uh=null,Vh=null,Wh=null,Xh={};function Yh(a){Cf(a.payload_name,a.payload,void 0,void 0)}
function Zh(a){var b=a.id;a=a.ve_type;var c=pf++;a=new nf(void 0,a,c,void 0,void 0);Xh[b]=a;b=Of();c=Nf();b&&c&&Sf(b,c,a)}
function $h(a){var b=a.csn;a=a.root_ve_type;if(b&&a&&(O("client-screen-nonce",b),O("ROOT_VE_TYPE",a),b&&Cf("foregroundHeartbeatScreenAssociated",{clientDocumentNonce:Hf,clientScreenNonce:b}),a=Nf()))for(var c in Xh){var d=Xh[c];d&&Sf(b,a,d)}}
function ai(a){Xh[a.id]=new nf(a.tracking_params)}
function bi(a){var b=Of();a=Xh[a.id];b&&a&&(R("interaction_click_on_gel_web")?Cf("visualElementGestured",{csn:b,ve:of(a),gestureType:"INTERACTION_LOGGING_GESTURE_TYPE_GENERIC_CLICK"}):Tf({click:{csn:b,visualElement:of(a)}}))}
function ci(a){a=a.ids;var b=Of();if(b)for(var c=0;c<a.length;c++){var d=Xh[a[c]];d&&Cf("visualElementShown",{csn:b,ve:of(d),eventType:1})}}
function di(){var a=Uh;a&&a.startInteractionLogging&&a.startInteractionLogging()}
;t("yt.setConfig",O,void 0);t("yt.config.set",O,void 0);t("yt.setMsg",Re,void 0);t("yt.msgs.set",Re,void 0);t("yt.logging.errors.log",Pe,void 0);
t("writeEmbed",function(){var a=P("PLAYER_CONFIG",void 0);Oh(!0);"gvn"==a.args.ps&&(document.body.style.backgroundColor="transparent");var b=document.referrer,c=P("POST_MESSAGE_ORIGIN");window!=window.top&&b&&b!=document.URL&&(a.args.loaderUrl=b);P("LIGHTWEIGHT_AUTOPLAY")&&(a.args.autoplay="1");a.args.autoplay&&gh(a.args);Uh=a=ah(a);a.addEventListener("onScreenChanged",$h);a.addEventListener("onLogClientVeCreated",Zh);a.addEventListener("onLogServerVeCreated",ai);a.addEventListener("onLogToGel",Yh);
a.addEventListener("onLogVeClicked",bi);a.addEventListener("onLogVesShown",ci);a.addEventListener("onReady",di);b=P("POST_MESSAGE_ID","player");P("ENABLE_JS_API")?Wh=new sh(a):P("ENABLE_POST_API")&&r(b)&&r(c)&&(Vh=new vh(window.parent,b,c),Wh=new mh(a,Vh.f));P("BG_P")&&(P("BG_I")||P("BG_IU"))&&oe();Ze()},void 0);
t("yt.www.watch.ads.restrictioncookie.spr",function(a){Le(a+"mac_204?action_fcts=1");return!0},void 0);
var ei=Pd(function(){zg("ol");var a=Qh.getInstance(),b=!!((Th("f"+(Math.floor(119/31)+1))||0)&67108864),c=1<window.devicePixelRatio;if(document.body&&rc(document.body,"exp-invert-logo"))if(c&&!rc(document.body,"inverted-hdpi")){var d=document.body;d.classList?d.classList.add("inverted-hdpi"):rc(d,"inverted-hdpi")||(d.className+=0<d.className.length?" inverted-hdpi":"inverted-hdpi")}else!c&&rc(document.body,"inverted-hdpi")&&sc();b!=c&&(b="f"+(Math.floor(119/31)+1),d=Th(b)||0,d=c?d|67108864:d&-67108865,
0==d?delete Y[b]:Y[b]=d.toString(16).toString(),a.save())}),fi=Pd(function(){var a=Uh;
a&&a.sendAbandonmentPing&&a.sendAbandonmentPing();P("PL_ATT")&&(ne=null);a=0;for(var b=Xe.length;a<b;a++)We(Xe[a]);Xe.length=0;le("//static.doubleclick.net/instream/ad_status.js");Ye=!1;O("DCLKSTAT",0);pc(Wh,Vh);if(a=Uh)a.removeEventListener("onScreenChanged",$h),a.removeEventListener("onLogClientVeCreated",Zh),a.removeEventListener("onLogServerVeCreated",ai),a.removeEventListener("onLogToGel",Yh),a.removeEventListener("onLogVeClicked",bi),a.removeEventListener("onLogVesShown",ci),a.removeEventListener("onReady",
di),a.destroy();Xh={}});
window.addEventListener?(window.addEventListener("load",ei),window.addEventListener("unload",fi)):window.attachEvent&&(window.attachEvent("onload",ei),window.attachEvent("onunload",fi));}).call(this);
