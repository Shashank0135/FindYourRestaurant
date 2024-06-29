# # Use the official Python image from the Docker Hub
# FROM python:3.11

# # Set the working directory in the container
# WORKDIR /code

# # Copy the current directory contents into the container at /code
# COPY . /code

# # Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt gunicorn

# # Make port 5000 available to the world outside this container
# EXPOSE 5000

# # Run the application with gunicorn
# CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]

FROM python:3.11
WORKDIR /code
COPY . /code
RUN pip install -r requirements.txt
CMD ["uvicorn", "app:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]