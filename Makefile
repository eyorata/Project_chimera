setup:
	pip install pytest

test:
	pytest -q

docker-build:
	docker build -t chimera .

docker-test:
	docker run --rm chimera

spec-check:
	@echo "Spec-check placeholder: manually ensure code aligns with specs/"
