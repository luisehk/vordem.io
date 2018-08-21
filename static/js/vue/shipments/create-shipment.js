var newShipmentApp = new Vue({
  el: '#new-shipment',
  delimiters: ['${', '}'],
  data: {
    shipment: {
      code: '',
      truck: {
        code: '',
        carrier: 1
      },
      plant: 1
    },
    plants: [
      {value: 1, text: 'Aurora, CO'},
      {value: 2, text: 'Duncan, SC'},
      {value: 3, text: 'Iowa Park, TX'},
      {value: 4, text: 'Saint Joe, MO'},
      {value: 5, text: 'Sturtevant, WI'},
    ],
    carriers: [
      {value: 1, text: 'KLLM'},
      {value: 2, text: 'CRE'},
    ],
    loading: false
  },
  computed: {
    formIsValid: function () {
      return this.shipment.code &&
        this.shipment.plant &&
        this.shipment.truck.code &&
        this.shipment.truck.carrier &&
        true;
    }
  },
  methods: {
    submit: function() {
      var self = this;

      this.loading = true;

      $.ajax({
        url: '/shipments/api/shipments/',
        type: 'POST',
        data: JSON.stringify(this.shipment),
        dataType: 'json',
        contentType: 'application/json',
        headers: {
          'X-CSRFToken': getCookie('csrftoken')
        },
        success : function(json) {
          self.loading = false;
          self.success.call(self, json);
        },
        error : function(xhr, status, error) {
          self.loading = false;
          self.success.call(self, xhr, status, error);
        }
      });
    },

    success: function(json) {
      // reset values
      this.shipment.code = '';
      this.shipment.truck.code = '';

      // close modal
      $(this.$el).modal('toggle')

      // notification
      $.gritter.add({
        title: 'Éxito',
        text: 'El embarque #' + json.code + ' ha sido creado exitosamente.',
        class_name: 'color success'
      });
    },

    error: function(xhr, status, error) {
      // notification
      $.gritter.add({
        title: 'Éxito',
        text: 'Hubo un error al crear el embarque.',
        class_name: 'color danger'
      });
    }
  }
});
