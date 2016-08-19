function submit() {
 	content = document.getElementById('content').value;
 	//alert(content);
 	if (content) {
 		document.location.href="/search/?q="+content;
 	};
}
