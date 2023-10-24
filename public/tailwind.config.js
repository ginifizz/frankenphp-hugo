/** @type {import('tailwindcss').Config} */

const defaultTheme = require('tailwindcss/defaultTheme');

module.exports = {
  content: ['../layouts/**/*.{html,js,md}', '../static/**/*.{html,js,php}'],
  theme: {
    container: {
      center: true,
      padding: '2rem',
    },
    colors: {
      green: {
        DEFAULT: '#b3d133',
        light: '#cbdb8b',
        dark: '#7e9324',
      },
      purple: {
        DEFAULT: '#230143',
        light: '#937da8',
        extralight: '#c3b2d3',
      },
      grey: {
        light: '#f8f6fc',
        dark: '#4e4e4e',
      },
      red: '#ee4322',
      white: '#ffffff',
      black: '#000000',
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

