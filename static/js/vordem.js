$(document).ready(function () {
  var form = $('#request-quote');
    not_sure = $('#id_build_4');
    id_other = $('#id_other');
    not_sure_time = $('#id_time_4');
    id_other_time = $('#id_other_time');

    not_sure.click(function(){
      if (this.checked == true){
        id_other.removeAttr('disabled');
        id_other.focus();
        id_other.prop('required', true)
        id_other.parsley().validate()
      } else {
        id_other.prop('disabled', true );
        id_other.val('');
        id_other.prop('required', false)
        id_other.parsley().reset();
      }
    })

    $('#request-quote input[name=time]').on('change', function() {
      option = $('input[name=time]:checked').val()
      if (option == "Not sure time"){
        id_other_time.removeAttr('disabled');
        id_other_time.focus();
        id_other_time.prop('required', true)
        id_other_time.parsley().validate()
      } else {
        id_other_time.prop( "disabled", true );
        id_other_time.val('');
        id_other_time.prop('required', false)
        id_other_time.parsley().reset();
      }
   });

   $('#send_form').click(function () {
      form.parsley().validate();
      form_is_valid = form.parsley().validate();
      if (form_is_valid) {
          form.submit();
      }
    })
});
