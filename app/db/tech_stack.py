CREATE_TECH_STACK = """
INSERT INTO tech_stack (id, name)
VALUES ($1, $2)
RETURNING *;
"""