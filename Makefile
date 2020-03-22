.PHONY: test
test:
	@pytest ./tests -vv

.PHONY: format
format:
	@black overwatch tests/test_crawler.py tests/util.py

.PHONY: checkformat
checkformat:
	@black overwatch tests/test_crawler.py tests/util.py --check

