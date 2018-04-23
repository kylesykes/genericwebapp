FROM python:3.6.5
MAINTAINER GenericWebApp

RUN apt-get update && apt-get install -y \
        build-essential

WORKDIR /app

# Install Requirements
COPY requirements.txt /app
RUN pip3 install -U -r /app/requirements.txt

# Now do rest of work
COPY . /app

# Distroless images seemed promising, but caused issues launching gunicorn unfortunately
# FROM gcr.io/distroless/python3
# EXPOSE 8080
# COPY --from=0 /app /app
# WORKDIR /app

# CMD ["gunicorn", "-w", "1", "--bind", "0.0.0.0:8080", "views:app"]
CMD ["python views.py"]
