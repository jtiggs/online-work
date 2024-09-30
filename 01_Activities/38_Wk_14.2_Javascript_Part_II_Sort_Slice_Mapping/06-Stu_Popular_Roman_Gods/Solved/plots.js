console.log(searchResults);

// Create a custom function to return Roman gods with more than 1 million search results
function popular(roman) {
  return roman.romanSearchResults > 1000000;
}

// Call the custom function with filter()
let popularRomans = searchResults.filter(popular);

// Trace for the Roman Data
let trace1 = {
    x: popularRomans.map(row => row.romanName),
    y: popularRomans.map(row => row.romanSearchResults),
    type: "bar"
};

// Data trace array
let data = [trace1];

// Apply a title to the layout
let layout = {
  title: "Popular Roman gods search results"
};

// Render the plot to the div tag with id "plot"
Plotly.newPlot("plot", data, layout);
