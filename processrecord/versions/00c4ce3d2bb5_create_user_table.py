"""create user table

Revision ID: 00c4ce3d2bb5
Revises: 6be83e29465e
Create Date: 2022-04-16 20:48:09.790767

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00c4ce3d2bb5'
down_revision = '6be83e29465e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users', 
    sa.Column('id', sa.Integer(), nullable=False, primary_key=True), 
    sa.Column('email', sa.String(), nullable=False), 
    sa.Column('password', sa.String(), nullable=False), 
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), 
    server_default=sa.text("now()"), nullable=False),
    sa.UniqueConstraint('email'))
    pass


def downgrade():
    op.drop_table('users')
    pass
