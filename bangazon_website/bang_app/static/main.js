/***************************************
Jquery used to listen for select change
event, show or hide the proper product
creation form and send the correct 
ProductType id value
****************************************/
$('#cat-list').on('change', function() {
	if (this.value == 'new') {
		$('#newCat').removeClass('hidden');
		$('#cat-list').addClass('hidden');
		$('#cats').addClass('hidden');
	}
	else {
		$('#product_type_id').val(this.value);
		console.log("id", this.value);
		$('#oldCat').removeClass('hidden');
		$('#cat-list').addClass('hidden');
		$('#cats').addClass('hidden');
	}
});