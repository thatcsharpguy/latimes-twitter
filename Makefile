POETRY=poetry
POETRY_RUN=$(POETRY) run

SOURCE_FILES=$(shell find . -path "./twitter/*.py")
TEST_FILES=$(shell find . -path "./tests/**/*.py")
SOURCES_FOLDER=twitter

style:
	$(POETRY_RUN) isort $(SOURCES_FOLDER) tests
	$(POETRY_RUN) black $(SOURCE_FILES) $(TEST_FILES)

lint:
	$(POETRY_RUN) isort $(SOURCES_FOLDER)  tests --check-only
	$(POETRY_RUN) black $(SOURCE_FILES) $(TEST_FILES) --check

test:
	PYTHONPATH=. $(POETRY_RUN) pytest tests
