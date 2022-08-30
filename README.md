# Bender Bot


## Description

My pet bot on aiogram3 is developing with good quality design.

Bot will be collect quotes, monitoring events and moke other other helpful job.

It will be deploy on VDS.


### Bot's features

Currently realize following test commands:
* */start*
* */name \<your name>*


### Quick start

Use Make file with `make` command with shortcuts to quick start bot locally.



## Technical Refresher

All commands necessary write with *`docker-compose exec <service_name>`* prefix to execute commands.


### Alembic
```bash
# Make migrations.
# Enter message. Alembic can view status of database and compare against the table metadata in the application
alembic revision --message="" --autogenerate

# Assert migrations
alembic upgrade head

# Rollback migrations, enter number:
alembic downgrade -1

# Watch Alembic history
alembic history
```
