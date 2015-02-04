/**
 * Created by blissray on 15. 1. 17.
 */


function helloGachon(){
    console.log("Hello Gachon");
}

function callYourName(name){
    return "Hello" + name;
}

helloGachon()

var hG = helloGachon();
hG

function helloTenTimes(helloFunction) {
    for (var i = 0; i < 10; i++) {
        helloFunction();
    }
}

helloTenTimes(helloGachon);

helloTenTimes(function () {
        console.log("HiHi")
    }
);
