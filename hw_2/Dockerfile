FROM python:latest

RUN apt-get update && \
    apt-get install -y --no-install-recommends texlive texlive-latex-extra texlive-fonts-recommended && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app


COPY . /app

RUN pip install --no-cache-dir latex_table_and_image_generator

RUN python task_2_2_main.py

RUN pdflatex -output-directory artifacts artifacts/2_2_table_image.tex

VOLUME /app/artifacts

CMD ["echo", "PDF файл создан и сохранен в директории artifacts"]