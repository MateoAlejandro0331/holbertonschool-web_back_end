export default function updateStudentGradeByCity(students, city, newGrades) {
  const newStudents = students.filter((student) => student.location === city)
    .map((student) => {
      for (const value of newGrades) {
        if (value.studentId === student.id) {
          const newStudent = { ...student };
          newStudent.grade = value.grade;
          return newStudent;
        }
      }
      const newStudent = { ...student };
      newStudent.grade = 'N/A';
      return newStudent;
    });
  return newStudents;
}
