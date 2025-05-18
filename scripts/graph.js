import * as d3 from "d3";
import { graphviz } from "d3-graphviz";

async function createGraphWithButtons(graphName, numStates) {
  const graphDiv = document.getElementById(graphName);
  let index = 0;

  // Fetch all DOT files for this graph
  const dotStates = await Promise.all(
    Array.from({ length: numStates }, (_, i) =>
      fetch(`assets/graphs/${graphName}_${i + 1}.dot`).then(r => r.text())
    )
  );

  const gv = graphviz(graphDiv) .transition(() => d3.transition().duration(500));
  
  const render = () => gv.renderDot(dotStates[index]);
  

  // Create button group
  const btnGroup = document.createElement("div");
  btnGroup.style.textAlign = "center";
  btnGroup.style.marginTop = "1em";
  const makeButton = (label, onClick) => {
    const btn = document.createElement("button");
    btn.textContent = label;
    btn.onclick = onClick;
    btnGroup.appendChild(btn);
  };
  makeButton("←", () => { if (index > 0) index--; render(); });
  makeButton("→", () => { if (index < dotStates.length - 1) index++; render(); });
  makeButton("↞", () => { index = 0; render(); });
  graphDiv.insertAdjacentElement("beforebegin", btnGroup);
  render();

  return { render, restart: () => { index = 0; render(); } };
}

async function createStaticGraph(graphName) {
  const graphDiv = document.getElementById(graphName);
  const dot = await fetch(`assets/${graphName}.dot`).then(r => r.text())
  graphviz(graphDiv).renderDot(dot)
}

createStaticGraph("distobjref")
createStaticGraph("gc")
createStaticGraph("dreduce")
createGraphWithButtons("graph1", 3)
createGraphWithButtons("chunknet", 13)
createGraphWithButtons("dlm", 10)
