function saveEntry() {
  const text = document.getElementById("entry").value.trim();
  if (text === "") return;

  const entries = JSON.parse(localStorage.getItem("journalEntries")) || [];
  entries.unshift({ text, date: new Date().toLocaleString() });

  localStorage.setItem("journalEntries", JSON.stringify(entries));
  document.getElementById("entry").value = "";
  displayEntries();
}

function displayEntries() {
  const entries = JSON.parse(localStorage.getItem("journalEntries")) || [];
  const entriesContainer = document.getElementById("entries");
  entriesContainer.innerHTML = "";

  entries.forEach(entry => {
    const div = document.createElement("div");
    div.className = "entry";
    div.innerHTML = `<strong>${entry.date}</strong><p>${entry.text}</p>`;
    entriesContainer.appendChild(div);
  });
}

window.onload = displayEntries;
