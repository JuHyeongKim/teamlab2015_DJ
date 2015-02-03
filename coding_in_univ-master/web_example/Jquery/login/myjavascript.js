function helloSubmit() {


    var password = document.getElementById("password").value;
    var id = document.getElementById("ID").value;

    if (id != "teamlab"){
        document.getElementById("password_waring_caption").innerHTML ="Check Your ID";
        return false;
    }


    if (password != "1234"){
        document.getElementById("password_waring_caption").innerHTML ="Check Your password";
    }else{
        document.getElementById("password_waring_caption").innerHTML ="";
        document.forms["login_form"].submit();

    }
    return false;
}