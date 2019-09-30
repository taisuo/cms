function setCookie(name, value, expires, path, domain, secure) {
	var cookieText = encodeURIComponent(name) + '=' + encodeURIComponent(value);
	if (typeof(expires)=="number")  {
		var _date=new Date();
		_date.setDate(_date.getDate()+expires);
		cookieText += '; expires=' + _date;
	}
	if (path) {
		cookieText += '; path =' + path;
	}
	if (domain) {
		cookieText += '; domain=' + domain;
	}
	document.cookie = cookieText;
}
function getCookie(name) {
	console.log("_--getCookie")
	var cookieName = encodeURIComponent(name) + '=';
	var cookieStart = document.cookie.indexOf(cookieName);
	var cookieValue = null;

	if (cookieStart > -1) {
		var cookieEnd = document.cookie.indexOf(';', cookieStart);
		if (cookieEnd == -1) {
			cookieEnd = document.cookie.length;
		}
		cookieValue = decodeURIComponent(
document.cookie.substring(cookieStart + cookieName.length, cookieEnd));
	}
	return cookieValue;
}




