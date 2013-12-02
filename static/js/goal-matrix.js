/**
 * @author Luis C. Berrocal
 */
function jq(){
	$( "a" ).click(function( event ) {
				alert( "The link will no longer take you to jquery.com" );
				event.preventDefault();
			});
}


function calculate_grade(){
	var employee_grade = 0;
	$('table#matrix > tbody > tr.goal').each(function (i, row) {
		var w = $('td.goal-weight', this).text();
		w = w.substring(0, w.length-1);
		var gd = $('td.goal-grade > input', this).val();
		if (gd == "None" || gd.length == 0){
			gd =0;
		}
		var eg = w * gd/100;
		employee_grade += eg;
		$('td.goal-emp-grade', this).text(eg);
	});
	$('td#employee-grade').text(employee_grade);
}
