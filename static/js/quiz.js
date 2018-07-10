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
      ' v-model="option.name" />' +
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
    '<h4>Opciones <button type="button" v-on:click="addNewOption">Agregar</button></h4>' +
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
      var self = this;

      $.ajax({
        url: '/content/options/?question_id=' + this.questionId,
        type: 'GET',
        tryCount : 0,
        retryLimit : 3,
        success : function(json) {
          // load the data
          self.loadData.call(self, json.results);

          // wrap it up
          self.addNewOptionIfEmpty.call(self);
        },
        error : function(xhr, textStatus, errorThrown ) {
          this.tryCount++;

          if (this.tryCount <= this.retryLimit) {
            // try again
            $.ajax(this);
            return;
          } else {
            // handle error
            console.error('error loading data');

            // wrap it up
            self.addNewOptionIfEmpty.call(self);
            return;
          }
        }
      });
    },
    loadData: function(data) {
      var self = this;
      data.forEach(function(element) {
        self.addOption.call(self, element);
      });
    },
    addOption: function(option) {
      this.options.push(option);
      app.allOptions.push(option);
    },
    addNewOption: function(event) {
      this.addOption({
        id: 0,
        question_id: this.questionId,
        name: ''
      });
    },
    deleteOption: function (option) {
      // delete option
      var index = this.options.indexOf(option);
      this.options.splice(index, 1);

      // delete option from general array too
      index = app.allOptions.indexOf(option);
      app.allOptions.splice(index, 1);

      // add new option if array is empty
      this.addNewOptionIfEmpty();
    },
    addNewOptionIfEmpty: function() {
      if(this.options.length <= 0)
        this.addNewOption();
    }
  }
});

var app = new Vue({
  el: '#questions-container',
  delimiters: ['${', '}'],
  data: {
    allOptions: []
  }
});
