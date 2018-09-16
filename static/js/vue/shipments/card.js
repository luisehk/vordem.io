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
    }
  }
});
