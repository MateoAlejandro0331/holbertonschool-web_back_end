export default function createInt8TypedArray(length, position, value) {
  if (position < length) {
    const buffer = new ArrayBuffer(length);
    const array = new Int8Array(buffer);
    array[position] = `0x${value.toString(16).toUpperCase()}`;
    const dataView = new DataView(buffer);
    return dataView;
  }
  return Error('Position outside range');
}
