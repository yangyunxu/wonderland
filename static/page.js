 $(function() {
      $('#rating').barrating({
          theme: 'fontawesome-stars',
      });
   });
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

var csrftoken = Cookies.get('csrftoken');
$("#submitComment").on("click",function () {
    var url = "category/submitComment/";
    var commentBox = $('#commentBox').val();
    var wonderName = $("#wonder").html().replace(/\s/g,"-");
    var inputName = $("")
    var data = {
        userRate: rate,
        userName: "11",
        userComment:commentBox,
        userWonder: wonderName
    };
    $.ajax({
            headers: {'X-CSRFToken': csrftoken},
            type: 'POST',
            url:"../../submitComment/",
            data:data,
            success:function () {

            }
        }
    );

})
