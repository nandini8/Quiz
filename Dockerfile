FROM python
RUN mkdir Quiz
COPY app/ Quiz
WORKDIR Quiz
CMD python scripts/main.py

