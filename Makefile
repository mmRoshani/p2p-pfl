update-req:	# update project reqiremnts
	@clear
	@echo "update project reqiremnts"
	@pip freeze > requirements.txt

clean:
	@clear
	@echo "1.remove error.log file"
	@rm error.log