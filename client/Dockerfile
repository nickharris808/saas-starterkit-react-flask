# Use an official Node.js image as the base image
FROM node:16

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to install dependencies
COPY package*.json ./

# Install the necessary dependencies
RUN npm install

# Copy the rest of the application files into the container
COPY . .

# Build the React app for production
RUN npm run build

# Use an official Nginx image to serve the React application
FROM nginx:alpine

# Copy the build folder to Nginx's default directory
COPY --from=0 /app/build /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]

ENV REACT_APP_API_BASE_URL=http://server:5000