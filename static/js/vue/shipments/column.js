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
