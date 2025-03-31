export default function getStudentIdsSum(listOfStudents) {
  if (!(listOfStudents instanceof Array)) {
    throw new TypeError('ListOfStudents must be an array');
  }

  const idsSum = listOfStudents
    .map((ids) => ids.id)
    .reduce((total, id) => total + id, 0);

  return idsSum;
}
