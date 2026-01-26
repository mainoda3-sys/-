// Simple static slot list (mock). If you later attach backend, replace fetch with real API call.
const slots = [
  { id: 1, name: 'Slot A1', marker: 'hiro' },
  { id: 2, name: 'Slot B2', marker: 'kanji' }
];

function renderSlots(){
  const el = document.getElementById('slots');
  el.innerHTML = '';
  slots.forEach(s => {
    const div = document.createElement('div');
    div.className = 'slot';
    div.innerHTML = `<strong>${s.name}</strong><br/>Marker: ${s.marker} <br/>
      <a class="btn" href="ar.html?slot=${s.id}" target="_blank">Navigate (AR)</a>
      <div style="margin-top:6px;font-size:13px;color:#666">Tip: open on mobile browser or open in new tab and point camera at the marker image.</div>`;
    el.appendChild(div);
  });
}

renderSlots();