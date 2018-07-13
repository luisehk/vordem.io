$(function() {
  var modals = $('.modal-inside');
  var closeButtons = $('.close');

  closeButtons.on('click', function() {
    hideModal(modals);
  });
});

function showModal(selector) {
  $(selector).css('display', 'flex');
}

function hideModal(selector) {
  $(selector).css('display', 'none');
}

