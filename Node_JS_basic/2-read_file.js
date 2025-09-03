const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.split('\n').filter((line) => line.trim() !== '');

    // Remove header row
    const students = lines.slice(1);

    console.log(`Number of students: ${students.length}`);

    const fields = {};

    students.forEach((student) => {
      const parts = student.split(',');
      const firstname = parts[0];
      const field = parts[parts.length - 1];

      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstname);
    });

    for (const [field, names] of Object.entries(fields)) {
      console.log(
        `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`
      );
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
