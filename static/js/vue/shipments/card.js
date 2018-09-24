Vue.component('shipment-card', {
  props: ['shipment'],
  delimiters: ['${', '}'],
  template: '#shipment-card',

  computed: {
    plantStyle: function() {
      return 'background-color: ' + this.shipment.plant.color;
    },
    carrierStyle: function() {
      return 'color: ' + this.shipment.truck.carrier.color;
    },
    timeStatusClass: function() {
      status = this.shipment.current_status.time_status;

      if(status == 'TOT')
        return 'badge-success';
      else if(status == 'TDE')
        return 'badge-warning';
      else if(status == 'TLA')
        return 'badge-danger';
      else
        return 'badge-success'
    },
    timeStatusLabel: function() {
      status = this.shipment.current_status.time_status;

      if(status == 'TOT')
        return 'OK';
      else if(status == 'TDE')
        return 'DL';
      else if(status == 'TLA')
        return 'LT';
      else
        return 'OK'
    },
    timeSinceStatusStart: function() {
      var hours = this.shipment.current_status.hours_since_start;

      if(hours >= 24) {
        var days = hours / 24;
        return days.toFixed(1) + ' dia(s)';
      } else {
        return hours + ' hora(s)';
      }
    }
  },

  methods: {
    showUpdateModal: function() {
      window.updateShipmentApp.open(
        JSON.parse(JSON.stringify(this.shipment))
      );
    },

    _formatDatetime: function(datetime) {
      if(datetime) {
        return this._formatDateWithoutYear(datetime) +
          ', ' +
          this._formatTime(datetime);
      } else {
        return '';
      }
    },

    _formatDate: function(date) {
      var date = new Date(date);
      var monthNames = [
        "Ene", "Feb", "Mar",
        "Abr", "May", "Jun", "Jul",
        "Ago", "Sep", "Oct",
        "Nov", "Dic"
      ];

      var day = date.getDate();
      var monthIndex = date.getMonth();
      var year = date.getFullYear();

      return day + ' de ' + monthNames[monthIndex] + ', ' + year;
    },

    _formatDateWithoutYear: function(date) {
      var date = this._formatDate(date);
      return date.substring(0, date.length - 6);
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
  }
});
