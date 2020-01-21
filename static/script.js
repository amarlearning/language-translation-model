$(function(){
    $('#show_hide').hide();
});

$("#form").submit(function(event) {

    event.preventDefault();

    var $form = $(this),
    text = $form.find('input[name="french-text"]').val(),
    url = $form.attr('action');

    var posting = $.post(url, {
        frenchtext: text
    });

    posting.done(function(data) {
       
        var $output = data

        if ($output.length == 0) {
            $('#show_hide').hide();
        } else {
            $('#show_hide').show();
            $('.card-b').text($output)
        }
    });
});