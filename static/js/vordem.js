$(document).ready(function () {
  var form = $('#request-quote');
    not_sure = $('#id_build_4');
    id_other = $('#id_other');
    not_sure_time = $('#id_time_4');
    id_other_time = $('#id_other_time');

   $('#send_form').click(function () {
      form.parsley().validate();
      form_is_valid = form.parsley().validate();
      if (form_is_valid) {
          form.submit();
      }
    })
});
