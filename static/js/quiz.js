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
      ' placeholder="Ingresa una opción"' +
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
    '<h4>Opciones <button type="button" v-on:click="addOption">Agregar</button></h4>' +
    '<options-item' +
      ' v-for="(option, index) in options"' +
      ' v-bind:key="index"' +
      ' v-bind:option="option"' +
      ' v-on:delete-option="deleteOption">' +
    '</options-item>' +
  '</div>',
  data: function () {
    return {
      options: []
    }
  },
  created: function () {
    this.loadOptions();
  },
  methods: {
    loadOptions: function() {
      this.addNewOptionIfEmpty();
    },
    addOption: function(event) {
      this.options.push({
        id: 0,
        questionId: this.questionId,
        text: ''
      });
    },
    deleteOption: function (option) {
      // delete option
      var index = this.options.indexOf(option);
      this.options.splice(index, 1);

      // add new option if array is empty
      this.addNewOptionIfEmpty();
    },
    addNewOptionIfEmpty: function() {
      if(this.options.length <= 0)
        this.addOption();
    }
  }
});

var app = new Vue({
  el: '#questions-container',
  delimiters: ['${', '}'],
  data: {}
});
