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
	@black overwatch tests --exclude="/snapshots"

.PHONY: checkformat
checkformat:
	@black overwatch tests --check --exclude="/snapshots"

