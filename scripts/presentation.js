import Reveal from 'reveal.js';
import RevealMarkdown from 'reveal.js/plugin/markdown/markdown'
import RevealNotes from 'reveal.js/plugin/notes/notes'
import RevealHighlight from 'reveal.js/plugin/highlight/highlight'
import 'reveal.js/dist/reveal.css';
import 'reveal.js/dist/theme/serif.css';
import * as AsciinemaPlayer from 'asciinema-player';
import 'asciinema-player/dist/bundle/asciinema-player.css'

AsciinemaPlayer.create('assets/lsmr.cast', document.getElementById('lsmr'));
AsciinemaPlayer.create('assets/lsr.cast', document.getElementById('lsr'));

fetch('assets/comparison-table.html')
      .then(response => response.text())
      .then(html => {
        document.getElementById('comparison-table').innerHTML = html;
      });

let deck = new Reveal();
deck.initialize({
  plugins: [RevealMarkdown, RevealNotes, RevealHighlight],
  totalTime: 1200,
  hash: true
});
