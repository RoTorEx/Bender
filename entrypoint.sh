echo "Entry point passed."

# Apply migrations
python -m alembic upgrade head

# Start bot inside (!) docker container
exec python -m bot
