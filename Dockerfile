# Use an official Python runtime as the base image
FROM python:3.6

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code into the container
COPY . /code/

RUN python manage.py collectstatic --noinput

# Expose port 7005
EXPOSE 7005

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:7005"]