module.exports = {
  purge: ['./src/**/*.{js,jsx}'],
  darkMode: 'class', // or 'media' or 'class'
  theme: {
    screens: {
      xs: '482px',
      sm: '640px',
      md: '768px',
      mdlg: '900px',
      lg: '1024px',
      xl: '1280px',
      '2xl': '1536',
    },
    extend: {
      fontSize: {
        base: '16px',
        'base-larger': '.9rem',
      },
      colors: {
        primary: '#5685F5',
        black: '#0D1117',
        gray: '#89929b',
        'gray-2': '#c6cdd5',
        white: '#ECF2F8',
        red: '#FA7970',
        orange: '#FAA356',
        green: '#7CE38B',
        cyan: '#A2D2FB',
        blue: '#77BDFB',
        purple: '#CEA5FB',
      }
    }
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
