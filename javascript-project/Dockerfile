FROM node:12

WORKDIR /usr/src/app

# Dependancies
COPY package*.json  ./

RUN npm install

# Code
COPY . .

EXPOSE 3500

CMD ["node", "server.js"]