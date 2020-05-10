FROM python:3
WORKDIR /usr/src/app
#WORKDIR C:\Users\sahit\cm\fa19-516\fa19-516-174\project\knn\web
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python", "server.py" ]
