(function() {

function init(){
	var date = window.location.toString().split('/').pop();
	$('.archive_table > tbody  > tr').each(function(){
		var row={};
		$('td',this).each(function(index){
			switch(index){
				case 0:
					row.time = $(this).text();
				break;
				case 1: 
					row.descr = $("img:first",this).attr("alt");
				break;
				case 2: 
					row.temperature = $(this).text();
				break;
				case 3: 
					row.wind = $(this).text();
					row.wind_direction = $("img:first",this).attr("alt");
				break;
				case 4: 
					row.atm_presh = $(this).text();
				break;
				case 5: 
					row.humidity = $(this).text();
				break;
			}
		});		

		if (Object.keys(row).length) {
			row.date=date;
			$.ajax({
			    type: "POST",
			    url: "http://localhost:8080/store.json",
			    data: JSON.stringify(row),
			    contentType: "application/json; charset=utf-8",
			    dataType: "text",
			    success: function(data){},
			    failure: function(errMsg){}
			});
		}
	});
	
	var url = window.location.toString().split('/');
	var nowD = new Date();
	var doc_date = new Date(Date.parse(date));
	var iii = 0;
	while( nowD > doc_date && iii<9000000) {
  			doc_date.setDate(doc_date.getDate() + 1);
			var m = doc_date.getMonth();
			while ( ![0, 1, 2, 3, 4, 9, 10, 11].includes(m) ) {
				doc_date.setDate(1);
				m = doc_date.getMonth()+1;
				doc_date.setMonth(m);
				continue;
			}
			iii++;
			var strd = doc_date.getFullYear() + '-' + ('0' + (doc_date.getMonth() + 1)).slice(-2) + '-' + ('0' + doc_date.getDate()).slice(-2);
			url.pop();
			url.push(strd);
			let ourl = url.join('/');
			console.log("next url: " +ourl);
			window.location.href = ourl;
			break;
	}
	console.log("Ok");

}
init();
})();

