// Use D3 to select the table
let table = d3.select("table");

// Use D3 to create a bootstrap striped table
// http://getbootstrap.com/docs/3.3/css/#table-striped
table.classed("table-striped", true);

// Use D3 to select the table body
let tbody = d3.select("tbody");

// BONUS: Dynamic table
// Loop through an array of grades and build the entire table body from scratch
let grades = [["Malcolm", 80], ["Zoe", 85], ["Kaylee", 99], ["Simon", 99], ["Wash", 79]];

for (let i = 0; i < grades.length; i++){
  // Get the current grade
  let grade = grades[i];

  // Append one table row `tr` to the table body
  let row = tbody.append("tr");

  // Append one cell for the student name
  row.append("td").text(grade[0]);

  // Append one cell for the student grade
  row.append("td").text(grade[1]);
}
