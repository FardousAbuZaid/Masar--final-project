// this function is to retrieve text from questionnare
function retrieval() {
    //Information retrieval from Meals Kind
    var breakfast_ = document.querySelector("#Breakfast").checked;
    var lunch_ = document.querySelector("#Brunch").checked;
    var brunch_ = document.querySelector("#Lunch").checked;
    var dinner_ = document.querySelector("#Dinner").checked;
    var meal_kind = "";
    if (breakfast_) meal_kind = "breakfast";
    if (lunch_) meal_kind = "lunch";
    if (brunch_) meal_kind = "brunch";
    if (dinner_) meal_kind = "dinner";
    WriteToFile(meal_kind);
    document.write("s");
    //Information retrieval from Food Type
    var food_type = document.getElementById("TypeOfFood").value;
    //Information retrieval about user's sensitivity
    var sensitiveType = If_sensitive();
    //Information retrieval about restaurant features
    var restaurantFeatures = document.getElementById("Restaurant_features").value;
    //Information retrieval- museum's description
    var museum_ = document.getElementById("Museum").value;
    //Information retrieval- walking tour description
    var walkingTour_ = document.getElementById("Walking_Tours").value;
}
/* check if user has a sensitivity and what is it*/
function If_sensitive() {
    var checkSensitivity = document.getElementById("myCheck").checked;
    var text = document.getElementById("text");
    if (checkSensitivity == true) {
        text.style.display = "block";
    } else {
        text.style.display = "none";
    }
    //Information retrieval about user's sensitivity
    const sensitivity_type = document.getElementById("sensitivity_type").value;
    return sensitivity_type;
}

//this function is to write all of the data (text) in questionnare to txt file
function download(filename, text) {
    var element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
    element.setAttribute('download', filename);

    element.style.display = 'none';
    document.body.appendChild(element);

    element.click();

    document.body.removeChild(element);

// Start file download.
// download("hello.txt","This is the content of my file :)");
    document.getElementById('form').addEventListener('submit', function () {
        var fname = document.getElementsByName('TypeOfFood')[0].value;
        var lname = document.getElementsByName('Restaurant_features')[0].value;
        var lname1 = document.getElementsByName('Walking_Tours')[0].value;

        download("a.txt",
            "First Name : "+fname+
            "\r\nLast Name : "+lname+
            "\r\nLast Name : "+lname1
        )
    });

}
