async function loadDocuments() {
  const modelSelector = document.getElementById('modelSelector');
  const selectedModel = modelSelector.value || "default";

  console.log("[loadDocuments] Using service:", selectedModel);

  const response = await fetch(`http://localhost:8000/documents?service=${selectedModel}`);
  const documents = await response.json();
  const list = document.getElementById('documentList');
  list.innerHTML = '';
  documents.forEach(doc => {
    const li = document.createElement('li');
    const label = document.createElement('label');
    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.value = doc.id || doc.file_id;
    checkbox.classList.add('doc-checkbox');
    label.appendChild(checkbox);
    label.appendChild(document.createTextNode(' ' + (doc.name || doc.filename || "Unnamed")));
    const deleteBtn = document.createElement('button');
    deleteBtn.textContent = 'Delete';
    deleteBtn.onclick = () => deleteDocument(checkbox.value);
    li.appendChild(label);
    li.appendChild(deleteBtn);
    list.appendChild(li);
  });
}

async function uploadDocument() {
  const fileInput = document.getElementById('uploadInput');
  const modelSelector = document.getElementById('modelSelector');
  const selectedModel = modelSelector.value || "default";

  console.log("[uploadDocument] Using service:", selectedModel);

  if (!fileInput.files.length) return;
  const formData = new FormData();
  formData.append('file', fileInput.files[0]);

  await fetch(`http://localhost:8000/documents?service=${selectedModel}`, {
    method: 'POST',
    body: formData
  });

  fileInput.value = '';
  loadDocuments();
}

async function deleteDocument(docId) {
  const modelSelector = document.getElementById('modelSelector');
  const selectedModel = modelSelector.value || "default";

  console.log("[deleteDocument] Using service:", selectedModel);

  await fetch(`http://localhost:8000/documents/${docId}?service=${selectedModel}`, {
    method: 'DELETE'
  });
  loadDocuments();
}

document.getElementById('uploadButton').addEventListener('click', uploadDocument);
window.addEventListener('DOMContentLoaded', () => {
  loadDocuments();

  // Servicewechsel führt zu erneutem Laden
  const modelSelector = document.getElementById('modelSelector');
  modelSelector.addEventListener('change', () => {
    console.log("[modelSelector] Changed to:", modelSelector.value);
    loadDocuments();
  });
});
