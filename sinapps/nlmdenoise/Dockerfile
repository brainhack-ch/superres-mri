# Use Ubuntu 16.04 LTS
FROM supermri-team/sinapps-core:0.1

#
#RUN groupadd -r -g 1000 cmp && \
#    useradd -r -M -u 1000 -g cmp cmp

# Add script for "nlmdenoise" sinapp
ADD run.py /app/run.py

# Activate conda environment and fix missing display (x11 server)
ENV CONDA_ENV supermri-env
RUN echo '#! /bin/bash \n . activate $CONDA_ENV \n chown -R $(id -u):$(id -g) /var/run/docker.sock /usr/bin/docker \n xvfb-run -a python /app/run.py $@' > /app/run_nlmdenoise.sh

# Set the working directory back to /app
# Acquire script to be executed
RUN chmod 775 /app/run.py
RUN chmod 775 /app/run_nlmdenoise.sh

ENTRYPOINT ["/app/run_nlmdenoise.sh"] 