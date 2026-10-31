// Read-only classifier. Node.js 18+, no packages or network access.
const fs = require('node:fs');
const { assess } = require('../guide/preflight.js');
if (process.argv.length !== 3) {
  console.error('Usage : node tools/check-vehicle.cjs fiche.json');
  process.exitCode = 2;
} else {
  try { console.log(JSON.stringify(assess(JSON.parse(fs.readFileSync(process.argv[2], 'utf8'))), null, 2)); }
  catch (error) { console.error('Fiche illisible : '+error.message); process.exitCode = 2; }
}
