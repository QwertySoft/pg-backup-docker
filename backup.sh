#!/bin/sh

NOW=$(date +"%Y-%m-%dT%H:%M:%SZ")

echo "Creating dump of ${POSTGRES_DATABASE} database from ${POSTGRES_HOST}..."
pg_dump $POSTGRES_HOST_OPTS $POSTGRES_DATABASE | gzip > "/backups/$NOW.sql.gz"

echo "Uploading dump to $S3_BUCKET"
