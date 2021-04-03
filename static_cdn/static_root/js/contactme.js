$(document).ready(function(){

    const form = document.querySelector('#contact-form');
    let csrf_token = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

    form.addEventListener('submit', function(e){
        e.preventDefault();
        $.ajax({
            type : 'POST', 
            url  : '',
            data : {
                'csrfmiddlewaretoken' : csrf_token,
                'name'    : document.querySelector('input[name="name"]').value,
                'email'   : document.querySelector('input[name="email"]').value,
                'phone'   : document.querySelector('input[name="phone"]').value,
                'messege' : document.querySelector('textarea[name="messege"]').value,
            },
            enctype: 'json',
            success : function(r){
                alert(r.result)
            },
            error : function(r){
                alert(r.result)
            },

        });
    });
})