function deleteCalendarEntry(entry){
    var $entry = $(entry)
    $entry.parent().remove()
    var id =$entry.data('id')

    $.ajax({
        url: 'entry/delete' + id,
        method:  'DELETE',
        beforeSend: function(xhr){
            xhr.setRequestHeader('X-CSRFToken', csrf_token)
        }
        })
}