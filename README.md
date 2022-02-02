# python_ee


# pull from https://hub.docker.com/r/continuumio/miniconda3

download image
```
docker pull continuumio/miniconda3
docker run -i -t continuumio/miniconda3 /bin/bash
```
or run as Jupyter Notebook server in browser
```
docker run -i -t -p 8888:8888 continuumio/miniconda3 /bin/bash -c "\
    conda install jupyter -y --quiet && \
    mkdir -p /opt/notebooks && \
    jupyter notebook \
    --notebook-dir=/opt/notebooks --ip='*' --port=8888 \
    --no-browser --allow-root"
```
opening http://localhost:8888 in your browser