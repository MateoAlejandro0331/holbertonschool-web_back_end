export default function hasValuesFromArray(set, array) {
  const result = array.every((element) => set.has(element));
  return result;
}
// Every method return true if all the elements in the array are in the set
