.PHONY: test
test:
	@pytest ./tests -vv

.PHONY: run
run:
	@python run.py

.PHONY: testupdate
testupdate:
	@pytest --snapshot-update

.PHONY: format
format:
	@black overwatch tests/test_crawler.py tests/util.py

.PHONY: checkformat
checkformat:
	@black overwatch tests/test_crawler.py tests/util.py --check

