var app = new Vue({
  el: '#shipments-dashboard',
  delimiters: ['${', '}'],
  data: {
    plants: []
  },
  created: function() {
    this.loadPlantsMetricsInLoop();
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


    loadPlantsMetricsInLoop: function() {
      var self = this;

      // load it the first time
      this.loadPlantsMetrics();

      // load every 5 seconds
      setInterval(function() {
        self.loadPlantsMetrics.call(self);
      }, 5000);
    },

    loadPlantsMetrics: function() {
      var self = this;

      this._get(
        '/shipments/shipments/metrics-per-plant/',
        function(json) {
          self.plants = json;
        },
        function(xhr, textStatus, errorThrown ) {
          console.error('error loading data');
        }
      );
    },

    getPlantStyle: function(plant) {
      return {
        'border-top-color': plant.color
      };
    }
  }
});
