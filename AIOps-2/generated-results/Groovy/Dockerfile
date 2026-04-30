```dockerfile
# Use an official Java 11 base image to ensure security and stability
FROM openjdk:11-jdk-alpine

# Set working directory in the container to /app
WORKDIR /app

# Install Maven dependencies using apt-get
RUN apt-get update && \
    apt-get install -y maven && \
    rm -rf /var/lib/apt/lists/*

# Copy pom.xml file from the current directory to /app
COPY pom.xml /app/

# Download and build the application using Maven
RUN mvn clean package

# Create a new layer for the compiled code
FROM scratch

# Copy the compiled code into this layer
COPY --from=builder /app/target/*.jar /app/

# Expose port 8080 for the Groovy web server
EXPOSE 8080

# Set the default command to run the application
CMD ["mvn", "run"]
```

```dockerfile
# Use multi-stage build to separate compilation and runtime dependencies
FROM openjdk:11-jdk-alpine AS builder

# Install Maven dependencies using apt-get in a temporary layer
RUN apt-get update && \
    apt-get install -y maven && \
    rm -rf /var/lib/apt/lists/*

# Copy pom.xml file from the current directory to /app
COPY pom.xml /app/

# Download and build the application using Maven in this stage
RUN mvn clean package

# Create a new layer for the compiled code
FROM scratch

# Copy the compiled code into this layer
COPY --from=builder /app/target/*.jar /app/

# In the final image, set working directory to /app and run the application
WORKDIR /app
CMD ["mvn", "run"]
```

```dockerfile
# Use multi-stage build with a separate stage for compilation
FROM openjdk:11-jdk-alpine AS builder

# Install Maven dependencies using apt-get in this stage
RUN apt-get update && \
    apt-get install -y maven && \
    rm -rf /var/lib/apt/lists/*

# Copy pom.xml file from the current directory to /app
COPY pom.xml /app/

# Download and build the application using Maven in this stage
RUN mvn clean package

# Create a new layer for the compiled code
FROM scratch

# Copy the compiled code into this layer
COPY --from=builder /app/target/*.jar /app/

# In the final image, set working directory to /app and run the application
WORKDIR /app

# Use a separate stage to compile and package the application
FROM maven:3.6.0-jdk-11 AS compiler

# Install Java dependencies using apt-get in this stage
RUN apt-get update && \
    apt-get install -y default-jdk && \
    rm -rf /var/lib/apt/lists/*

# Copy pom.xml file from the current directory to /app
COPY pom.xml /app/

# Download and build the application using Maven in this stage
RUN mvn clean package

# Copy the compiled code into the final image
COPY --from=compiler /app/target/*.jar /app/

# In the final image, set working directory to /app and run the application
WORKDIR /app
CMD ["mvn", "run"]
```

```dockerfile
# Use a multi-stage build with separate stages for Maven and Groovy compilation
FROM maven:3.6.0-jdk-11 AS maven-builder

# Install Java dependencies using apt-get in this stage
RUN apt-get update && \
    apt-get install -y default-jdk && \
    rm -rf /var/lib/apt/lists/*

# Copy pom.xml file from the current directory to /app
COPY pom.xml /app/

# Download and build the application using Maven in this stage
RUN mvn clean package

FROM openjdk:11-jdk-alpine AS groovy-builder

# Install Groovy dependencies using apt-get in this stage
RUN apt-get update && \
    apt-get install -y groovy-all && \
    rm -rf /var/lib/apt/lists/*

# Copy the compiled code from Maven into a new layer for Groovy compilation
COPY --from=maven-builder /app/target/*.jar /app/

# Download and compile the application using Groovy in this stage
RUN groovy -cp target/ main.Groovy

# In the final image, set working directory to /app and run the application
WORKDIR /app
CMD ["groovy", "-cp", "target/", "main.Groovy"]
```

```dockerfile
# Use a multi-stage build with separate stages for Maven and Groovy compilation
FROM maven:3.6.0-jdk-11 AS maven-builder

# Install Java dependencies using apt-get in this stage
RUN apt-get update && \
    apt-get install -y default-jdk && \
    rm -rf /var/lib/apt/lists/*

# Copy pom.xml file from the current directory to /app
COPY pom.xml /app/

# Download and build the application using Maven in this stage
RUN mvn clean package

FROM openjdk:11-jdk-alpine AS groovy-builder

# Install Groovy dependencies using apt-get in this stage
RUN apt-get update && \
    apt-get install -y groovy-all && \
    rm -rf /var/lib/apt/lists/*

# Copy the compiled code from Maven into a new layer for Groovy compilation
COPY --from=maven-builder /app/target/*.jar /app/

# Download and compile the application using Groovy in this stage
RUN groovy -cp target/ main.Groovy

FROM maven:3.6.0-jdk-11 AS groovy-app

# Install Java dependencies using apt-get in this stage
RUN apt-get update && \
    apt-get install -y default-jdk && \
    rm -rf /var/lib/apt/lists/*

# Copy the compiled code from Groovy into a new layer for running the application
COPY --from=groovy-builder /app/main.Groovy /app/

# In the final image, set working directory to /app and run the application
WORKDIR /app
CMD ["java", "-jar", "target/*.jar"]
