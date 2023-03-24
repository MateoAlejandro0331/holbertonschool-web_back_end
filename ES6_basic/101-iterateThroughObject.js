export default function iterateThroughObject(reportWithIterator) {
  let result = '';
  for (const value of reportWithIterator) {
    result += `${value} | `;
  }
  return result;
}
