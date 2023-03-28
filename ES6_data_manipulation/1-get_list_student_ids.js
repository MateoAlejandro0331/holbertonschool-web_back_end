export default function getListStudentIds(arr) {
  if (Array.isArray(arr)) {
    const list = arr.map((value) => value.id);
    return list;
  }
  return [];
}
