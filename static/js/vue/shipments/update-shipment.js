var updateShipmentApp = new Vue({
  el: '#update-shipment',
  delimiters: ['${', '}'],
  data: {
    shipment: {
      code: '',
      current_status: {
        checkpoint_display: '',
        time_status_display: ''
      },
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
    },
    startDate: function() {
      return this._formatDate(this.shipment.start_datetime);
     },
    startTime: function() {
      return this._formatTime(this.shipment.start_datetime);
    },
    timeStatusClass: function() {
      var timeStatus = this.shipment.current_status.time_status;

      if(timeStatus == 'TOT')
        return 'text-success';
      else if(timeStatus == 'TDE')
        return 'text-warning';
      else if(timeStatus == 'TLA')
        return 'text-danger';
      else
        return 'text-success';
    }
  },
  created: function() {
    this.loadPlants();
    this.loadCarriers();
  },
  methods: {
    _formatDate: function(date) {
      var date = new Date(date);
      var monthNames = [
        "Enero", "Febrero", "Marzo",
        "Abril", "Mayo", "Junio", "Julio",
        "Agosto", "Septiembre", "Octubre",
        "Noviembre", "Diciembre"
      ];

      var day = date.getDate();
      var monthIndex = date.getMonth();
      var year = date.getFullYear();

      return day + ' de ' + monthNames[monthIndex] + ', ' + year;
    },

    _formatTime: function(date) {
      var time = new Date(date);
      var hr = time.getHours();
      var min = time.getMinutes();

      // add initial zero to minute
      if (min < 10)
          min = "0" + min;

      // set AM or PM
      var ampm = "am";
      if( hr > 12 ) {
          hr -= 12;
          ampm = "pm";
      }

      return hr + ":" + min + ampm;
    },

    _timelineItemStatusStyle: function(status) {
      var timeStatus = status.time_status;
      var color = '#ffffff';

      if(timeStatus == 'TOT')
        color = '#ffffff'; //'#ebffeb';
      else if(timeStatus == 'TDE')
        color = '#fff1d9';
      else if(timeStatus == 'TLA')
        color = '#fff2f2';

      return {
        'background-color': color
      };
    },

    _isDelivered: function(status) {
      return status.checkpoint == 'UDE';
    },

    _isCurrentStatus: function(status) {
      return status.id == this.shipment.current_status.id;
    },

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

    nextCheckpoint: function() {
      if(confirm('¿Estás seguro de querer realizar esta acción?')) {
        var self = this;

        this.loading = true;

        this._post(
          '/shipments/shipments/' + this.shipment.id + '/next/',
          {},
          function(json) {
            self.loading = false;
            self.success.call(self, json);
          },
          function(xhr, status, error) {
            self.loading = false;
            self.success.call(self, xhr, status, error);
          }
        );
      }
    },

    success: function(json) {
      // close modal
      $(this.$el).modal('toggle');

      // notification
      $.gritter.add({
        title: 'Éxito',
        text: 'El embarque se ha movido al siguiente checkpoint.',
        class_name: 'color success'
      });
    },

    error: function(xhr, status, error) {
      // notification
      $.gritter.add({
        title: 'Error',
        text: 'Hubo un error al mover el embarque de checkpoint.',
        class_name: 'color danger'
      });
    }
  }
});
