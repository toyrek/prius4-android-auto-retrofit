'use strict';
const form = document.getElementById('vehicle-form');
const api = window.PriusPreflight;
const numbers = new Set(['year', 'audio', 'navigation_version']);
function readProfile() {
  const data = new FormData(form), profile = {};
  for (const key of Object.keys(api.fields)) {
    const value = String(data.get(key) ?? '').trim();
    profile[key] = value === '' ? null : value === 'true' ? true : value === 'false' ? false : numbers.has(key) ? Number(value) : value;
  }
  return profile;
}
function showResult(focus = false) {
  const profile = readProfile(), result = api.assess(profile);
  document.getElementById('result-title').textContent = result.title;
  document.getElementById('result-summary').textContent = result.summary;
  document.getElementById('result-next').textContent = result.next_action;
  const notes = document.getElementById('result-notes');
  notes.replaceChildren();
  for (const note of result.notes) { const li = document.createElement('li'); li.textContent = note; notes.append(li); }
  notes.hidden = result.notes.length === 0;
  const panel = document.getElementById('result');
  panel.hidden = false;
  panel.dataset.code = result.code;
  if (focus) panel.focus();
  return { profile, result };
}
function refreshPrompt() {
  const profile = readProfile();
  document.getElementById('agent-prompt').value = api.prompt(profile, api.assess(profile));
  document.getElementById('copy-status').textContent = '';
}
form.addEventListener('submit', event => { event.preventDefault(); showResult(true); });
form.addEventListener('input', () => {
  document.getElementById('writing-warning').hidden = form.elements.update_in_progress.value !== 'true';
  if (!document.getElementById('result').hidden) showResult();
  if (!document.getElementById('prompt-panel').hidden) refreshPrompt();
});
form.addEventListener('reset', () => {
  for (const id of ['result','prompt-panel','writing-warning']) document.getElementById(id).hidden = true;
  document.getElementById('agent-prompt').value = '';
  document.getElementById('copy-status').textContent = '';
});
document.getElementById('prepare-prompt').addEventListener('click', () => {
  showResult(); refreshPrompt();
  document.getElementById('prompt-panel').hidden = false;
  document.getElementById('agent-prompt').focus();
});
document.getElementById('copy-prompt').addEventListener('click', async () => {
  const textarea = document.getElementById('agent-prompt'), status = document.getElementById('copy-status');
  try { await navigator.clipboard.writeText(textarea.value); status.textContent = 'Message copié. Relisez-le dans votre conversation avant de l’envoyer.'; }
  catch { textarea.focus(); textarea.select(); status.textContent = 'Le message est sélectionné : utilisez Copier dans votre navigateur ou Ctrl+C.'; }
});
document.getElementById('download-profile').addEventListener('click', () => {
  const url = URL.createObjectURL(new Blob([JSON.stringify(readProfile(), null, 2) + '\n'], {type:'application/json'}));
  const a = document.createElement('a'); a.href = url; a.download = 'ma-fiche-autoradio.json'; a.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
});
