CREATE_TECH_STACK = """
INSERT INTO tech_stack (name)
VALUES ($1)
RETURNING *;
"""