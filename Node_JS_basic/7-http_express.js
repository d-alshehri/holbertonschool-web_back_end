const express = require('express');
const fs = require('fs').promises;

const database = process.argv[2];

const app = express();

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf8');
    const lines = data.split('\n').filter(line => line.trim() !== '');
    const students = lines.slice(1); // skip header
    const fields = {};

    students.forEach(line => {
      const parts = line.split(',');
      if (parts.length >= 4) {
        const name = parts[0].trim();
        const field = parts[3].trim();
        if (!fields[field]) fields[field] = [];
        fields[field].push(name);
      }
    });

    let result = `Number of students: ${students.length}`;
    Object.keys(fields).sort().forEach(field => {
      result += `\nNumber of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`;
    });

    return result;
  } catch {
    throw new Error('Cannot load the database');
  }
}

// / route
app.get('/', (req, res) => {
  res.set('Content-Type', 'text/plain');
  res.send('Hello Holberton School!');
});

// /students route
app.get('/students', async (req, res) => {
  res.set('Content-Type', 'text/plain');
  let output = 'This is the list of our students';
  try {
    const info = await countStudents(database);
    output += `\n${info}`;
    res.send(output);
  } catch (err) {
    res.status(500).send(err.message);
  }
});

app.listen(1245);

module.exports = app;
