var updateShipmentApp = new Vue({
  el: '#update-shipment',
  delimiters: ['${', '}'],
  data: {
    shipment: {
      code: '',
      status_history: [],
      current_status: {
        checkpoint_display: '',
        time_status_display: ''
      },
      truck: {
        code: '',
        carrier: {
          id: 1,
          name: '',
          code: ''
        }
      },
      plant: {
        id: 1,
        name: '',
        code: ''
      },
      estimated_arrival_datetime: new Date(),
      comments: []
    },
    plants: [],
    carriers: [],
    loading: false,
    checkpoints : {
        'MEX_TRANSIT': 'MTR',
        'MEX_CARRIER': 'MCA',
        'BORDER_CROSSING': 'BCR',
        'BORDER_CARRIER': 'BCA',
        'USA_TRANSIT': 'UTR',
        'USA_DELIVERED': 'UDE',
    },
    newComment: '',
    dateTimeToEdit: null,
    editingDateTime: null,
    onEditDateTimeSuccess: null,
    dateTimeMessage: 'Por favor establece el ETA en fecha y hora'
  },
  computed: {
    formIsValid: function () {
      return this.shipment.code &&
        this.shipment.plant &&
        this.shipment.truck.code &&
        this.shipment.truck.carrier &&
        true;
    },
    startDate: function() {
      return this._formatDate(this.shipment.start_datetime);
     },
    startTime: function() {
      return this._formatTime(this.shipment.start_datetime);
    },
    timeStatusClass: function() {
      var timeStatus = this.shipment.current_status.time_status;

      if(timeStatus == 'TOT')
        return 'text-success';
      else if(timeStatus == 'TDE')
        return 'text-warning';
      else if(timeStatus == 'TLA')
        return 'text-danger';
      else
        return 'text-success';
    },
    etaDate: function() {
      return this._etaStringValue(0);
    },
    etaTime: function() {
      if(this.shipment.estimated_arrival_datetime)
        return this._formatTimeForInput(
          this.shipment.estimated_arrival_datetime
        );
      else
        return null;
    },
    editingDate: function() {
      return this._datetimeStringValue(
        this.editingDateTime, 0);
    },
    editingTime: function() {
      return this._formatTimeForInput(
        this.editingDateTime
      );
    },
    timesCPM: function() {
      return {
        'start': this._formatDeparture(this.shipment.start_datetime),
        'duration': '',
        'end': ''
      };
    },

    timesTransitMX: function() {
      var s = this._getStatusByCheckpoint(this.checkpoints.MEX_TRANSIT);
      return this._statusTimes(s);
    },

    timesCarrierMX: function() {
      var s = this._getStatusByCheckpoint(this.checkpoints.MEX_CARRIER);
      return this._statusTimes(s);
    },

    timesCrossing: function() {
      var s = this._getStatusByCheckpoint(this.checkpoints.BORDER_CROSSING);
      return this._statusTimes(s);
    },

    timesCarrierUS: function() {
      var s = this._getStatusByCheckpoint(this.checkpoints.BORDER_CARRIER);
      return this._statusTimes(s);
    },

    timesTransitUS: function() {
      var s = this._getStatusByCheckpoint(this.checkpoints.USA_TRANSIT);
      return this._statusTimes(s);
    },

    timesDelivered: function() {
      var s = this._getStatusByCheckpoint(this.checkpoints.USA_DELIVERED);
      return this._statusTimes(s);
    },

    timesETA: function() {
      var eta = this.shipment.estimated_arrival_datetime;
      return this._formatETA(eta);
    }
  },
  created: function() {
    this.loadPlants();
    this.loadCarriers();
  },
  methods: {
    _userDisplayName: function(user) {
      if(user.first_name && user.last_name)
        return user.first_name + ' ' + user.last_name;
      else if(user.first_name)
        return user.first_name;
      else if(user.last_name)
        return user.last_name;
      else
        return user.email;
    },

    _statusTimes: function(s) {
      if(s)
        return {
          'start': this._formatArrival(s.start_datetime),
          'duration': this._formatDuration(s.hours_since_start),
          'end': this._formatDeparture(s.end_datetime),
          'empty': false
        };
      else
        return this._emptyTimes();
    },

    _emptyTimes: function() {
      return {
        'start': '',
        'duration': '',
        'end': '',
        'empty': true
      };
    },

    _formatETA: function(datetime) {
      return this._formatDatetimeWithIcon(datetime, '(ETA)');
    },

    _formatArrival: function(datetime) {
      return this._formatDatetimeWithIcon(datetime, '🡻');
    },

    _formatDeparture: function(datetime) {
      return this._formatDatetimeWithIcon(datetime, '🡺');
    },

    _formatDatetimeWithIcon: function(datetime, icon) {
      if(datetime) {
        return icon + ' ' +
          this._formatDateWithoutYear(datetime) +
          ', ' +
          this._formatTime(datetime);
      } else {
        return '';
      }
    },

    _formatDuration: function(hours) {
      if(hours >= 24) {
        var days = hours / 24;
        return '🕓 ' + days.toFixed(1) + ' dia(s)';
      } else {
        return '🕓 ' + hours + ' hora(s)';
      }
    },

    _etaStringValue: function(index) {
      var eta = this.shipment.estimated_arrival_datetime;

      if(eta) {
        // convert from string to date if necessary
        if(typeof(eta) == "string") {
          this.shipment.estimated_arrival_datetime = new Date(eta);
          eta = this.shipment.estimated_arrival_datetime;
        }

        return eta.toISOString().split('T')[index];
      }
      else
        return null;
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

    _timelineItemStatusStyle: function(status) {
      var timeStatus = status.time_status;
      var color = '#ffffff';

      if(timeStatus == 'TOT')
        color = '#ffffff'; //'#ebffeb';
      else if(timeStatus == 'TDE')
        color = '#fff1d9';
      else if(timeStatus == 'TLA')
        color = '#fff2f2';

      return {
        'background-color': color
      };
    },

    _isDelivered: function(status) {
      return status.checkpoint == 'UDE';
    },

    _isCurrentStatus: function(status) {
      return status.id == this.shipment.current_status.id;
    },

    _get: function(url, success, error) {
      $.ajax({
        url: url,
        type: 'GET',
        success : success,
        error : error
      });
    },

    _do_request: function(url, method, data, success, error) {
      $.ajax({
        url: url,
        type: method,
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

    _post: function(url, data, success, error) {
      this._do_request(url, 'POST', data, success, error);
    },

    _patch: function(url, data, success, error) {
      this._do_request(url, 'PATCH', data, success, error);
    },

    _getCarrierById: function(id) {
      return this.carriers.find(x => x.id == id);
    },

    _getPlantById: function(id) {
      return this.plants.find(x => x.id == id);
    },

    _getStatusByCheckpoint: function(checkpoint) {
      var status = this.shipment.status_history.filter(status => status.checkpoint == checkpoint);
      if(status.length > 0) return status[0];
      else return null;
    },

    open: function(shipment) {
      // open modal
      $(this.$el).modal('toggle');

      // set data
      this.shipment = shipment;
      this.dateTimeToEdit = null;
      this.newComment = '';
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

    nextCheckpoint: function() {
      if(confirm('¿Estás seguro de querer realizar esta acción?')) {
        var self = this;

        this.loading = true;

        this._post(
          '/shipments/shipments/' + this.shipment.id + '/next/',
          {},
          function(json) {
            self.loading = false;
            self.success.call(self, json);
          },
          function(xhr, status, error) {
            self.loading = false;
          }
        );
      }
    },

    addComment: function() {
      if(!this.newComment)
        return;

      var self = this;
      this.loading = true;

      this._post(
        '/shipments/api/comments/',
        {
          body: this.newComment,
          shipment: this.shipment.id
        },
        function(json) {
          // add comment to array
          self.shipment.comments.unshift(json);

          // reset flags
          self.loading = false;
          self.newComment = '';

          // notification
          $.gritter.add({
            title: 'Éxito',
            text: 'Comentario agregado exitosamente',
            class_name: 'color success'
          });
        },
        function(xhr, status, error) {
          // reset flags
          self.loading = false;

          // notification
          $.gritter.add({
            title: 'Error',
            text: 'Hubo un error agregando el comentario.',
            class_name: 'color danger'
          });
        }
      );
    },

    _get_current_eta: function() {
      if(!this.shipment.estimated_arrival_datetime)
        this.shipment.estimated_arrival_datetime = new Date();

      return this.shipment.estimated_arrival_datetime;
    },

    _showEta: function() {
      var c = this.shipment.current_status.checkpoint;
      var checkpoints = ['BCA', 'UTR', 'UDE'];
      return checkpoints.join(',').indexOf(c) > -1;
    },

    _getEtaInUTCString: function() {
      var eta = this._get_current_eta();
      var tzoffset = (new Date()).getTimezoneOffset() * 60000; // offset in milliseconds
      var localISOTime = (new Date(eta - tzoffset)).toISOString().slice(0, -1);
      return localISOTime;
    },

    _saveEta: function() {
      var self = this;
      this.loading = true;

      this._patch(
        '/shipments/api/shipments/' + this.shipment.id + '/',
        {
          'estimated_arrival_datetime': this._getEtaInUTCString()
        },
        function(json) {
          // update shipment with new data
          self.shipment = json;

          // flags
          self.loading = false;

          // notification
          $.gritter.add({
            title: 'Éxito',
            text: 'Se cambió el ETA exitosamente.',
            class_name: 'color success'
          });
        },
        function(xhr, status, error) {
          // flags
          self.loading = false;

          // notification
          $.gritter.add({
            title: 'Error',
            text: 'Hubo un error actualizando el ETA.',
            class_name: 'color danger'
          });
        }
      );
    },

    _getNextCheckpoint: function() {
      var currentCheckpoint = this.shipment.current_status.checkpoint;
      var checkpoints = this.checkpoints;

      if(currentCheckpoint == checkpoints.MEX_TRANSIT)
          return checkpoints.MEX_CARRIER;

      if(currentCheckpoint == checkpoints.MEX_CARRIER)
          return checkpoints.BORDER_CROSSING;

      if(currentCheckpoint == checkpoints.BORDER_CROSSING)
          return checkpoints.BORDER_CARRIER;

      if(currentCheckpoint == checkpoints.BORDER_CARRIER)
          return checkpoints.USA_TRANSIT;

      if(currentCheckpoint == checkpoints.USA_TRANSIT)
          return checkpoints.USA_DELIVERED;

      if(currentCheckpoint == checkpoints.USA_DELIVERED)
          return null;

      return null;
    },

    _getPreviousCheckpoint: function() {
      var currentCheckpoint = this.shipment.current_status.checkpoint;
      var checkpoints = this.checkpoints;

      if(currentCheckpoint == checkpoints.MEX_TRANSIT)
          return null;

      if(currentCheckpoint == checkpoints.MEX_CARRIER)
          return checkpoints.MEX_TRANSIT;

      if(currentCheckpoint == checkpoints.BORDER_CROSSING)
          return checkpoints.MEX_CARRIER;

      if(currentCheckpoint == checkpoints.BORDER_CARRIER)
          return checkpoints.BORDER_CROSSING;

      if(currentCheckpoint == checkpoints.USA_TRANSIT)
          return checkpoints.BORDER_CARRIER;

      if(currentCheckpoint == checkpoints.USA_DELIVERED)
          return checkpoints.USA_TRANSIT;

      return null;
    },

    _getCheckpointDisplay: function(checkpoint) {
      var checkpoints = this.checkpoints;

      if(checkpoint == checkpoints.MEX_TRANSIT)
        return 'Tránsito MX';

      if(checkpoint == checkpoints.MEX_CARRIER)
        return 'Carrier MX';

      if(checkpoint == checkpoints.BORDER_CROSSING)
        return 'En cruce';

      if(checkpoint == checkpoints.BORDER_CARRIER)
        return 'Carrier US';

      if(checkpoint == checkpoints.USA_TRANSIT)
        return 'Tránsito US';

      if(checkpoint == checkpoints.USA_DELIVERED)
        return 'Entregado';

      return null;
    },

    _isExitOrStay: function(checkpoint) {
      var checkpoints = this.checkpoints;

      switch(checkpoint) {
        case checkpoints.MEX_TRANSIT:
        case checkpoints.BORDER_CROSSING:
        case checkpoints.USA_TRANSIT:
          return 'exit';
        case checkpoints.MEX_CARRIER:
        case checkpoints.BORDER_CARRIER:
        case checkpoints.USA_DELIVERED:
          return 'stay';
        default:
          return 'unknown';
      };
    },

    _getNextCheckpointOrPlant: function() {
      var nextCheckpoint = this._getNextCheckpoint();

      if(nextCheckpoint && nextCheckpoint != this.checkpoints.USA_DELIVERED)
        return this._getCheckpointDisplay(nextCheckpoint);
      else
        return this.shipment.plant.name;
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

    changeEtaDate: function(date) {
      var eta = this._get_current_eta();
      this._changeDate(eta, date);
      this._saveEta();
    },

    changeEtaTime: function(time) {
      var eta = this._get_current_eta();
      this._changeTime(eta, time);
      this._saveEta();
    },

    applyDateChange: function(date) {
      this._changeDate(this.editingDateTime, date);
    },

    applyTimeChange: function(time) {
      this._changeTime(this.editingDateTime, time);
    },

    editETA: function() {
      this.editDateTime(
        this._get_current_eta(),
        this._saveEta,
        'Por favor establece el ETA en fecha y hora');
    },

    editDateTime: function(datetime, onEditDateTimeSuccess, message) {
      // dateTimeToEdit = datetime linked by reference
      // editingDateTime = datetime cloned, used as a temp var
      // to apply changes call saveDateTime, which applies the
      // changes to whatever field you specify, using the ref
      this.dateTimeToEdit = datetime;
      this.editingDateTime = new Date(this.dateTimeToEdit.getTime());
      this.onEditDateTimeSuccess = onEditDateTimeSuccess;
      this.dateTimeMessage = message;
    },

    cancelDateTimeEdition: function() {
      this.dateTimeToEdit = null;
      this.editingDateTime = null;
      this.onEditDateTimeSuccess = null;
      this.dateTimeMessage = '';
    },

    saveDateTime: function() {
      this._changeDate(this.dateTimeToEdit, this.editingDateTime);
      this._changeTime(this.dateTimeToEdit, this.editingDateTime);

      if(this.onEditDateTimeSuccess)
        this.onEditDateTimeSuccess();

      this.dateTimeToEdit = null;
      this.editingDateTime = null;
      this.onEditDateTimeSuccess = null;
      this.dateTimeMessage = '';
    },

    success: function(json) {
      // update shipment with new data
      this.shipment = json;

      // notification
      $.gritter.add({
        title: 'Éxito',
        text: 'El embarque se ha movido al siguiente checkpoint.',
        class_name: 'color success'
      });
    },

    error: function(xhr, status, error) {
      // notification
      $.gritter.add({
        title: 'Error',
        text: 'Hubo un error al mover el embarque de checkpoint.',
        class_name: 'color danger'
      });
    }
  }
});
