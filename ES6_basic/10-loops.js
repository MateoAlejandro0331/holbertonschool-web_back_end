export default function appendToEachArrayValue(array, appendString) {
  const auxArray = [];
  for (const value of array) {
    auxArray.push(appendString + value);
  }

  return auxArray;
}
