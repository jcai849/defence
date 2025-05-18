all: images/orcv.svg images/worker-data.svg images/locator-data.svg assets/graphs/chunknet_1.dot

images/%.svg: assets/%.svgbob
	svgbob $< >$@

images/%.svg: assets/%.puml
	plantuml -tsvg -p <$< >$@

assets/graphs/chunknet_1.dot: graph-gen/chunknet.py
	cd graph-gen && uv run chunknet.py

clean:
	rm -rf images/*
	rm -rf assets/graphs/*
