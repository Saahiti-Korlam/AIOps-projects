FROM node:20-alpine

# Set production environment
ENV NODE_ENV=production

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy package files first to leverage Docker layer caching
COPY package*.json ./

# Install only production dependencies
# Uses 'npm ci' for faster, reliable builds in CI/CD environments
RUN npm ci --omit=dev

# Copy the rest of the application source code
# Ensure you have a .dockerignore file to exclude node_modules and logs
COPY . .

# Use a non-privileged user for security (built-in to the Node image)
USER node

# Expose the port your app runs on
EXPOSE 3000

# Start the application
CMD [ "node", "index.js" ]
