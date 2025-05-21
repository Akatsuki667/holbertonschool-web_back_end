const fs = require('fs').promises;

async function countStudents(path) {
  try {
    // Lecture asynchrone fichier
    const file = await fs.readFile(path, 'utf8');

    // Division contenu en ligne
    const lines = file.split('\n');

    // Vérifier si il y a des données
    if (lines.length <= 1) {
      console.log('No students found');
      return;
    }

    // Extraire l'en-tête
    const headers = lines[0].split(',');

    // Trouver les indices colonnes
    const firstNameIndex = headers.findIndex((field) => field === 'firstname');
    const fieldIndex = headers.findIndex((field) => field === 'field');

    // Vérification colonnes existent
    if (firstNameIndex === -1 || fieldIndex === -1) {
      throw new Error('Missing required columns in the database');
    }

    // Initialisation tableau étudiants
    const students = [];
    // Parcourir  lignes de données
    for (let i = 1; i < lines.length; i += 1) {
      // Suppression espaces
      const line = lines[i].trim();
      // Ignorer lignes vides
      if (line !== '') {
        const values = line.split(',');

        // Vérification ligne a le bon nb de colonnes
        if (values.length === headers.length) {
          const student = {
            firstName: values[firstNameIndex],
            field: values[fieldIndex],
          };

          students.push(student);
        }
      }
    }

    // Afficher total étudiants
    console.log(`Number of students: ${students.length}`);

    // Regrouper les étudiants par champ d'étude
    const fieldGroups = {};

    for (const student of students) {
      // Utilisation de la destructuration d'objets
      const { field } = student;

      if (!fieldGroups[field]) {
        fieldGroups[field] = [];
      }

      fieldGroups[field].push(student);
    }

    // Afficher les statistiques pour chaque champ
    for (const [field, groupStudents] of Object.entries(fieldGroups)) {
      const firstNames = groupStudents.map((student) => student.firstName);
      console.log(`Number of students in ${field}: ${groupStudents.length}. List: ${firstNames.join(', ')}`);
    }
  } catch (error) {
    // En cas d'erreur, lancer une exception avec le message spécifié
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
