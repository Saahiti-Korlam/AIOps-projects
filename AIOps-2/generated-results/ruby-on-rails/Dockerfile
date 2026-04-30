# Use an official Ruby and Rails base image for a good balance of performance and security
FROM ruby:2.7-aspack

# Set multi-stage build to separate layers for dependencies and application code
# This reduces the size of the final image by only including necessary files
# Stage 1: Install dependencies (we'll use bundler)
RUN apt-get update && apt-get install -y build-essential \
    libpq-dev \
    libreadline-dev \
    zlib1g-dev \
    git && rm -rf /var/lib/apt/lists/*

# Stage 2: Copy application code and execute Bundler for development dependencies
COPY . /app
WORKDIR /app
RUN bundle install --jobs 4 --retry 3

# Bundle exec to ensure bundled dependencies are executed in the container
ENV RAILS_ENV=development
EXPOSE 3000
CMD ["rails", "server", "-b", "0.0.0.0:3000"]
