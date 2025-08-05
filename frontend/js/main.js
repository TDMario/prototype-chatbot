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

      // 🟢 EventListener nach dem Laden einbinden
      modelSelector.addEventListener("change", () => {
        console.log("Service switched to:", modelSelector.value);
        loadDocuments();
      });

      // 🟢 Initial einmal laden (mit Default oder erster Option)
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

    // === Checkbox-Dateien einsammeln ===
    const selectedFileIds = Array.from(document.querySelectorAll(".doc-checkbox:checked"))
      .map(cb => cb.value);

    try {
      const res = await fetch(`http://localhost:8000/chat?service=${selectedModel}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt, file_ids: selectedFileIds }),
      });
      const data = await res.json();
      responseOutput.textContent = data.response || "[No response]";
    } catch (error) {
      responseOutput.textContent = "Error fetching response.";
      console.error("Chat error:", error);
    }
  });

  // === Init ===
  loadServices();
});