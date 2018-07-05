var quill = new Quill('#editor-container', {
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
  var body = document.querySelector('input[name=body]');
  body.value = quill.root.innerHTML;
  return true;
};

form.onsubmit();