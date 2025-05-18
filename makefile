all: images/orcv.svg images/worker-data.svg images/locator-data.svg

images/%.svg: assets/%.svgbob
	svgbob $< >$@

images/%.svg: assets/%.puml
	plantuml -tsvg -p <$< >$@

clean:
	rm -rf images/*
