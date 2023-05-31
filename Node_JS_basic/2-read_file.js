const fs = require('fs');

const countStudents = (path) => {
  if (!fs.existsSync(path)) {
    throw new Error('Cannot load the database');
  }

  const fileContent = fs.readFileSync(path, 'utf8');
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
  process.stdout.write(`Number of students: ${data.length}\n`);
  const csStudents = data.filter((obj) => obj.field === 'CS');
  process.stdout.write(`Number of students in CS: ${csStudents.length}. List: `);
  csStudents.map((obj, index) => {
    if (index === csStudents.length - 1) {
      process.stdout.write(`${obj.firstname}\n`);
    } else {
      process.stdout.write(`${obj.firstname}, `);
    }
  });

  const sweStudents = data.filter((obj) => obj.field === 'SWE');
  process.stdout.write(`Number of students in SWE: ${sweStudents.length}. List: `);
  sweStudents.map((obj, index) => {
    if (index === sweStudents.length - 1) {
      process.stdout.write(`${obj.firstname}\n`);
    } else {
      process.stdout.write(`${obj.firstname}, `);
    }
  });
};

module.exports = countStudents;
