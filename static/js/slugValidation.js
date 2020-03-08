$(document).ready(function () {
    console.log('on key press')
    $('#slug').focusout(function () {
        var given_slug = $('#slug').val()
        var url = $('[name=URL]').val()

        $.ajax({
            url: '../slugValidation',
            type: 'GET',
            data: {
                'slug': given_slug
            }, success: function (data) {
                console.log(data.valid_slug)
                if (data.valid_slug == true) {
                    $('#button-addon2').prop('disabled', false)
                    $('#error_msg').prop('hidden', true)
                } else {
                    $('#error_msg').prop('hidden', false)
                    $('#button-addon2').prop('disabled', true)
                }
            }, error: function (error) {
                console.log(error)
            }
        })
    })
})