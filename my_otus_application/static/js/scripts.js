function myFunction() {
    var cards_section = document.getElementById("cards");
    var button_show_hide = document.getElementById("show-hide-button")
    if (cards_section.style.display === "none") {
        cards_section.removeAttribute('style');
        button_show_hide.innerHTML = "Hide courses"
    } else {
        cards_section.style.display = "none";
        button_show_hide.innerHTML = "Show courses"
    }
}