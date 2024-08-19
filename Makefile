update-req:
	@clear
	@echo "[Makefile]:	update project reqiremnts"
	@pip freeze > requirements.txt

clean:
	@clear
	@echo "[Makefile]:	multi stage project cleansing"
	@echo "1.remove INFO log file"
	@rm info.log

run:
	@clear
	@echo "[Makefile]:	run application (see application config file for more info)"
	@python3 main.py

proto-gen:
	@clear
	@echo "[Makefile]:	compiling proto files"
	@python3 -m grpc_tools.protoc -I=grpc/protobufs --python_out=grpc/compiled --grpc_python_out=grpc/compiled grpc/protobufs/node.proto --mypy_out=grpc/compiled


