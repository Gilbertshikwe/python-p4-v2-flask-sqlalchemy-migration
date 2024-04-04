"""rename department

Revision ID: 62446abac55f
Revises: ccf8fafe9aae
Create Date: 2024-04-04 09:16:48.979304

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62446abac55f'
down_revision = 'ccf8fafe9aae'
branch_labels = None
depends_on = None


def upgrade():
    # Create the departments table
    op.create_table('departments',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('address', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    # Check if the 'department' table exists before renaming it
    if op.get_bind().has_table('department'):
        op.rename_table('department', 'departments')


def downgrade():
    # Check if the 'departments' table exists before renaming it
    if op.get_bind().has_table('departments'):
        op.rename_table('departments', 'department')
    
    # Drop the 'departments' table
    op.drop_table('departments')

