/**
 * Created by blissray on 15. 1. 17.
 */
// This examples are from Effective JavaScript, Page 51~53 //
function sandwichMaker(magicIngredient){
    function make(filling) {
        return magicIngredient + " and " + filling;
    }
    return make;
}

var hamAnd = sandwichMaker("ham");
var cheese = hamAnd("cheese");
console.log(cheese);

var mustard = hamAnd("mustard");
console.log(mustard);

var turkeyAnd = sandwichMaker("tuerkey");
var swiss = turkeyAnd("Swiss");
console.log(swiss );

provolone = turkeyAnd("Provolone");
console.log(provolone );

console.log("\n");
console.log("Function Expression ");

function box(){
    var val = undefined;
    return {
        set: function (newVal) { val = newVal;},
        get: function() { return val;},
        type: function() { return typeof val; }
    };
}

var b = box();
console.log (b.type());
console.log (b.set(98.6));
console.log (b.get());
console.log (b.type());