<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <title>即死パラノーマルゲーム</title>
  <script src="https://cdn.jsdelivr.net/npm/pannellum/build/pannellum.js"></script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/pannellum/build/pannellum.css">
</head>
<body>
  <div id="panorama" style="width:100%;height:100vh;"></div>

  <script>
    pannellum.viewer('panorama', {
      type: 'equirectangular',
      panorama: 'panorama.jpg',
      autoLoad: true,
      hotSpots: [{
        pitch: 0,
        yaw: 100,
        type: 'info',
        text: '謎の扉を開ける',
        clickHandlerFunc: function() {
          alert('霊に襲われて即死しました…');
          location.reload();
        }
      }]
    });
  </script>
</body>
</html>