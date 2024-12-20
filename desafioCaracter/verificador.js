const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Digite uma palavra: ", (palavra) => {
    console.log(`A palavra "${palavra}" tem ${palavra.length} caracteres.`);
    rl.close();
});
