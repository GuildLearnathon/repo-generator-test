print-stage:
	@echo
	@echo '***** STAGE=$(STAGE) *****'
	@echo


build: clean
	pip install -r requirements.txt


clean:
	@echo 'Clean up'
	rm -rf .aws-sam
	rm -rf .pytest_cache
	rm -rf __pycache__
	rm -rf build
	rm -rf dist/