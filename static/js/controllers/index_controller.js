$(document).ready(function(){

        toastr.options = {
        "closeButton": true,
        "debug": false,
        "newestOnTop": false,
        "progressBar": false,
        "positionClass": "toast-top-right",
        "preventDuplicates": false,
        "onclick": null,
        "showDuration": "300",
        "hideDuration": "400",
        "timeOut": "5000",
        "extendedTimeOut": "1000",
        "showEasing": "swing",
        "hideEasing": "linear",
        "showMethod": "fadeIn",
        "hideMethod": "fadeOut"
    }


    $("p").click(function(){
        $(this).hide();
    });

    $("#btn_login").click(function(){
        usernameTxt = $('#username').val();
        passwordTxt = $('#password').val();
        if(usernameTxt == ""){
            toastr["error"]("Please enter your username!");
        }
        if(passwordTxt == ""){
            toastr["error"]("Please enter your password!");
        }
        if(usernameTxt != "" && passwordTxt !=""){
            data =  JSON.stringify({username : usernameTxt, password : passwordTxt })
            $.ajax({
                type: "POST",
                url: "/api-token-auth/",
                data: data,
                contentType: "application/json; charset=utf-8",
                dataType: "json",
                success: function (msg) {
                    toastr["success"]("You logged in successfully!");
                   //do something
                   //$(location).attr('href', '/dashboard')
                   //$(location).attr('href', '/dashboard')
                },
                error: function (errormessage) {
                    toastr["error"]("Provided credentials are wrong!");

                }
            });
        }
    });

    $("#btn_register").click(function(){
        registerUsernameTxt = $('#register_username').val();
        registerEmailTxt = $('#register_email').val();
        registerPasswordTxt = $('#register_password').val();
        registerRepeatPasswordTxt = $('#register_repeat_password').val();
        if(registerUsernameTxt == ""){
            toastr["error"]("Please enter your username that you want to register!");
        }
        if(registerEmailTxt == ""){
            toastr["error"]("Please enter your email that you want to register!");
        }
        if(registerPasswordTxt == ""){
            toastr["error"]("Please enter your password!");
        }
        if(registerRepeatPasswordTxt == ""){
            toastr["error"]("Please repeat your chosen password!");
        }
        if(registerPasswordTxt != registerRepeatPasswordTxt && registerPasswordTxt != ""  && registerRepeatPasswordTxt != ""){
            toastr["error"]("Your passwords do not match!");
        }
        if(usernameTxt != "" && passwordTxt !=""){
            data =  JSON.stringify({username : usernameTxt, password : passwordTxt })
            $.ajax({
                type: "POST",
                url: "/api-token-auth/",
                data: data,
                contentType: "application/json; charset=utf-8",
                dataType: "json",
                success: function (msg) {
                    toastr["success"]("You logged in successfully!");
                   //do something
                   //$(location).attr('href', '/dashboard')
                },
                error: function (errormessage) {
                    toastr["error"]("Provided credentials are wrong!");

                }
            });
        }
    });


});