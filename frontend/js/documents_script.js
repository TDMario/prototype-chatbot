
async function loadDocuments() {
  const response = await fetch('http://localhost:8000/documents');
  const documents = await response.json();
  const list = document.getElementById('documentList');
  list.innerHTML = '';
  documents.forEach(doc => {
    const li = document.createElement('li');
    const label = document.createElement('label');
    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.value = doc.id;
    checkbox.classList.add('doc-checkbox');
    label.appendChild(checkbox);
    label.appendChild(document.createTextNode(' ' + doc.name));
    const deleteBtn = document.createElement('button');
    deleteBtn.textContent = 'Delete';
    deleteBtn.onclick = () => deleteDocument(doc.id);
    li.appendChild(label);
    li.appendChild(deleteBtn);
    list.appendChild(li);
  });
}

async function uploadDocument() {
  const fileInput = document.getElementById('uploadInput');
  if (!fileInput.files.length) return;
  const formData = new FormData();
  formData.append('file', fileInput.files[0]);
  await fetch('http://localhost:8000/documents', {
    method: 'POST',
    body: formData
  });
  fileInput.value = '';
  loadDocuments();
}

async function deleteDocument(docId) {
  await fetch(`http://localhost:8000/documents/${docId}`, { method: 'DELETE' });
  loadDocuments();
}

document.getElementById('uploadButton').addEventListener('click', uploadDocument);
window.addEventListener('DOMContentLoaded', loadDocuments);
