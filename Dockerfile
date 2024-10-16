FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY test_params.py /app/test_params.py
COPY preprocess.py /app/preprocess.py
COPY requirements.txt /app/requirements.txt
COPY names.cbm /app/names.cbm

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "test_params.py"]

CMD ["--input_file_path", "alter_dataMini.csv", "--output_file_path", "test_output.csv", "--output_format", "M_F"]

# docker run --rm nameclassification --input_file_path alter_dataMini.csv --output_file_path test_input.csv --output_format M_F

# docker run --rm -v ${pwd}/test_input.csv:/app -v ${pwd}/output:/app/output nameclassification --input_file_path test_input.csv --output_file_path test_output.csv --output_format M_F