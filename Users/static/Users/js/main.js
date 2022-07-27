$(document).on("submit", "#formBtn", function(e) {
    e.preventDefault();
    sign_up();
});
$(document).on("submit", "#loginformBtn", function(e) {
    e.preventDefault();
    sign_in();
});
function sign_up(){
    first_name = document.getElementById("id_first_name").value;
    last_name = document.getElementById("id_last_name").value
    email_id = document.getElementById("id_email").value;
    username = document.getElementById('id_username').value
    password = document.getElementById("id_password").value;
    confirm_password= document.getElementById("id_confirm_password").value;
    $.ajax({
        url: '/register/',
        type: "POST",
        async: false,
        data: {
            first_name:first_name,
            last_name:last_name,
            email_id:email_id,
            username:username,
            password:password,
            confirm_password:confirm_password,
            csrfmiddlewaretoken:$('input[name="csrfmiddlewaretoken"]').val()
        },
        success: function(response){
            console.log(response)
            var message = $(response).find('#message')
            console.log(message)
            var message_class= $(message).attr('class')
            var message_text=message.text()
            console.log(message_class)
            console.log(message_text)
            if (message_class == "success"){
                $('#p1').text(message_text)
                $('.container').css("height","585px")
                $('#p1').css("background-color", "green");
                window.location='/login/'
            }
            else{
                $('#p1').text(message_text)
                $('.container').css("height","585px")
                $('#p1').css("background-color", "red");
            }
        }
        });
}


function sign_in(){
    username=document.getElementById('id_username').value
    password=document.getElementById('id_password').value
    $.ajax({
        url: '/login/',
        type: "POST",
        async: false,
        data: {
            username:username,
            password:password,
            csrfmiddlewaretoken:$('input[name="csrfmiddlewaretoken"]').val()
        },
        success: function(response){
            console.log(response)
            var message = $(response).find('#message')
            console.log(message)
            var message_class= $(message).attr('class')
            var message_text=message.text()
            console.log(message_class)
            console.log(message_text)
            if (message_class == "success"){
                $('#p1').text(message_text)
                $('.container').css("height","315px")
                $('#p1').css("background-color", "green");
                window.location='/home/'
            }
            else{
                $('#p1').text(message_text)
                $('.container').css("height","315px")
                $('#p1').css("background-color", "red");
            }
        }
        });

}



