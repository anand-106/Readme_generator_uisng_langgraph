/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.js"],
  theme: {
    extend: {
      fontFamily: {
        sans: [
          '"Segoe UI"',
          '"Noto Sans"',
          "ui-sans-serif",
          "system-ui",
          "sans-serif",
        ],
        mono: [
          "SFMono-Regular",
          "Consolas",
          "Liberation Mono",
          "Menlo",
          "monospace",
        ],
      },
    },
  },
  plugins: [require("@tailwindcss/typography")],
};
