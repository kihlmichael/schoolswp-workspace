import { readdirSync, copyFileSync, mkdirSync, readFileSync } from 'node:fs';

const srcDir = 'D:\\TÉLÉCHARGEMENT\\FireShot';
const destDir = 'D:\\VS Code\\CLAUDE CODE\\projects\\schoolswp\\assets\\article-images\\post-2289943';
mkdirSync(destDir, { recursive: true });

const map = {
  'Capture 480': 'src-480-assistant.png',
  'Capture 481': 'src-481-general.png',
  'Capture 482': 'src-482-schema.png',
};

for (const f of readdirSync(srcDir)) {
  for (const key of Object.keys(map)) {
    if (f.includes(key)) {
      const dest = destDir + '\\' + map[key];
      copyFileSync(srcDir + '\\' + f, dest);
      const buf = readFileSync(dest);
      console.log(`${map[key]}  [${buf.readUInt32BE(16)}x${buf.readUInt32BE(20)}]  <- ${f}`);
    }
  }
}
