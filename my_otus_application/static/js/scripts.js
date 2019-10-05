function myFunction() {
    let cards_section = document.getElementById("cards");
    let button_show_hide = document.getElementById("show-hide-button");
    if (cards_section.style.display === "none") {
        cards_section.removeAttribute('style');
        button_show_hide.innerHTML = "Hide courses"
    } else {
        cards_section.style.display = "none";
        button_show_hide.innerHTML = "Show courses"
    }
}

function filterTable() {
    let input = document.getElementById("inputField");
    let filter = input.value.toUpperCase();
    let table = document.getElementById("myTable");
    let tr = table.getElementsByTagName("tr");

    for (let i = 0; i < tr.length; i++) {
        let td = tr[i].getElementsByTagName("td")[0];
        if (td) {
            let txtValue = td.innerHTML;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}