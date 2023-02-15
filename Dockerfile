FROM pypy:latest
WORKDIR /app

pip3 install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.5.0/en_core_web_sm-3.5.0.tar.gz --user

# Copy requirements.txt from computer to image with the same filename
COPY requirements.txt requirements.txt

# Install requirements specified in requirements.txt
RUN pip3 install -r requirements.txt

# Copy all files from directory where requirements.txt is located.
COPY . .

CMD python garden.py