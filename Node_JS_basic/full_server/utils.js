import fs from 'fs/promises';

export async function readDatabase(filePath) {
  try {
    const content = await fs.readFile(filePath, 'utf8');
    const lines = content.split('\n').filter(line => line.trim() !== '');
    const rows = lines.slice(1); // skip header
    const studentsByField = {};

    rows.forEach(line => {
      const [firstName,, , field] = line.split(',');
      if (!studentsByField[field]) studentsByField[field] = [];
      studentsByField[field].push(firstName);
    });

    return studentsByField;
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}
