Vue.component('shipment-card', {
  props: ['shipment'],
  delimiters: ['${', '}'],
  template: '<div class="card card-border card-shipment" v-on:click="showUpdateModal">' +
    '<div class="card-body padding-5">' +
      '<div class="row no-margin shipment-title">' +
        '<div class="col-12 no-padding">' +
          '<span class="badge badge-carrier badge-ipt" :style="plantStyle">' +
          ' ${shipment.plant.code}</span>' +
          ' <strong>#${shipment.code}</strong>' +
        '</div>' +
      '</div>' +
      '<div class="row no-margin">' +
        '<div class="col-12 no-padding" :style="carrierStyle">' +
          '<span class="icon mdi mdi-account"></span>' +
          ' ${shipment.truck.carrier.code}' +
        '</div>' +
      '</div>' +
      '<div class="row no-margin">' +
        '<div class="col-12 no-padding" :style="carrierStyle">' +
          '<span class="icon mdi mdi-truck"></span>' +
          ' ${shipment.truck.code} <br />' +
        '</div>' +
      '</div>' +
      '<div class="row no-margin">' +
        '<div class="col-10 no-padding">' +
          '<span class="icon mdi mdi-hourglass-alt"></span> ${timeSinceStatusStart}' +
        '</div>' +
        '<div class="col-2 no-padding">' +
          '<span class="badge float-right" v-bind:class="timeStatusClass">${timeStatusLabel}</span>' +
        '</div>' +
      '</div>' +
    '</div>' +
  '</div>',

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