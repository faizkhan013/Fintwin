/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,jsx}"],
  theme: {
    extend: {
      colors: {
        ink: "#1B2620",
        inkdeep: "#121A16",
        paper: "#F6F2E9",
        paperdim: "#EDE6D6",
        stamp: "#B23A2E",
        verified: "#3F6B4F",
        brass: "#B08D57",
        charcoal: "#2A2A26",
        muted: "#7C7566"
      },
      fontFamily: {
        display: ["Fraunces", "serif"],
        body: ["IBM Plex Sans", "sans-serif"],
        mono: ["IBM Plex Mono", "monospace"]
      },
      backgroundImage: {
        ledger: "repeating-linear-gradient(180deg, rgba(176,141,87,0.07) 0px, rgba(176,141,87,0.07) 1px, transparent 1px, transparent 32px)"
      }
    },
  },
  plugins: [],
}
