// Mode "flowing"
process.stdin.setEncoding('utf8');

console.log('Welcome to Holberton School, what is your name?');

// Écouter l'événement
process.stdin.on('data', (data) => {
  const name = data.trim(); // Supprime retours à la ligne
  console.log('Your name is : ', name);
  console.log('This important software is now closing\n');
  process.exit(); // Quitter le programme
});
