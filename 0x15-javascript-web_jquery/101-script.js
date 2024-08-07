const $ = window.$;
$(document).ready(function () {
  $('#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('#remove_item').click(function () {
    $('UL.my_list').children().last().remove();
  });
  $('#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
