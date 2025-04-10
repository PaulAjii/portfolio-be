CREATE_TECH_STACK = """
INSERT INTO tech_stack (name)
VALUES ($1)
RETURNING *;
"""

GET_ALL_TECH_STACKS = """
SELECT * FROM tech_stack;
"""