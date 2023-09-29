/** @type {import('tailwindcss').Config} */

const defaultTheme = require('tailwindcss/defaultTheme');

module.exports = {
  content: ['../content/*.md', '../layouts/**/*.html'],
  theme: {
    container: {
      center: true,
      padding: '2rem',
    },
    colors: {
      green: '#b3d133',
      purple: '#230143',
      red: '#ee4322',
      white: '#ffffff',
      black: '#000000',
      'grey-dark': '#4e4e4e',
      current: 'currentColor',
      transparent: 'transparent',
    },
    extend: {
      fontFamily: {
        sans: ['Poppins', ...defaultTheme.fontFamily.sans],
      },
    },
  },
  plugins: [],
};

