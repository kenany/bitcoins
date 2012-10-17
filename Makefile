init:
	python setup.py develop
	pip install -r requirements.txt

test:
	nosetests tests/test_bitcoins.py

clean:
	git clean -Xfd

bitpy:
	rm -fr bitcoins/packages/bitcoinrpc
	git clone https://github.com/KenanY/bitcoin-python.git
	cd bitcoin-python && git checkout master && cd ..
	mv bitcoin-python/src/bitcoinrpc bitcoins/packages/
	rm -fr bitcoin-python
