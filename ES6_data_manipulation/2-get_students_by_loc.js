export default function getStudentsByLocation(listOfStudents, city) {
  if (!(listOfStudents instanceof Array)) {
    throw new TypeError('ListOfStudent must be an array');
  }

  if (typeof city !== 'string') {
    throw new TypeError('City must be a string');
  }

  const listSameCity = listOfStudents.filter((listOfStudent) => listOfStudent.location === 'San Francisco');
  return listSameCity;
}
