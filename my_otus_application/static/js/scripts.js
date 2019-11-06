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
        let td = tr[i].getElementsByTagName("td")[2];
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

function auth_and_redirect() {
    let username = $('#username').val();
    let password = $('#password').val();
    console.log(username);
    console.log(password);
    let auth_object = JSON.stringify({'username': username, 'password': password})
    return $.ajax({
        type: 'POST',
        url: '/api/auth',
        contentType: 'application/json',
        dataType: 'json',
        data: auth_object,
        success:
            function (xhr) {
                window.location.href = '/static/index.html';
            }
    })
}

async function fill_lesson_page() {
    let lessons_response = await fetch('../api/lessons/');
    let lessons_json;
    if (lessons_response.ok) {
        lessons_json = await lessons_response.json();
    }
    lessons_json.forEach(json => {
        $('#myTable > tbody:last-child').append(
            '<tr>' +
            '<th scope="row">' + json.id + '</th>' +
            '<td>' + json.start_date.split('T')[0] + '</td>' +
            '<td>' + json.start_date.split('T')[1] + '</td>' +
            '<td>' + json.description + '</td>' +
            '<td>' + json.homework + '</td>' +
            ' </tr>'
        );
    });
}