let currentLetter = "-";
let sentence = "";

document.getElementById("startBtn").addEventListener("click", () => {
  document.getElementById("welcome").style.display = "none";
  document.getElementById("recognition").style.display = "block";

  startWebcam();
  startPredictionLoop();
});

// Start webcam
function startWebcam() {
  const video = document.getElementById("video");

  navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => { video.srcObject = stream; })
    .catch(err => alert("Camera Not Detected"));
}

// Capture frame + send to Flask
function captureFrame() {
  const video = document.getElementById("video");

  const canvas = document.createElement("canvas");
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;

  const ctx = canvas.getContext("2d");
  ctx.drawImage(video, 0, 0);

  return canvas.toDataURL("image/jpeg");
}

// Send to Flask every 300ms
function startPredictionLoop() {
  setInterval(async () => {
    const frame = captureFrame();

    const res = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ image: frame })
    });

    const data = await res.json();
    currentLetter = data.letter;

    document.getElementById("currentLetter").innerText = currentLetter;
    document.getElementById("sentenceBox").innerText = sentence;

  }, 300);
}

// Keyboard controls
document.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && currentLetter !== "-") {
    sentence += currentLetter;
  }
  if (e.code === "Space") sentence += " ";
  if (e.key === "c" || e.key === "C") sentence = "";
  if (e.key === "Backspace") sentence = sentence.slice(0, -1);
  if (e.key === "s" || e.key === "S") speak(sentence);

  document.getElementById("sentenceBox").innerText = sentence;
});

// Browser speech
function speak(text) {
  const tts = new SpeechSynthesisUtterance(text);
  tts.rate = 1.0;
  speechSynthesis.speak(tts);
}
