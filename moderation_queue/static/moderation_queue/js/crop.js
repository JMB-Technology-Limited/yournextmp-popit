jQuery(function($) {

  function setVisibilityFromDecision() {
    var value = $('#id_decision').val();
    if (value == 'rejected') {
      $('.rejection_reason').show();
      $('.justification_for_use').hide();
    } else if (value == 'approved') {
      $('.rejection_reason').hide();
      $('.justification_for_use').show();
    } else if (value == 'undecided') {
      $('.rejection_reason').hide();
      $('.justification_for_use').show();
    }
  }

  $('.crop-coordinates').hide();
  setVisibilityFromDecision();

  $('#id_decision').change(function() {
    setVisibilityFromDecision()
  });

  function adjustFormValues(c) {
    $('input#id_x_min').val(c.x);
    $('input#id_x_max').val(c.x2);
    $('input#id_y_min').val(c.y);
    $('input#id_y_max').val(c.y2);
  }

  $('#image-for-review').Jcrop({
    onSelect: adjustFormValues,
    onChange: adjustFormValues,
    boxWidth: 600,
    boxHeight: 600
  });

});
