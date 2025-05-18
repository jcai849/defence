import Reveal from 'reveal.js';
import RevealMarkdown from 'reveal.js/plugin/markdown/markdown'
import RevealNotes from 'reveal.js/plugin/notes/notes'
import RevealHighlight from 'reveal.js/plugin/highlight/highlight'
import RevealMath from 'reveal.js/plugin/math/math'
import 'reveal.js/plugin/highlight/zenburn.css'
import 'reveal.js/dist/reveal.css';
import 'reveal.js/dist/theme/serif.css';

fetch('assets/comparison-table.html')
      .then(response => response.text())
      .then(html => {
        document.getElementById('comparison-table').innerHTML = html;
      });

let deck = new Reveal();
deck.initialize({
  plugins: [RevealMarkdown, RevealNotes, RevealHighlight, RevealMath.KaTeX],
  totalTime: 1200,
  hash: true,
  center: false
});
