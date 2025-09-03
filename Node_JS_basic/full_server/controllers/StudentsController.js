import { readDatabase } from '../utils.js';

export default class StudentsController {
  static async getAllStudents(req, res) {
    try {
      const db = await readDatabase(process.argv[2]);
      let output = 'This is the list of our students';
      Object.keys(db)
        .sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()))
        .forEach(field => {
          output += `\nNumber of students in ${field}: ${db[field].length}. List: ${db[field].join(', ')}`;
        });
      res.status(200).send(output);
    } catch (err) {
      res.status(500).send(err.message);
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const major = req.params.major;
    if (!['CS', 'SWE'].includes(major)) {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }
    try {
      const db = await readDatabase(process.argv[2]);
      const students = db[major] || [];
      res.status(200).send(`List: ${students.join(', ')}`);
    } catch (err) {
      res.status(500).send(err.message);
    }
  }
}
