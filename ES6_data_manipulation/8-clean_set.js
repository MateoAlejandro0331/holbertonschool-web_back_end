export default function cleanSet(set, startString) {
  let endString = '';
  let count = 0;
  set.forEach((str) => {
    if (str.includes(startString)) {
      if (startString === '') return endString;
      str = str.replace(startString, '');
      count += 1;
      if (count === parseInt(set.size - 1)) {
        endString += str;
      } else {
        endString = `${endString}${str}-`;
      }
    }
  });
  return endString;
}
