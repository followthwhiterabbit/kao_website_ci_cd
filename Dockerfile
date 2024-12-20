FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

# Create a non-root user and group
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

# Create and set the working directory
WORKDIR /kao_website

# copying requirements.txt first for leveraging cache
COPY requirements.txt /kao_website/

# Installing dependencies inside requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copying the rest of the application code
COPY . /kao_website/

# Changing ownership of the application directory
RUN chown -R appuser:appgroup /kao_website

# Switch to the non-root user
USER appuser

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"] 
