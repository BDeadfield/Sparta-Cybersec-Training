$(function() {
  $('#calcForm').submit(function(e) {

    var action = "/calculate2"

    $.ajax({
      type: 'POST',
      url : action,
      processData: false,
      dataType: 'json',
      async: false,
      headers: {},
      data: $('#calcForm').serialize(),

      success: function(response){
        result = response.data
        $('#resultInput').html('')
        $('#resultInput').append(result)
      },
      error: function(error){
        alert(error)
      },
      complete: function(){

      }
    });

    e.preventDefault();
  });
});
