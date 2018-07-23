$(function() {
  $('.skill-card').on('click', function(e) {
    var switcher = $(e.currentTarget);
    var expand = switcher.find('img');
    var card = switcher.parent();
    var list = card.find('ul');

    list.toggle();
    expand.toggle();
    return false;
  });
});
