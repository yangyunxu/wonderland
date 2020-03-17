 $(function() {
      $('#rating').barrating({
          theme: 'fontawesome-stars',
      });
   });
$('#rating').barrating('show', {
    theme: 'fontawesome-stars',
    onSelect: function(value, text, event) {
        if (typeof(event) !== 'undefined') {
            // rating was selected by a user
            console.log(value);
        }
    }
});