export default function getStudentIdsSum(sum) {
  const sumResult = sum.reduce((accumulator, students) => accumulator + students.id, 0);
  return sumResult;
}
// el ultimo paramtro es el valor inical del acumulador
