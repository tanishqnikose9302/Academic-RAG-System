import os
from datetime import datetime


def create_directory(path):

    if not os.path.exists(path):

        os.makedirs(path)


def save_uploaded_file(
    uploaded_file,
    upload_dir="data"
):

    create_directory(upload_dir)

    file_path = os.path.join(
        upload_dir,
        uploaded_file.name
    )

    with open(
        file_path,
        "wb"
    ) as file:

        file.write(
            uploaded_file.getbuffer()
        )

    return file_path


def timestamp():

    return datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


def format_sources(
    sources
):

    formatted = []

    for index, source in enumerate(
        sources,
        start=1
    ):

        formatted.append(
            f"Source {index}\n{source}\n"
        )

    return "\n".join(
        formatted
    )


def truncate_text(
    text,
    max_length=500
):

    if len(text) <= max_length:

        return text

    return (
        text[:max_length]
        + "..."
    )


def log_query(
    query,
    answer,
    log_file="logs/query_logs.txt"
):

    create_directory("logs")

    with open(
        log_file,
        "a",
        encoding="utf-8"
    ) as file:

        file.write(
            f"\n[{timestamp()}]\n"
        )

        file.write(
            f"QUESTION:\n{query}\n"
        )

        file.write(
            f"ANSWER:\n{answer}\n"
        )

        file.write(
            "-" * 80
        )

        file.write("\n")
