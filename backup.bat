@echo off
REM Set variables for database connection
set PGUSER=postgres
set PGDATABASE=postgres

REM Set the path where you want to store the backup files
set BACKUP_DIR=C:\Users\mrcra\Desktop

REM Get current date and time
for /f "tokens=2-4 delims=/ " %%a in ('date /t') do (set "datestamp=%%c-%%a-%%b")
for /f "tokens=1-2 delims=: " %%a in ('time /t') do (set "timestamp=%%a%%b")

REM Execute pg_dump command to dump the database
pg_dump -U %PGUSER% -d %PGDATABASE% -f "%BACKUP_DIR%\%PGDATABASE%_%datestamp%_%timestamp%.sql"