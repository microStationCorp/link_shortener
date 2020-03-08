console.log('grub')

$(document).ready(function () {
    $('#short').click(function () {
        var slug = $('[name=SLUG]').val()
        var url = $('[name=URL]').val()

        $.ajax({
            url: '../shorten',
            type: 'GET',
            data: {
                'slug': slug,
                'url': url,
            },
            success: function (data) {
                console.log(data)
                myHtml = `<div class="card mt-5">
                <div class="card-body">
                    <div class="card-text">Your URL : <a href="http://127.0.0.1:8000/${data.name}" class="url">http://127.0.0.1:8000/${data.name}</a>
                    </div>
                    <div class="card-text">Your URL Stat Page : <a href="http://127.0.0.1:8000/stat/${data.name}"
                            class="url">http://127.0.0.1:8000/stat/${data.name}</a></div>
                </div>
            </div>`

                $('#res').html(myHtml)
            }, error: function (error) {
                console.log(error)
            }
        })


    })
})