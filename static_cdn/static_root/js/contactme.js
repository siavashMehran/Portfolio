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
                document.querySelector('.submit-btn').innerHTML=`MESSAGE SENT SUCCESSFULLY `;
                document.querySelector('.submit-btn').style="background-color:green;";
                setTimeout(function(){
                    document.forms[1].reset()
                    
                }, 3000);
                setTimeout(function(){
                    document.querySelector('.submit-btn').innerHTML="Send Another One ";
                    document.querySelector('.submit-btn').style="background-color:red;";
                }, 3000);
            },
            error : function(r){
                
                alert(r.responseJSON.result);
                
            },

        });
    });


    
})

