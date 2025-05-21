const http = require('http');

// Créer serveur HTTP
const app = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/plain');
  res.write('Hello Holberton School!')
  res.end();
});

// Définir port d'écoute
const port = 1245;

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});

module.exports = app;
