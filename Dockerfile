# Base Image for building ML App
FROM python

WORKDIR /mlapp
# copy Requirements.txt and app.py
#COPY data/.  
#COPY requirements.txt ./
#COPY app.py ./
COPY . . 

# Libraries to be installed
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port 
#EXPOSE 5000

#default commands to run star the application. 
CMD [ "python", "mlkfapp.py" ]