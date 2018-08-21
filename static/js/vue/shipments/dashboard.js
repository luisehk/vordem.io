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
          '<span class="icon mdi mdi-hourglass-alt"></span> ${shipment.current_status.hours_since_start} hora(s)' +
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

Vue.component('shipments-column', {
  props: ['checkpoint'],
  delimiters: ['${', '}'],
  template: '<div class="card-holder">' +
    '<shipment-card' +
      ' v-for="(shipment, index) in shipments"' +
      ' v-bind:key="index"' +
      ' v-bind:shipment="shipment">' +
    '</shipment-card>' +
  '</div>',
  data: function () {
    return {
      shipments: []
    }
  },
  created: function () {
    this.loadShipmentsInLoop();
  },
  methods: {
    loadShipmentsInLoop: function() {
      var self = this;

      // load it the first time
      this.loadShipments();

      // load every 5 seconds
      setInterval(function() {
        self.loadShipments.call(self);
      }, 2000);
    },
    loadShipments: function() {
      var self = this;

      // limit to 5 in delivered category
      url = '/shipments/api/shipments/?current_status__checkpoint=' + this.checkpoint;
      if(this.checkpoint == 'UDE')
        url += '&limit=5'

      $.ajax({
        url: url,
        type: 'GET',
        success : function(json) {
          self.loadData.call(self, json.results);
        },
        error : function(xhr, textStatus, errorThrown ) {
          console.error('error loading data');
        }
      });
    },
    loadData: function(data) {
      this.shipments = data;
    }
  }
});

var app = new Vue({
  el: '#shipments-dashboard',
  delimiters: ['${', '}']
});
