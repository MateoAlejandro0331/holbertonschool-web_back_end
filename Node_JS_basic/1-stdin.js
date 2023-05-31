process.stdin.setEncoding('utf8');

console.log('Welcome to Holberton School, what is your name?');

process.stdin.on('data', (data) => {
  const input = data.trim(); // Remove trailing newline and convert to lowercase
  console.log(`Your name is: ${input}`);
});

process.on('exit', () => {
  console.log('This important software is now closing');
});

process.stdin.resume(); // Start listening for input
