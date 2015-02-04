/**
 * Created by blissray on 15. 1. 17.
 */


var value = 1;
console.log(++value);
console.log(value++);
console.log(value);

if (1 == "1"){
    console.log("Same Value");
}

if (1 === "1"){
    console.log("Same Value and Type");
} else {
    console.log("NOT Same Value and Type");
}

var value = 3;
switch (value) {
    case 1:
        console.log("Value is 1" );
        break;
    case 2:
        console.log("Value is 2" );

        break;
    case 3:
        console.log("Value is 3" );

        break;
    default :
        console.log("NOT Defined")
}


for (var count = 1; count < 5; count++){
    console.log("Hello Loop")
}