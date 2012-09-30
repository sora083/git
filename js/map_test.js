<body onlocad="initialize()">
<script src="http://map.google.com/maps/api/js?sensor=false"></script>
<script type="text.javascript">
	function initialize() {
		var latlng = new google.maps.LatLng(25.6642722, 139.7291455);
		var my options = {
			zoom: 8,
			center: latlng,
			mapTypeId: google.maps.MapTypeId.ROADMAP;
		}
		var map = new gogle.maps.Map(document.getElemwntById("map_canvas"), myOptions);
	}
</script>
<div id="map_canvas" style="width:100%; height:100%"></div>
</body>