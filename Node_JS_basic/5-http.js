const http = require('http');
const fs = require('fs').promises;

const app = http.createServer(async (req, res) => {

  const { url } = req;
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  if (url === '/') {
    res.write('Hello Holberton School!\n');
  }
  if (url === '/students') {
    res.write('This is the list of our students\n');
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
      res.write('Cannot load the database\n');
    }
  }
  res.end();
});

app.listen(1245, () => {
  console.log('Server is running on port 1245');
});

module.exports = app;
