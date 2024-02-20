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
      },
      fontFamily: {
        kumbh_regular: ["kumbh_regular", "sans-serif"],
        kumbh_bold: ["kumbh_bold", "sans-serif"],
      },
    },
  },
  plugins: [require("flowbite/plugin")],
};
