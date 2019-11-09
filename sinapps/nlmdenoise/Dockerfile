# Use Ubuntu 16.04 LTS
FROM sebastientourbier/sinapps-core:0.1

# Add script for "nlmdenoise" sinapp
ADD run.py /app/run.py

# Activate conda environment and fix missing display (x11 server)
ENV CONDA_ENV supermri-env
RUN echo '#! /bin/bash \n . activate $CONDA_ENV \n xvfb-run -a python /app/run.py $@' > /app/run_nlmdenoise.sh

# Set the working directory back to /app
# Acquire script to be executed
RUN chmod 775 /app/run.py
RUN chmod 775 /app/run_nlmdenoise.sh

ENTRYPOINT ["/app/run_nlmdenoise.sh"] 