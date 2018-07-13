var initQuill = function(fieldName) {
  var quill = new Quill(
    '#' + fieldName + '-editor-container', {
    modules: {
      toolbar: [
        [{ header: [1, 2, 3, 4, false] }],
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
