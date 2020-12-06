function search(kind, term){
	console.log(kind);
	console.log(term);
	loadDoc("cgi-bin/")
}
function loadDoc(url, cFunction){
	var xhttp;
	xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange() = function (){
		if (this.readyState == 4 && this.status == 200){
			console.log("Ojo: "+ this.responseText);
			cFunction(this);
		}
	}
	xhttp.open("GET", url, true)
	xhttp.send();
}
