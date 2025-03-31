export default function getListStudentIds(listids) {
  if (!(listids instanceof Array)) {
    return [];
  }
  const ids = listids.map((listid) => listid.id);
  return ids;
}
