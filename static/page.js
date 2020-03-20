
var rate = 0;
$('#rating').barrating('show', {
    theme: 'fontawesome-stars',
    onSelect: function(value, text, event) {
        if (typeof(event) !== 'undefined') {
            // rating was selected by a user
            rate = value;
            alert("You selected "+rate+" now leave your comment below!");
        }
    }
});
var existRate = $("#rate-box").attr("data-rate");
if( existRate == "anonymouse"){
    $('select').barrating('readonly', true );
}else if(existRate !="no"){
    $("#rating").barrating('set',existRate);
}

var csrftoken = Cookies.get('csrftoken');
$("#submitComment").on("click",function () {
    var url = "category/submitComment/";
    var commentBox = $('#commentBox').val();
    var wonderName = $("#wonder").html();
    var inputName = $("#user").html();
    var data = {
        userRate: rate,
        userName: inputName,
        userComment:commentBox,
        userWonder: wonderName
    };
    $.ajax({
            headers: {'X-CSRFToken': csrftoken},
            type: 'POST',
            url:"../../submitComment/",
            data:data,
            success:function () {
                alert("You have successfully submitted your comment!");
                location.reload();
            }
        }
    );

})
