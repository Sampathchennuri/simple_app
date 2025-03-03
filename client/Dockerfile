FROM node:18

WORKDIR /app

COPY package*.json /app/

RUN npm install

COPY . .

EXPOSE 3002

CMD ["npm", "run", "dev"]