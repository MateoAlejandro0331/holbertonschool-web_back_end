const fs = require('fs').promises;

const countStudents = async (path) => {
  try {
    const fileContent = await fs.readFile(path, 'utf8');
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

    console.log(`Number of students: ${data.length}`);

    const csStudents = data.filter((obj) => obj.field === 'CS');
    const csNames = csStudents.map((obj) => obj.firstname);
    const joinCsNames = csNames.join(', ');
    console.log(`Number of students in CS: ${csNames.length}. List: ${joinCsNames}`);

    const sweStudents = data.filter((obj) => obj.field === 'SWE');
    const sweNames = sweStudents.map((obj) => obj.firstname);
    const joinSweNames = sweNames.join(', ');
    console.log(`Number of students in SWE: ${sweNames.length}. List: ${joinSweNames}`);
  } catch (err) {
    throw new Error('Cannot load the database');
  }
};

module.exports = countStudents;
