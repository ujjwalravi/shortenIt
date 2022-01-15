function togglefn() {
	var x = document.getElementsByName("password");
	var t = document.getElementsByClassName("fapassword_toggler")[0];
	if (x[0].type == "password") {
		t.className = "fapassword_toggler fas fa-eye-slash";
		x[0].type = "text";
	}
	else {
		x[0].type = "password";
		t.className = "fapassword_toggler fas fa-eye";
	}
}