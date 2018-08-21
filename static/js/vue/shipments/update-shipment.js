var updateShipmentApp = new Vue({
  el: '#update-shipment',
  delimiters: ['${', '}'],
  data: {
    shipment: {
      code: '',
      truck: {
        code: '',
        carrier: {
          id: 1,
          name: '',
          code: ''
        }
      },
      plant: {
        id: 1,
        name: '',
        code: ''
      }
    },
    plants: [],
    carriers: [],
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
  created: function() {
    this.loadPlants();
    this.loadCarriers();
  },
  methods: {
    _get: function(url, success, error) {
      $.ajax({
        url: url,
        type: 'GET',
        success : success,
        error : error
      });
    },

    _post: function(url, data, success, error) {
      $.ajax({
        url: url,
        type: 'POST',
        dataType: 'json',
        contentType: 'application/json',
        headers: {
          'X-CSRFToken': getCookie('csrftoken')
        },
        data: JSON.stringify(data),
        success : success,
        error : error
      });
    },

    _getCarrierById: function(id) {
      return this.carriers.find(x => x.id == id);
    },

    _getPlantById: function(id) {
      return this.plants.find(x => x.id == id);
    },

    open: function(shipment) {
      // open modal
      $(this.$el).modal('toggle');

      // set data
      this.shipment = shipment;
    },

    loadPlants: function() {
      var self = this;

      this._get(
        '/company/api/plants/',
        function(json) {
          self.plants = json.results;
        },
        function(xhr, textStatus, errorThrown ) {
          console.error('error loading data');
        }
      );
    },

    loadCarriers: function() {
      var self = this;

      this._get(
        '/providers/api/carriers/',
        function(json) {
          self.carriers = json.results;
        },
        function(xhr, textStatus, errorThrown ) {
          console.error('error loading data');
        }
      );
    },

    submit: function() {
      var self = this;

      this.loading = true;

      this._post(
        '/shipments/api/shipments/',
        this.shipment,
        function(json) {
          self.loading = false;
          self.success.call(self, json);
        },
        function(xhr, status, error) {
          self.loading = false;
          self.success.call(self, xhr, status, error);
        }
      );
    },

    success: function(json) {
      // reset values
      this.shipment.code = '';
      this.shipment.truck.code = '';

      // close modal
      $(this.$el).modal('toggle');

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
