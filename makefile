all: images/orcv.svg images/worker-data.svg images/locator-data.svg assets/graphs/chunknet_1.dot # assets/graphs/dlm_1.dot # assets/graphs/chunk-call_1.dot

images/%.svg: assets/%.svgbob
	svgbob --background none $< >$@

images/%.svg: assets/%.puml
	plantuml -tsvg -p <$< >$@

assets/graphs/chunknet_1.dot: graph-gen/chunknet.py
	cd graph-gen && uv run chunknet.py

assets/graphs/dlm_1.dot: graph-gen/dlm.py
	cd graph-gen && uv run dlm.py

assets/graphs/chunk-call_1.dot: graph-gen/chunk-call.py
	cd graph-gen && uv run chunk-call.py

clean:
	rm -rf images/*
