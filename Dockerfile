FROM python
WORKDIR /app
COPY . .
CMD ["python3","./txt_to_csv_parser.py","fixed_width_file.txt","spec_file.txt","output.csv"]