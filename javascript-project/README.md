# Simple HTTP server
This is a simple express server. It works by getting GET requests and responding with a page that the user requested. 

## To start install all the dependancies:
```
$ npm i
```

## And then execute this command:
```
$ nodemon server
```
<br>
The server will start on http://localhost:3500

## Instruction
### You can switch between different pages by changing url:
http://localhost:3500/cat
http://localhost:3500/dog
http://localhost:3500/index
http://localhost:3500/subdir/hamster
http://localhost:3500/subdir/index
<br>
If you write another path, you will get 404 page.
<br>
Also you can see report of all your requests in /logs/repLogs.txt in the project directory.
<br>
I used 4 dependancies: nodemon for automatic project starting, uuid for generating id for the logs, date-fns for dates and express for the http-server itself.