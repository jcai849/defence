all: images/orcv.svg

images/orcv.svg: assets/orcv.svgbob
	svgbob $< >$@
