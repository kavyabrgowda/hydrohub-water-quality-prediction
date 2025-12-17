/** @type {import('tailwindcss').Config} */

module.exports = {
  content: [
      './hydrohub/src//*.{html,js,jsx,ts,tsx}', // Only scanning files in MDAI/src
      './contamination.html', // Add this if your HTML is directly in the root or public folder
      './index.html',
      './prediction.html',
      './rainfall.html',
      './result.html',
      './treatment.html',
      './hydrohub/templates//*.{html,js}' 
      // Adjust this based on where your files are
  ],
  theme: {
      extend: {
          fontFamily: {
              sans: ["var(--Georgia)"],
          },
          colors: {
              //"hero-white": "#F6F9FF",

          },
          backgroundImage: {
              'header-pattern': "url('/img/regestration.jpg')",
          },
      },
  },
  plugins: [],
}


/* Command to pass in bash to import the requirements to the css file of public folder from src folder
-->(Akhila) npx tailwindcss -i ./static/css/globals.css -o ./templates/styles.css --watch
*/