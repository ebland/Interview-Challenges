// Rentlytics Exercise - Lease Visualizer
// ======================================
// Using the dataset below, build a lease history gantt chart.  The X-Axis should be time, with the Y-Axis representing
// unique "unitName" values.  On the gantt chart, each lease is represented by a rectangle, in the row corresponding to the unit.
// The graph should also highlight the month with the highest aggregated rent.
// 
// Please fork this CodePen to submit your result, you may use any HTML/CSS/JS preprocessors or framework you wish.
//
// DO NOT USE A CHARTING/GRAPHING LIBRARY (excluding D3).

var leaseData = [
    {
        "unitName": "A101",
        "beginTimestamp": 1328256000000,
        "endTimestamp": 1359978400000,
        "rent": 1200
    },
    {
        "unitName": "B201",
        "beginTimestamp": 1298966400000,
        "endTimestamp": 1398966400000,
        "rent": 1300
    },
    {
        "unitName": "A301",
        "beginTimestamp": 1275721200000,
        "endTimestamp": 1298966400000,
        "rent": 1500
    },
    {
        "unitName": "A101",
        "beginTimestamp": 1298966400000,
        "endTimestamp": 1310664000000,
        "rent": 1100
    },
    {
        "unitName": "A301",
        "beginTimestamp": 1357878400000,
        "endTimestamp": 1369878400000,
        "rent": 2000
    }
];

$(function() {
  var $yAxis = $('.y-axis');
  $yAxis.html('unitName');
  for(var i=0; i < leaseData.length; i++) {
    $yAxis.append('<div class="y-label">' + leaseData[i]['unitName'] + '</div>');
  }


  var $graph = $('.graph');
  var monthWidth = $graph.width;
});

$(function() {
  var $xAxis = $('.x-axis');
  $xAxis.html('beginTimestamp');
  for(var i=0; i < leaseData.length; i++) {
    $xAxis.append('<div class="x-label">' + leaseData[i]['beginTimestamp'] + '</div>');
  }


  var $graph = $('.graph');
  var monthWidth = $graph.width;
});