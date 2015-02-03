var exampleArray = ['Gachon', 'University', 'Hello', 'World'];

console.log("Test Array");
for (var i = 0; i < exampleArray.length; i++) {
    console.log(exampleArray[i]);
}

var professor = {
    name: 'Sungchul',
    age: '34',
    children: '2',
    subject: 'Technology Management, Programming',
    hello: function () {
        console.log("My Name is ", this.name);
    }
};
console.log("Test Object");
console.log(professor.subject);
console.log(professor['name']);

professor.hello();

for (var key in professor) {
    console.log(professor[key]);
}

professor.hobby = "Sleeping";
console.log(professor.hobby);

