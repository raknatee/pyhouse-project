FROM node:16-buster as build_stage
WORKDIR /home/app


EXPOSE 80

COPY ./app/package*.json .
RUN npm install

COPY ./app .

RUN npm run build

FROM nginx:1.23.1
EXPOSE 80
COPY --from=build_stage /home/app/dist /usr/share/nginx/html