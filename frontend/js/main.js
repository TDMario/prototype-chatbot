document.getElementById("pingButton").addEventListener("click", async () => {
  const responseArea = document.getElementById("responseArea");
  responseArea.textContent = "Sending ping...";

  try {
    const res = await fetch("http://localhost:8000/test/test_ping");
    const data = await res.json();
    responseArea.textContent = data.message;
  } catch (err) {
    console.error(err);
    responseArea.textContent = "Error calling backend.";
  }
});