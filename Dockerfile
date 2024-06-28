FROM python:3.12.3 
WORKDIR /app 
COPY requirements.txt . 
RUN pip install --no-cache-dir --upgrade -r requirements.txt  
COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:create_app()"] 



#docker run -dp 5005:5000 -w /app -v "$(pwd):/app" flask-smorest-api