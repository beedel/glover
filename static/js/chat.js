$('#chat_form').on( 'submit', function(event)){
    event.preventDefault();

    $.ajax({
    url : '/message_post/',
    type : ' POST ',
    data : { msgbox : $('#chat_msg').val() },

    success:function(json){
        console.log(json);
        $('#chat_msg').val('');
        $('#msg_list').append('<li class="text-right list-group-item">' + json.msg + '<li>')
        var charlist = document.getElementById('msg_list_div');
        chatlist.scrollTop = chatlist.scrollHeight;
    }
    });
    });
    function getMessages(){
    if (!scrolling){
        $.get('/messages/', function(messages){
            console.log(messages);
            $('#msg_list').html(messages);
            var chatlist = document.getElementById('msg_list_div');
            chatlist.scrollTop = chatlist.scrollHeight;
        });
    }
    scrolling = false;
    }

    var scrolling = false;
    $(function(){
        $('#msg_list_div').on('scroll', function(){
            scrolling = true;
        });
        refreshTimer = setInterval(getMessages, 100);
    });

    $(document).ready(function(){
    $('#send').attr('disabled', 'disabled');
    $('#chat_msg').keyup(function(){
        if($(this).val() != ''){
            $('#send').removeAttr('disabled');
        }
        else{
            $('#send').removeAttr('disabled', 'disabled')
        }
    });
    });


// Took the functions below from Django Documentation

    function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});