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
      plant: 1,
      start_datetime: new Date()
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
    editingDate: function() {
      return this._datetimeStringValue(
        this.shipment.start_datetime, 0);
    },
    editingTime: function() {
      return this._formatTimeForInput(
        this.shipment.start_datetime
      );
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

    _datetimeStringValue: function(datetime, index) {
      if(datetime) {
        // convert from string to date if necessary
        if(typeof(datetime) == "string")
          datetime = new Date(datetime);

        return datetime.toISOString().split('T')[index];
      }
      else
        return null;
    },

    _formatTimeForInput: function(date) {
      var time = new Date(date);
      var hr = time.getHours();
      var min = time.getMinutes();

      // add initial zero to minute
      if (hr < 10)
          hr = "0" + hr;

      // add initial zero to minute
      if (min < 10)
          min = "0" + min;

      return hr + ":" + min;
    },

    _changeDate: function(date, newDate) {
      date.setDate(newDate.getUTCDate());
      date.setMonth(newDate.getUTCMonth());
      date.setFullYear(newDate.getUTCFullYear());
    },

    _changeTime: function(date, newTime) {
      date.setHours(newTime.getUTCHours());
      date.setMinutes(newTime.getUTCMinutes());
    },

    _getDatetimeInUTCString: function(datetime) {
      var tzoffset = (new Date()).getTimezoneOffset() * 60000; // offset in milliseconds
      var localISOTime = (new Date(datetime - tzoffset)).toISOString().slice(0, -1);
      return localISOTime;
    },

    applyDateChange: function(date) {
      this._changeDate(this.shipment.start_datetime, date);
    },

    applyTimeChange: function(time) {
      this._changeTime(this.shipment.start_datetime, time);
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
