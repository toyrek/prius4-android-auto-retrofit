/* Optional documentation build: npm install --no-save --package-lock=false sharp */
'use strict';
const path = require('node:path');
const sharp = require('sharp');
const root = path.resolve(__dirname, '..');
(async () => {
  for (const name of ['parcours', 'identifier', 'cles']) {
    await sharp(path.join(root, 'assets', name + '.svg'), {density:160})
      .png().toFile(path.join(root, 'assets', name + '.png'));
  }
  console.log('3 illustrations PNG générées à partir des SVG.');
})().catch(error => { console.error(error.message); process.exitCode = 1; });
