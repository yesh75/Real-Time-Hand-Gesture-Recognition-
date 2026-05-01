import { useState, useEffect, useRef } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { motion } from "framer-motion";

export default function ASLWebApp() {
  const [started, setStarted] = useState(false);
  const videoRef = useRef(null);

  useEffect(() => {
    if (started) {
      navigator.mediaDevices.getUserMedia({ video: true }).then((stream) => {
        if (videoRef.current) {
          videoRef.current.srcObject = stream;
        }
      });
    }
  }, [started]);

  return (
    <div className="min-h-screen w-full bg-gradient-to-br from-purple-700 to-indigo-900 text-white p-8">
      {!started && (
        <motion.div
          initial={{ opacity: 0, scale: 0.9 }}
          animate={{ opacity: 1, scale: 1 }}
          className="max-w-3xl mx-auto text-center mt-20"
        >
          <h1 className="text-5xl font-bold mb-6">ASL Hand Sign Recognition</h1>
          <p className="text-xl opacity-90 mb-8 leading-relaxed">
            A powerful real‑time system that converts American Sign Language hand gestures
            into text and speech. Built using advanced AI hand‑tracking landmarks,
            smooth gesture classification, and smart sentence-building controls.
          </p>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-12">
            <Card className="bg-white/10 backdrop-blur-md border border-white/20 rounded-2xl">
              <CardContent className="p-6 text-center">
                <h2 className="text-2xl font-semibold mb-3">Real‑Time Recognition</h2>
                <p className="opacity-80">Instant gesture detection powered by MediaPipe Hand Landmarks.</p>
              </CardContent>
            </Card>

            <Card className="bg-white/10 backdrop-blur-md border border-white/20 rounded-2xl">
              <CardContent className="p-6 text-center">
                <h2 className="text-2xl font-semibold mb-3">Sentence Builder</h2>
                <p className="opacity-80">Use keyboard shortcuts to construct full sentences quickly.</p>
              </CardContent>
            </Card>

            <Card className="bg-white/10 backdrop-blur-md border border-white/20 rounded-2xl">
              <CardContent className="p-6 text-center">
                <h2 className="text-2xl font-semibold mb-3">Text‑To‑Speech</h2>
                <p className="opacity-80">Convert recognized ASL gestures into spoken output instantly.</p>
              </CardContent>
            </Card>
          </div>

          <Button
            onClick={() => setStarted(true)}
            className="mt-10 px-10 py-4 bg-yellow-400 text-black font-bold rounded-xl text-xl hover:bg-yellow-300"
          >
            Start Project
          </Button>
        </motion.div>
      )}

      {started && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className="max-w-5xl mx-auto mt-10"
        >
          <h1 className="text-4xl font-bold text-center mb-6">Hand Recognition Live</h1>

          <div className="flex flex-col lg:flex-row gap-8 items-start mt-10">
            {/* Live Video */}
            <video
              ref={videoRef}
              autoPlay
              playsInline
              className="rounded-2xl shadow-xl border-4 border-white/20 w-full lg:w-2/3"
            />

            {/* Controls */}
            <Card className="bg-white/10 backdrop-blur-md border border-white/20 rounded-2xl w-full lg:w-1/3 text-white">
              <CardContent className="p-6">
                <h2 className="text-2xl font-semibold mb-4 text-center">Controls</h2>
                <ul className="space-y-3 text-lg opacity-90">
                  <li><b>ENTER</b> — Add predicted letter</li>
                  <li><b>SPACE</b> — Add space</li>
                  <li><b>BACKSPACE</b> — Delete last character</li>
                  <li><b>C</b> — Clear sentence</li>
                  <li><b>S</b> — Speak sentence</li>
                  <li><b>Q</b> — Quit</li>
                </ul>

                <h3 className="text-xl font-semibold mt-6 mb-2">Tips</h3>
                <ul className="space-y-2 text-sm opacity-80">
                  <li>Keep your hand inside the frame.</li>
                  <li>Ensure good lighting for best accuracy.</li>
                  <li>Hold gestures steady for smooth recognition.</li>
                </ul>
              </CardContent>
            </Card>
          </div>
        </motion.div>
      )}
    </div>
  );
}
