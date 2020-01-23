$(function(){
    $('#show_hide').hide();
});

$("#form").submit(function(event) {

    event.preventDefault();

    $("#pageloader").fadeIn();

    var $form = $(this),
    url = $form.attr('action'),
    text = $form.find('input[name="french-text"]').val();

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
            $("#pageloader").fadeOut();
        }
    });
});