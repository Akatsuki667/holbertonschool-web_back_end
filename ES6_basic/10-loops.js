export default function appendToEachArrayValue(array, appendString) {
  const new_array = [];

  for (const value of array) {
    new_array.push(value);
  }
  return new_array;
}
