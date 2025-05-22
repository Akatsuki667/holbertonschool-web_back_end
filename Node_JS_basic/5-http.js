const http = require('http');
const countStudents = require('./2-read_file');

// Création serveur
const app = http.createServer((req, res) => {
  // Obtenir URL et méthode requête
  const { url, method } = req;
  // Journalisation de la requête
  console.log(`${method} ${url}`);
  // Définition en-têtes
  res.setHeader('Content-Type', 'text/plain');

  // Routage simple
  if (url === '/') {
    res.end('Hello Holberton School!');
  } else if (url === '/students') {
    try {
      countStudents('database.csv');
      res.end('This is the list of our students');
    } catch (error) {
      res.end();
    }
  }
});

// Définir le port
const port = 1245;

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});

module.exports = app;
