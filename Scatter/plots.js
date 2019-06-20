
// Create the Traces
var trace1 = {
  x: data.Decade,
  y: data.Lowest_Price,
  mode: "markers",
  type: "scatter",
  name: "Dish",
  marker: {
    color: "#2077b4",
    symbol: "hexagram"
  }
};

var trace2 = {
  x: data.Decade,
  y: data.Highest_Price,
  mode: "markers",
  type: "scatter",
  name: "Highest Price",
  marker: {
    color: "orange",
    symbol: "diamond-x"
  }
};

var trace3 = {
  x: data.year,
  y: data.long_jump,
  mode: "markers",
  type: "scatter",
  name: data.Dish,
  marker: {
    color: "rgba(156, 165, 196, 1.0)",
    symbol: "cross"
  }
};

// Create the data array for the plot
var data = [trace1, trace2, trace3];

// Define the plot layout
var layout = {
  title: "Dishes by Lowest and Highest Menu Price Over Time",
  xaxis: { title: "Year" },
  yaxis: { title: "Dish" }
};

// Plot the chart to a div tag with id "plot"
Plotly.newPlot("plot", data, layout);
