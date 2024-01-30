/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        offwhite: "#F6F6F6",
        white: "#FFFFFF",
        black: "#101010",
        red: "#FF151F",
        blue: "#1D2269",
        sky: "#0596FF",
      },
      fontFamily: {
        'kumbh_regular': ['kumbh_regular','sans-serif'],
        'kumbh_bold': ['kumbh_bold','sans-serif']
      },
    },
  },
  plugins: [],
};
