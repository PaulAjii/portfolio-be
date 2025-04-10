from app.db.connection import get_db_connection

async def create_tables():
    """Create tables in the database"""

    connection = await get_db_connection()

    if connection:
        await connection.execute("""
            CREATE TABLE IF NOT EXISTS projects (
                id UUID PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT,
                github_url TEXT,
                demo_url TEXT
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)

        await connection.execute("""                 
            CREATE TABLE IF NOT EXISTS tech_stack (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL
            );
        """)

        await connection.execute("""          
            CREATE TABLE IF NOT EXISTS project_tech_stack (
                project_id UUID REFERENCES projects(id) ON DELETE CASCADE,
                tech_stack_id INTEGER REFERENCES tech_stack(id) ON DELETE CASCADE,
                PRIMARY KEY (project_id, tech_stack_id)
            );
        """)

        print("Tables created successfully")
        await connection.close()
    else:
        print("Failed to create tables: No database connection")