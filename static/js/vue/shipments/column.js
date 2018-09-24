Vue.component('shipments-column', {
  props: ['checkpoint'],
  delimiters: ['${', '}'],
  template: '#shipment-column',
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

      // load every 10 seconds
      setInterval(function() {
        self.loadShipments.call(self);
      }, 10000);
    },
    loadShipments: function() {
      var self = this;

      url = '/shipments/api/shipments/?current_status__checkpoint=' + this.checkpoint;

      // limit to 5 in delivered category
      // and order by arrival
      // else, order by start datetime
      if(this.checkpoint == 'UDE')
        url += '&limit=5&ordering=-arrival_datetime'
      else
        url += '&ordering=current_status__start_datetime'

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
