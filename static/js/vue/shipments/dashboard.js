Vue.component('shipment-card', {
  props: ['shipment'],
  delimiters: ['${', '}'],
  template: '<div class="card card-border card-shipment" v-on:click="showModal" data-toggle="modal" data-target="#form-bp1">' +
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
          '<span class="badge badge-success float-right">OK</span>' +
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
  },

  methods: {
    showModal: function() {

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
      }, 5000);
    },
    loadShipments: function() {
      var self = this;

      $.ajax({
        url: '/shipments/api/shipments/?current_status__checkpoint=' + this.checkpoint,
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
