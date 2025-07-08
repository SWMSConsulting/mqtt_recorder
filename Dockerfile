FROM python:3.12-alpine

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY mqtt_recorder/requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY mqtt_recorder/ ./mqtt_recorder/
COPY recording2.csv ./recording2.csv

# Set the command to run the startscript
CMD ["python", "mqtt_recorder/startscript.py"]