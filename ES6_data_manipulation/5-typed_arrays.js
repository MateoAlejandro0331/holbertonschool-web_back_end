export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const array = new Int8Array(buffer);
  const hex = `0x${value.toString(16).toUpperCase()}`;
  array[position] = hex;
  return array;
}
