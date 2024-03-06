# Corsproxy
A server in flask to bypass cors, ready to be deployed on vercel.  
To be used with [Jee-Mains-Marks-Calculator](https://github.com/timepassuser/Jee-Mains-Marks-Calculator)
## Running locally
In the root of the project run  
```
flask --app api/index run --debug
```
This will start the proxy at localhost port 5000  
## Deploying on vercel
Import a clone of this repository in vercel and it should automatically get deployed with the default settings