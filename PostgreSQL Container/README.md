# PostgreSQL Container - Task III

This folder contains all the files needed to run the complete Task III of the DevOps Internship 2025 project.

## Contents

- `init_company.sql` - SQL script for creating and populating databases
- `queries.sql` - SQL queries requested in the task
- `setup.sh` - Bash script for automating the whole process
- `output.log` - Log file with results of SQL queries
- `dump_company.sql` - PostgreSQL database export
- `README.md` - This documentation file

## What the project does

This task configures a PostgreSQL container, imports data into the database and runs relevant queries.

## Main steps

1. Create a Docker PostgreSQL container:
   - Database: `company_db`
   - Custom user: `ituser`
   - Exposed port: `5432`

2. Run the SQL script `init_company.sql`:
   - Create tables: `departments`, `employees`, `salaries`
   - Insert data in all three tables
   - Insert 76 employees and their salaries

3. Run the queries in `queries.sql`:
   - Displays the total number of employees
   - Select the names of employees in a given department
   - Calculates the maximum and minimum salary per department
   - Results are saved in `output.log`

4. Export the database to `dump_company.sql` using `pg_dump`

5. Automate all the above steps with the `setup.sh` script:
   - Create user `admin_cee`
   - Run `init_company.sql`
   - Run `queries`.


## How to use

> All commands are executed from an already started and configured container (with Docker and PostgreSQL installed)

### 1. Open the container:
```bash
docker exec -it pg-container bash
```

### 2. Run the setup script:
```bash
chmod +x setup.sh
./setup.sh
```

### 3. Check the results:
```bash
cat output.log
```

## Output

If everything is configured correctly, in the `output.log` file you will find:
- Total number of employees (76)
- Names of employees in the selected department
- Highest and lowest salary per department




