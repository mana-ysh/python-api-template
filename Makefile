
PROJECT_NAME := manaysh_api
DESCRIPTION := hoge

##### cookiecutter
create-project:
	cookiecutter ./

create-project-no-input:
	cookiecutter --no-input ./ \
		project_slug=${PROJECT_NAME} \
		description=${DESCRIPTION}

ci:
	cd ${PROJECT_NAME} && make ci

clean:
	rm -rf ${PROJECT_NAME}