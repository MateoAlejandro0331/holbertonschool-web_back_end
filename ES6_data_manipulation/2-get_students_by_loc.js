export default function getStudentsByLocation(students, city) {
  const list = students.filter((value) => value.location === city);
  return list;
}
