.PHONY: env all clean

ENV_NAME = spotify-analysis
NOTEBOOKS = $(wildcard *.ipynb)
OUTPUT_DIR = output
CONDA = /srv/conda/condabin/conda

env: environment.yml
	@if ! $(CONDA) env list | grep -q "^${ENV_NAME}\s"; then \
		$(CONDA) env create -f environment.yml; \
	else \
		$(CONDA) env update -n $(ENV_NAME) -f environment.yml; \
	fi

all: env
	@mkdir -p $(OUTPUT_DIR)
	@for nb in $(NOTEBOOKS); do \
		$(CONDA) run -n $(ENV_NAME) jupyter nbconvert --execute --to html --output-dir=$(OUTPUT_DIR) $$nb; \
	done

clean:
	rm -rf $(OUTPUT_DIR)
