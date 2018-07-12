var initQuill = function(fieldName) {
  var quill = new Quill(
    '#' + fieldName + '-editor-container', {
    modules: {
      toolbar: [
        ['bold', 'italic', 'strike', 'underline'],
        ['link', 'blockquote', 'image'],
        [{ list: 'ordered' }, { list: 'bullet' }]
      ]
    },
    theme: 'snow'
  });

  var form = document.querySelector('form');

  form.onsubmit = function() {
    // Populate hidden form on submit
    var field = document.querySelector(
      'input[name=' + fieldName + ']');
    field.value = quill.root.innerHTML;
    return true;
  };

  form.onsubmit();
}
