Vue.component('shipment-card', {
  props: ['shipment'],
  delimiters: ['${', '}'],
  template: '<div class="card card-border card-shipment">' +
    '<div class="card-body padding-5">' +
      '<div class="row no-margin shipment-title">' +
        '<div class="col-12 no-padding">' +
          '<span class="badge badge-carrier badge-ipt" style="background-color: ${shipment.plant.color};">' +
          ' ${shipment.plant.code}</span>' +
          ' <strong>#${shipment.code}</strong>' +
        '</div>' +
      '</div>' +
      '<div class="row no-margin">' +
        '<div class="col-12 no-padding" style="color: ${shipment.truck.carrier.color}">' +
          '<span class="icon mdi mdi-account"></span>' +
          ' ${shipment.truck.carrier.code}' +
        '</div>' +
      '</div>' +
      '<div class="row no-margin">' +
        '<div class="col-12 no-padding" style="color: ${shipment.truck.carrier.color}">' +
          '<span class="icon mdi mdi-truck"></span>' +
          ' ${shipment.truck.code} <br />' +
        '</div>' +
      '</div>' +
      '<div class="row no-margin">' +
        '<div class="col-10 no-padding">' +
          '<span class="icon mdi mdi-hourglass-alt"></span> 3 horas' +
        '</div>' +
        '<div class="col-2 no-padding">' +
          '<span class="badge badge-success float-right">OK</span>' +
        '</div>' +
      '</div>' +
    '</div>' +
  '</div>'
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
    this.loadShipments();
  },
  methods: {
    loadShipments: function() {
      var self = this;

      $.ajax({
        url: '/shipments/api/shipments/?current_status__checkpoint=' + this.checkpoint,
        type: 'GET',
        tryCount : 0,
        retryLimit : 3,
        success : function(json) {
          // load the data
          self.loadData.call(self, json.results);
        },
        error : function(xhr, textStatus, errorThrown ) {
          this.tryCount++;

          if (this.tryCount <= this.retryLimit)
            $.ajax(this); // try again
          else
            console.error('error loading data'); // handle error
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
