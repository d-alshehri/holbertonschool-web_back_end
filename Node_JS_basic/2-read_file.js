// 2-read_file.js
const fs = require('fs');

function countStudents(path) {
  try {
    const content = fs.readFileSync(path, 'utf8');
    const lines = content
      .split('\n')
      .filter((line) => line.trim().length > 0);

    // No valid rows besides header
    if (lines.length <= 1) {
      console.log('Number of students: 0');
      return;
    }

    const rows = lines.slice(1); // skip header
    console.log(`Number of students: ${rows.length}`);

    const byField = {};

    rows.forEach((row) => {
      const cols = row.split(',');
      // Expected CSV: firstname,lastname,age,field
      if (cols.length >= 4) {
        const firstName = cols[0].trim();
        const field = cols[3].trim();
        if (!byField[field]) byField[field] = [];
        byField[field].push(firstName);
      }
    });

    // Stable order so output matches tests (e.g., CS then SWE)
    Object.keys(byField).sort().forEach((field) => {
      const list = byField[field].join(', ');
      console.log(`Number of students in ${field}: ${byField[field].length}. List: ${list}`);
    });
  } catch (e) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
