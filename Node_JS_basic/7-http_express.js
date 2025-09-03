const express = require('express');
const fs = require('fs').promises;

const database = process.argv[2];

async function getStudentsInfo(path) {
  try {
    const content = await fs.readFile(path, 'utf8');
    const lines = content.split('\n').filter(line => line.trim() !== '');
    const rows = lines.slice(1); // skip header

    let output = `Number of students: ${rows.length}`;

    const byField = {};
    rows.forEach(row => {
      const cols = row.split(',');
      if (cols.length >= 4) {
        const firstName = cols[0].trim();
        const field = cols[3].trim();
        if (!byField[field]) byField[field] = [];
        byField[field].push(firstName);
      }
    });

    Object.keys(byField).sort().forEach(field => {
      output += `\nNumber of students in ${field}: ${byField[field].length}. List: ${byField[field].join(', ')}`;
    });

    return output;
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  let output = 'This is the list of our students\n';
  try {
    const info = await getStudentsInfo(database);
    output += info;
    res.send(output);
  } catch (err) {
    res.status(500).send(err.message);
  }
});

app.listen(1245);

module.exports = app;
