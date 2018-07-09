// django inlines
$('#add-question').djangoInlineFormAdd({
  prefix: "questions",
  postClick: function() {
    // wait half a second
    setTimeout(function() {
      var newElement = $('#questions-container').find('div:last-child');

      // scroll to newly added element
      $('html,body').animate({
        scrollTop: newElement.offset().top
      });
    }, 500);
  }
});

// vue for options inlines
Vue.component('options-item', {
  props: ['option'],
  delimiters: ['${', '}'],
  template: '<div class="options-item">' +
    '<input' +
      ' class="text-input block width-100"' +
      ' type="text"' +
      ' :value="option.text" />' +
    '<button' +
      ' type="button"' +
      ' class="delete"' +
      ' v-on:click="emitDeleteOption">Borrar</button>' +
  '</div>',
  methods: {
    emitDeleteOption: function(event) {
      this.$emit('delete-option', this.option);
    }
  }
});

Vue.component('question-options', {
  props: ['questionId'],
  template: '<div class="options-container">' +
    '<h4>Opciones <button type="button">Agregar</button></h4>' +
    '<options-item' +
      ' v-for="option in options"' +
      ' v-bind:key="option.id"' +
      ' v-bind:option="option"' +
      ' v-on:delete-option="deleteOption">' +
    '</options-item>' +
  '</div>',
  data: function () {
    return {
      options: [
        {id:1, questionId: this.questionId, text:'Opcion 1'},
        {id:2, questionId: this.questionId, text:'Opcion 2'},
        {id:3, questionId: this.questionId, text:'Opcion 3'}
      ]
    }
  },
  methods: {
    deleteOption: function (option) {
      var index = this.options.indexOf(option);
      this.options.splice(index, 1);
    }
  }
});

var app = new Vue({
  el: '#questions-container',
  delimiters: ['${', '}'],
  data: {}
});