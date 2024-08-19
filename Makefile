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