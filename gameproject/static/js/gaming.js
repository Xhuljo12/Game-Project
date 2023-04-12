//---- Header ----//

function change() {
    var image = document.getElementById("DarkKnight");
    if (image.src.match("../static/images/onion.png")) {
    image.src = "../static/images/DarkKnight.png";
    }
    else { 
    image.src = "../static/images/onion.png";
    }
}

function changeText() {
    var x = document.getElementById("text").innerHTML;
    if (x == "Enjoy your gaming<br>experience!") {
        document.getElementById("text").innerHTML = "Fall and Rise in order to achive victory!";
     }
    if (x == "Fall and Rise in order to achive victory!") {
        document.getElementById("text").innerHTML = "Enjoy your gaming<br>experience!";
    }
    }



//---- Contact ----//

    var LoginForm = document.getElementById("LoginForm");
    var RegisterForm = document.getElementById("RegisterForm");
    var Indicator = document.getElementById("Indicator");
        
        function register(){
            RegisterForm.style.transform = "translateX(0px)";
            LoginForm.style.transform = "translateX(0px)";
            Indicator.style.transform = "translateX(100px)";
        }

        function login(){
            RegisterForm.style.transform = "translateX(300px)";
            LoginForm.style.transform = "translateX(300px)";
            Indicator.style.transform = "translateX(0px)";
        }

        function openForm() {
            document.getElementById("myForm").style.display = "block";
          }
