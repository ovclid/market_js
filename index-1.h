<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>원, 선, 사각형, 다각형 표시하기</title>
    
</head>
<body>
<div id="map" style="width:100%;height:800px;"></div>    

<script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=56dd36038680e4d6f7b1cbc67b011a06"></script>
<script type="text/javascript" src="market_info.js"></script>
<script>
var mapContainer = document.getElementById('map'), // 지도를 표시할 div 
    mapOption = { 
        center: new kakao.maps.LatLng(36.8603322228225, 127.45164528725064), // 지도의 중심좌표
        level: 3 // 지도의 확대 레벨
    };  

var map = new kakao.maps.Map(mapContainer, mapOption); // 지도를 생성합니다

var mapTypeControl = new kakao.maps.MapTypeControl();    
map.addControl(mapTypeControl, kakao.maps.ControlPosition.TOPLEFT);

var market = ["진천전통시장", "진천중앙시장"];

for (var i = 0; i < 2; i++) {
    // 지도에 표시할 다각형을 생성합니다
    var polygon = new kakao.maps.Polygon({
        path:polygonPath[market[i]], // 그려질 다각형의 좌표 배열입니다
        strokeWeight: 3, // 선의 두께입니다
        strokeColor: '#FF0000', // 선의 색깔입니다
        strokeOpacity: 0.7, // 선의 불투명도 입니다 1에서 0 사이의 값이며 0에 가까울수록 투명합니다
        strokeStyle: 'line', // 선의 스타일입니다
        fillColor: '#A2FF99', // 채우기 색깔입니다
        fillOpacity: 0.4 // 채우기 불투명도 입니다
    });

    // 지도에 다각형을 표시합니다
    polygon.setMap(map);
}

</script>
</body>
</html>
