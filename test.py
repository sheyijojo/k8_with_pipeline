# Use the Distroless Java 17 base image
FROM gcr.io/distroless/java17:latest

# Create a directory to store the shell binary
WORKDIR /

# Download and install BusyBox (a lightweight shell utility)
RUN wget https://busybox.net/downloads/binaries/1.32.1-defconfig-multiarch/busybox-x86_64 -O /bin/busybox \
    && chmod +x /bin/busybox \
    && ln -s /bin/busybox /bin/sh

# Set the default command for the container
CMD ["/bin/sh"]
