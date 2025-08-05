document.addEventListener("DOMContentLoaded", () => {
  const pingButton = document.getElementById("pingButton");
  const sendPromptButton = document.getElementById("sendPrompt");
  const promptInput = document.getElementById("promptInput");
  const responseOutput = document.getElementById("responseOutput");
  const modelSelector = document.getElementById("modelSelector");

  // === 1. PING-Funktion testen ===
  pingButton.addEventListener("click", async () => {
    try {
      const res = await fetch("http://localhost:8000/test/test_ping");
      const data = await res.json();
      alert("Ping response: " + data.message);
    } catch (error) {
      alert("Ping failed.");
    }
  });

  // === 2. Services laden ===
  async function loadServices() {
    try {
      const res = await fetch("http://localhost:8000/services");
      const services = await res.json();

      modelSelector.innerHTML = "";
      services.forEach((key) => {
        const option = document.createElement("option");
        option.value = key;
        option.textContent = key.charAt(0).toUpperCase() + key.slice(1);
        modelSelector.appendChild(option);
      });

      modelSelector.addEventListener("change", () => {
        console.log("[modelSelector] Changed to:", modelSelector.value);
        loadDocuments();
      });

      loadDocuments();
    } catch (error) {
      console.error("Failed to load services:", error);
    }
  }

  // === 3. Prompt senden ===
  sendPromptButton.addEventListener("click", async () => {
    const prompt = promptInput.value.trim();
    if (!prompt) return;

    const selectedModel = modelSelector.value || "default";
    const selectedFileIds = Array.from(document.querySelectorAll(".doc-checkbox:checked"))
      .map(cb => cb.value);

    responseOutput.textContent = "Awaiting answer ...";

    try {
      const res = await fetch(`http://localhost:8000/chat?service=${selectedModel}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt, file_ids: selectedFileIds }),
      });

      if (!res.ok) {
        const errorData = await res.json();
        responseOutput.textContent = `Fehler: ${errorData.detail?.error || "Unkown error"}`;
        return;
      }

      const data = await res.json();
      responseOutput.textContent = data.response || "[Keine Antwort erhalten]";
    } catch (error) {
      responseOutput.textContent = "Error creating the answer, try again later";
      console.error("Chat error:", error);
    }
  });

  // === Init ===
  loadServices();
});
