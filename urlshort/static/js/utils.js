function copyFunction() {
  /* Get the text field */
  var copyText = document.getElementById("copytxt");

  /* Select the text field */

   /* Copy the text inside the text field */
  navigator.clipboard.writeText(copyText.textContent);

  /* Alert the copied text */
  alert("Copied");
}