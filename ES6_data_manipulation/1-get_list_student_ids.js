export default function getListStudentIds(arr) {
  if (typeof arr === 'object') {
    const list = arr.map((value) => value.id);
    return list;
  }
  return [];
}
