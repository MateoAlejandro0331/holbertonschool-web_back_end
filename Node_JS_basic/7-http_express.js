const express = require('express');
const fs = require('fs').promises;

const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  try {
    const fileContent = await fs.readFile(process.argv[2], 'utf8');
    const lines = fileContent.split('\n');
    const headers = lines[0].split(',');

    const data = [];
    for (let i = 1; i < lines.length; i += 1) {
      const row = lines[i].split(',');

      if (row.length === headers.length) {
        const rowData = {};
        for (let j = 0; j < headers.length; j += 1) {
          rowData[headers[j]] = row[j];
        }
        data.push(rowData);
      }
    }

    res.write(`Number of students: ${data.length}\n`);

    const csStudents = data.filter((obj) => obj.field === 'CS');
    const csNames = csStudents.map((obj) => obj.firstname);
    const joinCsNames = csNames.join(', ');
    res.write(`Number of students in CS: ${csNames.length}. List: ${joinCsNames}\n`);

    const sweStudents = data.filter((obj) => obj.field === 'SWE');
    const sweNames = sweStudents.map((obj) => obj.firstname);
    const joinSweNames = sweNames.join(', ');
    res.write(`Number of students in SWE: ${sweNames.length}. List: ${joinSweNames}`);
  } catch (err) {
    res.write('Cannot load the database');
  }
  res.send();
});

app.listen(1245, () => {
  console.log('Server is running on port 1245');
});

module.exports = app;
