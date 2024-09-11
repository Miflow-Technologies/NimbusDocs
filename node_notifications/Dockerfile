# Use an official Node.js runtime as a parent image
FROM node:14

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json
COPY node_notifications/package*.json ./

# Install any needed packages specified in package.json
RUN npm install

# Copy the rest of the application code
COPY node_notifications/ .

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run the Node.js server when the container launches
CMD ["node", "src/app.js"]
