/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/*.{html,js}", "./node_modules/flowbite/**/*.js"],
  theme: {
    extend: {
      colors: {
        offwhite: "#F6F6F6",
        white: "#FFFFFF",
        black: "#101010",
        red: "#FF151F",
        blue: "#1D2269",
        hoverblue: "#000986",
        sky: "#0596FF",
        hoversky: "#057AFF",
      },
      fontFamily: {
        kumbh_regular: ["kumbh_regular", "sans-serif"],
        kumbh_bold: ["kumbh_bold", "sans-serif"],
      },
      keyframes: {
        timer: {
          from: { width: "100%" },
          to: { width: "0%" },
        },
      },
      animation: {
        timer: "timer 5s ease-in-out forwards", // Define the animation name and duration
      },
    },
  },
  plugins: [require("flowbite/plugin")],
};
