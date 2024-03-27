FROM python:3.12-bookworm

# copy all files to docker directory
COPY . /app/

# run a pip installation
# RUN pip install -r requirements.txt

# launch application
CMD [ "python", api.py ] 
