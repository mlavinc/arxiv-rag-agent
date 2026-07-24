/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        paper: "#faf8f4",
        ink: "#2f2e2b",
        sage: {
          50: "#f4f6f3",
          100: "#e6ebe3",
          200: "#cdd8c8",
          300: "#adbfa4",
          400: "#8ba17e",
          500: "#6e8760",
          600: "#566b4b",
          700: "#44543c",
        },
        clay: {
          50: "#faf3ee",
          100: "#f2e2d6",
          200: "#e4c4ad",
          300: "#d4a482",
          400: "#c3835a",
          500: "#a9663f",
        },
        sand: {
          50: "#f8f5ef",
          100: "#eee7d8",
          200: "#ddd0b3",
        },
      },
      fontFamily: {
        serif: ["Georgia", "Cambria", "'Times New Roman'", "serif"],
        mono: ["'JetBrains Mono'", "'Courier New'", "monospace"],
      },
    },
  },
  plugins: [],
};
