.PHONY: build img

IMGNAME := test_joget_upload_plugin
PORT := 8080

all : build

build:
	docker build -t $(IMGNAME):latest -f Dockerfile .

start:
	docker run --rm -it -p $(PORT):8080 $(IMGNAME)

background:
	docker run --rm -d -p $(PORT):8080 $(IMGNAME)

shell:
	docker exec -it $(shell docker ps | grep $(IMGNAME) | awk '{split($$0,a," "); print a[1]}') bash

stop:
	docker stop $(shell docker ps | grep $(IMGNAME) | awk '{split($$0,a," "); print a[1]}')