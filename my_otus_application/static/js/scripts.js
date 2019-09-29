function myFunction() {
  var x = document.getElementById("cards");
  if (x.style.display === "none") {
   x.removeAttribute('style');
  } else {
    x.style.display = "none";
  }
}