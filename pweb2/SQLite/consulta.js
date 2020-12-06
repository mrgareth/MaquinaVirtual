function search(kind, term){
	console.log(kind);
	console.log(term);
	var url = 'cgi-bin/consulta.py?kind='+kind+'?term'+term;
	console.log(url);
	loadDoc(url,render);
	}
}

function render(data){
	//Aqui leemos los datos y los devolveremos hacia el html
}

function loadDoc(url, cFunction){
	var xhttp;
	xhttp = new XMLHttpRequest(); 
	xhttp.onreadystatechange == function(){
		if (this.readystate == 4 && this.status == 200){
			console.log('OJO: ' + this.responseText);
			json = JSON.parse(this.responseText);
			cFunction(json);
	}
	xhttp.open('GET', url, true);
	xhttp.send();
}
