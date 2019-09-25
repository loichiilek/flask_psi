$(function () {
  $.ajax({
    type: "GET",
    url: "/api_call",
    headers: {
      "Content-Type": "application/json"
    },
    success: function(result) {
      console.log("north: " + result['psi_twenty_four_hourly']['north']);
      console.log("south: " + result['psi_twenty_four_hourly']['south']);
      console.log("east: " + result['psi_twenty_four_hourly']['east']);
      console.log("west: " + result['psi_twenty_four_hourly']['west']);
      console.log("central: " + result['psi_twenty_four_hourly']['central']);

      $('#map-north-button').attr('data-content', "PSI: " + result['psi_twenty_four_hourly']['north'])
      $('#map-south-button').attr('data-content', "PSI: " +  result['psi_twenty_four_hourly']['south'])
      $('#map-east-button').attr('data-content', "PSI: " +  result['psi_twenty_four_hourly']['east'])
      $('#map-west-button').attr('data-content', "PSI: " +  result['psi_twenty_four_hourly']['west'])
      $('#map-central-button').attr('data-content', "PSI: " +  result['psi_twenty_four_hourly']['central'])
    },
    error: function(result) {
      console.log("error: " + result);
      $('#map-north-button').attr('data-content', "Error")
      $('#map-south-button').attr('data-content', "Error")
      $('#map-east-button').attr('data-content', "Error")
      $('#map-west-button').attr('data-content', "Error")
      $('#map-central-button').attr('data-content', "Error")
    }
  });
  $('[data-toggle="popover"]').popover()

  $('.map-annotation').click(function() {

    


  })
})