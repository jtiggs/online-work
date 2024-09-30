console.log(searchResults);

// Greek god names
let names = searchResults.map(function (row){
  return row.greekName
});

// Trace for the Greek Data
let trace1 = {
    x: searchResults.map(row => row.greekName),
    y: searchResults.map(row => row.greekSearchResults),
    type: "bar"
  };

// Data trace array
let data = [trace1];

// Apply a title to the layout
let layout = {
  title: "Greek gods search results"
};

// Render the plot to the div tag with id "plot"
Plotly.newPlot("plot", data, layout);
