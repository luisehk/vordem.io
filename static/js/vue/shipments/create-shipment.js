var newShipmentApp = new Vue({
  el: '#new-shipment',
  delimiters: ['${', '}'],
  data: {
    shipment: {
      code: '',
      truck: {
        code: '',
        carrier: 1
      },
      plant: 1
    },
    plants: [
      {value: 1, text: 'Aurora, CO'},
      {value: 2, text: 'Duncan, SC'},
      {value: 3, text: 'Iowa Park, TX'},
      {value: 4, text: 'Saint Joe, MO'},
      {value: 5, text: 'Sturtevant, WI'},
    ],
    carriers: [
      {value: 1, text: 'KLLM'},
      {value: 2, text: 'CRE'},
    ],
    loading: false
  }
});
